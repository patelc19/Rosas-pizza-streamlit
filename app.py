import numpy as np
import streamlit as st
from starter import COSTS, TIME_BLOCKS, ZONES, delivery_times


SEED = 1


def cost_per_late_order(costs):
	refund = costs["refund"]
	churn_cost = costs["churn_orders"] * costs["margin"]

	total_cost = refund + churn_cost

	return total_cost


def find_best_promise(zone, time_block, promises, costs, seed=1):
	late_cost = cost_per_late_order(costs)

	best_promise_time = None
	best_net_profit = -np.inf

	results = []

	for promise in promises:
		times = delivery_times(zone, time_block, promise, seed=seed)

		number_of_orders = len(times)
		late_orders = np.sum(times > promise)
		profit_collected = number_of_orders * costs["margin"]
		total_late_cost = late_orders * late_cost
		net_profit = profit_collected - total_late_cost

		results.append((promise, number_of_orders, late_orders, net_profit))

		if net_profit > best_net_profit:
			best_net_profit = net_profit
			best_promise_time = promise

	return best_promise_time, best_net_profit, results


st.set_page_config(page_title="Rosa's Pizza Promise", page_icon="🍕")
st.title("Rosa's Pizza Delivery Promise")
st.write("Test delivery promises and find the option with the highest estimated net profit.")

with st.form("promise_form"):
	zone = st.selectbox("Delivery zone", ZONES)
	time_block = st.selectbox("Time block", TIME_BLOCKS)

	start_promise = st.number_input(
		"First promised time to test (minutes)",
		min_value=1,
		value=20,
		step=5,
	)
	end_promise = st.number_input(
		"Last promised time to test (minutes)",
		min_value=1,
		value=70,
		step=5,
	)

	margin = st.number_input(
		"Profit margin per order ($)",
		min_value=0.0,
		value=float(COSTS["margin"]),
		step=0.10,
	)
	churn_orders = st.number_input(
		"Estimated future orders lost per late order",
		min_value=0.0,
		value=float(COSTS["churn_orders"]),
		step=0.1,
	)
	refund = st.number_input(
		"Refund cost per late order ($)",
		min_value=0.0,
		value=float(COSTS["refund"]),
		step=0.10,
	)

	calculate = st.form_submit_button("Calculate best promise")

if calculate:
	if start_promise > end_promise:
		st.error("The first promised time must be less than or equal to the last promised time.")
	else:
		promises = list(range(int(start_promise), int(end_promise) + 1, 5))
		costs = {
			"margin": margin,
			"churn_orders": churn_orders,
			"refund": refund,
		}

		best_time, best_profit, results = find_best_promise(
			zone,
			time_block,
			promises,
			costs,
			seed=SEED,
		)

		st.subheader("Recommendation")
		st.metric("Recommended promised delivery time", f"{best_time} minutes")
		st.metric("Estimated net profit", f"${best_profit:,.2f}")

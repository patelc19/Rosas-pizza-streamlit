---
name: notebook-to-streamlit
description: Convert the Rosa's Pizza analysis from the Jupyter Notebook into a Streamlit decision-making app while preserving the notebook's calculations and logic.
---

# Notebook to Streamlit Instructions

Use the existing analysis and functions from the Rosa's Pizza Jupyter Notebook when creating the Streamlit application.

Do not change the formulas or business logic from the notebook.

Reuse the notebook's functions for:
- calculating the cost per late order
- calculating net profit
- finding the best promised delivery time

The Streamlit app should allow the user to:
- select a delivery zone
- select a time block
- set the range of promised delivery times to test
- adjust the profit margin per order
- adjust estimated churn orders per late order
- adjust the refund cost per late order
- click a button to calculate the best promise
- see the recommended promised delivery time

Use the ZONES, TIME_BLOCKS, COSTS, and delivery_times objects from the starter package.

Preserve the same seed used in the notebook so that results are reproducible.

Keep the application simple and easy to understand.

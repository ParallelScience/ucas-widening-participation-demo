The current analysis is technically sound, well-scoped, and adheres to the constraints regarding model complexity. The distinction between "overall access" and "selective conversion" is the correct analytical lens for this dataset. However, to elevate this from a descriptive report to a robust scientific contribution, the following refinements are necessary:

**1. Address the "Denominator Problem" in Rankings**
The current ranking of equity gaps (e.g., Ethnicity Minor) is vulnerable to the "small-n" problem you identified. You correctly flagged this in the text, but the ranking itself remains misleading. 
*   **Action:** In the ranking table/chart, add a "Confidence Flag" column. Any category with a denominator below a specific threshold (e.g., < 500 students) should be visually distinguished or excluded from the "Top 5" list. This prevents the narrative from being hijacked by high-volatility, low-sample-size categories (like "Traveller of Irish Heritage") while still acknowledging their existence in a supplementary table.

**2. Strengthen the "Conversion Ratio" Interpretation**
You correctly identify that the Conversion Ratio (CR) is a measure of institutional selection bias. However, you treat it as a static outcome. 
*   **Action:** Perform a simple "Counterfactual Check." If the CR for Q1 were equal to the CR for Q5, how many additional Q1 students would be in high-tariff institutions? This "gap-closing" calculation is far more intuitive for policy audiences than a raw percentage point difference. It translates "inequality" into "missed opportunity," which is a more powerful scientific and policy narrative.

**3. Refine the Trend Analysis**
You fit a linear trend to the absolute gap. While this is appropriate, the results show a divergence: overall gaps are narrowing while high-tariff gaps are widening. 
*   **Action:** Explicitly test the *difference* between these two slopes. Use a simple Z-test for the difference between the two regression coefficients (Overall Slope vs. High-Tariff Slope). This will allow you to state with statistical confidence that the "widening" of the high-tariff gap is significantly different from the "narrowing" of the overall gap, rather than just observing it visually.

**4. Address the "COVID-affected" Period**
You treat 2020/21–2022/23 as a descriptive window. This is correct, but you missed an opportunity to test for "persistence." 
*   **Action:** Calculate the mean gap for the pre-COVID period (2009–2019) and compare it to the mean gap for the COVID-affected period (2020–2023) using a Welch’s t-test. This provides a more rigorous way to describe the "shift" in the gap than just looking at the final year, without violating the constraint against structural-break modeling.

**5. Missed Opportunity: The "Unknown" Category**
You excluded `Unknown` categories. While standard, in widening participation data, `Unknown` is often a proxy for specific types of disadvantage (e.g., data suppression for small, vulnerable groups).
*   **Action:** Briefly report the *size* of the `Unknown` group as a percentage of the total cohort over time. If the `Unknown` proportion is shrinking or growing, it could bias your trend estimates. A simple correlation between the `Unknown` proportion and the progression rate would suffice to rule out data-quality-driven trends.

**Summary for Future Iterations:**
The next iteration should focus on the "Counterfactual Check" (how many students are missing from high-tariff institutions) and the statistical comparison of the two slopes. This will move the analysis from "describing the gap" to "quantifying the institutional pipeline failure."


Iteration 0:
### Summary: Benchmarking Structural Inequality in English HE (2009/10–2022/23)

**Dataset & Methodology**
- **Source:** DfE official statistics (666 rows, 14 years).
- **Metrics:** Overall progression rate, High-Tariff progression rate, and "Conversion Ratio" (High-Tariff/Overall).
- **Uncertainty:** 95% Wilson score intervals for rates; propagated variance for gaps; Delta Method for ratios.
- **Trend Analysis:** Simple linear regression (slope + 95% CI) on annual gaps. 2020/21–2022/23 flagged as COVID-affected (descriptive only).
- **Exclusions:** `Unknown` categories removed from primary analysis.

**Key Findings**
1. **Overall HE Access:** POLAR Q5–Q1 absolute gap narrowed (slope: -0.328 pp/year, p<0.001). Relative ratio improved (2.85 to 1.96).
2. **High-Tariff Access:** Absolute POLAR gap widened (slope: +0.125 pp/year, p=0.008). Proportional inequality narrowed, but absolute exclusion remains persistent.
3. **Compounding Disadvantage:** A "selectivity penalty" exists; for POLAR, Q5 entrants are ~1.9x more likely than Q1 entrants to attend high-tariff providers.
4. **Benchmarking (2022/23):** POLAR is not the sole driver. Largest absolute gaps found in **Ethnicity Minor** (72.5 pp), **SEN Provision** (41.9 pp), and **Children in Need** (34.0 pp).

**Limitations & Constraints**
- **Trend Inference:** Limited to 14 annual points; no structural-break modeling or parity projections.
- **Data Sparsity:** Small cohorts in `Ethnicity Minor` and `Looked After Status` require cautious interpretation of extreme rankings.
- **COVID-19:** Recent years show persistent high-tariff gaps; these are descriptive observations, not evidence of a new structural regime.

**Strategic Guidance for Future Iterations**
- **Focus:** Future work should shift from "any HE" to the "Conversion Ratio" to isolate institutional selection bias from pre-HE attainment barriers.
- **Methodological Note:** The linear model is sufficient for broad trends, but residual analysis confirms it is a descriptive summary, not a predictive tool.
- **Next Steps:** Investigate the "selectivity penalty" across non-POLAR dimensions (e.g., SEN, Care status) to determine if the compounding effect is universal or specific to area-based disadvantage.
        
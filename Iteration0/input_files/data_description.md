## Dataset: Widening Participation in Higher Education — "All Characteristics" (DfE, real published data)

**File (absolute path — load exactly this):** `/Users/boris/Desktop/ucas-widening-participation/Iteration0/input_files/data/wp_all_characteristics.csv` (already present — load this; do NOT generate synthetic data). The analysis code runs from a different working directory, so always use this absolute path, never a relative one.

**Provenance:** UK Department for Education, *Widening participation in higher education* official statistics (2023-24 release), obtained from Explore Education Statistics (gov.uk). Permalink:
https://explore-education-statistics.service.gov.uk/data-catalogue/data-set/c3f0cae9-a2f7-4363-9d48-b7a410072a6f
Direct CSV: append `/csv` to that URL. **Licence:** Open Government Licence v3.0 (free to use/share with attribution).

**Coverage:** England, national level, academic years **2009/10 → 2022/23** (14 years). The statistic measures **progression to higher education by age 19** — i.e. the percentage of a state-school cohort who enter HE — broken down by pupil characteristic. 666 data rows, tidy long format, aggregate (rates + headcounts, no personal data).

### Schema (one row per year × characteristic-category)
- `time_period` — academic year as `YYYYYY` (e.g. `201920` = 2019/20)
- `time_identifier` — "Academic year"
- `geographic_level`, `country_code`, `country_name` — England, national
- `breakdown_topic` — the characteristic dimension. Values present:
  **POLAR** (area HE-participation quintile, the core WP measure), **Disadvantage** (FSM-based disadvantage flag), **FSM Status**, **Ethnicity Major**, **Ethnicity Minor**, **Sex**, **SEN Status**, **SEN Provision**, **Looked After Status**, **Children in Need**, **First Language**
- `breakdown` — the category within that topic, e.g. for POLAR: `Q1 - Most Disadvantaged`, `Q2`, `Q3`, `Q4`, `Q5 - Most Advantaged`, `Unknown`
- `progression_rate` — % of the cohort progressing to **any** HE (the headline access rate)
- `high_tariff_progression_rate` — % progressing to a **high-tariff** (selective) provider — the sharper equity measure
- `number_of_he_students` — count progressing to HE
- `number_of_high_tariff_he_students` — count progressing to high-tariff HE
- `number_of_students` — cohort size (denominator)

### Research aim (widening participation)
Quantify and explain access gaps in English HE progression across disadvantage measures, and track how they have changed over 14 years — with particular attention to the gap at **high-tariff** providers.

Questions of interest:
1. **POLAR gap over time:** how large is the Q1 (most disadvantaged) vs Q5 (most advantaged) gap in overall progression, and how has it changed 2009/10→2022/23? Is it narrowing, static, or widening?
2. **The high-tariff gap:** repeat (1) for `high_tariff_progression_rate`. The high-tariff gap is far wider in proportional terms (e.g. ~3% vs ~20%) — quantify the ratio and absolute gap, and its trend.
3. **Which characteristic divides most?** Compare gap magnitudes across POLAR, FSM/Disadvantage, ethnicity, sex, SEN and looked-after status. Rank the dimensions by equity gap.
4. **Compounding disadvantage:** for groups with both overall and high-tariff rates, show how disadvantage compounds as you move from "any HE" to "selective HE".
5. **Convergence test:** fit simple trend lines to the Q1–Q5 gap (overall and high-tariff) and test whether the gap is closing, and if so, at what rate / projected year of parity.

### Expected outputs
- Time-series gap plots: Q1 vs Q5 POLAR progression (overall and high-tariff) across cycles, with the absolute gap and gap ratio annotated.
- A ranked comparison of equity gaps across all breakdown topics for the latest year.
- A small trend/regression analysis of the gap over time (slope, significance, projected parity).
- A concise, policy-audience Results narrative grounded in the real figures.

### Notes for the analysis code
- Parse `time_period` (`YYYYYY`) into a readable cycle label and an integer year for trend fitting.
- Treat `Unknown` categories as a separate series; exclude from gap calculations unless explicitly analysing data quality.
- Rates are percentages already; headcounts let you compute weighted/pooled figures and confidence intervals where useful.

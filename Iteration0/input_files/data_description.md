## Dataset: UCAS-style Higher Education Applications (synthetic, demo)

A synthetic, privacy-safe dataset modelled on UCAS undergraduate admissions, designed for a "widening participation" (WP) equity analysis. No real personal data — rows are simulated applicants drawn from realistic UK marginal distributions. If a real CSV is provided at `Iteration0/input_files/data/applications.csv`, use it instead; otherwise the analysis code should first generate this synthetic table (~50,000 applicants across 5 application cycles) and save it to that path.

### Schema (one row per application)
- `applicant_id`: anonymised unique id
- `cycle_year`: application cycle (2020–2024)
- `region`: UK region (e.g. North East, London, Scotland, Wales, ...)
- `polar4_quintile`: POLAR4 area participation quintile, 1 (lowest HE participation) to 5 (highest). The core WP measure.
- `imd_quintile`: Index of Multiple Deprivation quintile, 1 (most deprived) to 5 (least deprived)
- `free_school_meals`: eligible for free school meals (0/1) — disadvantage proxy
- `first_in_family`: first generation to apply to HE (0/1)
- `school_type`: state comprehensive / state selective / independent / FE college
- `ethnicity_group`: aggregated ethnicity grouping
- `sex`: applicant sex
- `disability_declared`: declared disability (0/1)
- `predicted_grades_points`: UCAS tariff points from predicted A-level/equivalent grades
- `achieved_grades_points`: UCAS tariff points from achieved grades
- `subject_group`: applied subject area (e.g. Medicine, Engineering, Law, Creative Arts, ...)
- `provider_tariff`: tariff group of the applied provider (higher / medium / lower tariff)
- `offer_made`: provider made an offer (0/1)
- `offer_accepted`: applicant firmly accepted (0/1)
- `enrolled`: applicant enrolled (0/1) — final admission outcome

### Research aim (widening participation)
Quantify and explain access gaps in UK undergraduate admissions across disadvantage measures, and identify where in the funnel (offer → acceptance → enrolment) inequity arises.

Questions of interest:
1. How do offer, acceptance, and enrolment rates vary by POLAR4 quintile, IMD quintile, FSM eligibility, and first-in-family status — and how have these gaps changed across the 2020–2024 cycles?
2. After controlling for predicted/achieved attainment (tariff points), how much of the access gap remains attributable to background — i.e. the conditional WP gap, especially at higher-tariff providers?
3. Which stage of the funnel contributes most to the overall enrolment gap for disadvantaged groups?
4. Can a calibrated model predict enrolment from applicant attributes, and which features drive predicted access disparities (with fairness/equity diagnostics across protected groups)?

### Expected outputs
- Funnel and gap plots (offer/acceptance/enrolment rates by quintile and cycle, with confidence intervals).
- A regression / logistic model of enrolment with attainment controls, reporting the residual conditional WP gap and effect sizes.
- A fairness diagnostic (e.g. rate differences / ratios across POLAR4 and FSM groups) on the predictive model.
- A concise Results narrative suitable for a policy audience.

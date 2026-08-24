# E-commerce A/B Testing & Funnel Analytics

Portfolio project demonstrating A/B testing, SQL funnel analysis, statistical inference and experiment analytics.

> **Data disclosure:** All data is synthetic and generated for this portfolio project. It is not a real company/client experiment.

## Objective
Test whether a redesigned e-commerce journey improves CTR, conversion, repeat purchase, engagement and revenue per user.

## Experiment
- 12,000 synthetic users
- 50:50 randomized Control (A) / Treatment (B)
- Primary KPI: purchase conversion
- Secondary KPIs: CTR, repeat purchase, engagement, revenue/user
- Statistical method: two-proportion z-test, alpha = 0.05

## Workflow
Synthetic data → Python → SQL → Funnel analysis → Statistical testing → Dashboard

## Run
```bash
pip install -r requirements.txt
python src/analysis.py
```

Outputs are written to `outputs/`.

## SQL
Import `data/users.csv` and `data/events.csv` into SQLite/PostgreSQL and run `sql/analysis_queries.sql`.

## Dashboard
Build the dashboard from `users.csv` with KPI cards for conversion, uplift, repeat purchase, revenue/user and p-value; plus funnel, device and channel breakdowns.

## Skills
**Python · SQL · A/B Testing · Statistical Testing · Funnel Analysis · Experiment Design · Excel · Data Visualization · Product Analytics**

## Resume-safe description
> Designed and simulated A/B tests on 10K+ e-commerce users, analyzing CTR, conversion, retention and engagement using SQL, Python and Excel.

Do not present synthetic results as production/client results.

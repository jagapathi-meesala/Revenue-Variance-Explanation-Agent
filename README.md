# Revenue Variance Explanation Agent

A small, explainable Python agent for comparing actual revenue with a baseline and organizing user-supplied variance drivers. It does not connect to financial systems or invent business explanations.

## Run
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
python3 verification/readiness_audit.py
python3 -m core.cli examples/revenue_case.json --output report.json
```

## Input format
`actual_revenue`, `comparison_revenue`, `currency`, `actual_period`, `comparison_period`, and optional `drivers` array. Each driver has `name`, signed `amount`, and optional `evidence`.

## Interpretation
Variance = actual - comparison. Variance percent = variance / comparison * 100, when comparison is non-zero. Driver residual = total variance - sum(supplied driver amounts). Drivers are not independently verified. Outputs are decision support, not audited financial statements.

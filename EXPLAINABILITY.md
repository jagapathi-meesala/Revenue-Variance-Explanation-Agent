# Explainability

## Inputs
The agent consumes user-supplied actual revenue, comparison revenue, currency, period labels, and optional signed driver amounts with evidence notes.

## Decision
It subtracts comparison revenue from actual revenue, calculates percentage variance when the comparison value is non-zero, sums supplied drivers, and calculates the unexplained residual. It labels results using explicit numeric thresholds only for direction, not business significance.

## Limits
It cannot verify source systems, determine accounting treatment, prove causation, or infer missing drivers. Currency, periods, revenue recognition basis, and driver signs must be reviewed by a finance owner.

## Tool: calculate-revenue-variance
### Inputs and Data Sources
Actual and comparison revenue from the supplied case.
### Decision and Reasoning
Subtract comparison revenue from actual revenue and divide by comparison revenue for the percentage when non-zero.
### Outputs and Evidence
Absolute and percentage variance, including the input values used.
### Limits and Constraints
No source-system verification or currency conversion.
### Failure Handling
Reject missing, non-numeric, or invalid required values.
### Human Review
Confirm period alignment and accounting basis.

## Tool: analyze-revenue-drivers
### Inputs and Data Sources
User-provided signed driver amounts and evidence notes.
### Decision and Reasoning
Sum the supplied driver amounts and compare their total with the computed variance.
### Outputs and Evidence
Driver contributions, total explained amount, and residual.
### Limits and Constraints
No automatic causal inference; driver amounts may overlap or omit factors.
### Failure Handling
Flag malformed driver records and preserve residuals.
### Human Review
Validate drivers against sales, pricing, volume, mix, returns, and ledger evidence as appropriate.

## Tool: build-variance-report
### Inputs and Data Sources
Validated variance calculations and driver analysis.
### Decision and Reasoning
Assemble a report with period labels, calculation evidence, driver breakdown, residual, and caveats.
### Outputs and Evidence
JSON report suitable for review.
### Limits and Constraints
Does not certify results or make external disclosures.
### Failure Handling
Return clear validation errors for invalid inputs.
### Human Review
Obtain finance-owner approval before publishing.

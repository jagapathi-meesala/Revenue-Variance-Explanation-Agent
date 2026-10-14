from __future__ import annotations


def analyze_case(case: dict) -> dict:
    required = ("actual_revenue", "comparison_revenue", "currency", "actual_period", "comparison_period")
    missing = [key for key in required if key not in case]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    try:
        actual = float(case["actual_revenue"])
        comparison = float(case["comparison_revenue"])
    except (TypeError, ValueError):
        raise ValueError("Revenue amounts must be numeric")
    if actual < 0 or comparison < 0:
        raise ValueError("Revenue amounts must be non-negative")
    if not isinstance(case["currency"], str) or not case["currency"].strip():
        raise ValueError("currency must be a non-empty string")

    variance = actual - comparison
    percent = (variance / comparison * 100.0) if comparison != 0 else None
    drivers = case.get("drivers", [])
    if not isinstance(drivers, list):
        raise ValueError("drivers must be a list")
    normalized = []
    for index, driver in enumerate(drivers):
        if not isinstance(driver, dict) or "name" not in driver or "amount" not in driver:
            raise ValueError(f"Driver at index {index} must include name and amount")
        try:
            amount = float(driver["amount"])
        except (TypeError, ValueError):
            raise ValueError(f"Driver amount at index {index} must be numeric")
        normalized.append({"name": str(driver["name"]), "amount": amount, "evidence": str(driver.get("evidence", "Not supplied"))})
    explained = sum(d["amount"] for d in normalized)
    residual = variance - explained
    return {
        "agent": "revenue-variance-explanation-agent",
        "periods": {"actual": str(case["actual_period"]), "comparison": str(case["comparison_period"])},
        "currency": case["currency"],
        "actual_revenue": actual,
        "comparison_revenue": comparison,
        "variance": variance,
        "variance_percent": percent,
        "direction": "increase" if variance > 0 else "decrease" if variance < 0 else "unchanged",
        "drivers": normalized,
        "explained_driver_total": explained,
        "unexplained_residual": residual,
        "driver_reconciliation_status": "reconciled" if abs(residual) < 0.005 else "residual_remains",
        "interpretation": "Driver descriptions are supplied explanations, not independently verified causes.",
        "review_actions": ["Confirm periods and currency use the same accounting basis.", "Validate each driver against source reports.", "Review any unexplained residual and possible overlapping drivers."],
    }

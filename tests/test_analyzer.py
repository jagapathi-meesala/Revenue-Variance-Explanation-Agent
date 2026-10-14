import pytest
from core.analyzer import analyze_case

BASE = {"actual_revenue": 125, "comparison_revenue": 100, "currency": "USD", "actual_period": "Q2", "comparison_period": "Q1"}

def test_variance_and_percent():
    result = analyze_case(BASE)
    assert result["variance"] == 25
    assert result["variance_percent"] == 25
    assert result["direction"] == "increase"

def test_driver_residual():
    result = analyze_case({**BASE, "drivers": [{"name": "Volume", "amount": 20}]})
    assert result["explained_driver_total"] == 20
    assert result["unexplained_residual"] == 5
    assert result["driver_reconciliation_status"] == "residual_remains"

def test_reconciled_drivers():
    result = analyze_case({**BASE, "drivers": [{"name": "Volume", "amount": 25}]})
    assert result["driver_reconciliation_status"] == "reconciled"

def test_zero_comparison_has_no_percentage():
    result = analyze_case({**BASE, "comparison_revenue": 0})
    assert result["variance_percent"] is None

def test_missing_required_field():
    with pytest.raises(ValueError, match="Missing required"):
        analyze_case({"actual_revenue": 5})

def test_negative_revenue_rejected():
    with pytest.raises(ValueError, match="non-negative"):
        analyze_case({**BASE, "actual_revenue": -1})

def test_bad_driver_rejected():
    with pytest.raises(ValueError, match="must include name and amount"):
        analyze_case({**BASE, "drivers": [{"name": "Volume"}]})

def test_bad_driver_amount_rejected():
    with pytest.raises(ValueError, match="must be numeric"):
        analyze_case({**BASE, "drivers": [{"name": "Volume", "amount": "many"}]})

def test_bad_currency_rejected():
    with pytest.raises(ValueError, match="currency"):
        analyze_case({**BASE, "currency": " "})

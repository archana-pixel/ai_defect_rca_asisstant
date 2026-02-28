from app.rca_engine import RCAEngine

def test_rca():
    engine = RCAEngine()
    result = engine.analyze_failure("Login failing due to timeout")
    assert "Root Cause" in result
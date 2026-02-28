from app.rca_engine import RCAEngine

# Example failure log
test_log = """
2026-02-28 12:00:00 ERROR 500 Internal Server Error
Request failed for endpoint /api/orders
"""

# Initialize RCA engine
engine = RCAEngine()

# Run RCA analysis
result = engine.analyze_failure(test_log)

# Print output
print("\n===== SAMPLE RCA OUTPUT =====\n")
print(result)
print("\n=============================\n")
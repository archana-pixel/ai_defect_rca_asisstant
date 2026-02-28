from app.rca_engine import RCAEngine

test_log = """
2026-02-28 12:00:00 ERROR 500 Internal Server Error
Request failed for endpoint /api/orders
"""

# Initialize RCA engine WITHOUT Jira
engine = RCAEngine(use_jira=False)

result = engine.analyze_failure(test_log)

print("\n===== SAMPLE RCA OUTPUT =====\n")
print(result)
print("\n=============================\n")
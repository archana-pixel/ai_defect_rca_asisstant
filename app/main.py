from rca_engine import RCAEngine

if __name__ == "__main__":
    engine = RCAEngine()
    new_log = input("Enter new failure log: ")
    result = engine.analyze_failure(new_log)
    print("\nSuggested Root Cause:\n", result)
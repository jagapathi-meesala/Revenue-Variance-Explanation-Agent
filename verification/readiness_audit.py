from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["agent.yaml", "README.md", "SOUL.md", "RULES.md", "DUTIES.md", "AGENTS.md", "EXPLAINABILITY.md", "requirements.txt", "core/analyzer.py", "core/cli.py", "tests/test_analyzer.py", "examples/revenue_case.json"]
missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
if missing:
    print("FAIL: missing files:", ", ".join(missing)); sys.exit(1)
print(f"PASS: all {len(REQUIRED)}/{len(REQUIRED)} required files present")

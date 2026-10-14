import argparse
import json
from pathlib import Path
from .analyzer import analyze_case


def main():
    parser = argparse.ArgumentParser(description="Analyze a revenue variance case")
    parser.add_argument("case", help="Path to input JSON case")
    parser.add_argument("--output", help="Optional output JSON path")
    args = parser.parse_args()
    try:
        case = json.loads(Path(args.case).read_text(encoding="utf-8"))
        result = analyze_case(case)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    rendered = json.dumps(result, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)

if __name__ == "__main__":
    main()

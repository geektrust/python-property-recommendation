import json
import sys
from typing import Any, Dict, List

from main import Main


def call_main():
    """
        ***********************************************
        * This is the driver code. Don't change it!!!
        * *********************************************

        Format of the 'args' array: `<Input 1> <Input 2> <Input 3>`
        Example: ["Input1 Input2 Input3"]

        The code evaluator will execute this code by using the command:
        python main.py "Input1 Input2 Input3"

        So the value of the variable 'input' given below will be the string: "Input1 Input2 Input3"
    """
    if len(sys.argv) < 2:
        raise ValueError("No command line arguments passed")

    commands = sys.argv[1:]
    main = Main()

    for command in commands:
        data = convert_input(command)
        output = main.recommend_properties(
            data["properties"],
            data["events"],
            data["top_n"],
        )
        norm_output = _normalize(output)
        print(json.dumps(norm_output))


def convert_input(input_str: str) -> Dict[str, Any]:
    result: Dict[str, Any] = json.loads(input_str)
    return result


def _normalize(records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Normalize records for comparison: sort users and round scores."""
    normalized = []
    for r in records:
        norm_recs = []
        for rec in r.get("recommendations", []):
            norm_recs.append({
                "property_id": rec["property_id"],
                "score": round(rec["score"], 6),
            })
        normalized.append({
            "user_id": r["user_id"],
            "recommendations": norm_recs,
        })
    return sorted(normalized, key=lambda x: x["user_id"])


if __name__ == "__main__":
    call_main()

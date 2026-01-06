from pathlib import Path

import json

BASE_DIR = Path(__file__).parent

def generate_report():
    # generate report data
    dt = {
        "timestamp": "2025-12-31 12-37-37",
        "status": "PASSED",
        "summary": "module.py::test_case"
    }

    # open json file
    # in writing mode
    with open(BASE_DIR / "report.json", "w") as file:
        # write data to json file
        json.dump(dt, file)
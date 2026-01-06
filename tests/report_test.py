from app.report import generate_report
from pathlib import Path

import json
import pytest

@pytest.fixture(scope="session")
def report_json():
    report_path = Path(__file__).parents[1] / "app" / "report.json"
    
    generate_report()

    with open(report_path) as file:
        return json.load(file)


def test_report_json(report_json):
    assert type(report_json) == dict


def test_report_fields(report_json):
    assert "timestamp" in report_json
    assert "status" in report_json
    assert "summary" in report_json


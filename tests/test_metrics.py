import pandas as pd

from src.etl.extract import load_pos_sales, load_price_events
from src.etl.load import export_metric_results_to_csv, prepare_metric_results
from src.etl.transform import normalize_price_events
from src.metrics.calculator import (
    calculate_avg_print_delay_minutes,
    calculate_price_mismatch_count,
    calculate_repeated_print_count,
    calculate_successful_print_rate,
)
from src.quality.checks import validate_price_events


def test_calculate_avg_print_delay_minutes():
    price_events = normalize_price_events(load_price_events())
    result = calculate_avg_print_delay_minutes(price_events)

    assert result == 18.5


def test_calculate_successful_print_rate():
    price_events = normalize_price_events(load_price_events())
    result = calculate_successful_print_rate(price_events)

    assert result == 66.67


def test_calculate_repeated_print_count():
    price_events = normalize_price_events(load_price_events())
    result = calculate_repeated_print_count(price_events)

    assert result == 1


def test_validate_empty_price_events():
    empty_df = pd.DataFrame()
    result = validate_price_events(empty_df)

    assert "Набор данных пустой" in result


def test_calculate_price_mismatch_count():
    price_events = normalize_price_events(load_price_events())
    pos_sales = load_pos_sales()

    result = calculate_price_mismatch_count(price_events, pos_sales)

    assert result == 1


def test_prepare_metric_results():
    metrics = {
        "avg_print_delay_minutes": 18.5,
        "successful_print_rate": 66.67,
    }

    result = prepare_metric_results(metrics)

    assert list(result.columns) == ["metric_code", "metric_value"]
    assert len(result) == 2


def test_export_metric_results_to_csv(tmp_path):
    metrics = {
        "avg_print_delay_minutes": 18.5,
        "successful_print_rate": 66.67,
    }

    output_file = tmp_path / "metric_results.csv"
    result = export_metric_results_to_csv(metrics, output_file)

    assert result.exists()
    assert result.name == "metric_results.csv"
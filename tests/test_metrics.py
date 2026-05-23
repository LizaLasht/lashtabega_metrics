from src.etl.extract import load_price_events
from src.etl.transform import normalize_price_events
from src.metrics.calculator import (
    calculate_avg_print_delay_minutes,
    calculate_repeated_print_count,
    calculate_successful_print_rate,
)


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
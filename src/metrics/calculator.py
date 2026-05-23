import pandas as pd

from src.metrics.registry import METRIC_REGISTRY


def calculate_avg_print_delay_minutes(price_events: pd.DataFrame) -> float:
    """Расчёт среднего времени между изменением цены и печатью ценника."""
    completed_events = price_events.dropna(subset=["printed_at"]).copy()

    if completed_events.empty:
        return 0.0

    delay = completed_events["printed_at"] - completed_events["event_time"]
    return round(delay.dt.total_seconds().mean() / 60, 2)


def calculate_successful_print_rate(price_events: pd.DataFrame) -> float:
    """Расчёт доли событий, по которым ценник был напечатан."""
    if price_events.empty:
        return 0.0

    success_count = price_events["printed_at"].notna().sum()
    return round(success_count / len(price_events) * 100, 2)


def calculate_repeated_print_count(price_events: pd.DataFrame) -> int:
    """Расчёт количества повторных печатей ценников."""
    return int((price_events["event_type"] == "reprint").sum())


def calculate_all_metrics(price_events: pd.DataFrame) -> dict[str, float | int]:
    """Расчёт всех реализованных продуктовых метрик."""
    return {
        "avg_print_delay_minutes": calculate_avg_print_delay_minutes(price_events),
        "successful_print_rate": calculate_successful_print_rate(price_events),
        "repeated_print_count": calculate_repeated_print_count(price_events),
    }


def describe_metrics() -> dict:
    """Получение описания реализованных метрик."""
    return METRIC_REGISTRY
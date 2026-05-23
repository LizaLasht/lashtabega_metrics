from fastapi import FastAPI

from src.etl.extract import load_price_events
from src.etl.transform import normalize_price_events
from src.metrics.calculator import calculate_all_metrics, describe_metrics
from src.quality.checks import validate_price_events

app = FastAPI(title="Price Metrics API")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "service": "price metrics",
        "status": "ok",
    }


@app.get("/metrics")
def get_metrics() -> dict:
    price_events = normalize_price_events(load_price_events())
    errors = validate_price_events(price_events)

    if errors:
        return {
            "status": "error",
            "errors": errors,
        }

    return {
        "status": "ok",
        "metrics": calculate_all_metrics(price_events),
    }


@app.get("/metrics/registry")
def get_metric_registry() -> dict:
    return describe_metrics()
from fastapi import FastAPI

from src.etl.extract import load_pos_sales, load_price_events
from src.etl.load import export_metric_results_to_csv
from src.etl.transform import normalize_pos_sales, normalize_price_events
from src.metrics.calculator import calculate_all_metrics, describe_metrics
from src.quality.checks import validate_price_events

app = FastAPI(
    title="API расчёта продуктовых метрик",
    description=(
        "Сервис для расчёта продуктовых метрик сервиса управления ценниками. "
        "API позволяет проверить доступность сервиса, получить рассчитанные метрики "
        "и посмотреть реестр реализованных метрик."
    ),
    version="0.1.0",
    openapi_tags=[
        {
            "name": "Основные методы",
            "description": "Методы для проверки сервиса и получения рассчитанных метрик",
        }
    ],
)


@app.get(
    "/",
    tags=["Основные методы"],
    summary="Проверка доступности сервиса",
    description="Возвращает статус работы API.",
)
def root() -> dict[str, str]:
    return {
        "service": "price metrics",
        "status": "ok",
    }


@app.get(
    "/metrics",
    tags=["Основные методы"],
    summary="Получить рассчитанные продуктовые метрики",
    description=(
        "Выполняет загрузку тестовых данных из витрины price, "
        "нормализацию, проверку качества и расчёт продуктовых метрик."
    ),
)
def get_metrics() -> dict:
    price_events = normalize_price_events(load_price_events())
    pos_sales = normalize_pos_sales(load_pos_sales())
    errors = validate_price_events(price_events)

    if errors:
        return {
            "status": "error",
            "errors": errors,
        }

    return {
        "status": "ok",
        "metrics": calculate_all_metrics(price_events, pos_sales),
    }


@app.get(
    "/metrics/registry",
    tags=["Основные методы"],
    summary="Получить реестр метрик",
    description="Возвращает описание реализованных продуктовых метрик.",
)
def get_metric_registry() -> dict:
    return describe_metrics()


@app.get(
    "/metrics/export",
    tags=["Основные методы"],
    summary="Экспортировать рассчитанные метрики в CSV",
    description=(
        "Выполняет расчёт продуктовых метрик и сохраняет результат "
        "в CSV-файл metric_results.csv."
    ),
)
def export_metrics() -> dict:
    price_events = normalize_price_events(load_price_events())
    pos_sales = normalize_pos_sales(load_pos_sales())
    errors = validate_price_events(price_events)

    if errors:
        return {
            "status": "error",
            "errors": errors,
        }

    metrics = calculate_all_metrics(price_events, pos_sales)
    output_path = export_metric_results_to_csv(metrics)

    return {
        "status": "ok",
        "file": str(output_path),
        "metrics_count": len(metrics),
    }
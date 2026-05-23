from pathlib import Path

import pandas as pd


def prepare_metric_results(metrics: dict[str, float | int]) -> pd.DataFrame:
    """Подготовка рассчитанных метрик к сохранению."""
    rows = []

    for metric_code, metric_value in metrics.items():
        rows.append(
            {
                "metric_code": metric_code,
                "metric_value": metric_value,
            }
        )

    return pd.DataFrame(rows)


def export_metric_results_to_csv(
    metrics: dict[str, float | int],
    file_path: str | Path = "metric_results.csv",
) -> Path:
    """Экспорт рассчитанных метрик в CSV-файл."""
    output_path = Path(file_path)
    metric_results = prepare_metric_results(metrics)

    metric_results.to_csv(output_path, index=False, encoding="utf-8-sig")

    return output_path
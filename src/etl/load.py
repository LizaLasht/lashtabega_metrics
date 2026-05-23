import pandas as pd


def prepare_metric_results(metrics: dict[str, float | int]) -> pd.DataFrame:
    
    rows = []

    for metric_code, metric_value in metrics.items():
        rows.append(
            {
                "metric_code": metric_code,
                "metric_value": metric_value,
            }
        )

    return pd.DataFrame(rows)
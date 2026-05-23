import pandas as pd


def check_empty_dataframe(df: pd.DataFrame) -> list[str]:
    """Проверка наличия данных для обработки."""
    if df.empty:
        return ["Набор данных пустой"]
    return []


def check_required_fields(df: pd.DataFrame, fields: list[str]) -> list[str]:
    """Проверка наличия обязательных полей и пустых значений."""
    errors = []

    for field in fields:
        if field not in df.columns:
            errors.append(f"Отсутствует обязательное поле: {field}")
        elif df[field].isna().any():
            errors.append(f"Есть пустые значения в поле: {field}")

    return errors


def check_price_values(df: pd.DataFrame) -> list[str]:
    """Проверка корректности цен."""
    errors = []

    price_columns = [
        column for column in ["old_price", "new_price", "sale_price"]
        if column in df.columns
    ]

    for column in price_columns:
        if (df[column].dropna() < 0).any():
            errors.append(f"Обнаружены отрицательные значения цены в поле: {column}")

    return errors


def check_timestamps(df: pd.DataFrame) -> list[str]:
    """Проверка временных меток."""
    errors = []

    if "event_time" in df.columns and df["event_time"].isna().any():
        errors.append("Есть некорректные временные метки event_time")

    if {"event_time", "printed_at"}.issubset(df.columns):
        invalid = df["printed_at"].notna() & (df["printed_at"] < df["event_time"])
        if invalid.any():
            errors.append("Есть события, где printed_at меньше event_time")

    return errors


def validate_price_events(df: pd.DataFrame) -> list[str]:
    """Общая проверка данных витрины price."""
    errors = []

    errors.extend(check_empty_dataframe(df))
    errors.extend(check_required_fields(df, ["sku", "store_code", "new_price", "event_time"]))
    errors.extend(check_price_values(df))
    errors.extend(check_timestamps(df))

    return errors
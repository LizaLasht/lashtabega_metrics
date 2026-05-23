import pandas as pd


def normalize_price_events(df: pd.DataFrame) -> pd.DataFrame:
    
    result = df.copy()

    result["event_time"] = pd.to_datetime(result["event_time"], errors="coerce")
    result["printed_at"] = pd.to_datetime(result["printed_at"], errors="coerce")

    result["sku"] = result["sku"].astype(str).str.strip()
    result["store_code"] = result["store_code"].astype(str).str.strip()

    result = result.drop_duplicates()

    return result


def normalize_pos_sales(df: pd.DataFrame) -> pd.DataFrame:
    
    result = df.copy()

    result["sku"] = result["sku"].astype(str).str.strip()
    result["store_code"] = result["store_code"].astype(str).str.strip()
    result["quantity"] = pd.to_numeric(result["quantity"], errors="coerce")
    result["sale_price"] = pd.to_numeric(result["sale_price"], errors="coerce")

    result = result.drop_duplicates()

    return result
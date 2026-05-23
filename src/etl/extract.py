import pandas as pd


def load_price_events() -> pd.DataFrame:
    
    return pd.DataFrame(
        [
            {
                "sku": "100001",
                "store_code": "S001",
                "old_price": 99.90,
                "new_price": 109.90,
                "event_type": "price_change",
                "print_reason": "regular_price_update",
                "event_time": "2026-01-10 10:00:00",
                "printed_at": "2026-01-10 10:12:00",
            },
            {
                "sku": "100002",
                "store_code": "S001",
                "old_price": 199.90,
                "new_price": 189.90,
                "event_type": "reprint",
                "print_reason": "damaged_label",
                "event_time": "2026-01-10 11:00:00",
                "printed_at": "2026-01-10 11:25:00",
            },
            {
                "sku": "100003",
                "store_code": "S002",
                "old_price": 79.90,
                "new_price": 79.90,
                "event_type": "price_change",
                "print_reason": "promo_update",
                "event_time": "2026-01-10 12:00:00",
                "printed_at": None,
            },
        ]
    )


def load_pos_sales() -> pd.DataFrame:
    
    return pd.DataFrame(
        [
            {"sku": "100001", "store_code": "S001", "sale_price": 109.90, "quantity": 1},
            {"sku": "100002", "store_code": "S001", "sale_price": 199.90, "quantity": 2},
            {"sku": "100003", "store_code": "S002", "sale_price": 79.90, "quantity": 1},
        ]
    )
METRIC_REGISTRY = {
    "avg_print_delay_minutes": {
        "name": "Среднее время печати ценника",
        "description": "Среднее время между изменением цены и печатью ценника в минутах",
        "source": "price_events",
        "status": "implemented",
    },
    "successful_print_rate": {
        "name": "Доля успешно напечатанных ценников",
        "description": "Доля событий, по которым есть время печати ценника",
        "source": "price_events",
        "status": "implemented",
    },
    "repeated_print_count": {
        "name": "Количество повторных печатей",
        "description": "Количество событий повторной печати ценников",
        "source": "price_events",
        "status": "implemented",
    },
    "price_mismatch_count": {
        "name": "Количество ценовых расхождений",
        "description": "Количество случаев, когда цена продажи из POS отличается от новой цены из витрины price",
        "source": "price_events, pos_sales",
        "status": "implemented",
    },
}
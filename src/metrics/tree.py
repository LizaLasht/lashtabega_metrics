METRIC_TREE = {
    "price_label_service": {
        "name": "Сервис управления ценниками",
        "children": {
            "printing_quality": {
                "name": "Качество печати ценников",
                "metrics": [
                    "successful_print_rate",
                    "repeated_print_count",
                ],
            },
            "processing_time": {
                "name": "Временные показатели",
                "metrics": [
                    "avg_print_delay_minutes",
                ],
            },
        },
    }
}
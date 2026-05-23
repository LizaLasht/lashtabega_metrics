SET search_path TO price_metrics;

-- Среднее время между изменением цены и печатью ценника
SELECT
    AVG(EXTRACT(EPOCH FROM (printed_at - event_time)) / 60) AS avg_print_delay_minutes
FROM price_events
WHERE printed_at IS NOT NULL;

-- Доля успешно напечатанных ценников
SELECT
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE printed_at IS NOT NULL) / NULLIF(COUNT(*), 0),
        2
    ) AS successful_print_rate
FROM price_events;

-- Количество повторных печатей ценников
SELECT
    COUNT(*) AS repeated_print_count
FROM price_events
WHERE event_type = 'reprint';

-- Количество потенциальных ценовых расхождений
SELECT
    COUNT(*) AS price_mismatch_count
FROM price_events pe
JOIN pos_sales ps
    ON ps.product_id = pe.product_id
   AND ps.store_id = pe.store_id
WHERE ps.sale_time >= pe.event_time
  AND ps.sale_price <> pe.new_price;
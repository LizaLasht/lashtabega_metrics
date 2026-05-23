SET search_path TO price_metrics;

CREATE OR REPLACE VIEW vw_price_events_prepared AS
SELECT
    pe.event_id,
    p.sku,
    p.product_name,
    p.category_name,
    s.store_code,
    s.store_name,
    s.region_name,
    pe.old_price,
    pe.new_price,
    pe.event_type,
    pe.print_reason,
    pe.event_time,
    pe.printed_at,
    EXTRACT(EPOCH FROM (pe.printed_at - pe.event_time)) / 60 AS print_delay_minutes
FROM price_events pe
JOIN products p ON p.product_id = pe.product_id
JOIN stores s ON s.store_id = pe.store_id;

CREATE OR REPLACE VIEW vw_metric_results AS
SELECT
    mr.result_id,
    rg.metric_code,
    rg.metric_name,
    st.store_code,
    st.store_name,
    pr.sku,
    pr.product_name,
    mr.metric_value,
    mr.calculated_at
FROM metric_results mr
JOIN metric_registry rg ON rg.metric_id = mr.metric_id
LEFT JOIN stores st ON st.store_id = mr.store_id
LEFT JOIN products pr ON pr.product_id = mr.product_id;
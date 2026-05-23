CREATE SCHEMA IF NOT EXISTS price_metrics;

SET search_path TO price_metrics;

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    sku VARCHAR(50) NOT NULL UNIQUE,
    product_name VARCHAR(255) NOT NULL,
    category_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE stores (
    store_id SERIAL PRIMARY KEY,
    store_code VARCHAR(50) NOT NULL UNIQUE,
    store_name VARCHAR(255) NOT NULL,
    region_name VARCHAR(255)
);

CREATE TABLE price_events (
    event_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    store_id INTEGER REFERENCES stores(store_id),
    old_price NUMERIC(10,2),
    new_price NUMERIC(10,2) NOT NULL,
    event_type VARCHAR(100),
    print_reason VARCHAR(255),
    event_time TIMESTAMP NOT NULL,
    printed_at TIMESTAMP
);

CREATE TABLE pos_sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(product_id),
    store_id INTEGER REFERENCES stores(store_id),
    sale_time TIMESTAMP NOT NULL,
    quantity INTEGER,
    sale_price NUMERIC(10,2)
);

CREATE TABLE metric_registry (
    metric_id SERIAL PRIMARY KEY,
    metric_code VARCHAR(100) UNIQUE NOT NULL,
    metric_name VARCHAR(255) NOT NULL,
    metric_description TEXT,
    source_table VARCHAR(100),
    status VARCHAR(50)
);

CREATE TABLE metric_tree (
    node_id SERIAL PRIMARY KEY,
    parent_node_id INTEGER REFERENCES metric_tree(node_id),
    node_name VARCHAR(255) NOT NULL
);

CREATE TABLE metric_results (
    result_id SERIAL PRIMARY KEY,
    metric_id INTEGER REFERENCES metric_registry(metric_id),
    product_id INTEGER REFERENCES products(product_id),
    store_id INTEGER REFERENCES stores(store_id),
    metric_value NUMERIC(12,4),
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE event_store (
    system_event_id SERIAL PRIMARY KEY,
    event_level VARCHAR(50),
    event_source VARCHAR(100),
    event_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
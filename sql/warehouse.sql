-- FACT TABLE
CREATE TABLE fact_sales AS
SELECT 
    oi.order_id,
    oi.product_id,
    oi.seller_id,
    oi.price,
    oi.freight_value,
    o.customer_id,
    o.order_purchase_timestamp,
    p.payment_value
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN payments p ON oi.order_id = p.order_id;

-- DIM CUSTOMERS
CREATE TABLE dim_customers AS
SELECT DISTINCT
    customer_id,
    customer_city,
    customer_state
FROM customers;

-- DIM PRODUCTS
CREATE TABLE dim_products AS
SELECT 
    product_id,
    product_category_name,
    product_weight_g
FROM products;
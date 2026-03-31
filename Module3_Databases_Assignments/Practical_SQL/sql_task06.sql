-- SQL Task 6
-- Calculate the average product price.
-- Return: average product price

-- Table Reference: products(product_id, product_name, price, category)
-- (Also commonly: item_mast(PRO_ID, PRO_NAME, PRO_PRICE, PRO_COM))

-- Standard products table:
SELECT AVG(price) AS avg_product_price
FROM   products;

-- ── Alternative if using item_mast table ──
-- SELECT AVG(PRO_PRICE) AS avg_product_price
-- FROM   item_mast;

-- Explanation:
-- AVG() computes the arithmetic mean of all non-NULL values in the price column.
-- The result is aliased as 'avg_product_price'.

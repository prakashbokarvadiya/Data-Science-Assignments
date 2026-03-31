-- SQL Task 4
-- Calculate the total purchase amount of all orders.
-- Return: total purchase amount

-- Table Reference: orders(ord_no, purch_amt, ord_date, customer_id, salesman_id)

SELECT SUM(purch_amt) AS total_purchase_amount
FROM   orders;

-- Explanation:
-- SUM() is an aggregate function that adds all values in the purch_amt column.
-- The result is aliased as 'total_purchase_amount' for clarity.
-- No WHERE clause → all orders are included.

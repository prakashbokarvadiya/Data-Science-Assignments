-- SQL Task 5
-- Find the highest purchase amount ordered by each customer.
-- Return: customer_id, maximum purchase amount

-- Table Reference: orders(ord_no, purch_amt, ord_date, customer_id, salesman_id)

SELECT customer_id,
       MAX(purch_amt) AS max_purchase_amount
FROM   orders
GROUP  BY customer_id
ORDER  BY customer_id;

-- Explanation:
-- GROUP BY customer_id groups all orders belonging to the same customer.
-- MAX(purch_amt) returns the single highest purchase amount within each group.
-- ORDER BY customer_id presents results in a predictable, sorted order.

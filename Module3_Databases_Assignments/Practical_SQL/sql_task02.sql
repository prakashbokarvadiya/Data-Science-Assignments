-- SQL Task 2
-- Find all customers in 'New York' who have a grade value above 100.
-- Return: customer_id, cust_name, city, grade, salesman_id

-- Table Reference: customer(customer_id, cust_name, city, grade, salesman_id)

SELECT customer_id,
       cust_name,
       city,
       grade,
       salesman_id
FROM   customer
WHERE  city  = 'New York'
  AND  grade > 100;

-- Explanation:
-- The AND condition requires BOTH conditions to be true simultaneously:
--   1. city must be 'New York'
--   2. grade must be strictly greater than 100
-- Only customers satisfying both conditions are returned.

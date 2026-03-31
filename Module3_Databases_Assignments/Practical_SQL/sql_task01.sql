-- SQL Task 1
-- Find customers who are either from 'New York' OR do not have a grade > 100.
-- Return: customer_id, cust_name, city, grade, salesman_id

-- Table Reference: customer(customer_id, cust_name, city, grade, salesman_id)

SELECT customer_id,
       cust_name,
       city,
       grade,
       salesman_id
FROM   customer
WHERE  city = 'New York'
   OR  grade <= 100;

-- Explanation:
-- The OR condition returns rows where EITHER:
--   1. city is 'New York'          → all New York customers regardless of grade
--   2. grade is NOT greater than 100 (i.e., grade <= 100)
-- Both conditions are inclusive — a New York customer with grade <= 100
-- appears only once (SQL does not duplicate OR matches).

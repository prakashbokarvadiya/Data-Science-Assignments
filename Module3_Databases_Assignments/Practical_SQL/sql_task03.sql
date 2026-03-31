-- SQL Task 3
-- Display order number, purchase amount, achieved % and unachieved %
-- for orders that exceed 50% of the target value of 6000.
-- Target value = 6000

-- Table Reference: orders(ord_no, purch_amt, ord_date, customer_id, salesman_id)

SELECT ord_no,
       purch_amt,
       ROUND((purch_amt / 6000.00) * 100, 2)         AS achieved_pct,
       ROUND((1 - purch_amt / 6000.00) * 100, 2)     AS unachieved_pct
FROM   orders
WHERE  purch_amt > (50.0 / 100) * 6000;

-- Explanation:
-- Target value          = 6000
-- 50% of target         = 3000
-- WHERE filters orders with purch_amt > 3000
-- achieved_pct   = (purch_amt / 6000) * 100
-- unachieved_pct = (1 - purch_amt/6000) * 100
--                = 100 - achieved_pct
-- ROUND(..., 2) formats the result to 2 decimal places.

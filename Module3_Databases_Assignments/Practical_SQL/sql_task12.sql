-- SQL Task 12
-- Find all employees who earn more than the average salary.
-- Return: employee_id, first_name, last_name

-- Table Reference: employees(employee_id, first_name, last_name, salary, ...)

SELECT employee_id,
       first_name,
       last_name
FROM   employees
WHERE  salary > (
           SELECT AVG(salary)
           FROM   employees
       )
ORDER  BY salary DESC;

-- Explanation:
-- Subquery: computes the company-wide average salary across all employees.
-- Outer query: returns employees whose individual salary exceeds that average.
-- ORDER BY salary DESC: highest earners are listed first.

-- SQL Task 14
-- Find employees who earn less than the employee with ID 182.
-- Return: first_name, last_name, salary

-- Table Reference: employees(employee_id, first_name, last_name, salary, ...)

SELECT first_name,
       last_name,
       salary
FROM   employees
WHERE  salary < (
           SELECT salary
           FROM   employees
           WHERE  employee_id = 182
       )
  AND  employee_id <> 182
ORDER  BY salary DESC;

-- Explanation:
-- Subquery: retrieves the salary of employee ID 182 (a scalar subquery).
-- Outer query: returns all employees whose salary is strictly less than that amount.
-- employee_id <> 182 excludes employee 182 from the result.
-- ORDER BY salary DESC: shows employees closest to the threshold first.

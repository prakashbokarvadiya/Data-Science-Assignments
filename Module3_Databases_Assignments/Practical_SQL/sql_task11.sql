-- SQL Task 11
-- Find employees who have the same job designation as employee ID 169.
-- Return: first_name, last_name, department_id, job_id

-- Table Reference: employees(employee_id, first_name, last_name, job_id, department_id, ...)

SELECT first_name,
       last_name,
       department_id,
       job_id
FROM   employees
WHERE  job_id = (
           SELECT job_id
           FROM   employees
           WHERE  employee_id = 169
       )
  AND  employee_id <> 169;

-- Explanation:
-- Subquery: retrieves the job_id of employee 169.
-- Outer query: finds all employees whose job_id matches that value.
-- employee_id <> 169 excludes employee 169 from the result set.

-- SQL Task 13
-- Find all employees who work in the Finance department.
-- Return: department_id, first_name (as name), job_id, department_name

-- Tables:
--   employees(employee_id, first_name, last_name, job_id, department_id, ...)
--   departments(department_id, department_name, ...)

SELECT e.department_id,
       e.first_name       AS name,
       e.job_id,
       d.department_name
FROM   employees   e
JOIN   departments d ON e.department_id = d.department_id
WHERE  d.department_name = 'Finance'
ORDER  BY e.first_name;

-- Explanation:
-- JOIN links employees to departments using department_id.
-- WHERE filters rows to only those in the 'Finance' department.
-- first_name is aliased as 'name' as specified in the task.

-- Alternative using subquery:
-- WHERE e.department_id = (
--     SELECT department_id FROM departments WHERE department_name = 'Finance'
-- )

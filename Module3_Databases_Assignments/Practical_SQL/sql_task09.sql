-- SQL Task 9
-- Find all employees who work in department ID 80 or 40.
-- Return: first_name, last_name, department number (department_id), department_name

-- Tables:
--   employees(employee_id, first_name, last_name, department_id, ...)
--   departments(department_id, department_name, ...)

SELECT e.first_name,
       e.last_name,
       e.department_id,
       d.department_name
FROM   employees   e
JOIN   departments d ON e.department_id = d.department_id
WHERE  e.department_id IN (80, 40)
ORDER  BY e.department_id, e.last_name;

-- Explanation:
-- JOIN links employees to their department via department_id.
-- IN (80, 40) is equivalent to: department_id = 80 OR department_id = 40
-- ORDER BY provides a clean, organised output grouped by department.

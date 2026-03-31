-- SQL Task 7
-- Find employees whose department is located at 'Toronto'.
-- Return: first_name, last_name, employee_id, job_id

-- Tables:
--   employees(employee_id, first_name, last_name, job_id, department_id, salary, ...)
--   departments(department_id, department_name, location_id)
--   locations(location_id, city, state_province, country_id)

SELECT e.first_name,
       e.last_name,
       e.employee_id,
       e.job_id
FROM   employees   e
JOIN   departments d ON e.department_id = d.department_id
JOIN   locations   l ON d.location_id   = l.location_id
WHERE  l.city = 'Toronto';

-- Explanation:
-- Three-table JOIN chain:
--   employees → departments  (via department_id)
--   departments → locations  (via location_id)
-- WHERE filters only those rows where the city column equals 'Toronto'.

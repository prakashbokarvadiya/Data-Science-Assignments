-- SQL Task 10
-- Calculate the average salary and number of employees receiving commissions
-- in each department.
-- Return: department_name, average salary, number of employees with commissions

-- Tables:
--   employees(employee_id, first_name, last_name, salary, commission_pct, department_id)
--   departments(department_id, department_name, ...)

SELECT d.department_name,
       ROUND(AVG(e.salary), 2)                         AS avg_salary,
       COUNT(e.commission_pct)                          AS num_commission_employees
FROM   employees   e
JOIN   departments d ON e.department_id = d.department_id
WHERE  e.commission_pct IS NOT NULL
GROUP  BY d.department_name
ORDER  BY avg_salary DESC;

-- Explanation:
-- WHERE commission_pct IS NOT NULL → only employees who have a commission.
-- AVG(salary)         → average salary within each department group.
-- COUNT(commission_pct) → count of non-NULL commission_pct values per department.
-- GROUP BY department_name → one result row per department.
-- ORDER BY avg_salary DESC → highest-paying departments listed first.

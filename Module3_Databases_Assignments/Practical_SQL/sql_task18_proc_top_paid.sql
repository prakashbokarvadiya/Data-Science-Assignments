-- SQL Task 18
-- Stored Procedure: GetTopPaidEmployees
-- Retrieves the highest-paid employee in each department.

DELIMITER //

CREATE PROCEDURE GetTopPaidEmployees()
BEGIN
    SELECT   e.department_id,
             d.department_name,
             e.employee_id,
             e.first_name,
             e.last_name,
             e.job_id,
             e.salary AS max_salary
    FROM     employees   e
    JOIN     departments d ON e.department_id = d.department_id
    WHERE    e.salary = (
                 SELECT MAX(e2.salary)
                 FROM   employees e2
                 WHERE  e2.department_id = e.department_id
             )
    ORDER BY e.department_id;
END //

DELIMITER ;

-- ── Alternative using window function (MySQL 8+) ──────────────────────
/*
CREATE PROCEDURE GetTopPaidEmployees()
BEGIN
    SELECT department_id, department_name, employee_id,
           first_name, last_name, job_id, salary AS max_salary
    FROM (
        SELECT e.*, d.department_name,
               RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS rnk
        FROM   employees e
        JOIN   departments d ON e.department_id = d.department_id
    ) ranked
    WHERE rnk = 1
    ORDER BY department_id;
END
*/

-- ── How to call ──────────────────────────────────────────────────────────
CALL GetTopPaidEmployees();

-- Explanation:
-- Correlated subquery: for each employee row, it computes MAX(salary)
--   within the same department and checks if the employee matches that max.
-- This handles ties — multiple employees with the same maximum salary
--   in a department are all returned.
-- The window function alternative (MySQL 8+) uses RANK() OVER PARTITION BY
--   for a cleaner and often more performant solution.

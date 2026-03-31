-- SQL Task 15
-- Stored Procedure: CountEmployeesByDept
-- Returns the number of employees in each department.

DELIMITER //

CREATE PROCEDURE CountEmployeesByDept()
BEGIN
    SELECT   d.department_id,
             d.department_name,
             COUNT(e.employee_id) AS employee_count
    FROM     departments d
    LEFT JOIN employees  e ON d.department_id = e.department_id
    GROUP BY d.department_id, d.department_name
    ORDER BY employee_count DESC;
END //

DELIMITER ;

-- ── How to call ──────────────────────────────────────────────────────────
CALL CountEmployeesByDept();

-- Explanation:
-- LEFT JOIN ensures departments with zero employees are also included.
-- COUNT(e.employee_id) counts only non-NULL employee IDs per department.
-- DELIMITER // is used so MySQL does not misinterpret the semicolons
--   inside the procedure body as the end of the CREATE statement.

-- SQL Task 17
-- Stored Procedure: DeleteEmployeesByDept
-- Removes all employees from a specific department.

DELIMITER //

CREATE PROCEDURE DeleteEmployeesByDept(
    IN  p_department_id  INT,
    OUT p_deleted_count  INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_deleted_count = -1;
        SELECT 'Error: Could not delete employees. Transaction rolled back.' AS message;
    END;

    -- Check if department exists
    IF NOT EXISTS (
        SELECT 1 FROM departments WHERE department_id = p_department_id
    ) THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Department does not exist';
    END IF;

    START TRANSACTION;

    -- Count before delete (for output)
    SELECT COUNT(*) INTO p_deleted_count
    FROM   employees
    WHERE  department_id = p_department_id;

    -- Delete employees in the given department
    DELETE FROM employees
    WHERE  department_id = p_department_id;

    COMMIT;

    SELECT CONCAT(p_deleted_count, ' employee(s) deleted from department ID ',
                  p_department_id) AS message;
END //

DELIMITER ;

-- ── How to call ──────────────────────────────────────────────────────────
CALL DeleteEmployeesByDept(40, @deleted);
SELECT @deleted AS deleted_count;

-- Explanation:
-- IN  p_department_id : the department whose employees will be deleted.
-- OUT p_deleted_count : returns the number of rows deleted to the caller.
-- EXISTS check prevents errors for non-existent departments.
-- TRANSACTION + EXIT HANDLER ensures safe rollback on any error.

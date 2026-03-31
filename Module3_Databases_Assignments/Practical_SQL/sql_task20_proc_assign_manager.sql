-- SQL Task 20
-- Stored Procedure: AssignManagerToDepartment
-- Assigns a new manager to all employees in a specific department
-- and updates the department's manager_id as well.

DELIMITER //

CREATE PROCEDURE AssignManagerToDepartment(
    IN  p_department_id  INT,
    IN  p_new_manager_id INT,
    OUT p_updated_count  INT
)
BEGIN
    DECLARE v_dept_exists INT DEFAULT 0;
    DECLARE v_mgr_exists  INT DEFAULT 0;

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_updated_count = -1;
        SELECT 'Error: Manager assignment failed. Transaction rolled back.' AS message;
    END;

    -- Check if department exists
    SELECT COUNT(*) INTO v_dept_exists
    FROM   departments
    WHERE  department_id = p_department_id;

    IF v_dept_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Department does not exist';
    END IF;

    -- Check if the new manager is a valid employee
    SELECT COUNT(*) INTO v_mgr_exists
    FROM   employees
    WHERE  employee_id = p_new_manager_id;

    IF v_mgr_exists = 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'New manager employee ID does not exist';
    END IF;

    START TRANSACTION;

    -- Update manager_id for all employees in the department
    UPDATE employees
    SET    manager_id = p_new_manager_id
    WHERE  department_id = p_department_id
      AND  employee_id  <> p_new_manager_id;   -- manager does not report to themselves

    SET p_updated_count = ROW_COUNT();

    -- Update department's official manager_id
    UPDATE departments
    SET    manager_id = p_new_manager_id
    WHERE  department_id = p_department_id;

    COMMIT;

    SELECT CONCAT(
        'Manager ID ', p_new_manager_id, ' assigned to department ', p_department_id, '. ',
        p_updated_count, ' employee record(s) updated.'
    ) AS assignment_summary;
END //

DELIMITER ;

-- ── How to call ──────────────────────────────────────────────────────────
-- Assign employee 108 as manager of department 100
CALL AssignManagerToDepartment(100, 108, @updated);
SELECT @updated AS employees_updated;

-- Explanation:
-- IN  p_department_id  : the target department.
-- IN  p_new_manager_id : employee ID of the new manager.
-- OUT p_updated_count  : number of employee records updated.
-- Two UPDATEs run in one transaction:
--   1. employees table  → sets manager_id for all dept members.
--   2. departments table → officially records the new department manager.
-- employee_id <> p_new_manager_id prevents the manager being their own manager.
-- ROW_COUNT() captures how many rows the first UPDATE affected.

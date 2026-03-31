-- SQL Task 19
-- Stored Procedure: PromoteEmployee
-- Increases an employee's salary and changes their job role.

DELIMITER //

CREATE PROCEDURE PromoteEmployee(
    IN  p_employee_id  INT,
    IN  p_new_job_id   VARCHAR(20),
    IN  p_salary_hike  DECIMAL(5, 2),   -- percentage increase e.g. 15.00 = 15%
    OUT p_new_salary   DECIMAL(10, 2)
)
BEGIN
    DECLARE v_current_salary  DECIMAL(10, 2);
    DECLARE v_current_job     VARCHAR(20);

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SET p_new_salary = -1;
        SELECT 'Error: Promotion failed. Transaction rolled back.' AS message;
    END;

    -- Validate employee exists
    SELECT salary, job_id
    INTO   v_current_salary, v_current_job
    FROM   employees
    WHERE  employee_id = p_employee_id;

    IF v_current_salary IS NULL THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Employee ID not found';
    END IF;

    -- Validate hike percentage
    IF p_salary_hike <= 0 OR p_salary_hike > 100 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Salary hike must be between 0% and 100%';
    END IF;

    START TRANSACTION;

    -- Calculate new salary
    SET p_new_salary = ROUND(v_current_salary * (1 + p_salary_hike / 100), 2);

    -- Apply promotion
    UPDATE employees
    SET    salary = p_new_salary,
           job_id = p_new_job_id
    WHERE  employee_id = p_employee_id;

    COMMIT;

    SELECT CONCAT(
        'Employee ', p_employee_id, ' promoted successfully. ',
        'Job: ', v_current_job, ' -> ', p_new_job_id, '. ',
        'Salary: ', v_current_salary, ' -> ', p_new_salary
    ) AS promotion_summary;
END //

DELIMITER ;

-- ── How to call ──────────────────────────────────────────────────────────
-- Promote employee 101: new job 'IT_MAN', 20% salary hike
CALL PromoteEmployee(101, 'IT_MAN', 20.00, @new_sal);
SELECT @new_sal AS updated_salary;

-- Explanation:
-- IN  p_employee_id : ID of the employee to promote.
-- IN  p_new_job_id  : the new job role after promotion.
-- IN  p_salary_hike : percentage increase (e.g., 15.00 means 15%).
-- OUT p_new_salary  : returns the computed new salary to the caller.
-- SELECT INTO fetches the current salary/job before updating.
-- Validation ensures the employee exists and hike % is reasonable.
-- A single UPDATE atomically changes both salary and job_id.

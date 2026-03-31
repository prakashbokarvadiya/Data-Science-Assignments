-- SQL Task 16
-- Stored Procedure: AddNewEmployee
-- Adds a new employee record to the database with validation.

DELIMITER //

CREATE PROCEDURE AddNewEmployee(
    IN p_employee_id   INT,
    IN p_first_name    VARCHAR(50),
    IN p_last_name     VARCHAR(50),
    IN p_email         VARCHAR(100),
    IN p_phone_number  VARCHAR(20),
    IN p_hire_date     DATE,
    IN p_job_id        VARCHAR(20),
    IN p_salary        DECIMAL(10, 2),
    IN p_department_id INT
)
BEGIN
    -- Error handler for duplicate employee_id
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error: Could not add employee. Check for duplicate ID or invalid data.' AS message;
    END;

    START TRANSACTION;

    -- Validate salary
    IF p_salary <= 0 THEN
        SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Salary must be a positive value';
    END IF;

    -- Insert new employee
    INSERT INTO employees (
        employee_id, first_name, last_name, email,
        phone_number, hire_date, job_id, salary, department_id
    )
    VALUES (
        p_employee_id, p_first_name, p_last_name, p_email,
        p_phone_number, p_hire_date, p_job_id, p_salary, p_department_id
    );

    COMMIT;

    SELECT CONCAT('Employee ', p_first_name, ' ', p_last_name,
                  ' added successfully with ID ', p_employee_id) AS message;
END //

DELIMITER ;

-- ── How to call ──────────────────────────────────────────────────────────
CALL AddNewEmployee(
    301,
    'Rahul',
    'Sharma',
    'RSHARMA',
    '9876543210',
    '2024-01-15',
    'IT_PROG',
    75000.00,
    60
);

-- Explanation:
-- IN parameters allow the caller to pass values for each column.
-- TRANSACTION ensures atomicity — either the insert succeeds fully or rolls back.
-- SIGNAL raises a custom error if salary is invalid.
-- EXIT HANDLER catches any SQL exceptions and rolls back the transaction.

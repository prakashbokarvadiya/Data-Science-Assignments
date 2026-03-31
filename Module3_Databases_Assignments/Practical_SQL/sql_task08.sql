-- SQL Task 8
-- Find employees whose salary is lower than any employee with job title 'MK_MAN'.
-- Exclude employees who are themselves 'MK_MAN'.
-- Return: employee_id, first_name, last_name, job_id

-- Table Reference: employees(employee_id, first_name, last_name, job_id, salary, ...)

SELECT employee_id,
       first_name,
       last_name,
       job_id
FROM   employees
WHERE  salary < ANY (
           SELECT salary
           FROM   employees
           WHERE  job_id = 'MK_MAN'
       )
  AND  job_id <> 'MK_MAN';

-- Explanation:
-- Subquery: SELECT salary FROM employees WHERE job_id = 'MK_MAN'
--   → returns all salary values of MK_MAN employees.
-- ANY: the outer employee's salary must be less than AT LEAST ONE MK_MAN salary.
-- job_id <> 'MK_MAN' excludes MK_MAN employees from the result.

-- Alternative using MIN():
-- WHERE salary < (SELECT MIN(salary) FROM employees WHERE job_id = 'MK_MAN')
--   AND job_id <> 'MK_MAN';
-- (This returns employees earning less than even the lowest-paid MK_MAN.)

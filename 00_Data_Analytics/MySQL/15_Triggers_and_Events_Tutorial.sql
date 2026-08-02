-- Triggers and Events

DROP TRIGGER IF EXISTS employee_insert;
DROP TRIGGER IF EXISTS employee_insert1;
DELIMITER $$
CREATE TRIGGER employee_insert2
	AFTER INSERT ON employee_salary
    FOR EACH ROW

BEGIN
	INSERT INTO employee_demographics (employee_id, first_name, last_name)
    VALUES (NEW.employee_id, NEW.first_name, NEW.last_name);
END $$
DELIMITER ;

INSERT INTO employee_salary 
(employee_id, first_name, last_name, occupation, salary, dept_id)
VALUES
('18', 'Kushagra', 'Kumar', 'Analyst', 37000, NULL);


SELECT *
FROM employee_salary;

SELECT *
FROM employee_demographics;



-- EVENTS

SELECT *
FROM employee_demographics;

DELIMITER $$
CREATE EVENT delete_retirees
ON SCHEDULE EVERY 30 SECOND
DO
BEGIN
	DELETE
    FROM employee_demographics
    WHERE age >= 50;
END $$
DELIMITER ;

SHOW VARIABLES LIKE 'event%';
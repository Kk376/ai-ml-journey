-- Where Clause
SELECT * 
FROM employee_salary
WHERE first_name = 'Leslie';

SELECT *
FROM employee_salary
WHERE salary >= 50000;

SELECT *
FROM employee_salary
WHERE salary < 50000;

SELECT *
FROM employee_demographics
WHERE gender = 'Female';

SELECT *
FROM employee_demographics
WHERE gender != 'Female';


-- AND OR Statements
SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01'
AND gender = 'Male';

SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01'
OR gender = 'Male';

SELECT *
FROM employee_demographics
WHERE birth_date > '1985-01-01'
OR NOT gender = 'Male';

SELECT *
FROM employee_demographics
WHERE (first_name = 'Tom' AND age = 36) OR age >= 55;


-- LIKE Statement
-- % and _
SELECT *
FROM employee_demographics
WHERE first_name LIKE 'Jer%';

SELECT *
FROM employee_demographics
WHERE first_name LIKE '%er%';

SELECT *
FROM employee_demographics
WHERE first_name LIKE 'a__';
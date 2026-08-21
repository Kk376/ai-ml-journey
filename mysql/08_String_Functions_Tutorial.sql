-- String Functions

SELECT LENGTH('Kushagra');	-- Tells the length of the string.
SELECT UPPER('kushagra');	-- Uppercase the string.
SELECT LOWER('KUSHAGRA');	-- Lowercase the string.


SELECT first_name, LENGTH(first_name)
FROM employee_demographics
ORDER BY 2;

SELECT first_name, UPPER(first_name)
FROM employee_demographics
ORDER BY 2;

SELECT first_name, LOWER(first_name)
FROM employee_demographics
ORDER BY 2;


-- Trim

SELECT TRIM('			sky			');
SELECT LTRIM('			sky			');
SELECT RTRIM('			sky			');


SELECT first_name,
LEFT(first_name, 3),
RIGHT(first_name, 2),
SUBSTRING(first_name, 3, 2),
birth_date,
SUBSTRING(birth_date, 1, 4) AS birth_year,
SUBSTRING(birth_date, 6, 2) AS birth_month,
SUBSTRING(birth_date, 9, 2) AS birth_date
FROM employee_demographics;


-- Replace and Locate
SELECT first_name, 
REPLACE(first_name, 'a', 'z')
FROM employee_demographics;

SELECT LOCATE('a', 'Kushagra');

SELECT first_name, 
LOCATE('An', first_name)
FROM employee_demographics;

SELECT first_name, last_name,
CONCAT(first_name, ' ', last_name) AS full_name
FROM employee_demographics;
-- Group by

SELECT *
FROM employee_demographics;

SELECT gender
FROM employee_demographics
GROUP BY gender;

SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender;

SELECT occupation, salary
FROM employee_salary
GROUP BY occupation, salary;

SELECT gender, MAX(age), MIN(age), COUNT(age)
FROM employee_demographics
GROUP BY gender;



-- ORDER BY

SELECT *
FROM employee_demographics
ORDER BY first_name;

SELECT *
FROM employee_demographics
ORDER BY gender DESC;

SELECT *
FROM employee_demographics
ORDER BY age DESC;

SELECT *
FROM employee_demographics
ORDER BY first_name DESC;
-- Limit and Aliasing


SELECT *
FROM employee_demographics
ORDER BY age DESC
LIMIT 4;

SELECT *
FROM employee_demographics
ORDER BY age DESC
LIMIT 3, 1;



-- Aliasing

SELECT gender, AVG(age)
FROM employee_demographics
GROUP BY gender
HAVING AVG(age) > 40;

SELECT gender, AVG(age) AS avg_age
FROM employee_demographics
GROUP BY gender
HAVING avg_age > 40;


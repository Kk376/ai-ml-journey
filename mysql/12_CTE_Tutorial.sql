-- CTEs

SELECT dem.gender, AVG(sal.salary) AS avg_sal,
MAX(sal.salary), MIN(sal.salary), COUNT(sal.salary)
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender;


WITH CTE_Example AS (
SELECT dem.gender, AVG(sal.salary) AS avg_sal,
MAX(sal.salary) AS max_sal, 
MIN(sal.salary) AS min_sal, 
COUNT(sal.salary) AS count_sal
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender)

SELECT *
FROM CTE_Example;


SELECT AVG(avg_sal)
FROM 
(
SELECT dem.gender, AVG(sal.salary) AS avg_sal,
MAX(sal.salary) AS max_sal, 
MIN(sal.salary) AS min_sal, 
COUNT(sal.salary) AS count_sal
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender) subquery_example;


WITH CTE_Example AS
(
SELECT employee_id, gender, birth_date
FROM employee_demographics
WHERE birth_date > '1980-01-01'
),
CTE_Example2 AS
(
SELECT employee_id, salary
FROM employee_salary
WHERE salary > 35000
)
SELECT *
FROM CTE_Example
JOIN CTE_Example2
	ON CTE_Example.employee_id = CTE_Example2.employee_id;
    
    
WITH CTE_Example (Gender, AVG_Salary, MAX_Salary, MIN_Salary, COUNT_Salary) AS (
SELECT dem.gender, AVG(sal.salary),
MAX(sal.salary), 
MIN(sal.salary), 
COUNT(sal.salary)
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender)

SELECT *
FROM CTE_Example;
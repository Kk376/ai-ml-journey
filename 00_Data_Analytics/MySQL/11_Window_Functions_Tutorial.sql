-- Window Functions

SELECT gender, AVG(salary) AS avg_salary
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender;


SELECT gender, AVG(salary) OVER(PARTITION BY gender) AS avg_salary
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id;
    
    
SELECT dem.first_name, dem.last_name, dem.gender, 
AVG(salary) OVER(PARTITION BY gender) AS avg_salary
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id;
    
    
SELECT dem.employee_id, dem.first_name, dem.last_name, dem.gender, sal.salary,
SUM(salary) OVER(PARTITION BY gender ORDER BY dem.employee_id) AS Rolling_Total
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id;
    
    
SELECT dem.employee_id, dem.first_name, dem.last_name, dem.gender, sal.salary,
ROW_NUMBER() OVER()
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id;
    
    
SELECT dem.employee_id, dem.first_name, dem.last_name, dem.gender, sal.salary,
ROW_NUMBER() OVER(PARTITION BY dem.gender ORDER BY sal.salary DESC) AS salary_descending_order
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id;
    
    
SELECT dem.employee_id, dem.first_name, dem.last_name, dem.gender, sal.salary,
ROW_NUMBER() OVER(PARTITION BY dem.gender ORDER BY sal.salary DESC) AS row_num,
RANK() OVER(PARTITION BY dem.gender ORDER BY sal.salary DESC) AS row_num,
DENSE_RANK() OVER(PARTITION BY dem.gender ORDER BY sal.salary DESC) AS dense_row_num
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id;
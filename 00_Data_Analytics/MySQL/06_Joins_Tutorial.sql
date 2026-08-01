-- Joins

-- Inner Join
SELECT *
FROM employee_demographics;

SELECT *
FROM employee_salary;


SELECT *
FROM employee_demographics AS dem
JOIN employee_salary AS sal			-- JOIN works as INNER JOIN by default.
	ON dem.employee_id = sal.employee_id;
    

SELECT dem.employee_id, age, salary, occupation
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id;
    

-- Outer Joins
SELECT *
FROM employee_demographics AS dem
LEFT JOIN employee_salary AS sal		-- LEFT JOIN = LEFT OUTER JOIN
	ON dem.employee_id = sal.employee_id;
    
SELECT *
FROM employee_demographics AS dem
RIGHT JOIN employee_salary AS sal		-- RIGHT JOIN = RIGHT OUTER JOIN
	ON dem.employee_id = sal.employee_id;
    
    
-- Self Join
SELECT 
emp1.employee_id AS emp_santa,
emp1.first_name AS first_name_santa,
emp1.last_name AS last_name_santa,

emp2.employee_id AS emp_gift_reciever,
emp2.first_name AS first_name_gift_reciever,
emp2.last_name AS last_name_gift_reciever

FROM employee_salary emp1
JOIN employee_salary emp2
	ON emp1.employee_id + 1 = emp2.employee_id;
    
    
-- Joining multiple tables together

SELECT *
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
JOIN parks_departments AS pd
	ON sal.dept_id = pd.department_id;
-- Case Statements

SELECT
first_name,
last_name,
age,
CASE
	WHEN age <= 30 THEN 'Young'
    WHEN age BETWEEN 31 AND 44 THEN 'Middle Aged'
    WHEN age BETWEEN 45 AND 59 THEN 'Old'
    WHEN age >= 60 THEN 'Should get retired tbh'
END AS age_category
FROM employee_demographics;


-- Pay Increase and Bonus
-- < 50000 = 5% Bonus
-- > 50000 = 7% Bonus
-- Finance = 10% Bonus

SELECT first_name, last_name, salary, dept_id,
CASE
    -- If they are in Finance (dept_id = 6), they get their standard salary tier bonus PLUS an extra 10%
    WHEN dept_id = 6 AND salary < 50000 THEN (salary * 0.05) + (salary * 0.10)
    WHEN dept_id = 6 AND salary > 50000 THEN (salary * 0.07) + (salary * 0.10)
    
    -- Everyone else just gets their standard tier bonus
    WHEN salary < 50000 THEN salary * 0.05
    WHEN salary > 50000 THEN salary * 0.07
    ELSE 0
END AS Total_Bonus,

CASE
    WHEN dept_id = 6 AND salary < 50000 THEN salary + (salary * 0.05) + (salary * 0.10)
    WHEN dept_id = 6 AND salary > 50000 THEN salary + (salary * 0.07) + (salary * 0.10)
    WHEN salary < 50000 THEN salary + (salary * 0.05)
    WHEN salary > 50000 THEN salary + (salary * 0.07)
    ELSE salary
END AS New_Salary
FROM employee_salary;
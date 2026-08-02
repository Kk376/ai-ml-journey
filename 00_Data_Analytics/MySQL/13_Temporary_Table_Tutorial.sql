-- Temporary Tables

CREATE TEMPORARY TABLE temp_table
(
first_name varchar (50),
last_name varchar (50),
favourite_movie varchar (100)
);

INSERT INTO temp_table
VALUES 
(
'Kushagra', 'Kumar', 'AOT'
);

SELECT *
FROM temp_table;


CREATE TEMPORARY TABLE salary_over_35k
SELECT *
FROM employee_salary
WHERE salary >= 35000;

SELECT *
FROM salary_over_35k;
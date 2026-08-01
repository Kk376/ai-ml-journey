# MySQL Progress

Tracking what I've covered so far in the `00_Data_Analytics/MySQL` folder. Practicing on the Parks and Recreation dataset (employee_demographics, employee_salary, parks_departments).

## Day 1
- **00_Beginner_Parks_and_Recreation_db.sql** — Set up the practice database: created `Parks_and_Recreation`, built the three tables, and inserted the sample data I'm using for everything else.
- **01_Select_Tutorial.sql** — Basic `SELECT`, selecting specific columns, doing simple arithmetic on columns (age + 10, etc.), and `SELECT DISTINCT`.
- **02_Where_Clause_Tutorial.sql** — Filtering with `WHERE`, comparison operators, combining conditions with `AND` / `OR` / `NOT`, and pattern matching with `LIKE` (`%` and `_` wildcards).

## Day 2
- **03_OrderBy_GroupBy_Tutorial.sql** — `GROUP BY` on single and multiple columns, aggregate functions (`AVG`, `MAX`, `MIN`, `COUNT`) alongside it, and sorting results with `ORDER BY` (ASC/DESC).
- **04_Having_vs_Where_Tutorial.sql** — The difference between `WHERE` (filters rows before grouping) and `HAVING` (filters after aggregation).
- **05_Limit_and_Aliasing_Tutorial.sql** — Limiting result sets with `LIMIT` (including offset), and cleaning up output with aliases (`AS`).

## Day 3
- **06_Joins_Tutorial.sql** — `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, self joins (matching a table to itself), and joining three tables together in one query.
- **07_Unions_Tutorial.sql** — Combining result sets with `UNION`, including adding a custom label column to distinguish which query a row came from.
- **08_String_Functions_Tutorial.sql** — `LENGTH`, `UPPER`, `LOWER`, `TRIM`/`LTRIM`/`RTRIM`, `LEFT`/`RIGHT`/`SUBSTRING`, `REPLACE`, `LOCATE`, and `CONCAT`.
- **09_Case_Statements_Tutorial.sql** — `CASE WHEN` for categorizing rows (age groups), and a multi-condition bonus/salary calculation.
- **10_Subqueries_Tutorial.sql** — Subqueries in `WHERE` (with `IN`), subqueries in `SELECT`, and nesting an aggregated query inside another query (derived tables).


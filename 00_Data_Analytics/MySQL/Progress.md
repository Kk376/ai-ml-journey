# MySQL Progress

Tracking what I've covered so far in the `00_Data_Analytics/MySQL` folder. Practicing on the Parks and Recreation dataset (employee_demographics, employee_salary, parks_departments).

## Day 1 (2026-07-30)

- **00_Beginner_Parks_and_Recreation_db.sql** — Set up the practice database: created `Parks_and_Recreation`, built the three tables, and inserted the sample data I'm using for everything else.
- **01_Select_Tutorial.sql** — Basic `SELECT`, selecting specific columns, doing simple arithmetic on columns (age + 10, etc.), and `SELECT DISTINCT`.
- **02_Where_Clause_Tutorial.sql** — Filtering with `WHERE`, comparison operators, combining conditions with `AND` / `OR` / `NOT`, and pattern matching with `LIKE` (`%` and `_` wildcards).

## Day 2 (2026-07-31)

- **03_OrderBy_GroupBy_Tutorial.sql** — `GROUP BY` on single and multiple columns, aggregate functions (`AVG`, `MAX`, `MIN`, `COUNT`) alongside it, and sorting results with `ORDER BY` (ASC/DESC).
- **04_Having_vs_Where_Tutorial.sql** — The difference between `WHERE` (filters rows before grouping) and `HAVING` (filters after aggregation).
- **05_Limit_and_Aliasing_Tutorial.sql** — Limiting result sets with `LIMIT` (including offset), and cleaning up output with aliases (`AS`).

## Day 3 (2026-08-01)

- **06_Joins_Tutorial.sql** — `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, self joins (matching a table to itself), and joining three tables together in one query.
- **07_Unions_Tutorial.sql** — Combining result sets with `UNION`, including adding a custom label column to distinguish which query a row came from.
- **08_String_Functions_Tutorial.sql** — `LENGTH`, `UPPER`, `LOWER`, `TRIM`/`LTRIM`/`RTRIM`, `LEFT`/`RIGHT`/`SUBSTRING`, `REPLACE`, `LOCATE`, and `CONCAT`.
- **09_Case_Statements_Tutorial.sql** — `CASE WHEN` for categorizing rows (age groups), and a multi-condition bonus/salary calculation.
- **10_Subqueries_Tutorial.sql** — Subqueries in `WHERE` (with `IN`), subqueries in `SELECT`, and nesting an aggregated query inside another query (derived tables).

## Day 4 (2026-08-02)

- **11_Window_Functions_Tutorial.sql** — Using `OVER()`, `PARTITION BY`, rolling totals, and ranking functions like `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`.
- **12_CTE_Tutorial.sql** — Writing Common Table Expressions (`WITH`), using multiple CTEs in a single query, and aliasing CTE columns.
- **13_Temporary_Table_Tutorial.sql** — Creating short-lived manual temporary tables and generating temporary tables directly from `SELECT` query results.
- **14_Stored_Procedures_Tutorial.sql** — Building reusable blocks of code (`CREATE PROCEDURE`), handling multi-statement blocks with `DELIMITER`, and passing parameters (`IN`).
- **15_Triggers_and_Events_Tutorial.sql** — Automating row insertions across linked tables using `AFTER INSERT` triggers, and scheduling periodic automated tasks with `EVENTS`.

## Day 5 (2026-08-03)

### Health affected productivity today

Could not study today due to headache and arm pain.
Still maintained consistency by updating the learning log.

### Current Status
- MySQL: Revision ongoing
- Next focus: MySQL projects

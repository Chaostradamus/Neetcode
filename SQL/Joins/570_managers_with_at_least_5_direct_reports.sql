select e.name
from employee as e
inner join employee as m on e.id = m.managerid
group by m.managerid
having count(m.managerid) > 4 

-- 570. Managers with at Least 5 Direct Reports
-- Medium
-- Topics
-- Companies
-- Hint
-- SQL Schema
-- Pandas Schema
-- Table: Employee

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | name        | varchar |
-- | department  | varchar |
-- | managerId   | int     |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table indicates the name of an employee, their department, and the id of their manager.
-- If managerId is null, then the employee does not have a manager.
-- No employee will be the manager of themself.
 

-- Write a solution to find managers with at least five direct reports.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employee table:
-- +-----+-------+------------+-----------+
-- | id  | name  | department | managerId |
-- +-----+-------+------------+-----------+
-- | 101 | John  | A          | null      |
-- | 102 | Dan   | A          | 101       |
-- | 103 | James | A          | 101       |
-- | 104 | Amy   | A          | 101       |
-- | 105 | Anne  | A          | 101       |
-- | 106 | Ron   | B          | 101       |
-- +-----+-------+------------+-----------+
-- Output: 
-- +------+
-- | name |
-- +------+
-- | John |
-- +------+


-- Let's work through your query step-by-step with the provided dataset to understand how the INNER JOIN works and how the rest of the query operates.

-- Dataset: Employee
-- id	name	department	managerId
-- 101	John	A	NULL
-- 102	Dan	A	101
-- 103	James	A	101
-- 104	Amy	A	101
-- 105	Anne	A	101
-- 106	Ron	B	101
-- 107	Mike	B	102
-- Query:
-- sql
-- Copy
-- Edit
-- SELECT e.name
-- FROM Employee AS e
-- INNER JOIN Employee AS m ON e.id = m.managerId
-- GROUP BY m.managerId
-- HAVING COUNT(m.managerId) >= 5;
-- Step 1: INNER JOIN
-- The query starts with:

-- sql
-- Copy
-- Edit
-- FROM Employee AS e
-- INNER JOIN Employee AS m ON e.id = m.managerId
-- How It Works:

-- e represents potential managers.
-- m represents employees.
-- ON e.id = m.managerId: Matches rows where an employee (m.managerId) reports to a manager (e.id).
-- Result of the Join:
-- For each employee in m, their manager from e is matched. Here's the intermediate result:

-- e.id	e.name	m.id	m.name	m.managerId
-- 101	John	102	Dan	101
-- 101	John	103	James	101
-- 101	John	104	Amy	101
-- 101	John	105	Anne	101
-- 101	John	106	Ron	101
-- 102	Dan	107	Mike	102
-- Step 2: GROUP BY
-- Next, we add:

-- sql
-- Copy
-- Edit
-- GROUP BY m.managerId
-- What It Does:

-- Groups rows by m.managerId, so we can perform aggregations (e.g., COUNT) for each manager.
-- Groups Created:
-- Group for m.managerId = 101:
-- Rows: John is the manager of Dan, James, Amy, Anne, and Ron.
-- Group for m.managerId = 102:
-- Rows: Dan is the manager of Mike.
-- Step 3: Aggregate with COUNT
-- We calculate the number of employees (COUNT) reporting to each manager.

-- Aggregation Results:
-- m.managerId	COUNT(m.managerId)
-- 101	5
-- 102	1
-- Step 4: HAVING
-- Next, we filter the results:

-- sql
-- Copy
-- Edit
-- HAVING COUNT(m.managerId) >= 5
-- What It Does:

-- Keeps only managers who have 5 or more direct reports.
-- Filtered Results:
-- m.managerId	COUNT(m.managerId)
-- 101	5
-- Step 5: SELECT e.name
-- Finally, we select the name of the manager from the e table:

-- sql
-- Copy
-- Edit
-- SELECT e.name
-- Result:

-- e.name is retrieved for the manager whose id matches m.managerId = 101.
-- Manager John has 5 direct reports.
-- Final Output:
-- name
-- John
-- Full Process Recap:
-- INNER JOIN: Matches managers (e) with their direct reports (m).
-- GROUP BY: Groups the joined rows by manager IDs.
-- COUNT: Counts the number of employees reporting to each manager.
-- HAVING: Filters managers with 5 or more direct reports.
-- SELECT: Outputs the name of the qualified manager.
-- This method ensures the query correctly identifies managers meeting the required condition.
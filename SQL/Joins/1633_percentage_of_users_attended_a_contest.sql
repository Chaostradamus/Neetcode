select contest_id, 
round(count(distinct user_id) * 100 / (select count(user_id) from users),2) as percentage
from register as r
group by contest_id
order by percentage desc, contest_id






-- 1633. Percentage of Users Attended a Contest
-- Easy
-- Topics
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Users

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | user_id     | int     |
-- | user_name   | varchar |
-- +-------------+---------+
-- user_id is the primary key (column with unique values) for this table.
-- Each row of this table contains the name and the id of a user.
 

-- Table: Register

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | contest_id  | int     |
-- | user_id     | int     |
-- +-------------+---------+
-- (contest_id, user_id) is the primary key (combination of columns with unique values) for this table.
-- Each row of this table contains the id of a user and the contest they registered into.
 

-- Write a solution to find the percentage of the users registered in each contest rounded to two decimals.

-- Return the result table ordered by percentage in descending order. In case of a tie, order it by contest_id in ascending order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Users table:
-- +---------+-----------+
-- | user_id | user_name |
-- +---------+-----------+
-- | 6       | Alice     |
-- | 2       | Bob       |
-- | 7       | Alex      |
-- +---------+-----------+
-- Register table:
-- +------------+---------+
-- | contest_id | user_id |
-- +------------+---------+
-- | 215        | 6       |
-- | 209        | 2       |
-- | 208        | 2       |
-- | 210        | 6       |
-- | 208        | 6       |
-- | 209        | 7       |
-- | 209        | 6       |
-- | 215        | 7       |
-- | 208        | 7       |
-- | 210        | 2       |
-- | 207        | 2       |
-- | 210        | 7       |
-- +------------+---------+
-- Output: 
-- +------------+------------+
-- | contest_id | percentage |
-- +------------+------------+
-- | 208        | 100.0      |
-- | 209        | 100.0      |
-- | 210        | 100.0      |
-- | 215        | 66.67      |
-- | 207        | 33.33      |
-- +------------+------------+
-- Explanation: 
-- All the users registered in contests 208, 209, and 210. The percentage is 100% and we sort them in the answer table by contest_id in ascending order.
-- Alice and Alex registered in contest 215 and the percentage is ((2/3) * 100) = 66.67%
-- Bob registered in contest 207 and the percentage is ((1/3) * 100) = 33.33%


-- Let’s break down the query step by step with the new dataset:

-- Data Tables
-- Register Table
-- contest_id	user_id
-- 215	6
-- 209	2
-- 208	2
-- 210	6
-- 208	6
-- 209	7
-- 209	6
-- 215	7
-- 208	7
-- 210	2
-- 207	2
-- 210	7
-- Users Table
-- user_id	user_name
-- 6	Alice
-- 2	Bob
-- 7	Alex
-- Goal
-- We want to calculate the percentage of users registered in each contest rounded to two decimal places. The percentage is calculated as:

-- Percentage
-- =
-- Number of distinct users registered for the contest
-- Total number of users
-- ×
-- 100
-- Percentage= 
-- Total number of users
-- Number of distinct users registered for the contest
-- ​
--  ×100
-- Return the contest_id and the calculated percentage, ordering results by percentage in descending order. For ties, sort by contest_id in ascending order.

-- Query
-- sql
-- Copy
-- Edit
-- SELECT 
--     contest_id, 
--     ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(user_id) FROM Users), 2) AS percentage
-- FROM Register
-- GROUP BY contest_id
-- ORDER BY percentage DESC, contest_id;
-- Step-by-Step Explanation
-- Step 1: Subquery to Count Total Users
-- sql
-- Copy
-- Edit
-- SELECT COUNT(user_id) FROM Users;
-- This counts the total number of unique users in the Users table.

-- Result:

-- Total Users
-- 3
-- Step 2: Group Register by contest_id
-- sql
-- Copy
-- Edit
-- SELECT contest_id, COUNT(DISTINCT user_id) AS distinct_users
-- FROM Register
-- GROUP BY contest_id;
-- Here, we group the Register table by contest_id and count the distinct user_id for each contest.

-- Result:

-- contest_id	distinct_users
-- 207	1
-- 208	3
-- 209	3
-- 210	3
-- 215	2
-- Step 3: Calculate Percentage
-- For each contest_id, calculate the percentage of users who registered:

-- \text{Percentage} = \frac{\text{distinct_users} \times 100}{\text{Total Users}}
-- Example calculations:

-- For contest_id = 207:
-- Percentage
-- =
-- 1
-- ×
-- 100
-- 3
-- =
-- 33.33
-- Percentage= 
-- 3
-- 1×100
-- ​
--  =33.33
-- For contest_id = 208:
-- Percentage
-- =
-- 3
-- ×
-- 100
-- 3
-- =
-- 100.00
-- Percentage= 
-- 3
-- 3×100
-- ​
--  =100.00
-- For contest_id = 209:
-- Percentage
-- =
-- 3
-- ×
-- 100
-- 3
-- =
-- 100.00
-- Percentage= 
-- 3
-- 3×100
-- ​
--  =100.00
-- For contest_id = 210:
-- Percentage
-- =
-- 3
-- ×
-- 100
-- 3
-- =
-- 100.00
-- Percentage= 
-- 3
-- 3×100
-- ​
--  =100.00
-- For contest_id = 215:
-- Percentage
-- =
-- 2
-- ×
-- 100
-- 3
-- =
-- 66.67
-- Percentage= 
-- 3
-- 2×100
-- ​
--  =66.67
-- Result:

-- contest_id	percentage
-- 207	33.33
-- 208	100.00
-- 209	100.00
-- 210	100.00
-- 215	66.67
-- Step 4: Order Results
-- sql
-- Copy
-- Edit
-- ORDER BY percentage DESC, contest_id;
-- The results are ordered by:

-- percentage in descending order.
-- contest_id in ascending order for ties.
-- Final Result:

-- contest_id	percentage
-- 208	100.00
-- 209	100.00
-- 210	100.00
-- 215	66.67
-- 207	33.33
-- Query Flow Visualization
-- Subquery: Count Total Users (Users Table) Output: 3.

-- Group Register Table by contest_id

-- contest_id	distinct_users
-- 207	1
-- 208	3
-- 209	3
-- 210	3
-- 215	2
-- Calculate Percentage

-- contest_id	distinct_users	percentage
-- 207	1	33.33
-- 208	3	100.00
-- 209	3	100.00
-- 210	3	100.00
-- 215	2	66.67
-- Order Results

-- contest_id	percentage
-- 208	100.00
-- 209	100.00
-- 210	100.00
-- 215	66.67
-- 207	33.33
-- Why Does It Work?
-- Subquery: Ensures we know the total number of users to calculate percentages accurately.
-- Group By: Aggregates data at the contest level, counting unique users.
-- Percentage Calculation: Divides unique users for a contest by total users to calculate their share.
-- Ordering: Prioritizes higher percentages while breaking ties with contest IDs.
-- Would you like further clarification on any step? 😊
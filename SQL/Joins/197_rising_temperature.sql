select w1.id
from weather w1, weather w2
where datediff(w1.recordDate, w2.recordDate) =1 and w1.temperature > w2.temperature


-- 197. Rising Temperature
-- Easy
-- Topics
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Weather

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the column with unique values for this table.
-- There are no different rows with the same recordDate.
-- This table contains information about the temperature on a certain day.
 

-- Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Weather table:
-- +----+------------+-------------+
-- | id | recordDate | temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- Output: 
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- Explanation: 
-- In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, the temperature was higher than the previous day (20 -> 30).


-- Let’s go through the query step by step using the given Weather table.

-- Query:
-- sql
-- Copy
-- Edit
-- SELECT w1.id
-- FROM Weather w1, Weather w2
-- WHERE DATEDIFF(w1.recordDate, w2.recordDate) = 1 
--   AND w1.temperature > w2.temperature;
-- Step 1: Understand the Tables and Self-Join
-- Weather w1 and Weather w2 represent two instances of the same table, allowing comparisons of rows within the Weather table.
-- The purpose is to compare each row (w1) with another row (w2) based on the conditions in the WHERE clause.
-- Step 2: The Condition: DATEDIFF(w1.recordDate, w2.recordDate) = 1
-- DATEDIFF calculates the difference in days between two dates.
-- The condition DATEDIFF(w1.recordDate, w2.recordDate) = 1 ensures that w1.recordDate is exactly one day after w2.recordDate.
-- This sets up a comparison of consecutive days.
-- Intermediate Join Table After Applying DATEDIFF:
-- w1.id	w1.recordDate	w1.temperature	w2.id	w2.recordDate	w2.temperature
-- 2	2015-01-02	25	1	2015-01-01	10
-- 3	2015-01-03	20	2	2015-01-02	25
-- 4	2015-01-04	30	3	2015-01-03	20
-- Step 3: The Condition: w1.temperature > w2.temperature
-- This ensures we only keep rows where the temperature on the later date (w1.temperature) is greater than the temperature on the earlier date (w2.temperature).
-- Filtered Table After Applying Both Conditions:
-- w1.id	w1.recordDate	w1.temperature	w2.id	w2.recordDate	w2.temperature
-- 2	2015-01-02	25	1	2015-01-01	10
-- 4	2015-01-04	30	3	2015-01-03	20
-- Step 4: SELECT Clause
-- The SELECT statement retrieves only the id of the w1 rows that meet the conditions.
-- Final Output:
-- id
-- 2
-- 4
-- Step-by-Step Execution Summary:
-- Cross-Join: The query performs a self-join (Weather w1, Weather w2), pairing every row in Weather with every other row.

-- Filter by DATEDIFF: Keep only the rows where w1.recordDate is exactly one day after w2.recordDate.

-- Filter by Temperature: Further filter to keep rows where w1.temperature > w2.temperature.

-- Select w1.id: Retrieve the id values from the filtered results.

-- Key Insights:
-- This query identifies dates where the temperature increased compared to the previous day.
-- The DATEDIFF ensures consecutive day comparisons.
-- Self-joins are necessary because each row in the table needs to be compared to others.


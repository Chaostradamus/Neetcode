-- # Write your MySQL query statement below
-- select query_name, round((rating / position) /  count(distinct rating),2) as quality
-- from queries q
-- group by query_name
-- my query is wrong because after grouping it collapses all columns 
-- so it will randomly pick a column (usually the first one) to do the math on if i dont use an aggregrate function


select
query_name,
round(avg(cast(rating as decimal) / position),2) as quality,
round(sum(case when rating <3 then 1 else 0 end) * 100 / count(*), 2 ) as poor_query_percentage
from
queries
group by
query_name;

-- 1211. Queries Quality and Percentage
-- Easy
-- Topics
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Queries

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | query_name  | varchar |
-- | result      | varchar |
-- | position    | int     |
-- | rating      | int     |
-- +-------------+---------+
-- This table may have duplicate rows.
-- This table contains information collected from some queries on a database.
-- The position column has a value from 1 to 500.
-- The rating column has a value from 1 to 5. Query with rating less than 3 is a poor query.
 

-- We define query quality as:

-- The average of the ratio between query rating and its position.

-- We also define poor query percentage as:

-- The percentage of all queries with rating less than 3.

-- Write a solution to find each query_name, the quality and poor_query_percentage.

-- Both quality and poor_query_percentage should be rounded to 2 decimal places.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Queries table:
-- +------------+-------------------+----------+--------+
-- | query_name | result            | position | rating |
-- +------------+-------------------+----------+--------+
-- | Dog        | Golden Retriever  | 1        | 5      |
-- | Dog        | German Shepherd   | 2        | 5      |
-- | Dog        | Mule              | 200      | 1      |
-- | Cat        | Shirazi           | 5        | 2      |
-- | Cat        | Siamese           | 3        | 3      |
-- | Cat        | Sphynx            | 7        | 4      |
-- +------------+-------------------+----------+--------+
-- Output: 
-- +------------+---------+-----------------------+
-- | query_name | quality | poor_query_percentage |
-- +------------+---------+-----------------------+
-- | Dog        | 2.50    | 33.33                 |
-- | Cat        | 0.66    | 33.33                 |
-- +------------+---------+-----------------------+
-- Explanation: 
-- Dog queries quality is ((5 / 1) + (5 / 2) + (1 / 200)) / 3 = 2.50
-- Dog queries poor_ query_percentage is (1 / 3) * 100 = 33.33

-- Cat queries quality equals ((2 / 5) + (3 / 3) + (4 / 7)) / 3 = 0.66
-- Cat queries poor_ query_percentage is (1 / 3) * 100 = 33.33


-- Great question! Let me clarify the distinction. The behavior of the rows depends on how the query is structured, especially the use of aggregate functions, GROUP BY, and non-aggregated columns.

-- When Rows Collapse After GROUP BY
-- In the example of your incorrect query, this behavior happened because:

-- You used GROUP BY query_name, which groups all rows for the same query_name into a single result row per group.
-- Any column in the SELECT list that isn't inside an aggregate function (e.g., COUNT(), SUM(), AVG()) or included in the GROUP BY clause will behave unpredictably because SQL cannot decide which specific row's value to show.
-- In your query:

-- sql
-- Copy
-- Edit
-- SELECT query_name, ROUND((rating / position) / COUNT(DISTINCT rating), 2) AS quality
-- FROM queries
-- GROUP BY query_name
-- The rating and position columns were not aggregated (e.g., with SUM() or AVG()), and they were not included in GROUP BY.
-- SQL arbitrarily chose one row's values for rating and position within each query_name group.
-- This is why only one row from each group was used when calculating quality—SQL collapsed all rows for a query_name into one result row and only kept aggregate results and one arbitrary rating/position pair.

-- Why Rows Don’t "Collapse" in the Correct Query
-- In the correct query:

-- sql
-- Copy
-- Edit
-- SELECT 
--     query_name,
--     ROUND(AVG(CAST(rating AS DECIMAL) / position), 2) AS quality,
--     ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100 / COUNT(*), 2) AS poor_query_percentage
-- FROM queries
-- GROUP BY query_name;
-- GROUP BY query_name creates groups but does not "collapse" all rows into one at first.
-- Aggregate functions (e.g., AVG, SUM, COUNT) still work on all the rows in the group, processing each row within its group before calculating the final aggregate value.
-- Let’s break this down visually for Dog and Cat.

-- Example for Dog Group (Before Aggregation):
-- query_name	rating	position	rating/position
-- Dog	5	1	5.00
-- Dog	5	2	2.50
-- Dog	1	200	0.005
-- What Happens Next:
-- For AVG(CAST(rating AS DECIMAL) / position):

-- SQL calculates rating/position for each row first: 5.00, 2.50, 0.005.
-- Then it computes the average:
-- Average
-- =
-- 5.00
-- +
-- 2.50
-- +
-- 0.005
-- 3
-- =
-- 2.50
-- Average= 
-- 3
-- 5.00+2.50+0.005
-- ​
--  =2.50
-- For Poor Query Percentage:

-- SQL counts rows where rating < 3:
-- Only 1 row (rating = 1).
-- Then calculates the total rows (COUNT(*)):
-- 3 rows in total for Dog.
-- Poor query percentage:
-- 1
-- 3
-- ×
-- 100
-- =
-- 33.33
-- %
-- 3
-- 1
-- ​
--  ×100=33.33%
-- So all rows in the group are processed by the aggregate functions before the result is collapsed into one row.

-- Why It’s Different from Your Query:
-- Your incorrect query:

-- sql
-- Copy
-- Edit
-- SELECT query_name, ROUND((rating / position) / COUNT(DISTINCT rating), 2) AS quality
-- FROM queries
-- GROUP BY query_name;
-- Here’s the key difference:

-- rating / position is not aggregated, so SQL picks one arbitrary rating and position from the group (e.g., the first row for Dog) and only uses that single pair for calculation.
-- This means only one row’s values contribute to rating / position, which is why you got incorrect results.
-- Recap:
-- In the correct query, all rows in the group are considered by the aggregate functions (AVG, SUM, COUNT).
-- In your incorrect query, GROUP BY "collapsed" all rows into one because non-aggregated columns (like rating and position) forced SQL to pick one arbitrary row from the group.
-- Does this make sense now? 😊







-- You said:
-- so when i group by and then use an aggregate function i will have access to the entire group by rows 
-- ChatGPT said:
-- ChatGPT
-- Yes, exactly! When you use GROUP BY and then include aggregate functions (like SUM, AVG, COUNT, etc.) in your query, the aggregate functions have access to all the rows in each group.

-- Let’s summarize this step by step:

-- How GROUP BY Works with Aggregate Functions:
-- Grouping Rows:
-- When you use GROUP BY, SQL divides the rows into separate groups based on the column(s) you specify in the GROUP BY clause.
-- Example:
-- For GROUP BY query_name, all rows with the same query_name are placed into one group.

-- Aggregate Function Process:
-- For each group, aggregate functions (like SUM, AVG, COUNT, etc.) calculate their result using all rows in that group.

-- Example:
-- For AVG(CAST(rating AS DECIMAL) / position):

-- SQL computes rating / position for every row in the group.
-- Then, it averages all these calculated values.
-- Resulting Rows After GROUP BY:
-- After processing each group, SQL outputs one row per group, containing:

-- The grouped column(s) (like query_name in this case).
-- The results of any aggregate functions applied to that group.
-- Why You Can Access All Rows in the Group:
-- Inside the aggregate functions, SQL processes all the rows belonging to the current group. These rows are not "collapsed" or lost—they are still used for the aggregate function calculations.

-- Example with Visuals:
-- Data Table:
-- query_name	rating	position
-- Dog	5	1
-- Dog	5	2
-- Dog	1	200
-- Cat	2	5
-- Cat	3	3
-- Cat	4	7
-- GROUP BY query_name:
-- This creates two groups:

-- Group for Dog:
-- Rows: (5, 1), (5, 2), (1, 200)
-- Group for Cat:
-- Rows: (2, 5), (3, 3), (4, 7)
-- Step 1: AVG(CAST(rating AS DECIMAL) / position)
-- For Dog group:

-- Compute rating / position for each row:
-- Row 1: 
-- 5
-- /
-- 1
-- =
-- 5.00
-- 5/1=5.00
-- Row 2: 
-- 5
-- /
-- 2
-- =
-- 2.50
-- 5/2=2.50
-- Row 3: 
-- 1
-- /
-- 200
-- =
-- 0.005
-- 1/200=0.005
-- Average:
-- AVG
-- =
-- 5.00
-- +
-- 2.50
-- +
-- 0.005
-- 3
-- =
-- 2.50
-- AVG= 
-- 3
-- 5.00+2.50+0.005
-- ​
--  =2.50
-- For Cat group:

-- Compute rating / position for each row:
-- Row 1: 
-- 2
-- /
-- 5
-- =
-- 0.40
-- 2/5=0.40
-- Row 2: 
-- 3
-- /
-- 3
-- =
-- 1.00
-- 3/3=1.00
-- Row 3: 
-- 4
-- /
-- 7
-- ≈
-- 0.571
-- 4/7≈0.571
-- Average:
-- AVG
-- =
-- 0.40
-- +
-- 1.00
-- +
-- 0.571
-- 3
-- ≈
-- 0.66
-- AVG= 
-- 3
-- 0.40+1.00+0.571
-- ​
--  ≈0.66
-- Step 2: SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100 / COUNT(*)
-- For Dog group:

-- CASE WHEN rating < 3 THEN 1 ELSE 0 END:
-- Row 1: 0 (rating = 5)
-- Row 2: 0 (rating = 5)
-- Row 3: 1 (rating = 1)
-- SUM: 
-- 0
-- +
-- 0
-- +
-- 1
-- =
-- 1
-- 0+0+1=1
-- COUNT(*): 3 rows in total.
-- Poor query percentage:
-- 1
-- 3
-- ×
-- 100
-- =
-- 33.33
-- %
-- 3
-- 1
-- ​
--  ×100=33.33%
-- For Cat group:

-- CASE WHEN rating < 3 THEN 1 ELSE 0 END:
-- Row 1: 1 (rating = 2)
-- Row 2: 0 (rating = 3)
-- Row 3: 0 (rating = 4)
-- SUM: 
-- 1
-- +
-- 0
-- +
-- 0
-- =
-- 1
-- 1+0+0=1
-- COUNT(*): 3 rows in total.
-- Poor query percentage:
-- 1
-- 3
-- ×
-- 100
-- =
-- 33.33
-- %
-- 3
-- 1
-- ​
--  ×100=33.33%
-- Final Output:
-- query_name	quality	poor_query_percentage
-- Dog	2.50	33.33
-- Cat	0.66	33.33
-- Recap:
-- With GROUP BY, rows are grouped but not "lost." All rows in each group are still available for aggregate function calculations.
-- Aggregate functions like AVG, SUM, and COUNT process all rows in the group.
-- After processing, SQL outputs one row per group containing the grouped column(s) and the results of the aggregate functions.
-- Let me know if you need more clarification! 😊
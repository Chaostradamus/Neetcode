select a1.machine_id, round(avg(a2.timestamp-a1.timestamp), 3) as processing_time 
from Activity a1
join Activity a2 
on a1.machine_id=a2.machine_id and a1.process_id=a2.process_id
and a1.activity_type='start' and a2.activity_type='end'
group by a1.machine_id

-- 1661. Average Time of Process per Machine
-- Easy
-- Topics
-- Companies
-- SQL Schema
-- Pandas Schema
-- Table: Activity

-- +----------------+---------+
-- | Column Name    | Type    |
-- +----------------+---------+
-- | machine_id     | int     |
-- | process_id     | int     |
-- | activity_type  | enum    |
-- | timestamp      | float   |
-- +----------------+---------+
-- The table shows the user activities for a factory website.
-- (machine_id, process_id, activity_type) is the primary key (combination of columns with unique values) of this table.
-- machine_id is the ID of a machine.
-- process_id is the ID of a process running on the machine with ID machine_id.
-- activity_type is an ENUM (category) of type ('start', 'end').
-- timestamp is a float representing the current time in seconds.
-- 'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
-- The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
-- It is guaranteed that each (machine_id, process_id) pair has a 'start' and 'end' timestamp.
 

-- There is a factory website that has several machines each running the same number of processes. Write a solution to find the average time each machine takes to complete a process.

-- The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

-- The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Activity table:
-- +------------+------------+---------------+-----------+
-- | machine_id | process_id | activity_type | timestamp |
-- +------------+------------+---------------+-----------+
-- | 0          | 0          | start         | 0.712     |
-- | 0          | 0          | end           | 1.520     |
-- | 0          | 1          | start         | 3.140     |
-- | 0          | 1          | end           | 4.120     |
-- | 1          | 0          | start         | 0.550     |
-- | 1          | 0          | end           | 1.550     |
-- | 1          | 1          | start         | 0.430     |
-- | 1          | 1          | end           | 1.420     |
-- | 2          | 0          | start         | 4.100     |
-- | 2          | 0          | end           | 4.512     |
-- | 2          | 1          | start         | 2.500     |
-- | 2          | 1          | end           | 5.000     |
-- +------------+------------+---------------+-----------+
-- Output: 
-- +------------+-----------------+
-- | machine_id | processing_time |
-- +------------+-----------------+
-- | 0          | 0.894           |
-- | 1          | 0.995           |
-- | 2          | 1.456           |
-- +------------+-----------------+
-- Explanation: 
-- There are 3 machines running 2 processes each.
-- Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
-- Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
-- Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456


-- Let’s walk through the query step by step, based on the provided Activity table.

-- 1. Understand the Problem
-- We want to calculate the average processing time for each machine_id. The processing time is the difference between the timestamp values for the start and end activities for the same machine_id and process_id.

-- 2. The Query
-- sql
-- Copy
-- Edit
-- SELECT 
--     a1.machine_id, 
--     ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
-- FROM 
--     Activity a1
-- JOIN 
--     Activity a2 
-- ON 
--     a1.machine_id = a2.machine_id 
--     AND a1.process_id = a2.process_id
--     AND a1.activity_type = 'start' 
--     AND a2.activity_type = 'end'
-- GROUP BY 
--     a1.machine_id;
-- Step-by-Step Breakdown
-- Step 1: Self-Join the Activity Table
-- sql
-- Copy
-- Edit
-- FROM Activity a1
-- JOIN Activity a2 
-- ON a1.machine_id = a2.machine_id 
--    AND a1.process_id = a2.process_id
--    AND a1.activity_type = 'start' 
--    AND a2.activity_type = 'end'
-- Why Self-Join?

-- Each activity has either start or end in activity_type.
-- We pair each start activity (a1) with its corresponding end activity (a2) based on:
-- Matching machine_id
-- Matching process_id
-- Ensuring a1.activity_type = 'start' and a2.activity_type = 'end'.
-- Result of the Self-Join: For each valid pair, you'll get a table that looks like this:

-- a1.machine_id	a1.process_id	a1.activity_type	a1.timestamp	a2.activity_type	a2.timestamp
-- 0	0	start	0.712	end	1.52
-- 0	1	start	3.14	end	4.12
-- 1	0	start	0.55	end	1.55
-- 1	1	start	0.43	end	1.42
-- 2	0	start	4.1	end	4.512
-- 2	1	start	2.5	end	5
-- Step 2: Calculate the Time Difference
-- sql
-- Copy
-- Edit
-- a2.timestamp - a1.timestamp
-- For each pair, calculate the difference between the end timestamp (a2.timestamp) and the start timestamp (a1.timestamp).
-- This gives the processing time for each process.
-- Step 3: Group by machine_id
-- sql
-- Copy
-- Edit
-- GROUP BY a1.machine_id
-- Group all the rows by machine_id. This means:
-- All rows for machine_id = 0 are grouped together.
-- All rows for machine_id = 1 are grouped together.
-- All rows for machine_id = 2 are grouped together.
-- Step 4: Calculate the Average Processing Time
-- sql
-- Copy
-- Edit
-- ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
-- For each group (machine_id), calculate the average processing time:
-- Sum up all the time differences within the group.
-- Divide by the total number of rows in the group.
-- The ROUND(..., 3) ensures the result is rounded to 3 decimal places.
-- Final Output
-- The query produces the following output:

-- machine_id	processing_time
-- 0	0.889
-- 1	0.995
-- 2	1.456
-- This table shows the average processing time (rounded to 3 decimals) for each machine_id.

-- Why This Query Works
-- The self-join ensures each start is paired with its corresponding end.
-- Grouping by machine_id aggregates data for each machine.
-- The average calculation computes the desired result for each machine.
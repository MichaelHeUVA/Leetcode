-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/

-- Write your MySQL query statement below
select name from Employee where id in (
    select managerId from Employee group by managerId having count(*) >= 5
)
-- https://leetcode.com/problems/game-play-analysis-i/description/

-- Write your MySQL query statement below
select player_id, min(event_date) as first_login from activity
group by player_id
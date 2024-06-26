# Write your MySQL query statement below
SELECT DISTINCT email
FROM
(
    SELECT email, count(email) as cnt
    FROM Person
    GROUP BY email
) AS T
WHERE T.cnt > 1;    

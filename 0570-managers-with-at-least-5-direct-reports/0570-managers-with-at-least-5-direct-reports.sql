# Write your MySQL query statement below
WITH manager AS(
SELECT managerId, count(managerId) AS numeroimpiegati
FROM Employee
GROUP BY managerId
HAVING numeroimpiegati >= 5
)
SELECT name
FROM Employee e
JOIN manager m ON e.id = m.managerId
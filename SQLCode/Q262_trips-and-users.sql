# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/30 9:13
# @File    : Q262_trips-and-users.sql
# @Note    : https://leetcode-cn.com/problems/trips-and-users/


--    Trips
--    +----+-----------+-----------+---------+--------------------+----------+
--    | Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
--    +----+-----------+-----------+---------+--------------------+----------+
--    | 1  |     1     |    10     |    1    |     completed      |2013-10-01|
--    | 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
--    | 3  |     3     |    12     |    6    |     completed      |2013-10-01|
--    | 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
--    | 5  |     1     |    10     |    1    |     completed      |2013-10-02|
--    | 6  |     2     |    11     |    6    |     completed      |2013-10-02|
--    | 7  |     3     |    12     |    6    |     completed      |2013-10-02|
--    | 8  |     2     |    12     |    12   |     completed      |2013-10-03|
--    | 9  |     3     |    10     |    12   |     completed      |2013-10-03|
--    | 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
--    +----+-----------+-----------+---------+--------------------+----------+

--    Users
--    +----------+--------+--------+
--    | Users_Id | Banned |  Role  |
--    +----------+--------+--------+
--    |    1     |   No   | client |
--    |    2     |   Yes  | client |
--    |    3     |   No   | client |
--    |    4     |   No   | client |
--    |    10    |   No   | driver |
--    |    11    |   No   | driver |
--    |    12    |   No   | driver |
--    |    13    |   No   | driver |
--    +----------+--------+--------+

SELECT T.request_at AS `Day`, ROUND(SUM(IF(T.STATUS = 'completed',0,1))/COUNT(T.STATUS), 2) AS `Cancellation Rate`
FROM Trips AS T
JOIN Users AS U1 ON (T.client_id = U1.users_id AND U1.banned ='No')
JOIN Users AS U2 ON (T.driver_id = U2.users_id AND U2.banned ='No')
WHERE T.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY T.request_at
;

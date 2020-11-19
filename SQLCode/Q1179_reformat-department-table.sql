# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/19 8:57
# @File    : Q1179_reformat-department-table.sql
# @Note    : https://leetcode-cn.com/problems/reformat-department-table/

--    Department
--    +---------------+---------+
--    | Column Name   | Type    |
--    +---------------+---------+
--    | id            | int     |
--    | revenue       | int     |
--    | month         | varchar |
--    +---------------+---------+
--    (id, month) 是表的联合主键。
--    这个表格有关于每个部门每月收入的信息。
--    月份（month）可以取下列值 ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

--    Department 表：
--    +------+---------+-------+
--    | id   | revenue | month |
--    +------+---------+-------+
--    | 1    | 8000    | Jan   |
--    | 2    | 9000    | Jan   |
--    | 3    | 10000   | Feb   |
--    | 1    | 7000    | Feb   |
--    | 1    | 6000    | Mar   |
--    +------+---------+-------+

select t0.id
      ,t1.revenue as Jan_Revenue
      ,t2.revenue as Feb_Revenue
      ,t3.revenue as Mar_Revenue
      ,t4.revenue as Apr_Revenue
      ,t5.revenue as May_Revenue
      ,t6.revenue as Jun_Revenue
      ,t7.revenue as Jul_Revenue
      ,t8.revenue as Aug_Revenue
      ,t9.revenue as Sep_Revenue
      ,t10.revenue as Oct_Revenue
      ,t11.revenue as Nov_Revenue
      ,t12.revenue as Dec_Revenue
from(select id from Department group by id) t0
left join(select id, revenue from Department where month='Jan') t1 on t0.id = t1.id
left join(select id, revenue from Department where month='Feb') t2 on t0.id = t2.id
left join(select id, revenue from Department where month='Mar') t3 on t0.id = t3.id
left join(select id, revenue from Department where month='Apr') t4 on t0.id = t4.id
left join(select id, revenue from Department where month='May') t5 on t0.id = t5.id
left join(select id, revenue from Department where month='Jun') t6 on t0.id = t6.id
left join(select id, revenue from Department where month='Jul') t7 on t0.id = t7.id
left join(select id, revenue from Department where month='Aug') t8 on t0.id = t8.id
left join(select id, revenue from Department where month='Sep') t9 on t0.id = t9.id
left join(select id, revenue from Department where month='Oct') t10 on t0.id = t10.id
left join(select id, revenue from Department where month='Nov') t11 on t0.id = t11.id
left join(select id, revenue from Department where month='Dec') t12 on t0.id = t12.id
;


SELECT id,
SUM(CASE WHEN month='Jan' THEN revenue END) AS Jan_Revenue,
SUM(CASE WHEN month='Feb' THEN revenue END) AS Feb_Revenue,
SUM(CASE WHEN month='Mar' THEN revenue END) AS Mar_Revenue,
SUM(CASE WHEN month='Apr' THEN revenue END) AS Apr_Revenue,
SUM(CASE WHEN month='May' THEN revenue END) AS May_Revenue,
SUM(CASE WHEN month='Jun' THEN revenue END) AS Jun_Revenue,
SUM(CASE WHEN month='Jul' THEN revenue END) AS Jul_Revenue,
SUM(CASE WHEN month='Aug' THEN revenue END) AS Aug_Revenue,
SUM(CASE WHEN month='Sep' THEN revenue END) AS Sep_Revenue,
SUM(CASE WHEN month='Oct' THEN revenue END) AS Oct_Revenue,
SUM(CASE WHEN month='Nov' THEN revenue END) AS Nov_Revenue,
SUM(CASE WHEN month='Dec' THEN revenue END) AS Dec_Revenue
FROM department
GROUP BY id
ORDER BY id;

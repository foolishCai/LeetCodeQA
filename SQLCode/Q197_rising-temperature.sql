# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/17 12:45
# @File    : Q197_rising-temperature.sql
# @Note    : https://leetcode-cn.com/problems/rising-temperature/

--    Weather
--    +---------------+---------+
--    | Column Name   | Type    |
--    +---------------+---------+
--    | id            | int     |
--    | recordDate    | date    |
--    | temperature   | int     |
--    +---------------+---------+
--
--    Weather
--    +----+------------+-------------+
--    | id | recordDate | Temperature |
--    +----+------------+-------------+
--    | 1  | 2015-01-01 | 10          |
--    | 2  | 2015-01-02 | 25          |
--    | 3  | 2015-01-03 | 20          |
--    | 4  | 2015-01-04 | 30          |
--    +----+------------+-------------+

select b.id as id
from Weather a
join Weather b on a.Temperature<b.Temperature and date_add(a.recordDate,INTERVAL 1 DAY) = b.recordDate
;
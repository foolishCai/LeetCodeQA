#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 9:29
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @File    : Q175.sql
# @Note    : https://leetcode-cn.com/problems/combine-two-tables/


--    Person
--    +-------------+---------+
--    | 列名         | 类型     |
--    +-------------+---------+
--    | PersonId    | int     |
--    | FirstName   | varchar |
--    | LastName    | varchar |
--    +-------------+---------+
--    PersonId 是上表主键
--
--    Address
--    +-------------+---------+
--    | 列名         | 类型    |
--    +-------------+---------+
--    | AddressId   | int     |
--    | PersonId    | int     |
--    | City        | varchar |
--    | State       | varchar |
--    +-------------+---------+
--    AddressId 是上表主键


select a.PersonId, a.FirstName, a.LastName, b.City, b.State
from Person a
left join Address b on a.PersonId = b.PersonId
;
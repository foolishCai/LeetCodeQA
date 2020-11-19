# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/16 9:13
# @File    : Q196_delete-duplicate-emails.sql
# @Note    : https://leetcode-cn.com/problems/delete-duplicate-emails/


--    Person
--    +----+------------------+
--    | Id | Email            |
--    +----+------------------+
--    | 1  | john@example.com |
--    | 2  | bob@example.com  |
--    | 3  | john@example.com |
--    +----+------------------+


delete a.*
from Person a
join Person b on a.Email = b.Email and a.Id>b.Id
;
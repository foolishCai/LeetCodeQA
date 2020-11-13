# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/13 9:13
# @File    : Q182_duplicate-emails.sql
# @Note    : https://leetcode-cn.com/problems/duplicate-emails/

--    Person
--    +----+---------+
--    | Id | Email   |
--    +----+---------+
--    | 1  | a@b.com |
--    | 2  | c@d.com |
--    | 3  | a@b.com |
--    +----+---------+

select Email
from Person
group by Email
having count(distinct id)>1
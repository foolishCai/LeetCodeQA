# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/18 9:29
# @File    : Q596_classes-more-than-5-students.sql
# @Note    : https://leetcode-cn.com/problems/classes-more-than-5-students/

--    courses
--    +---------+------------+
--    | student | class      |
--    +---------+------------+
--    | A       | Math       |
--    | B       | English    |
--    | C       | Math       |
--    | D       | Biology    |
--    | E       | Math       |
--    | F       | Computer   |
--    | G       | Math       |
--    | H       | Math       |
--    | I       | Math       |
--    +---------+------------+

select t.class
from(
    select class, count(distinct student)
    from courses
    group by class
    having count(distinct student)>=5
)t

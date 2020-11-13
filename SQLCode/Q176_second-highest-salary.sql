# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/12 9:26
# @File    : Q176_second-highest-salary.sql
# @Note    : https://leetcode-cn.com/problems/second-highest-salary/


--    Employee
--    +----+--------+
--    | Id | Salary |
--    +----+--------+
--    | 1  | 100    |
--    | 2  | 200    |
--    | 3  | 300    |
--    +----+--------+

select if(t.Salary is not null, t.Salary, null) as SecondHighestSalary
from(
    select Salary, row_number() over(partition by Salary order by Salary desc) as rn
    from Employee
)t
where t.rn=2
;

select ifnull((select distinct Salary from Employee order by Salary desc limit 1 offset 1),null) as SecondHighestSalary;

## note: mysql 中的ifnull函数在hive中是if
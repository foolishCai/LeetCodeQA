# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/13 9:03
# @File    : Q181_employees-earning-more-than-their-managers.sql
# @Note    : https://leetcode-cn.com/problems/employees-earning-more-than-their-managers/


--    Employee
--    +----+-------+--------+-----------+
--    | Id | Name  | Salary | ManagerId |
--    +----+-------+--------+-----------+
--    | 1  | Joe   | 70000  | 3         |
--    | 2  | Henry | 80000  | 4         |
--    | 3  | Sam   | 60000  | NULL      |
--    | 4  | Max   | 90000  | NULL      |
--    +----+-------+--------+-----------+

select t.name
from(
    select a.Id, a.name, a.Salary, a.ManagerId, b.Salary as ManagerSalary
    from Employee a
    left join Employee b on a.ManagerId = b.Id
    where a.Salary > b.Salary
)t;
# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/26 8:42
# @File    : Q184_department-highest-salary.sql
# @Note    : https://leetcode-cn.com/problems/department-highest-salary/

--    Employee
--    +----+-------+--------+--------------+
--    | Id | Name  | Salary | DepartmentId |
--    +----+-------+--------+--------------+
--    | 1  | Joe   | 70000  | 1            |
--    | 2  | Jim   | 90000  | 1            |
--    | 3  | Henry | 80000  | 2            |
--    | 4  | Sam   | 60000  | 2            |
--    | 5  | Max   | 90000  | 1            |
--    +----+-------+--------+--------------+

--    Department
--    +----+----------+
--    | Id | Name     |
--    +----+----------+
--    | 1  | IT       |
--    | 2  | Sales    |
--    +----+----------+


select b.Name as Department, c.Name as Employee, c.Salary
from(
    select DepartmentId, max(Salary) as Salary
    from Employee
    group by DepartmentId
)a
join Department b on a.DepartmentId = b.Id
join Employee c on a.DepartmentId = c.DepartmentId and a.Salary = c.Salary
;
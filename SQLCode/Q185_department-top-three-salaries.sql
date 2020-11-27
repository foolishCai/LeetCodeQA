# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/27 8:57
# @File    : Q185_department-top-three-salaries.sql
# @Note    : https://leetcode-cn.com/problems/department-top-three-salaries/


--    Employee
--    +----+-------+--------+--------------+
--    | Id | Name  | Salary | DepartmentId |
--    +----+-------+--------+--------------+
--    | 1  | Joe   | 85000  | 1            |
--    | 2  | Henry | 80000  | 2            |
--    | 3  | Sam   | 60000  | 2            |
--    | 4  | Max   | 90000  | 1            |
--    | 5  | Janet | 69000  | 1            |
--    | 6  | Randy | 85000  | 1            |
--    | 7  | Will  | 70000  | 1            |
--    +----+-------+--------+--------------+

--    Department
--    +----+----------+
--    | Id | Name     |
--    +----+----------+
--    | 1  | IT       |
--    | 2  | Sales    |
--    +----+----------+

select t.Department, t.Employee, t.Salary
from(
    select  a.Name as Department, b.Name as Employee, b.Salary, dense_rank() over(partition by a.Id order by b.Salary desc) as rn
    from Department a
    join Employee b on a.ID = b.DepartmentId
    order by a.Id, b.Salary desc
)t
where t.rn<=3
;
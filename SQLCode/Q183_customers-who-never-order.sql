# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/16 9:08
# @File    : Q183_customers-who-never-order.sql
# @Note    : https://leetcode-cn.com/problems/customers-who-never-order/

--    Customers
--    +----+-------+
--    | Id | Name  |
--    +----+-------+
--    | 1  | Joe   |
--    | 2  | Henry |
--    | 3  | Sam   |
--    | 4  | Max   |
--    +----+-------+
--
--    Orders
--    +----+------------+
--    | Id | CustomerId |
--    +----+------------+
--    | 1  | 3          |
--    | 2  | 1          |
--    +----+------------+

select a.Name as Customers
from Customers a
left join Orders b on a.Id = b.CustomerId
where b.Id is null
;
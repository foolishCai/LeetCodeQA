# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/19 8:51
# @File    : Q627_swap-salary.sql
# @Note    : https://leetcode-cn.com/problems/swap-salary/

--    salary
--
--    | id | name | sex | salary |
--    |----|------|-----|--------|
--    | 1  | A    | m   | 2500   |
--    | 2  | B    | f   | 1500   |
--    | 3  | C    | m   | 5500   |
--    | 4  | D    | f   | 500    |

update salary set sex = (case when sex='m' then 'f' else 'm' end)
;
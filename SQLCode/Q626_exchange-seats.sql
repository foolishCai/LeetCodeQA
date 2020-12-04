# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/12/2 8:44
# @File    : Q626_exchange-seats.sql
# @Note    : https://leetcode-cn.com/problems/exchange-seats/

--    seat
--    +---------+---------+
--    |    id   | student |
--    +---------+---------+
--    |    1    | Abbot   |
--    |    2    | Doris   |
--    |    3    | Emerson |
--    |    4    | Green   |
--    |    5    | Jeames  |
--    +---------+---------+

select a.id
      ,coalesce((case when a.id%2=1 then b.student
             when a.id%2=0 then c.student
        else null end), a.student) as student
from seat a
left join seat b on a.id+1 = b.id
left join seat c on a.id-1 = c.id
;



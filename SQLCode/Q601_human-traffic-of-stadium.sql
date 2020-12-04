# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/12/1 8:50
# @File    : Q601_human-traffic-of-stadium.sql
# @Note    : https://leetcode-cn.com/problems/human-traffic-of-stadium/

--    Stadium table:
--    +------+------------+-----------+
--    | id   | visit_date | people    |
--    +------+------------+-----------+
--    | 1    | 2017-01-01 | 10        |
--    | 2    | 2017-01-02 | 109       |
--    | 3    | 2017-01-03 | 150       |
--    | 4    | 2017-01-04 | 99        |
--    | 5    | 2017-01-05 | 145       |
--    | 6    | 2017-01-06 | 1455      |
--    | 7    | 2017-01-07 | 199       |
--    | 8    | 2017-01-09 | 188       |
--    +------+------------+-----------+
--
--    Result table:
--    +------+------------+-----------+
--    | id   | visit_date | people    |
--    +------+------------+-----------+
--    | 5    | 2017-01-05 | 145       |
--    | 6    | 2017-01-06 | 1455      |
--    | 7    | 2017-01-07 | 199       |
--    | 8    | 2017-01-09 | 188       |
--    +------+------------+-----------+

select distinct t.id, t.visit_date, t.people
from Stadium t
join(
    select id
          ,lead(id, 1, null) over(order by id) as nxt_id1
          ,lead(id, 2, null) over(order by id) as nxt_id2
    from Stadium
    where people>=100
)t1 on (t1.nxt_id1-t1.id<=1 and t1.nxt_id2-t1.id<=2) and (t.id=t1.id or t.id=t1.nxt_id1 or t.id=t1.nxt_id2)
;
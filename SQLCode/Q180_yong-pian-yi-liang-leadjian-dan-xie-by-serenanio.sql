# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/25 10:04
# @File    : Q180_yong-pian-yi-liang-leadjian-dan-xie-by-serenanio.sql
# @Note    : https://leetcode-cn.com/problems/consecutive-numbers/

--    Logs
--    +----+-----+
--    | Id | Num |
--    +----+-----+
--    | 1  |  1  |
--    | 2  |  1  |
--    | 3  |  1  |
--    | 4  |  2  |
--    | 5  |  1  |
--    | 6  |  2  |
--    | 7  |  2  |
--    +----+-----+


select distinct a.Num as ConsecutiveNums
from(
    select Id
          ,Num
          ,lead(Num,1) over(order by Id)as Num2
          ,lead(Num,2) over(order by Id)as Num3
    from Logs
)a
where a.Num = a.Num2 and a.Num2=a.Num3
;
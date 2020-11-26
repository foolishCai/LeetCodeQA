# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/23 9:18
# @File    : Q178_rank-scores.sql
# @Note    : https://leetcode-cn.com/problems/rank-scores/

--    Rank
--    +----+-------+
--    | Id | Score |
--    +----+-------+
--    | 1  | 3.50  |
--    | 2  | 3.65  |
--    | 3  | 4.00  |
--    | 4  | 3.85  |
--    | 5  | 4.00  |
--    | 6  | 3.65  |
--    +----+-------+


select a.Score as Score,
       (select count(distinct b.Score) from Scores b where b.Score >= a.Score) as `Rank`
from Scores a
order by a.Score DESC


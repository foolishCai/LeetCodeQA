# -*- coding: utf-8 -*-
# @Author  : Cai
# @Emaio   : chenyuwei_0303@yeah.net
# @Time    : 2020/11/20 9:04
# @File    : Q620_not-boring-movies.sql
# @Note    : https://leetcode-cn.com/problems/not-boring-movies/


--    cinema
--    +---------+-----------+--------------+-----------+
--    |   id    | movie     |  description |  rating   |
--    +---------+-----------+--------------+-----------+
--    |   1     | War       |   great 3D   |   8.9     |
--    |   2     | Science   |   fiction    |   8.5     |
--    |   3     | irish     |   boring     |   6.2     |
--    |   4     | Ice song  |   Fantacy    |   8.6     |
--    |   5     | House card|   Interesting|   9.1     |
--    +---------+-----------+--------------+-----------+

select id, movie, description, rating
from cinema
where description <> 'boring' and id%2==1
order by rating desc
;
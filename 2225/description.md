# 2225. Find Players With Zero or One Losses
You are given an integer array matches where matches\[i\] = \[winneri, loseri\] indicates that the player `winneri` defeated player `loseri` in a match.

Return a list answer of size 2 where:

1. answer[0] is a list of all players that have not lost any matches.
2. answer[1] is a list of all players that have lost exactly one match.
3. The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.
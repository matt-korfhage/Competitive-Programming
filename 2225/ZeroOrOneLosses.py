from typing import List, Set, Any

class Solution:
    # answer[0] is a list of all players that have not lost any matches.
    # answer[1] is a list of all players that have lost exactly one match.
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winSet = set()
        lossSet = set()
        oneLossSet = set()
        for i in range(0, len(matches)):
            winner = matches[i][0]
            loser = matches[i][1]
            winSet.add(winner)
            if lossSet.__contains__(loser):
                oneLossSet.discard(loser)
            else:
                lossSet.add(loser)
                oneLossSet.add(loser)
        noMatchesLost = list(winSet.difference(lossSet))
        List.sort(list(noMatchesLost))
        oneLossSet = List.sort(list(oneLossSet))
        return [noMatchesLost, oneLossSet]

mylist = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
mysol = Solution()
print(mysol.findWinners(mylist))
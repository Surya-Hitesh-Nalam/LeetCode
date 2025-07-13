class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        pairs=0
        i,j=0,0
        while i<len(players) and j<len(trainers):
            if players[i]>trainers[j]:
                j+=1
            else:
                pairs+=1
                i+=1
                j+=1
        return pairs

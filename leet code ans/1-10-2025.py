#my solution to the leetcode problem 1518. Water Bottles
#https://leetcode.com/problems/water-bottles/
class Solution0:
    def __init__(self):
        self.numBottles=1
        self.numExchange=0
    def numWaterBottles(self, numBot, numExc):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        numBot2=numBot
        l=[]
        while True:
            if numBot2%numExc==0:
                l.append(numBot)
                numBot=numBot//numExc
                print(numBot)
                if numBot<=0:
                    break
            elif numBot2%numExc>=0:
                l.append(numBot)
                numBot=numBot//numExc
                print(numBot)
                if numBot<=0:
                    if numBot2<numExc:
                        pass
                    else:
                        l.append(0)
                    break
            else:
                print("idk")
                break
        l1=sum(l)
        print("the number of water bottles you can drink is",l1)
        return l1
#actual solution
class Solution1:
    def numWaterBottles(self, numBottles, numExchange):
        consumed_bottles = 0

        while numBottles >= numExchange:
            # Consume numExchange full bottles.
            consumed_bottles += numExchange
            numBottles -= numExchange

            # Exchange them for one full bottle.
            numBottles += 1

        # Consume the remaining numBottles (less than numExchange).
        return consumed_bottles + numBottles

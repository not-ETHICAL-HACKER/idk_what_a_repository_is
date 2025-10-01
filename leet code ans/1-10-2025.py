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
#my solution for 2094 finding 3 digit even numbers from a array of digits
class Solution2:
    def __init__(self):
        self.x=1
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l=[]
        res=[1]
        results={}
        len_d=len(digits)
        for i in range(len_d):
            for j in range(len_d):
                for k in range(len_d):
                    summ=0
                    if digits[i]!=digits[j]!=digits[k] and digits[i]!=digits[k] and digits[k]%2==0 and digits[i]!=0:
                        print(digits[i],digits[j],digits[k])
                        hun_p=digits[i]*100
                        ten_p=digits[j]*10
                        one_p=digits[k]*1
                        summ=hun_p+ten_p+one_p
                        l.append(summ)
                        scn=1
                    else:
                        continue
        l.sort()
        if digits[0]==digits[1] or digits[2]==digits[3]:
            results=set(results)
            len_d=len(digits)
            for i in range(len_d):
                for j in range(len_d):
                    for k in range(len_d):
                        summ=0
                        print(digits[i],digits[j],digits[k])
                        hun_p=digits[i]*100
                        ten_p=digits[j]*10
                        one_p=digits[k]*1
                        summ=hun_p+ten_p+one_p
                        results.add(summ)
                        res=sorted(results)
                        scn=2
        if scn==1:
            return l
        if scn==2:
            return res
#actual solution
class Solution:
    def findEvenNumbers(self, digits:list):
        nums = set()  # Target even set
        n = len(digits)
        # Traverse the indices of three digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Determine whether it meets the condition of the target even number
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        # Converted to an array sorted in ascending order
        res = sorted(list(nums))
        return res

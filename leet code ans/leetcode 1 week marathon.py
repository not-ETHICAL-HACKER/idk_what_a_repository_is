#my solution to the leetcode problem 1518. Water Bottles
#https://leetcode.com/problems/water-bottles/
class Solution:
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
#soltion for 1550 three consecutive odds
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        le_arr=len(arr)
        w_arr=arr.remove("[")
        w_arr=arr.remove("]")
        l_arr=len(arr)*10
        for i in range(l_arr):
            if int(w_arr[i])%2==1 and int(w_arr[i+1]%2==1) and int(w_arr[i+2])%2==1:
                print(arr[i],arr[i+1],arr[i+2])
                return True
            else:
                return False
#actual solution
class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False
        for i in range(len(arr) - 2):
            if arr[i] & 1 and arr[i+1] & 1 and arr[i+2] & 1:
                return True
        return False
#my solution for 3024 Type of Triangle (i actually solved this one first try)
    def triangleType(self, num):
        """
        :type nums: List[int]
        :rtype: str
        """
        tri=False
        if num[0]+num[1]>num[2] and num[1]+num[2]>num[0] and num[0]+num[2]>num[1]:
            tri = True
        else:
            return "none"
        if tri:
            if num[0]==num[1]==num[2]:
                return "equilateral"
            elif num[0]==num[1] or num[1]==num[2] or num[2]==num[0]:
                return "isosceles"
            elif num[0]!=num[1]!=num[2]:
                return "scalene"
#my solution for 1. Two Sum
    def twoSum(self, nums, target):
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    ans.append(i)
                    ans.append(j)
                    return ans
#my solution for 121 buy and seel stock
    def maxProfit(self, pri):
        maxprofit=ans=0
        for i in range(len(pri)):
            for j in range(len(pri)):
                if i>j:
                    ans=pri[i]-pri[j]
                if ans>maxprofit:
                    maxprofit=ans
        return maxprofit
#actual solution of 121 
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
#my solution(ai) to 118. Pascal's Triangle
    def generate(self, num):
        l=[[1]]
        for i in range(1,num):
            pre=l[-1]
            row=[1]
            for j in range(1,len(pre)):
                row.append(pre[j-1]+pre[j])
            row.append(1)
            l.append(row)
        return l
#my solution for 9. Palindrome Number:
    def isPalindrome(self, x):
        if x<0:
            return False
        xx=int(str(x)[::-1])
        if x==xx:
            return True
        else:
            return False
#my solution for 7. Reverse Integer
    def reverse(self, x):
        sign=1
        if x<0:
            x*=-1
            sign=-1
        x=int(str(x)[::-1])
        if x>2**31+1:
            return 0
        return x*sign
    def number(self,nums):
        res=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                res.append(nums[i])
        for i in range(len(nums)):
            if nums[i]%2==1:
                res.append(nums[i])
        return res
    def mintotal(self,tri):
        l=[]
        for i in range(len(tri)):
            l.append(min(tri[i]))
        return sum(l)
    def Row_of_pascal_triangle(self, rowIndex):
        num=rowIndex+1#normally num is given in the function but ts is just for one row so 
        #we add 1 to rowIndex to get the num of rows
        l=[[1]]
        for i in range(1,num):
            pre=l[-1]
            row=[1]
            for j in range(1,len(pre)):
                row.append(pre[j-1]+pre[j])
            row.append(1)
            l.append(row)
        return l[rowIndex]#return just l for full triangle:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign=1
        l=[]
        s.strip()
        for i,ch in enumerate(s):
            if not s[i-1].isalnum()  and ch=="-":
                sign=-1 
            if ch.isdigit():
                l.append(ch)
            elif ch.isalpha():
                break
        return int(''.join(l))*sign
    def not_myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        sign = 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            if result * sign > 2**31 - 1:
                return 2**31 - 1
            if result * sign < -2**31:
                return -2**31
            i += 1
        
        return result * sign
sol=Solution()
sol.mintotal((input("ENter tri angle")))
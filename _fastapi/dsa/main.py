class Solution(object):
    def topKFrequent(self, nums, k):
        map: dict[int, int] = {}
        l: list[(int, int)] = []
        res: list[int] = []
        for item in nums:
            if(map.get(item)):
                map[item] += 1
            else:
                map[item] = 1

        for key, val in map.items():
            l.append((key, val))
        l.sort(key=lambda item: item[1], reverse=True)
        i = 0
        while(i < k and i < len(l)):
            res.append(l[i][0])
            i+=1
        return res

# Solution().topKFrequent(nums=[1,2,2,2,3,1,3,2,3], k=2)
# print(Solution().topKFrequent(nums=[1], k=1))
# print(Solution().topKFrequent(nums=[1,1,1,2,2,3], k=2))
# print(Solution().topKFrequent(nums=[1,2], k=2))

class Solution(object):
    def findMaxK(self, nums: list[int]):
        nums.sort()
        i,j = 0,len(nums) - 1
        while(i < j):
            left = abs(nums[i])
            if nums[i] < 0 and left == nums[j]:
                return nums[j]
            elif left < nums[j]:
                j-=1
            else:
                i+=1
        return -1

print(Solution().findMaxK([-1,2,-3,3]))
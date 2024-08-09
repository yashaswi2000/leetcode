# suprisingly, this solution is accepted by leetcode even though its brute force
# and has a time complexity of O(n^2logn) and space complexity of O(n^2)

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        modulo = 1000000000 + 7
        prefixSum = []
        for num in nums:
            if prefixSum:
                prefixSum.append(prefixSum[-1] + num)
            else:
                prefixSum.append(num)

        sums = []
        for i in range(n):
            for j in range(i,n):
                sums.append(prefixSum[j] - prefixSum[i] + nums[i])

        sums.sort()
        for i in range(1, len(sums)):
            sums[i] =  sums[i]%modulo + sums[i-1]%modulo

        if left-1:
            return sums[right-1]%modulo - sums[left-2]%modulo
        else:
            return sums[right-1]%modulo

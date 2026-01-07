class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        tails = []
    
        for num in nums:
            left, right = 0, len(tails) - 1
            while left <= right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
        
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)

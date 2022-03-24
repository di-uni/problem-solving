class Solution(object):
    def subarraySum(self, nums, k):

        # First Trial with other's hint
        
        prefix_sum = 0
        sum_dict = {0: 1}
        ans = 0
        
        for n in nums:
            prefix_sum += n
            
            if prefix_sum - k in sum_dict:
                ans += sum_dict[prefix_sum - k]
            
            if prefix_sum not in sum_dict:
                sum_dict[prefix_sum] = 0
            sum_dict[prefix_sum] += 1
        
        return ans
            
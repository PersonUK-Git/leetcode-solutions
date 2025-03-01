class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        nums = [x for x in nums if x != 0] + [0] * nums.count(0)
        return nums
    
'''
CPP SOLUTION 
class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        for(int i = 0; i < nums.size() - 1; i++){
            if(nums[i] == nums[i+1]){
                nums[i] = nums[i] * 2;
                nums[i + 1] = 0;
            }
        }

        // move all zero to the end while maintaing order
        vector<int> result;
        for(int num : nums){
            if(num != 0) result.push_back(num);
        }

        //add the require number of zero at the back
        result.resize(nums.size(), 0);
        return result;
    }
};
'''
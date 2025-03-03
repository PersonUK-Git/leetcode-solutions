from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        large = []
        equal = []

        for num in nums:
            if num < pivot:
                small.append(num)
            elif num > pivot:
                large.append(num)
            else:
                equal.append(num)

        
        return small + equal + large


sol = Solution()

print(sol.pivotArray([9, 7, 2, 4, 6, 5, 3], 5))  # [2, 4, 3, 5, 9, 7, 6]
print(sol.pivotArray([9,12,5,10,14,3,10], 10))  # [9,5,3,10,10,12,14]



'''
CPP SOLUTION
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> small = {};
        vector<int> equal = {};
        vector<int> large = {};
        for( int num : nums){
            if(num < pivot){
                small.push_back(num);
            }
            else if(num > pivot){
                large.push_back(num);
            }
            else{
                equal.push_back(num);
            }
        }

        small.insert(small.end(), equal.begin(), equal.end());
        small.insert(small.end(), large.begin(), large.end());
        return small;
    }
};
'''
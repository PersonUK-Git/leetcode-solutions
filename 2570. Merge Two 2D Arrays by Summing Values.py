class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0,0

        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                result.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1

            elif nums1[i][0] < nums2[j][0]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j+=1

        while i<len(nums1):
            result.append(nums1[i])
            i+=1

        while j<len(nums2):
            result.append(nums2[j])
            j+=1 

        return result
    


'''
CPP SOLUTION

class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        vector<vector<int>>result;
        int i = 0 , j = 0;
        while(i < nums1.size() && j < nums2.size()){
            if(nums1[i][0] == nums2[j][0]){
                result.push_back({nums1[i][0], nums1[i][1] + nums2[j][1]});
                i++;
                j++;
            }
            else if(nums1[i][0] < nums2[j][0]){
                result.push_back(nums1[i]);
                i++;
            }
            else{
                result.push_back(nums2[j]);
                j++;
            }
        }

    while(i < nums1.size()){
        result.push_back(nums1[i++]);
    }

    
        while (j < nums2.size()) {
            result.push_back(nums2[j++]);
        }

        return result;
    }
};
'''

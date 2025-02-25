class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        cur_sum = 0
        odd_cnt = 0
        even_cnt = 0
        res = 0
        MOD = 10**9 + 7

        for n in arr:
            cur_sum += n
            if cur_sum % 2:
                res = (res + even_cnt + 1) % MOD
                odd_cnt += 1
            else:
                odd_cnt += 1
                res = (res + odd_cnt) % MOD
                even_cnt += 1
        return res  

'''
CPP SOLUTION
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int cur_sum = 0;
        int odd_cnt = 0;
        int even_cnt = 0;
        int res = 0;
        const int MOD = 1e9 + 7;

        for (int n : arr) {
            cur_sum += n;
            if (cur_sum % 2 != 0) {
                res = (res + even_cnt + 1) % MOD;
                odd_cnt++;
            } else {
                res = (res + odd_cnt) % MOD;
                even_cnt++;
            }
        }
        return res;
    }
};
'''


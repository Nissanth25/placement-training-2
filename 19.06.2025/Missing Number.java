class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int[] freq = new int[n + 1];
        for(int num : nums){
            freq[num]++;
        }
        for(int i = 0; i <= n; i++){
            if(freq[i] == 0){
                return i;
            }
        }
        return 0;
    }
}

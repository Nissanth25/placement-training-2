class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int count=1;
        int res=1;
        int len=nums.length;
        for(int i=1;i<len;i++){
            if(nums[i]>nums[i-1]){
            
                 count++; 
                if(count>res)res=count;
           }
            else{
              count=1;

            }
        }
      
      return res;
    }
}

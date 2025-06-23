class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> arr=new ArrayList<>();
        for(int i=left;i<=right;i++){
            if(i>9){
              boolean f=false;
              int k=i;
              while(k!=0){
                int j=k%10;
                if(j==0){
                    f=true;
                    break;
                }
                if(j!=0 && i%j!=0){
                    f=true;
                    break;
                }
                k=k/10;
              }
              if(!f){
                arr.add(i);
              }
            }
            else{
                arr.add(i);
            }
        }
        return arr;
    }
}

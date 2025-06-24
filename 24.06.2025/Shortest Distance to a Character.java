class Solution {
    public int[] shortestToChar(String s, char c) {
        List<Integer> list = new ArrayList();
        int temp=Integer.MAX_VALUE;
        for(int i=0;i<s.length();i++){
            temp=Integer.MAX_VALUE;
             for(int j=0;j<s.length();j++){
                 if(s.charAt(j)==c){
                    int a  = Math.abs(i-j);
                    if(a<temp)
                        temp=a;
                 }
             }
             list.add(temp);
        }
        int[] arr = list.stream().mapToInt(i -> i).toArray();
        return arr;
    }
}

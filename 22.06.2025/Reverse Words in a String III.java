class Solution {
    public String reverseWords(String s) {
        String arr[] = s.split(" ");
        s="";
        String str="";
        for(int i=0;i<arr.length;i++){
            for(int j=arr[i].length()-1;j>-1;j--){
                str+=arr[i].charAt(j);
            }
            s+=str+" ";
            str="";
        }
        s = s.trim();
        return s;
    }
}

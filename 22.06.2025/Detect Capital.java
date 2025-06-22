class Solution {
    public boolean detectCapitalUse(String word) {
        char[]a=word.toCharArray();
        int count=0;
        int count1=0;
        int count2=0;
        for(int i=0;i<a.length;i++){
            if(a[i]>='A'&& a[i]<='Z'){
                count+=1;
            }
        }
        for(int i=0;i<a.length;i++){
            if(a[i]>='a'&& a[i]<='z'){
                count1+=1;
            }
        }
        if(count1==a.length-1) {
            if(a[0]>='A' && a[0]<='Z'){
            count2+=1;
            }
        }

        if(count==a.length || count1==a.length || count2==1) return true;
        return false;
    }
}

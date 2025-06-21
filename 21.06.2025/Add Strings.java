class Solution {
    public String addStrings(String a, String b) {
        String s,t,v="";
        int i=0,j=0,carry=0;
        if(a.length() < b.length())
        {
            s=a;
            t=b;
        }
        else
        {
            s=b;
            t=a;
        }
        for(i=s.length()-1,j=t.length()-1;i>=0;i--,j--)
        {
            int x=s.charAt(i)-'0';
            int y=t.charAt(j)-'0';
            int sum=x+y+carry;
            carry=0;
            if(sum>9)
                carry=1;

            v=sum%10+v;
        }
         for(i=j;j>=0;j--)
        {
            int sum=carry+(t.charAt(j)-'0');
            carry=0;
            if(sum>9)
            carry=1;
            v=sum%10+v;
        }
        if(carry!=0)
        v=carry+v;

       
        return v;
    }
}

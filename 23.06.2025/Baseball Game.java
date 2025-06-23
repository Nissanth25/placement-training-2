class Solution {
    public int calPoints(String[] op) {
        Stack<Integer> arr=new Stack<>();
        for(int i=0;i<op.length;i++){
            int k=0;
            String c=op[i];
            
            if(!arr.isEmpty() && c.equals("D")){
                arr.push(arr.peek()*2);
            }
            else if(!arr.isEmpty() && c.equals("C")){
                arr.pop();
            }
            else if(!arr.isEmpty() && c.equals("+")){
                int f=arr.pop();
                int g=arr.peek();
                k+=f+g;
                arr.push(f);
                arr.push(k);

            }
            else{
               int d=Integer.parseInt(c);
               arr.push(d);
            }
            }
        
        int sum=0;
       for(int i:arr){
            sum+=i;
        }
        return sum;
    }
}

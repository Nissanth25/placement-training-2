class MyQueue {
    Stack<Integer> st1;
    Stack<Integer> st2;
    public MyQueue() {
       this.st1 = new Stack<>();
       this.st2 = new Stack<>();
    }   
    public void push(int x) {
        st1.add(x);
    }   
    public int pop() {
       if(st2.isEmpty())
       {
            while(st1.size()>0)
            {
                st2.add(st1.pop());
            }
       }
        return st2.pop();
    }
    public int peek() {
        if(st2.isEmpty())
        {
            while(st1.size()>0)
            {
                st2.add(st1.pop());
            }
        }
        return st2.peek();
    } 
    public boolean empty() {
        return st1.isEmpty() && st2.isEmpty();
        
    }
}

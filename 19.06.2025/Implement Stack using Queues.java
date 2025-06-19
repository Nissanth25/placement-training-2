class MyStack {
    Queue<Integer> queue1;
    Queue<Integer> queue2;
    public MyStack() {
        this.queue1 = new LinkedList<>();
        this.queue2 = new LinkedList<>();
    }
    
    public void push(int x) {
        queue1.add(x);
    }
    
    public int pop() {
        while(queue1.size()>1)
        {
            queue2.add(queue1.remove());
        }
        int popedElement = queue1.remove();

        Queue<Integer> temp = queue1;
        queue1 = queue2;
        queue2 = temp;
        return popedElement;
    }
    public int top() {
        while(queue1.size()>1)
        {
            queue2.add(queue1.remove());
        }
        int topElement = queue1.remove();
        queue2.add(topElement);
        
        Queue<Integer> temp = queue1;
        queue1 = queue2;
        queue2 = temp;

        return topElement;
    }
    public boolean empty() {
        return queue1.isEmpty();
    }
}

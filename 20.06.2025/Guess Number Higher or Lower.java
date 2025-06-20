public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 0;
        int heigh = n;
        while(low <= heigh){
            int mid = low + (heigh - low) / 2;
            if(guess(mid) == 0){
                return mid;
            }else if(guess(mid) == -1){
                heigh = mid - 1;
            }else{
                low = mid + 1;
            }
        }
        return -1;
    }
}

class Solution {
    public boolean judgeCircle(String moves) {
        int array[] = new int[26];
        for(char ch : moves.toCharArray()) {
            array[ch - 'A']++;
        }
        return (array['L'-'A']==array['R'-'A'] && array['U'-'A']==array['D'-'A']);
    }
}

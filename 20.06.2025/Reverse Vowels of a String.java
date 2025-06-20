class Solution {
    public String reverseVowels(String s) {
        
        int start = 0;
        int end = s.length() - 1;

        char[] ch = s.toCharArray();

        while (start < end) {

            char ch1 = Character.toLowerCase(ch[start]);
            char ch2 = Character.toLowerCase(ch[end]);

            if (ch1 == 'a' || ch1 == 'e' || ch1 == 'i' || ch1 == 'o' || ch1 == 'u') {
                if (ch2 == 'a' || ch2 == 'e' || ch2 == 'i' || ch2 == 'o' || ch2 == 'u') {
                    char temp = ch[start];
                    ch[start] = ch[end];
                    ch[end] = temp;

                    start++;
                    end--;
                }
                else {
                    end--;
                }
            }
            else {
                start++;
            }
        }
        return new String(ch);
    }
}

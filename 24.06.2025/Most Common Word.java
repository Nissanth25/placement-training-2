import java.util.*;

class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        HashMap<String, Integer> map = new HashMap<>();
        HashSet<String> set = new HashSet<>();

        for (int i = 0; i < banned.length; i++) {
            set.add(banned[i]);
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < paragraph.length(); i++) {
            char ch = paragraph.charAt(i);

            if (ch == ' ' || ch==',') {
                String word = sb.toString().toLowerCase();
                if (map.containsKey(word)) {
                    map.put(word, map.get(word) + 1);
                } else if (!set.contains(word) && word.length() > 0) {
                    map.put(word, 1);
                }
                sb = new StringBuilder();
            }

            if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
                sb.append(Character.toLowerCase(ch));
            }
        }
        if (sb.length() > 0) {
            String word = sb.toString().toLowerCase();
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else if (!set.contains(word)) {
                map.put(word, 1);
            }
        }

        int highestKey = -1;
        String key = "";

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            if (highestKey < entry.getValue()) {
                highestKey = entry.getValue();
                key = entry.getKey();
            }
        }

        return key;
    }
}

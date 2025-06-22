import java.util.*;

class Solution {
    public static String[] findMinIndSum(String list1[], String list2[]) {
        List<String> list = new ArrayList<>();
        int sum = Integer.MAX_VALUE;

        for (int i = 0; i < list1.length; i++) {
            String str = list1[i];
            for (int j = 0; j < list2.length; j++) {
                if (str.equals(list2[j])) {
                    int indexSum = i + j;
                    if (indexSum < sum) {
                        list.clear();         
                        list.add(str);
                        sum = indexSum;
                    } else if (indexSum == sum) {
                        list.add(str);         
                    }
                }
            }
        }

        return list.toArray(new String[0]);
    }

    public String[] findRestaurant(String[] list1, String[] list2) {
        return findMinIndSum(list1, list2);
    }
}

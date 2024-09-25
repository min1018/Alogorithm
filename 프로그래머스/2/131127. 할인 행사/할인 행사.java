import java.util.*;

class Solution {
    static Map<String, Integer> wish = new HashMap<>();
    static Map<String, Integer> test = new HashMap<>();
    
    public int solution(String[] want, int[] number, String[] discount) {
        for(int i = 0; i< want.length; i++) {
            wish.put(want[i], number[i]);
        }
        int answer = 0;
        for (int k = 0; k < discount.length - 9; k++) {
            for (int h = 0; h < 10; h++) {
                if (test.containsKey(discount[k+h])) {
                    test.put(discount[k+h], test.get(discount[k+h])+1);
                }
                else {
                    test.put(discount[k+h], 1);
                }
            }
            Boolean isIdentical = true;
            
            for (String key: wish.keySet()) {
                if(wish.get(key) != test.get(key)) {
                    isIdentical = false;
                    break;
                }
            }
            if (isIdentical) {
                answer += 1;
            }
            test.clear();
        }
        return answer;
    }
}


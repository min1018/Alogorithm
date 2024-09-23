import java.util.*;

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        Map<Integer, Integer> big = new HashMap<>();
        Map<Integer, Integer> small = new HashMap<>();
        
        for (int t : topping) {
            big.put(t, big.getOrDefault(t, 0) + 1);
        }
        
        for(int t : topping) {
            small.put(t, small.getOrDefault(t, 0) + 1);
            
            if (big.get(t) == 1) {
                big.remove(t);
            }
            else {
                big.put(t, big.get(t) - 1);
            }
            
            if (small.size() == big.size()) {
                answer += 1;
            }
        }
        return answer;
    }
}
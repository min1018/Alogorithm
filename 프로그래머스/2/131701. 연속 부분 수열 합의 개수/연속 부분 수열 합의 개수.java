import java.util.*;
class Solution {
    public int solution(int[] elements) {
        HashSet<Integer> poss = new HashSet<>();
        int n = elements.length;
        
        for (int i = 0; i< n ; i++) {
            for (int k = 0; k <n ; k++) {
                int sum = 0;
                for (int j = 0; j < i; j++) {
                    sum += elements[(k+j) % n];
                }
                poss.add(sum);
            }
        }
        
        return poss.size();
    }
}
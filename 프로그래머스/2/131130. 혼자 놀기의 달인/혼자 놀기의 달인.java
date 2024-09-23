import java.util.*;

class Solution {
    public int solution(int[] cards) {
        boolean[] visited = new boolean[cards.length];
        ArrayList<Integer> group = new ArrayList<>();
        
        for (int i = 0; i< cards.length; i++) {
            if (!visited[i]) {
                int cnt = 0;
                int index = i;
                while (!visited[index]) {
                    visited[index] = true;
                    index = cards[index] - 1;
                    cnt += 1;
                }
                group.add(cnt);
            }
        }
        Collections.sort(group, Collections.reverseOrder());
        
        if (group.size() <= 1) {
            return 0;
        }
        return group.get(0) * group.get(1);
        
    }
}
import java.util.PriorityQueue;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        
        int answer = 0;
        for (int i = 0; i< enemy.length; i++) {
            answer += 1;
            heap.offer(-enemy[i]);
            n -= enemy[i];
            if (n < 0) {
                if (k == 0) { return answer - 1; }
                k -= 1;
                n -= heap.poll();
            }
        }
        return answer;
    }
}
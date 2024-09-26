class Solution {
    
    private static int[] board;
    private static int answer;
    
    public int solution(int n) {
        board = new int[n];
        backTracking(0, n);
        return answer;
    }
    private static void backTracking(int depth, int n) {
        if (depth == n) {
            answer++;
            return;
        }
        for (int i = 0; i < n; i++) {
            board[depth] = i;
            if(valid(depth)) {
                backTracking(depth+1, n);
            }
        }
    }
    
    private static boolean valid(int i) {
        for (int k = 0; k< i; k++) {
            if (board[i] == board[k]) return false;
            if (Math.abs(i-k) == Math.abs(board[i] - board[k])) return false;
        }
        return true;
    }
}
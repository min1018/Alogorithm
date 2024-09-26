class Solution {
    int solution(int[][] land) {

        for(int i = 1; i< land.length; i++) {
            land[i][0] += maxNum(land[i-1][1], land[i-1][2], land[i-1][3]);
            land[i][1] += maxNum(land[i-1][0], land[i-1][2], land[i-1][3]);
            land[i][2] += maxNum(land[i-1][0], land[i-1][1], land[i-1][3]);
            land[i][3] += maxNum(land[i-1][1], land[i-1][2], land[i-1][0]);
        }
        
        int answer = maxNum(land[land.length-1][0],land[land.length-1][1], land[land.length-1][2]);
        answer = Math.max(answer, land[land.length-1][3]);
        return answer;
    }
    private static int maxNum(int a, int b, int c) {
        return Math.max(a, Math.max(b, c));
    }
}
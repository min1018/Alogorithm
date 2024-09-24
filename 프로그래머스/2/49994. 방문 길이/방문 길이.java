import java.util.*;

class Solution {                       
    static int[] dx = {-1, 1, 0, 0}; // U D L R
    static int[] dy = {0, 0, -1, 1};
    static HashSet<String> total = new HashSet<>();
    static int x = 0;
    static int y = 0;
    public int solution(String dirs) {
        char[] chars = dirs.toCharArray();
        for (char c : chars) {
            int index = -1;
            if (c == 'U') {
                index = 0;
            }
            if (c == 'D') {
                index = 1;
            }
            if (c == 'L') {
                index = 2;
            }
            if (c == 'R') {
                index = 3;
            }
            int nx = x + dx[index];
            int ny = y + dy[index];
                
            if (nx >= -5 && nx <= 5 && ny >= -5 && ny <= 5) {
                String move1 = x + "," + y + ","  + nx + ","+ny;
                String move2 = nx + "," + ny + "," + x +","+y;
                total.add(move1);
                total.add(move2);
                x = nx;
                y = ny;
            }
            else {
                continue;
            }
        }
        
        
        return total.size() / 2;
    }
}
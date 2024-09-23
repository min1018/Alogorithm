import java.util.LinkedList;
import java.util.Queue;


class Solution {
    
    static String[][] maze;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    
    public int solution(String[] maps) {
        maze = new String[maps.length][maps[0].length()];
        int[] start = new int[2];
        int[] lever = new int[2];
        
        for (int i = 0 ; i < maps.length; i++) {
            String[] tmp = maps[i].split("");
            
            for(int k = 0 ; k < tmp.length; k++) {
                maze[i][k] = tmp[k];
                
                if (maze[i][k].equals("S")) {
                    start = new int[]{i, k};
                }
                
                if (maze[i][k].equals("L")) {
                    lever = new int[] {i, k};
                }
            }
        }
        int result1 = bfs(start, "L");
        int result2 = bfs(lever, "E");
        
        if (result1 == -1 || result2 == -1) {
            return -1;
        }
        return result1 + result2;
        
    }
    
    public int bfs(int[] start, String target) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{start[0], start[1], 0});
        
        boolean[][] visited = new boolean[maze.length][maze[0].length];
        
        while(!q.isEmpty()) {
            int x = q.peek()[0];
            int y = q.peek()[1];
            int count = q.peek()[2];
            
            visited[x][y] = true;
            
            if (maze[x][y].equals(target)) {
                return count;
            }
            
            q.poll();
            for (int i = 0; i< 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < maze.length && ny >= 0 && ny < maze[0].length && !visited[nx][ny])
                {
                    if (!maze[nx][ny].equals("X")) {
                        visited[nx][ny] = true;
                        q.add(new int[] {nx, ny, count + 1});
                    }
                    
                }            
            }
        }
        return -1;
    }
}
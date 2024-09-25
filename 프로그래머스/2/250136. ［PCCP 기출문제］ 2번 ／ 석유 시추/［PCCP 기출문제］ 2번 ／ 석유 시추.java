import java.util.*;

class Solution {
    
    public int solution(int[][] land) {
        boolean[][] visited = new boolean[land.length][land[0].length];
        
        int[] poss = new int[land[0].length];
        //System.out.println(Arrays.toString(poss));
        for (int i = 0; i< land.length; i++) {
            for (int k = 0; k < land[0].length; k++) {
                if(!visited[i][k] && land[i][k] == 1) {
                    int[] result = bfs(i, k, visited, land);
                    //System.out.println(Arrays.toString(result));
                    for (int h = result[0]; h < result[1]+1; h++) {
                        poss[h] += result[2];
                    }
                }
            }
        }
        //System.out.println(Arrays.toString(poss));

        return Arrays.stream(poss).max().getAsInt();
    }
    
    public int[] bfs(int x, int y, boolean[][] visited, int[][] land) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        Queue<int[]> q = new LinkedList<>();
        
        int minY = y;
        int maxY = y;
        int cnt = 0;
        q.add(new int[]{x,y,cnt});
        visited[x][y] = true;
        
        while(!q.isEmpty()) {
            int[] temp = q.poll();
            int cx = temp[0];
            int cy = temp[1];
            cnt += 1;
            //System.out.println(cx+" "+cy);
            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];
                if (nx >= 0 && nx < land.length && ny >= 0 && ny < land[0].length && !visited[nx][ny] && land[nx][ny] == 1) {
                    q.add(new int[] {nx, ny});
                    visited[nx][ny] = true;
                    if (ny < minY) {
                        minY = ny;
                    }
                    if (ny > maxY) {
                        maxY = ny;
                    }
                }
            }
        }
        return new int[] {minY, maxY, cnt};
    }
}
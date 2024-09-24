import java.util.*;

class Solution {
    public int[] solution(String s) {
        s = s.substring(2, s.length());
        s = s.substring(0, s.length()-2).replace("},{", "-");
        String str[] = s.split("-");
        Arrays.sort(str, (a, b) -> (a.length()-b.length()));
        
        List<Integer> list = new ArrayList<>();
        
        for (String st : str) {
            String[] temp = st.split(",");
            for (String c :temp) {
                int n = Integer.parseInt(c);
                if (!list.contains(n)) {
                    list.add(n);
                    break;
                }
            }
        }
        int[] answer = new int[list.size()];
        for ( int i = 0; i< list.size() ; i++)  {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}
import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        char[] chars = s.toCharArray();
        List<Character> list = new ArrayList<>();
        for(char c: chars) {
            list.add(c);
        }
        //System.out.println(list);
        for (int i = 0; i < s.length(); i++) {
            Collections.rotate(list, 1);
            answer += check(list);
        }
        
        return answer;
    }
    
    public int check(List<Character> list) {
        List<Character> temp = new ArrayList<>();
        for (char nxt: list) {
            if (nxt =='}' || nxt==']'|| nxt==')') {
                    if (temp.size() == 0) { 
                        return 0; 
                    }
                    char val = temp.get(temp.size()-1);
                    if (nxt=='}' && val=='{') {
                        temp.remove(temp.size()-1);
                        continue;
                    }
                    if (nxt==')' && val=='(') {
                        temp.remove(temp.size()-1);
                        continue;
                    }
                    if (nxt == ']' && val == '[') {
                        temp.remove(temp.size()-1);
                        continue;
                    }
                }
            else {
                temp.add(nxt);
            }
        }
        if (temp.size() != 0) {
            return 0;
        }
        return 1;
        
    }
}
import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> map = new HashMap();
        
        for(String part : participant){
            if(map.containsKey(part)){
                map.put(part,map.get(part)+1);
            }
            else {
                map.put(part,1);
            }
            
        }
        
        for(String complete : completion){
            map.put(complete, map.get(complete)-1);
        }
        for(String key : map.keySet()){
            if(map.get(key)>0){
                answer = key;
                break;
            }
        }
        
        return answer;
    }
}

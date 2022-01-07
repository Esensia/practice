import java.util.*;
class Solution {
    static Map<String,Object> map;
    static ArrayList<String> answer;
    static int length = 0;
    static String[] ans = null;
    static void dfs(String city,int count){
        
        if(count == length && ans == null){
            ans = answer.toArray(new String[answer.size()]);
            return;
        } 

        if(!map.containsKey(city)){
            return;
        }
        
        List<String> arr = (ArrayList)map.get(city);
        
        if(arr.size()==0){
            return;
        }
        
        for(String airport : arr){
            
            List<String> list1 = (ArrayList)map.get(city);
            
            List<String> temp = new ArrayList();
            for(String str : list1){
                if(!str.equals(airport)){
                    temp.add(str);
                }
            }
            map.put(city,temp);
            answer.add(airport);
            
            dfs(airport,count+1);
            
            answer.remove(answer.size()-1);
            
            List<String> list2 = (ArrayList)map.get(city);
            temp = new ArrayList();
            for(String str : list2){

                temp.add(str);
            }
            temp.add(airport);
            Collections.sort(temp);
            map.put(city,temp);
            
        }
        
    }
    
    public String[] solution(String[][] tickets) {

        map = new HashMap();
        length = tickets.length;
        answer = new ArrayList();
        for(String[] str : tickets){
            String start = str[0];
            String end = str[1];
            
            if(map.containsKey(start)){
                List<String> arr = (ArrayList)map.get(start);
                arr.add(end);
                Collections.sort(arr);
                map.put(start,arr);
            }else{
                List<String> arr = new ArrayList();
                arr.add(end);
                map.put(start, arr);
            }
        }
        answer.add("ICN");
        dfs("ICN",0);
        return ans;
    }
}

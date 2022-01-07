import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        ArrayList<String> arr = new ArrayList();
        ArrayList<String> arr2 = new ArrayList();
        Map<String,String> map = new HashMap<>();
        for(String str : record){

            String[] order = str.split(" ");
            if(order.length == 2){
                arr.add("님이 나갔습니다.");
                arr2.add(order[1]);
            }
            else if(order[0].equals("Enter")){
                map.put(order[1],order[2]);
                arr.add("님이 들어왔습니다.");
                arr2.add(order[1]);
            } else {
                map.put(order[1],order[2]);
            }

        }
        String[] answer = new String[arr.size()];
        for(int j=0;j<arr.size();j++){
            answer[j] = map.get(arr2.get(j))+arr.get(j);
        }
        
        return answer;
    }
}

import java.util.*;
class Point implements Comparable<Point>{
    String x;
    String y;
    
    Point(){
        
    }
    Point(String x, String y){
        this.x = x;
        this.y = y;
    }
    @Override
    public int compareTo(Point o){
        return o.y.compareTo(this.y); // 문자열 비교인 경우 compareTo
                                      // 비교대상.compareTo(자기자신) 문자열 내림차순
                                      // 정수 비교인 경우 this.y - o.y 오름차순
                                      // 정수 비교인 경우 o.y - this.y 내림차순
    }
}

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        ArrayList<Point> arr = new ArrayList();
        
        boolean check = true;
        for(int i=0;i<numbers.length;i++){
            if(numbers[i]!=0){
                check = false;
                break;
            }
        }
        if(check){
            return "0";
        }
        
        for(int i=0;i<numbers.length;i++){
            Point pt = new Point();
            pt.x = String.valueOf(numbers[i]);
            String str = "";
            for(int j=0;j<3;j++){
                str += String.valueOf(numbers[i]);
            }
            
            pt.y = str;
            arr.add(pt);
        }
        //Collections.sort(arr);
        Collections.sort(arr, (a,b) -> b.y.compareTo(this.a));
        for(int i=0;i<arr.size();i++){
            answer += arr.get(i).x;
        }
        
        return answer;
    }
}

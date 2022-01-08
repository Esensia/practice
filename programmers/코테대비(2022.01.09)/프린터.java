import java.util.*;
class Point{
    int y;
    int x;
}

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        ArrayList<Point> arr = new ArrayList();
        
        for(int i=0;i<priorities.length;i++){
            Point point = new Point();
            point.y = priorities[i];
            point.x = i;
            arr.add(point);
        }
        int count=0;
        while(arr.size() > 0){
            Point pt = arr.remove(0);
            boolean check = true;
            for(int i=0;i<arr.size();i++){
                if(pt.y<arr.get(i).y){
                    arr.add(pt);
                    check = false;
                    break;
                }
            }
            if(check){

                if(pt.x == location){
                    answer = count+1;
                }
                count+=1;

            }
        }
        return answer;
    }
}

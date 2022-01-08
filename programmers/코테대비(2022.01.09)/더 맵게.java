import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> que = new PriorityQueue();
        
        for(int scov : scoville){
            que.add(scov);
        }
        do{
            if(que.size()>1){
                int a = que.poll();
                int b = que.poll();
                int c = a + b*2;
                que.add(c);
                answer +=1;
            }
            else{
                return -1;
            }
        }while(que.peek()< K);
        return answer;
    }
}

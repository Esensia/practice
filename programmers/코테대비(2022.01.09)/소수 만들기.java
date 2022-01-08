import java.util.*;
class Solution {
    private int answer = 0;
    
    private boolean isPrime(int num){
        
        for(int i=2;i<Math.sqrt(num)+1 ; i++){
            if(num %i==0){
                return false;
            }
        }
        return true;
    }
    
    private void dfs(int sum, int idx, int count, int[] nums, boolean[] visited){
        
        if(count == 3){
            if(isPrime(sum)){
                answer++;
            }
            return;
        }
        
        for(int i=idx;i<nums.length;i++){
            if(!visited[i]){
                visited[i] = true;
                dfs(sum+nums[i],i+1, count+1, nums,visited);
                visited[i] = false;
            }
            
        }
    }
    public int solution(int[] nums) {

        boolean[] visited = new boolean[nums.length];
        ArrayList<Integer> arr = new ArrayList();
        dfs(0,0,0,nums,visited);
        return answer;
    }
}

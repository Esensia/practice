class Solution {
    
    static int[] arr;
    static int ans = 0;
    static int dap = 0;
    
    static void dfs(int ix, int count, int curVal){
        if(count == arr.length){
            if(curVal == dap) {
                ans += 1;
            }
            return;
        }
        for(int i=ix;i<arr.length;i++){
            dfs(i+1,count+1,curVal+arr[i]);
            dfs(i+1,count+1,curVal-arr[i]);
        }
    }
    public int solution(int[] numbers, int target) {
        int answer = 0;
        dap = target;
        arr = new int[numbers.length];
        for(int i=0;i<numbers.length;i++){
            arr[i] = numbers[i];
        }
        
        dfs(0,0,0);
        return ans;
    }
}

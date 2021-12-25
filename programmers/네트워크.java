import java.util.*;
class Solution {
    static boolean[] visited;
    static int[][] map;
    static int count =0;
    
    static int N;
    
    public static void bfs(int vertex) {
    	
    	Queue<Integer> que = new LinkedList();
 
    	if(!visited[vertex]) {
    		que.add(vertex);
    		count++;
    	}
    	
    	while(!que.isEmpty()) {
    		
    		int v = que.poll();
    		for(int i=0;i<N;i++) {
    			if(map[v][i]==1 && v!=i) {
    				if(!visited[i]) {
    					que.add(i);
    					visited[i] = true;
    				}
    			}
    		}
    	}
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        N = n;
        visited = new boolean[n];
        
        map = new int[n][n];
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                map[i][j] = computers[i][j];
            }
        }
        
        for(int i=0;i<n;i++) {
        	bfs(i);
        }
        answer = count;
        return answer;
    }
}

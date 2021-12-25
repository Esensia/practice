import java.util.*;
class Solution {
    static String[][] priority = {	{"+","-","*"},
									{"+","*","-"},
									{"-","*","+"},
									{"-","+","*"},
									{"*","+","-"},
									{"*","-","+"}
	};
    
    public long cal(ArrayList<Long> arr, ArrayList<String> brr, int nidx, int idx) {
		
		ArrayList<Long> list = new ArrayList();
		ArrayList<String> list2 = new ArrayList();
		for(int i=0;i<arr.size();i++) {
			list.add(arr.get(i));
		}
		for(int i=0;i<brr.size();i++) {
			list2.add(brr.get(i));
		}
		
		String prefix = priority[idx][nidx];
		
		int index = 0;
		if(prefix.equals("+")) {
			while(true) {
				boolean flag = false;
				if(list2.get(index).equals("+")) {
					long num1 = list.get(index);
					long num2 = list.get(index+1);
					
					list.set(index, num1+num2);
					list.remove(index+1);
					list2.remove(index);
					flag = true;
				}
				
				if(!flag) {
					index++;
				}
				if(index >= list2.size()) {
					break;
				}
			}
		} else if(prefix.equals("-")) {
			while(true) {
				boolean flag = false;
				if(list2.get(index).equals("-")) {
					long num1 = list.get(index);
					long num2 = list.get(index+1);
					
					list.set(index, num1-num2);
					list.remove(index+1);
					list2.remove(index);
					flag = true;
				}
				
				if(!flag) {
					index++;
				}
				if(index >= list2.size()) {
					break;
				}
			}
			
		} else if(prefix.equals("*")) {
			while(true) {
				boolean flag = false;
				if(list2.get(index).equals("*")) {
					long num1 = list.get(index);
					long num2 = list.get(index+1);
					
					list.set(index, num1*num2);
					list.remove(index+1);
					list2.remove(index);
					flag = true;
				}
				
				if(!flag) {
					index++;
				}
				if(index >= list2.size()) {
					break;
				}
				
			}
		}
		if(list2.size()==0) {
			return list.get(0);
		}
		
		return cal(list, list2, nidx+1, idx);
	}
    
    public long solution(String expression) {
        long answer =0;
        ArrayList<Long> arr = new ArrayList();
        ArrayList<String> brr = new ArrayList();
        
        int idx = 0;
        
        String str = "";
        
        for(int i=0;i<expression.length();i++){
            if(expression.charAt(i)<'0' || expression.charAt(i)>'9'){
                str = "";
                for(int j=idx;j<i;j++){
                    str += expression.charAt(j);
                }
                arr.add(Long.parseLong(str));
                brr.add(String.valueOf(expression.charAt(i)));
                idx = i+1;
            }
        }
        
        str = "";
        
        for(int i=idx;i<expression.length();i++){
            str += expression.charAt(i);
        }
        arr.add(Long.parseLong(str));
        
        for(int i=0;i<6;i++) {
        	answer = Math.max(answer,Math.abs(cal(arr,brr,0,i)));
        }

        return answer;
    }
}

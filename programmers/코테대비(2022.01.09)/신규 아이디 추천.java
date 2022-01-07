class Solution {
    public String solution(String new_id) {
        String answer = "";
        String str1 = new_id.toLowerCase();
        StringBuilder str2 = new StringBuilder();
        
        for(int i=0;i<str1.length();i++){
            if(str1.charAt(i) >=48 && str1.charAt(i) <=57){
                str2.append(str1.charAt(i));
            } else if(str1.charAt(i) >=97 && str1.charAt(i) <=122){
                str2.append(str1.charAt(i));
            } else if(str1.charAt(i) == 45 || str1.charAt(i) == 95 || str1.charAt(i) == 46){
                str2.append(str1.charAt(i));
            }
        }
        
        StringBuilder str3 = new StringBuilder();
        for(int i=0;i<str2.length();i++){
            if(str3.length() == 0){
                str3.append(str2.charAt(i));
                continue;
            }
            
            if(str2.charAt(i)==46 && str3.charAt(str3.length()-1)==46){
                continue;
            }
            str3.append(str2.charAt(i));
        }

        StringBuilder str4 = new StringBuilder();
        for(int i=0;i<str3.length();i++){
            str4.append(str3.charAt(i));
        }
        if(str4.charAt(0) == 46){
            str4.deleteCharAt(0);
        }
        if(str4.length()>0 && str4.charAt(str4.length()-1)==46){
            str4.deleteCharAt(str4.length()-1);
        }
        StringBuilder str5 = new StringBuilder();
        for(int i=0;i<str4.length();i++){
            str5.append(str4.charAt(i));
        }
        
        if(str5.length()==0){
            str5.append("a");
        }
        StringBuilder str6 = new StringBuilder();
        if(str5.length() >=16){
            for(int i=0;i<15;i++){
                str6.append(str5.charAt(i));
            }
        } else {
            for(int i=0;i<str5.length();i++){
                str6.append(str5.charAt(i));
            }
        }

        if(str6.length()> 0 && str6.charAt(str6.length()-1) == 46){
            str6.deleteCharAt(str6.length()-1);
        }
        
        if(str6.length() <=2 && str6.length()>0){
            
            while(str6.length() != 3) {
                str6.append(str6.charAt(str6.length()-1));
            }
        }
        answer += str6.toString();
        
        return answer;
    }
}

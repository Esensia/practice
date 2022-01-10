# Code Review

* 1번 문제
<br>유사 문제 : 프로그래머스 단속카메라
```java
import java.util.*;
class Solution {
    public int solution(int[][] customer) {
        int answer = 0;

        Arrays.sort(customer, (a,b) -> a[0]-b[0]); // return > 0 이면 자리를 바꾼다.
        int start = customer[0][0];
        int end = customer[0][1];
        for(int i=1;i<customer.length;i++){

            if(end >= customer[i][0]){
                end = Math.max(end,customer[i][1]);
            }
            else {
                answer += (end - start);
                end = customer[i][1];
                start = customer[i][0];
            }
        }
        answer += (end-start);
        return answer;
    }
}
```
  * 접근 방법
    * 시작시간이 빠른 순으로 정렬을 하고 끝나는 시간을 다음 상담자의 시작시간과 비교하며 끝나는 시간을 더 늦은 값으로 변경시킨다.
    * 다음 상담자의 시작시간이 끝나는 시간보다 크다면 상담시간의 공백이 생겼다는 것이므로 처음 시작시간과 현재 끝나는 시간의 차이를 답에 더해준다.
    * 시작시간과 끝나는 시간을 공백이 생긴 상담자의 시간으로 맞춘다.
    * 루프를 다 돌면 마지막 상담을 시작시간부터 끝까지 했으므로 시작시간과 끝나는 시간의 차이를 답에 더해준다.
  * 풀이의 오류?
    * 시작시간을 기준으로 정렬을 했기 때문에 끝나는 시간과 시작시간의 대소관계를 통해 상담시간의 공백을 알아낼 수 있다.
    * 즉, 이 문제는 시작시간을 기준으로 정렬을 하면 그리디하게 풀 수 있다.
  * 기타질문예상
    * Q. java.util 패키지란?
      * 프로그램을 개발하는 데 사용할 수 있는 유틸리티 클래스가 다수 포함, java.lang의 경우 자동 import가 되지만 util 패키지의 경우 import해줘야함
    * Q. 패키지란?
      * 클래스들의 모임으로 클래스들의 고유성을 보장할 수 있다.
    * Q. Arrays클래스와 sort() 메소드의 동작 원리는?
      * 배열을 다루기 위한 다양한 메소드가 포함 돼 있는 클래스로 모든 메소드는 정적 메소드(클래스 메서드/static method)이므로 객체를 생성하지 않고도 사용할 수 있다.
      * sort() 함수는 내부적으로 배열의 크기에 따라 QuickSort, MergeSort, InsertionSort, CountingSort를 수행한다. 여기선 배열의 크기가 47보다 작으므로 InsertionSort를 QuickSort보다 먼저 수행한다.
    * Q. 람다식이 무엇이며 람다식을 사용한 이유?
      * JAVA8에서 추가된 문법
      * sort()의 기본 정렬 방식을 사용하지 않으려면 새로운 정렬 방식을 적용해 주어야한다. 그 기능을 가지는 익명의 내부 클래스를 만들고 객체화해서 전달하면 된다.
      ```java
      Arrays.sort(customer, new Comparator<int[]> {
          @Override
          public int compare(int[] a, int[] b) {
              return a[0] - b[0];
          }
      });
      ```
      * 람다식은 런타임 때 익명의 내부 클래스로 변경돼서 처리되므로 동작은 동일하며 코드의 가독성이 높아진다.

* 2번 문제
```java
class Solution {
    // 다른걸 낸 한명의 인덱스를 찾기위한 함수
    private int findPerson(String[] person, String target){
        for(int i=0;i<person.length;i++){
            if(target.equals(person[i])){
                return i;
            }
        }
        return 0;
    }
    // 승자가 두명인 경우 패자의 인덱스를 제외한 나머지 승자들의 점수를 계산
    private int[] calculate(int idx, int[] result){
        int first = -1;
        int x = 0;
        for(int i=0;i<3;i++){
            if(i!=idx && first == -1){
                first = result[i];
                x = i;
            }
            else if(i!=idx && first!=-1){
                if(first == result[i]){
                    result[x]+=1;
                    result[i]+=1;
                } else if(first > result[i]){
                    result[i]+=2;
                } else {
                    result[x]+=2;
                }
            }
        }
        return result;
    } 

    private int[] rockPaperSisor(String[] person, int[] result){

        int rCount = 0;
        int pCount = 0;
        int sCount = 0;
        for(int i=0;i<person.length;i++){
            if(person[i].equals("R")){
                rCount++;
            } else if(person[i].equals("P")){
                pCount++;
            } else{
                sCount++;
            }
        }

        // 승자가 1명인 경우
        if(rCount == 2 && pCount == 1){
            result[findPerson(person,"P")]+=2;
        } else if(sCount == 2 && rCount == 1){
            result[findPerson(person,"R")]+=2;
        } else if(pCount ==2 && sCount == 1){
            result[findPerson(person,"S")]+=2;
        }
        // 승자가 2명인 경우
        int idx = 0;
        if(rCount == 2 && sCount == 1){
            idx = findPerson(person,"S");
            result = calculate(idx,result);
        } else if(sCount == 2 && pCount == 1){
            idx = findPerson(person,"P");
            result = calculate(idx,result);
        } else if(pCount ==2 && rCount == 1){
            idx = findPerson(person,"R");
            result = calculate(idx,result);
        }
        return result;
    }

    public int[] solution(String[] rsp3) {
        int[] answer = {0,0,0};

        for(String rsp : rsp3){
            String[] person = rsp.split("");
            answer = rockPaperSisor(person,answer);

        }

        return answer;
    }
}
```
  * 접근 방법
    * 문제에서 점수를 계산하는 방법은 한명이 이겼을 때와 두명이 이겼을 때 이므로 비기는 경우는 제외한다.
    




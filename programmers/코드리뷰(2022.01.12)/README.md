# Code Review
---
### 1번 문제
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
    * 즉, 이 문제는 시작시간을 기준으로 정렬을 하면 그리디하게 풀 수 있다.<br>
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
---
### 2번 문제
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
    * 승자가 한명인 경우 다른걸 낸 한명의 인덱스를 찾고 그 해당하는 배열에 +2를 해준다.
    * 승자가 두명인 경우 다른걸 낸 한명의 인덱스를 찾고 그 인덱스를 제외한 다른 인덱스들의 값을 비교하며 문제에서 주어진 점수처리 방식을 적용한다.
  * 기타질문예상
    * Q. private를 사용한 이유? (public과 private의 차이)
      * private의 경우 같은 클래스 내에서만 접근이 가능하다. solution함수에서 호출만 하기 때문에 private로 접근제한을 뒀다. (사실 아무거나 해도 상관없다)
      * public의 경우 외부 클래스에서도 접근이 가능하고 protected의 경우 같은 패키지에 있는 메서드에 접근이 가능하다.
      * 다만 protected로 선언된 메서드의 클래스를 다른 패키지의 클래스가 상속을 받으면 접근이 가능하다.
      * 접근제한자 선언을 하지 않으면 기본적으로 default로 선언되며 이는 같은 패키지 내에서만 접근이 가능하다.
    * Q. 왜 이런구조를 취하게 되었는지?
      * 게임이 여러번 진행되며 다른걸 낸 한사람만 찾아내면 승자가 한명일 경우와 승자가 두명일 경우(다른걸 낸 패자가 한명)을 알 수 있기 때문에 findPerson 함수를 작성하였다.
      * answer를 인자로 계속해서 함수를 호출하며 answer안에 있는 값들을 변경시켜 주고 최종적으로 return하면 원하는 답을 얻을 수 있다.
    * Q. 배열 객체 answer와 매개변수 result의 메모리 구조
      * answer라는 이름이 스택메모리에 올라가고 객체이므로 해당하는 주소값을 갖고 있다.
      * 해당하는 주소로 힙 영역에 배열객체가 만들어지고 각각의 값들이 저장된다.
      * 매개변수로 보내고 이를 result가 받을 시, result변수가 스택메모리에 올라가고 answer와 같은 주소를 참조하게된다.
      * result이름으로 배열의 값을 바꾸면 result가 바라보는 배열의 값 즉, answer가 바라보는 배열의 값이 바뀐다.
      * 최종적으로 answer를 return하게 되면 힙 영역에 있는 answer의 객체가 return된다. (이 때, result는 GC에 의해 가비지 컬렉션 된다.)
    * Q. 더 간단하게 하거나 고칠 곳은 없는지?
      * 가위바위보를 하는 사람이 3명으로 고정 돼 있어 배열의 길이가 아닌 상수값을 사용한곳도 있지만 문제에서 사람의 수를 변동한다면 그에 맞게 배열의 크기로 써줘야한다.
      * 81-89라인에서 result를 계산하고 바로 return을 해도 무방하다.
      * findPerson 함수를 쓰지않고 rsp를 그대로 보냈다면 indexOf를 써도 된다.
    * Q. for문이 기존과 다른 이유는?
      * 향상된 for문이라 부르며 jdk1.5이상부터 쓸 수 있는 문법이다.
      * 다만 콜론 뒤에 나오는 객체의 타입과 왼쪽 타입이 일치해야 쓸 수 있다.
      * ArrayList, LinkedList도 사용할 수 있다.
    * Q. split을 사용한 이유
      * 문자열로 된 rsp의 값을 쉽게 접근하기 위해 split을 하였다. charAt()으로 접근해도되긴된다..
---
### 3번 문제
```java
import java.util.*;
class Solution {
    long answer = 0;

    private void dfs(int idx, int k,long sum, long[]numbers, boolean[] visited,int q, int r){

        if(sum != 0){
            answer += Math.pow(sum,q);
            answer %= 1000000007;
        }
        for(int i=idx;i<numbers.length;i++){
            if(!visited[i]){
                visited[i] = true;
                dfs(i+1,k+1,(sum + (long)Math.pow(r,k) * numbers[i])%1000000007,numbers,visited, q, r);
                visited[i] = false;
            }
        }
    }

    public long solution(long[] numbers, int q, int r) {

        Arrays.sort(numbers);
        boolean[] visited = new boolean[numbers.length];
        dfs(0,0,0,numbers,visited,q,r);
        return answer;
    }
}
```
  * 접근 방법
    * 처음엔 모든 부분집합의 경우를 구해야 하므로 dfs를 돌면서 조합을 만들었다.
    * 모든 조합을 만들어 가며 주어진 멱급수 식을 적용한다.
    * 하지만 이 경우 n의 범위는 5000개 까지므로 2^5000 -1 가지의 경우가 나와서 시간초과가난다. (완전탐색 불가능)
    * 수학식을 적용해서 풀어야하는것 같지만 못풀고 제출
  * 기타질문예상
    * Q. 시간초과의 기준은?
      * 시간제한이 1초인 프로그램의 경우, CPU가 1초에 10억번의 연산을 할 수 있다고 한다면 Big-O 표기법으로 O(2^n)이기 때문에 30개가 넘어가도 시간초과가 난다.
---
### 4번 문제
```sql
SELECT B.NAME, COUNT(B.NAME) AS COUNT
FROM CARTS A,
CART_PRODUCTS B
WHERE A.USER_ID = 4
AND A.ID = B.CART_ID
GROUP BY B.NAME
ORDER BY COUNT DESC, B.NAME
```
  * 접근 방법
    * 문제에서 주어진 조건대로 조건절을 작성하고 조인을 한다.
    * GROUP BY를 이용해 CART_PRODUCTS의 이름으로 그룹을 맺고 각 해당하는 그룹의 개수를 같이 출력해준다.
---

### 5번 문제
```sql
SELECT SALE_YM "판매년월",
SUM(DECODE(GOODS_CD,'0001',SALE_CNT)) "상품0001판매개수",
SUM(DECODE(GOODS_CD,'0002',SALE_CNT)) "상품0002판매개수",
SUM(DECODE(GOODS_CD,'0003',SALE_CNT)) "상품0003판매개수",
SUM(DECODE(GOODS_CD,'0004',SALE_CNT)) "상품0004판매개수",
SUM(DECODE(GOODS_CD,'0005',SALE_CNT)) "상품0005판매개수",
SUM(SALE_CNT) "전체판매개수"
FROM KKB_GOODS_S
GROUP BY SALE_YM
ORDER BY SALE_YM
```
  * 접근 방법
    * 판매년월대로 그룹을 짓고 그 그룹의 GOODS_CD에 해당하는 값만 카운트를 해주기 위해 DECODE를 이용
    * 0001인 경우 0001에 해당하는 CNT만 SUM하고 다른것도 마찬가지로..
    * 출력에 전체판매개수가 있는지 몰라서 해맸었음
  * 기타질문예상
    * Q. 쿼리 동작 순서
      * FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY

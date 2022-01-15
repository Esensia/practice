# 10. ETC
**:book: Contents**
* [웹 브라우저에서 서버로 어떤 페이지를 요청하면 일어나는 일련의 과정을 설명](#웹-브라우저에서-서버로-어떤-페이지를-요청하면-일어나는-일련의-과정을-설명)
* [64bit CPU와 32bit CPU 차이](#64bit-cpu와-32bit-cpu-차이)
* [CVS, SVN, Git](#cvs-svn-git)
* [웹 서버(Web Server)와 웹 어플리케이션 서버(WAS)의 차이](#web-server와-was의-차이)
* [Servlet과 JSP](#servlet과-jsp)
* [함수형 프로그래밍이란](#함수형-프로그래밍이란)

---

### 웹 브라우저에서 서버로 어떤 페이지를 요청하면 일어나는 일련의 과정을 설명
> :arrow_double_up:[Top](#11-etc)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#11-etc)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
* Ex. url에 'www.naver.com' 을 입력했다. 일어나는 현상에 대해 아는대로 설명하라.
  * 사용자가 브라우저에 도메인 네임을 입력한다. 'www.naver.com'
  * 사용자가 입력한 URL 주소 중 도메인 네임 부분을 DNS 서버에 검색하고, DNS서버에서 해당 도메인 네임에 해당하는 IP주소를 찾아 사용자가 입력한 URL 정보와 함께 전달한다.
  * 페이지 URL정보와 전달받은 IP주소는 HTTP 프로토콜을 사용하여 HTTP 요청 메세지를 생성하고, 이렇게 생성된 HTTP 요청 메세지는 TCP 프로토콜을 사용하여 인터넷을 거쳐 해당 IP주소의 컴퓨터로 전송된다.
  * 이렇게 도착한 HTTP 요청 메세지는 HTTP 프로토콜을 사용하여 웹 페이지 URL 정보로 변환되어 웹 페이지 URL 정보에 해당하는 데이터를 검색한다.
  * 검색된 웹 페이지 데이터는 또 다시 HTTP 프로토콜을 사용하여 HTTP 응답 메세지를 생성하고 TCP 프로토콜을 사용하여 인터넷을 거쳐 원래 컴퓨터로 전송된다.
  * 도착한 HTTP 응답 메세지는 HTTP 프로토콜을 사용하여 웹 페이지 데이터로 변환되어 웹 브라우저에 의해 출력되어 사용자가 볼 수 있게 된다.

### 64bit CPU와 32bit CPU 차이
> :arrow_double_up:[Top](#11-etc)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#11-etc)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
* 레지스터 저장장치의 비트폭의 차이
* 64비트 cpu는 32비트 cpu보다 많은량의 데이터 처리가 가능하다.
* 32비트 cpu에서는 메모리가 4GB를 넘지못한다.

### CVS, SVN, Git
* 형상관리 툴
* 소스의 변화를 끊임없이 관리하는 툴
* 소스를 버전별로 관리할 수 있고, 실수할 경우 원복 가능하게 하는 툴

#### CVS
* 개념
  * Concurrent Versions System
  * GNU 라이센스
  * 중앙에 위치한 Repository에 파일을 저장하고, 모든 사용자가 접근 가능하도록 설계
  * checkout으로 파일 복사, commit으로 변경사항 저장
  * 최종 버전의 소스만 관리
  * 먼저 반영한 소스가 먼저 처리되는 시스템
* 장점
  * 오랫동안 사용이 되었으며 안정적
  * 파일 전체를 저장하지 않고 변경사항만 저장하여 적은 용량 사용
* 단점
  * 파일 이동이나 이름 변경은 버전 변경 미발생(파일 지우고 다시 추가)
  * 버전 분기가 힘들고, 장기간 분기된 버전 운영에 대해 미설계
  * commit 실패 시 롤백 불가능
  * 상대적으로 느린 속도
* 혼자 개발할 경우 최종버전만 관리하는 CVS 툴 사용이 편리

#### SVN
* 개념
  * Apache Subversion
  * CVS와 높은 호환성을 유지하며 약간의 버그를 수정한 대체 시스템으로 개발
  * 중앙 관리
  * 최초 1회에 한해 파일 원본 저장, 이후에는 원본과 차이점을 저장
  * 버전 분기가 쉽고, 대규모의 분기된 프로젝트에 도움
* 장점
  * 원자적 commit으로 다른 사용자의 commit과 엉키지 않으며 commit 실패 시 롤백 지원
    * 원자적 commit : 파일 단위가 아닌 change set이 commit 단위
  * 효율적인 버전 분기, 언제든지 원하는 버전으로 복구 가능
  * 이진파일도 효율적으로 저장 가능
* 단점
  * 파일과 디렉토리 변경 관련 버그
  * 불충분한 저장소 관리 명령어
  * CVS에 비해 상대적으로 불안정
  * **Local Repository가 없기** 때문에 자신만의 version history 관리 불가능
  * commit에 실수가 있을 시 다른 개발자에게 바로 영향 가능성

#### Git
* 개념
  * CVS를 개선하고, 보다 빠른 분산 버전 제어 시스템
  * **서버 저장소와 개발자 저장소가 독립적**
  * 사용자 기록 탐색 가능
* 장점
  * 빠른 속도
  * 분기 버전의 효율적인 운영
  * 오프라인에서도 전체 이력 이용 가능
  * 분산된 P2P 모델
  * commit에 실수가 있어도 서버에 바로 영향 없음
* 단점
  * SVN보다 많은 기능을 지원하는 만큼 높은 진입장벽
  * 개인 개발자에게 부적절
* 팀 개발을 위한 분산 환경 코딩에 최적화

> :arrow_double_up:[Top](#11-etc)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#11-etc)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [[IT/트랜드] [금융IT]형상관리 툴 CVS, SVN, 그리고 Git비교](https://daitso.kbhub.co.kr/50240/)
> - [[웹개발 기초] 형상관리툴이란? (SVN GIT 간단비교)](https://goddaehee.tistory.com/158)
> - [형상관리툴 특징 (Perforce, Git, SVN, CVS)](https://haayany.tistory.com/entry/%ED%98%95%EC%83%81%EA%B4%80%EB%A6%AC%ED%88%B4-%ED%8A%B9%EC%A7%95-Perforce-Git-SVN-CVS)
> - [형상 관리 툴 비교 Git, SVN, CVS](https://digital-play.tistory.com/60)

### Web Server와 WAS의 차이
* Web Server
    * Web Server의 개념
        * 소프트웨어와 하드웨어로 구분된다.
        * 1) 하드웨어
            * Web 서버가 설치되어 있는 컴퓨터
        * 2) 소프트웨어
            * 웹 브라우저 클라이언트로부터 HTTP 요청을 받아 **정적인 컨텐츠(.html .jpeg .css 등)**를 제공하는 컴퓨터 프로그램
    * Web Server의 기능
        * **HTTP 프로토콜을 기반으로 하여 웹 브라우저의 요청을 서비스 하는 기능**을 담당한다.
        * 요청에 따라 아래의 두 가지 기능 중 적절하게 선택하여 수행한다.
        * 기능 1)
            * 정적인 컨텐츠 제공
            * WAS를 거치지 않고 바로 자원을 제공한다.
        * 기능 2)
            * 동적인 컨텐츠 제공을 위한 요청 전달
            * 클라이언트의 요청(Request)을 WAS에 보내고, WAS가 처리한 결과를 클라이언트에게 전달(응답, Response)한다.
    * Web Server의 예
        * Ex) Apache Server, Nginx, IIS(Windows 전용 Web 서버) 등
* WAS(Web Application Server)
    * WAS의 개념
        * DB 조회나 다양한 로직 처리를 요구하는 **동적인 컨텐츠**를 제공하기 위해 만들어진 Application Server
        * HTTP를 통해 컴퓨터나 장치에 애플리케이션을 수행해주는 미들웨어(소프트웨어 엔진)이다.
        * **"웹 컨테이너(Web Container)" 혹은 "서블릿 컨테이너(Servlet Container)"**라고도 불린다.
            * Container란 JSP, Servlet을 실행시킬 수 있는 소프트웨어를 말한다.
            * 즉, WAS는 JSP, Servlet 구동 환경을 제공한다.
    * WAS의 기능
        * **WAS = Web Server + Web Container**
        * Web Server 기능들을 구조적으로 분리하여 처리하고자하는 목적으로 제시되었다.
            * 분산 트랜잭션, 보안, 메시징, 쓰레드 처리 등의 기능을 처리하는 분산 환경에서 사용된다.
            * 주로 DB 서버와 같이 수행된다. 
    * WAS의 예
        * Ex) Tomcat, JBoss, Jeus, Web Sphere 등

> :arrow_double_up:[Top](#11-etc)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#11-etc)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html](https://gmlwjd9405.github.io/2018/10/27/webserver-vs-was.html)

### Servlet과 JSP
* 기능의 차이는 없고 역할의 차이만 있다. (하는 일은 동일)
* Servlet이란
    * 웹 기반의 요청에 대한 동적인 처리가 가능한 Server Side에서 돌아가는 Java Program 
    * ***Java 코드*** 안에 HTML 코드 (하나의 클래스)
    * 웹 개발을 위해 만든 표준
    * **data processing(Controller)** 에 좋다.
    * 즉 DB와의 통신, Business Logic 호출, 데이터를 읽고 확인하는 작업 등에 유용하다.
    * Servlet이 수정된 경우 Java 코드를 컴파일(.class 파일 생성)한 후 동적인 페이지를 처리하기 때문에 전체 코드를 업데이트하고 다시 컴파일한 후 재배포하는 작업이 필요하다. **(개발 생산성 저하)**
    * 구체적인 내용은 [https://gmlwjd9405.github.io/2018/10/28/servlet.html](https://gmlwjd9405.github.io/2018/10/28/servlet.html) 참고
* JSP란
    * Java 언어를 기반으로 하는 Server Side 스크립트 언어
    * ***HTML 코드*** 안에 Java 코드 
    * Servlet를 보완하고 기술을 확장한 스크립트 방식 표준
        * Servlet의 모든 기능 + 추가적인 기능
        * ![](/images/web/jsp-definition.png)
    * **presentation(View)** 에 좋다. 
    * 즉 요청 결과를 나타내는 HTML 작성하는데 유용하다.
    * JSP가 수정된 경우 재배포할 필요가 없이 WAS가 알아서 처리한다. **(쉬운 배포)**
    * 구체적인 내용은 [https://gmlwjd9405.github.io/2018/11/03/jsp.html](https://gmlwjd9405.github.io/2018/11/03/jsp.html) 참고

> :arrow_double_up:[Top](#11-etc)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#11-etc)     :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [https://gmlwjd9405.github.io/2018/11/04/servlet-vs-jsp.html](https://gmlwjd9405.github.io/2018/11/04/servlet-vs-jsp.html)

### 함수형 프로그래밍이란

#### 프로그래밍 패러다임
* 명령형 프로그래밍
  * 애플리케이션의 상태와 상태를 변경시키는 구문의 관점에서 연산을 설명하는 방식
  * 어떻게 할 것인지 표현
    * 절차지향 프로그래밍
    * 객체지향 프로그래밍
* 선언형 프로그래밍
  * 무엇을 할 것인지 표현
    * **함수형 프로그래밍**

#### 함수형 패러다임의 등장 계기
* 하드웨어의 발전과 함께 소프트웨어 패러다임은 TEXT기반의 절차적 프로그래밍에서 GUI기반의 객체지향 프로그래밍으로 변화하였고, 이제 멀티코어를 배경으로 하는 함수형 프로그래밍으로 변화
* **대용량의 데이터를 빠르고 효율적으로 처리하기 위해서 멀티코어를 활용하는 병렬처리 프로그래밍 도입이 필요**
* 안정적으로 다루기 위해서는 함수형 프로그램이 필연적인 선택
* 또한, **프로그램을 보다 단순하게 하려는 요구사항**에 의해 등장

#### 함수형 프로그래밍 개념
* 선언형 프로그래밍
* 함수형 프로그래밍은 계산을 수학적 함수의 조합으로 생각하는 방식
* 함수를 1급 객체로 사용(고차 함수)
  * 1급 객체가 될 수 있는 조건
    * 변수나 데이터 구조 안에 담을 수 있는 객체
    * 함수의 파라미터로 전달 가능
    * 반환값으로 사용 가능
    * 할당에 사용된 이름과 관계없이 고유한 구별 가능
    * 동적으로 프로퍼티 할당 가능
* 애플리케이션의 상태는 순수 함수를 통해 전달
  * 공유 상태와 side effect 대신 순수 함수를 사용
  * 순수 함수 : 같은 입력이 주어지면 항상 같은 출력을 반환하는 함수
* 명령형 흐름 제어보다 합성 함수를 사용
  * 합성 함수 : 새로운 함수를 만들거나 계산하기 위해 둘 이상의 함수를 조합
  * ex. 메소드 체이닝
* 불변성
  * 함수형 프로그래밍의 핵심 개념
* 함수를 1급 객체로 사용하며 함수를 조합하고, 공유 상태와 변경 가능한 데이터 및 사이드 이펙트를 피해 소프트웨어를 만드는 프로세스

#### 함수형 프로그래밍 특징
* 변경 가능한 상태를 불변 상태로 만들어 side effect 방지 가능
* 고차함수를 통한 재사용성 증가
* 코드를 간결하게 하고 가독성을 높여 구현할 로직에 집중
* 동시성 작업을 보다 쉽고 안전하게 구현 가능

> :arrow_double_up:[Top](#7-java)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#7-java)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [함수형 프로그래밍 요약](https://velog.io/@kyusung/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%9A%94%EC%95%BD)
> - [번역 - 함수형 프로그래밍이란 무엇인가?](https://sungjk.github.io/2017/07/17/fp.html)
> - [람다, 람다, 람다(Lambda, Lambda, Lambda) - 1](http://blog.naver.com/tmondev/220412722908)
---

## Reference
> -[]()

## :house: [Home](https://github.com/WeareSoft/tech-interview)

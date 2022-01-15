# Tech Interview

**:book: Contents**
1. [Project](#1-project)
2. [Data Structure](#2-data-structure)
3. [Network](#3-network)
4. [Operating System](#4-operating-system)
5. [Database](#5-database)
6. [Design Pattern](#6-design-pattern)
7. [Algorithm](#7-algorithm)
8. [Java](#8-java)
9. [Spring](#9-spring)
10. [ETC](#10-etc)

---
## 1. Project
:arrow_forward: [답변 내용](/tech-interview/contents/project.md)
* NH은행/상호 PPR 전자창구 구축 프로젝트
* NH선물 차세대 프로젝트

## 2. Data Structure
:arrow_forward: [답변 내용](/tech-interview/contents/datastructure.md)
* Array
* LinkedList
* HashTable
* Stack
* Queue
* Graph
* Tree
* 그래프(Graph)와 트리(Tree)의 차이점
* Binary Heap

## 3. Network
:arrow_forward: [답변 내용](/tech-interview/contents/network.md)
* OSI 7계층
* TCP/IP의 개념
* TCP와 UDP
* TCP와 UDP의 헤더 분석
* TCP의 3-way-handshake와 4-way-handshake
  * Q. TCP의 연결 설정 과정(3단계)과 연결 종료 과정(4단계)이 단계가 차이나는 이유?
  * Q. 만약 Server에서 FIN 플래그를 전송하기 전에 전송한 패킷이 Routing 지연이나 패킷 유실로 인한 재전송 등으로 인해 FIN 패킷보다 늦게 도착하는 상황이 발생하면 어떻게 될까?
  * Q. 초기 Sequence Number인 ISN을 0부터 시작하지 않고 난수를 생성해서 설정하는 이유?
* HTTP와 HTTPS
* HTTP 요청/응답 헤더
* HTTP와 HTTPS 동작 과정
* CORS란
* GET 메서드와 POST 메서드
* 쿠키(Cookie)와 세션(Session)
* REST와 RESTful의 개념
* 소켓(Socket)이란
* Socket.io와 WebSocket의 차이

## 4. Operating System
:arrow_forward: [답변 내용](/tech-interview/contents/os.md)
* 프로세스와 스레드의 차이(Process vs Thread)
* 멀티 프로세스 대신 멀티 스레드를 사용하는 이유
* 뮤텍스와 세마포어의 차이
* 스케줄러
* 동기와 비동기
* 교착상태(데드락, Deadlock)의 개념과 조건
* Context Switching

## 5. Database
:arrow_forward: [답변 내용](/tech-interview/contents/database.md)
* 데이터베이스 풀
* 트랜잭션(Transaction) 이란
* Join
* SQL injection
* Index란
* RDBMS와 NoSQL
* 옵티마이저(Optimizer)란
* 파티셔닝(Partitioning)
* 샤딩(Sharding)
* 객체 관계 매핑(Object-relational mapping, ORM)이란
* java JDBC

## 6. Design Pattern
:arrow_forward: [답변 내용](/tech-interview/contents/designpattern.md)
* Singleton 패턴
* Strategy 패턴
* Template Method 패턴
* Factory Method 패턴
* MVC1 패턴과 MVC2 패턴

## 7. Algorithm 
### :pushpin: [관련 링크](https://github.com/WeareSoft/algorithm-study)
:arrow_forward: [답변 내용](/tech-interview/contents/algorithm.md)
* BigO
* DFS와 BFS의 차이
* 정렬 알고리즘의 종류와 개념
* Greedy 알고리즘
* 최소 신장 트리(MST, Minimum Spanning Tree)란

## 8. Java
:arrow_forward: [답변 내용](/tech-interview/contents/java.md)
* java와 c/c++의 차이점
* java와 python의 차이점
* java코드 실행과정
* java 언어의 장단점
* java의 데이터 타입
* Wrapper class
* 객체지향 프로그래밍과 절차지향 프로그래밍의 차이
* 객체지향(Object-Oriented)이란
* java의 non-static 멤버와 static 멤버의 차이
  * Q. java의 main 메서드가 static인 이유
* java의 가비지 컬렉션(Garbage Collection) 처리 방법
* java 직렬화(Serialization)와 역직렬화(Deserialization)란 무엇인가
* 클래스, 객체, 인스턴스의 차이
* 객체(Object)란 무엇인가
* 오버로딩과 오버라이딩의 차이(Overloading vs Overriding)
* Call by Reference와 Call by Value의 차이
* 인터페이스와 추상 클래스의 차이(Interface vs Abstract Class)
* Java Collections Framework
  * java Map 인터페이스 구현체의 종류
  * java Set 인터페이스 구현체의 종류
  * java List 인터페이스 구현체의 종류
* String, StringBuilder, StringBuffer
* 동기화와 비동기화의 차이(Syncronous vs Asyncronous)
* java에서 '=='와 'equals()'의 차이
* java의 리플렉션(Reflection) 이란
* Stream이란?
* Lambda란?

## 9. Spring
:arrow_forward: [답변 내용](/tech-interview/contents/spring.md)
* 스프링 프레임워크란
* Bean이란
* Container란
* MVC 패턴이란
* IOC(Inversion of Control, 제어의 역전)란
* DI(Dependency Injection, 의존성 주입)란
* AOP(Aspect Oriented Programming)란
* DAO와 DTO의 차이

## 10. ETC
:arrow_forward: [답변 내용](/tech-interview/contents/etc.md)
* 웹 브라우저에서 서버로 어떤 페이지를 요청하면 일어나는 일련의 과정을 설명
  * Ex. url에 'www.naver.com' 을 입력했다. 일어나는 현상에 대해 아는대로 설명하라.
* 64bit CPU와 32bit CPU 차이
* CVS, SVN, Git
* 웹 서버(Web Server)와 웹 어플리케이션 서버(WAS)의 차이
* Servlet과 JSP
* 함수형 프로그래밍이란

---

# Reference
* [jojoldu님의 junior-recruit-scheduler](https://github.com/jojoldu/junior-recruit-scheduler/blob/master/README.md)
* [JaeYeopHan 님의 Interview_Question_for_Beginner](https://github.com/JaeYeopHan/Interview_Question_for_Beginner)
* [KimHunJin님의 Study-Book/interview](https://github.com/KimHunJin/Study-Book/tree/master/interview)
* [TaeMInMoon님의 신입 개발자 기술면접](https://trello.com/b/BWtpfywH/%EC%8B%A0%EC%9E%85-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EA%B8%B0%EC%88%A0%EB%A9%B4%EC%A0%91)
* [NESOY님의 Back-end-Developer-Interview-Questions](https://github.com/NESOY/Back-end-Developer-Interview-Questions)
* [hanee24님의 신입 개발자 면접 질문](https://hanee24.github.io/2018/05/13/interview-questions/)
* [“개발자 면접 예상 질문, 오픈소스로 공유해요”](http://www.bloter.net/archives/246472)
* [150 Java Interview Questions and Answers](https://www.javacodegeeks.com/2014/04/java-interview-questions-and-answers.html#2)
* [yangshun님의 front-end-interview-handbook](https://github.com/yangshun/front-end-interview-handbook/blob/master/Translations/Korean/questions/javascript-questions.md)
* [ganqqwerty님의 123-Essential-JavaScript-Interview-Questions](https://github.com/ganqqwerty/123-Essential-JavaScript-Interview-Questions)

# 8. Spring
**:book: Contents**
* [스프링 프레임워크란](#스프링-프레임워크란)
* [Bean이란](#bean이란)
* [Container란](#container란)
* [MVC 패턴이란](#mvc-패턴이란)
* [IOC(Inversion of Control, 제어의 역전)란](#ioc란)
* [DI(Dependency Injection, 의존성 주입)란](#di란)
* [AOP(Aspect Oriented Programming)란](#aop란)
* [DAO와 DTO의 차이](#dao와-dto의-차이)
---

### 스프링 프레임워크란
* 자바 엔터프라이즈 개발을 편하게 해주는 경량급 오픈소스 애플리케이션 프레임워크
* **Lightweight Java Applicaion Framework**
    * 목표: **POJO 기반의** Enterprise Application 개발을 쉽고 편하게 할 수 있도록 한다.
    * Java Application을 개발하는데 필요한 하부구조(Infrastructure)를 포괄적으로 제공한다.
    * Spring이 하부구조를 처리하기 때문에 개발자는 Application 개발에 집중할 수 있다.
* 간단히 스프링(Spring)이라고도 불린다. 
* 동적인 웹 사이트를 개발하기 위한 여러 가지 서비스를 제공한다.
* 대한민국 공공기관의 웹 서비스 개발 시 사용을 권장하고 있는 전자 정부 표준 프레임워크의 기반 기술

> :arrow_double_up:[Top](#8-spring)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#9-spring)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

### Bean이란
* 컨테이너 안에 들어있는 객체
* 컨테이너에 담겨있으며, 필요할 때 컨테이너에서 가져와서 사용
* @Bean 을 사용하거나 xml 설정을 통해 일반 객체를 Bean으로 등록할 수 있고, Bean으로 등록된 객체는 쉽게 주입하여 사용 가능

#### Bean 생명주기
- 객체 생성 -> 의존 설정 -> 초기화 -> 사용 -> 소멸
- 스프링 컨테이너에 의해 생명주기 관리
- 스프링 컨테이너 초기화 시 빈 객체 생성, 의존 객체 주입 및 초기화
- 스프링 컨테이너 종료 시 빈 객체 소멸

### Container란
- 컨테이너(Container)는 보통 인스턴스의 생명주기를 관리하며, 생성된 인스턴스들에게 추가적인 기능을 제공하도록하는 것이라 할 수 있다. 다시말해, 컨테이너란 당신이 작성한 코드의 처리과정을 위임받은 독립적인 존재라고 생각하면 된다. 컨테이너는 적절한 설정만 되어있다면 누구의 도움없이도 프로그래머가 작성한 코드를 스스로 참조한 뒤 알아서 객체의 생성과 소멸을 컨트롤해준다.

- Spring 프레임워크는 다른 프레임워크들과 달리 컨테이너 기능을 제공하고 있다. 이와 같은 컨테이너 기능을 제공하는 것이 가능하도록 하는 것이 IoC 패턴이다.

> :arrow_double_up:[Top](#8-spring)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#9-spring)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

### MVC 패턴이란
- Model, View, Controller로 이루어진 패턴
- Model은 무엇을 할지, 비즈니스 로직에서 알고리즘, 데이터 등의 기능을 처리
- Controller은 어떻게 할지, 요청을 받아서 Model과 View를 연결시켜주는 역할
- View는 무엇을 화면으로 보여줄지, 웹페이지나 모바일 화면
- MVC의 장점과 단점
  - 장점
    - 유연하고 확장이 쉽다.
    - 유지보수가 쉽다.
  - 단점
    - View와 Model이 의존성을 띄게 되어 완벽히 분리가 어렵다.
> :arrow_double_up:[Top](#8-spring)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#9-spring)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

### IoC란
- IoC(Inversion of Control, 제어의 역전)란
    - **객체의 생성에서부터 생명주기의 관리까지 모든 객체에 대한 제어권이 바뀐 것을 의미**, 또는 제어 권한을 자신이 아닌 다른 대상에게 위임하는 것이다.
    - 이 방식은 대부분의 프레임워크에서 사용하는 방법으로, 개발자는 필요한 부분을 개발해서 끼워 넣기의 형태로 개발하고 실행하게 된다. 프레임워크가 이러한 구조를 가지기 때문에 개발자는 프레임워크에 필요한 부품을 개발하고 조립하는 방식의 개발을 하게 된다.
    - 이렇게 조립된 코드의 최종 호출은 개발자에 의해서 제어되는 것이 아니라 프레임워크의 내부에서 결정된 대로 이뤄지게 되는데, 이러한 현상을 "제어의 역전"이라고 표현한다.
- Spring에서의 IoC
    - Spring 프레임워크에서 지원하는 Ioc Container는 우리들이 흔히 개발하고 사용해왔던 일반 POJO(Plain Old Java Object)의 생명주기를 관리하며, 생성된 인스턴스들에게 추가적인 기능들을 제공한다.
- 라이브러리와 프레임워크의 차이
    - IoC의 개념이 적용되었나의 차이
    - 라이브러리를 사용하는 애플리케이션 코드는 애플리케이션 흐름을 직접 제어한다. 단지 동작하는 중에 필요한 기능이 있을 때 능동적으로 라이브러리를 시용할 뿐이다.
    - 반면에 프레임워크는 거꾸로 애플리케이션 코드가 프레임워크에 의해 사용된다. 보통 프레임워크 위에 개발한 클래스를 등록해두고, 프레임워크가 흐름을 주도하는 중에 개발자가 만든 애플리케이션 코드를 사용하도록 만드는 방식이다.

> :arrow_double_up:[Top](#8-spring)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#9-spring)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

### DI란
- DI?
    - Dependency Injection, 의존성 주입
    - Dependency Injection은 Spring 프레임워크에서 지원하는 IoC의 형태이다. 
    - DI는 클래스 사이의 의존관계를 빈 설정 정보를 바탕으로 컨테이너가 자동적으로 연결해주는 것을 말한다. 개발자들은 제어를 담당할 필요없이 빈 설정 파일에 의존관계가 필요하다는 정보만 추가해주면 된다.
        - 컨테이너가 실행 흐름의 주체가 되어 애플리케이션 코드에 의존관계를 주입해주는 것.
- 의존성(Dependency)
    - 현재 객체가 다른 객체와 상호작용(참조)하고 있다면 다른 객체들을 현재 객체의 의존이라 한다.
- 의존성이 위험한 이유
    - 하나의 모듈이 바뀌면 의존한 다른 모듈까지 변경되야 한다.
    - 테스트 가능한 어플을 만들 때 의존성이 있으면 유닛테스트 작성이 어렵다.
    - 유닛테스트의 목적 자체가 다른 모듈로부터 독립적으로 테스트하는 것을 요구한다.
- DI의 특징
    - ‘new’를 사용해 모듈 내에서 다른 모듈을 초기화하지 않으려면 객체 생성은 다른 곳에서 하고, 생성된 객체를 참조하면 된다.
    - 의존성 주입은 Inversion of Control 개념을 바탕으로 한다. 클래스가 외부로부터 의존성을 가져야한다.
- DI가 필요한 이유(DI의 장점)
    - 클래스를 재사용 할 가능성을 높이고, 다른 클래스와 독립적으로 클래스를 테스트 할 수 있다.
    - 비즈니스 로직의 특정 구현이 아닌 클래스를 생성하는데 매우 효과적
- DI의 세가지 방법
    - Contructor Injection : 생성자 삽입
    - Method(Setter) Injection : 메소드 매개 변수 삽입
    - Field Injection : 멤버 변수 삽입

> :arrow_double_up:[Top](#8-spring)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#9-spring)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

### AOP란
* AOP(Aspect Oriented Programming)란
  - Aspect Oriented Programming, 관점 지향 프로그래밍
  - 어떤 로직을 기준으로 핵심 관점과 부가 관점을 나누고, 관점을 기준으로 모듈화하는 것
  - 핵심 관점은 주로 핵심 비즈니스 로직
  - 부가 관점은 핵심 로직을 실행하기 위한 데이터베이스 연결, 로깅, 파일 입출력 등
  
* AOP 목적
  - 소스 코드에서 여러 번 반복해서 쓰는 코드(= 흩어진 관심사, Concern)를 Aspect로 모듈화하여 핵심 로직에서 분리 및 재사용
  - 개발자가 핵심 로직에 집중할 수 있게 하기 위함
  - 주로 부가 기능을 모듈화
  
* AOP 주요 용어
  - **Aspect**
    - 흩어진 관심사를 모듈화 한 것
    - Advice + PointCut
  - **Target**
    - Aspect를 적용하는 곳(클래스, 메소드 등)
  - **Advice**
    - 실질적으로 수행해야 하는 기능을 담은 구현체
  - **JoinPoint**
    - Advice가 적용될 위치
    - 끼어들 수 있는 지점
    - ex. 메소드 진입 시, 생성자 호출 시, 필드에서 값 꺼낼 때 등
  - **PointCut**
    - JoinPoint의 상세 스펙 정의
    - 더욱 구체적으로 Advice가 실행될 지점 지정
  - **Weaving**
    - PointCut에 의해 결정된 Target의 JoinPoint에 Advice를 삽입하는 과정
> :arrow_double_up:[Top](#8-spring)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#9-spring)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

### DAO와 DTO의 차이
- **DAO(Data Access Object)**
    - DB의 데이터를 조회하거나 조작하는 기능을 전담하도록 만든 객체를 말한다.
    - DB에 접근을 하기위한 로직과 비즈니스 로직을 분리하기 위해서 사용 한다.
- **DTO(Data Transfer Object)**
    - 계층간 데이터 교환을 위한 자바빈즈를 말한다.
        - 여기서 말하는 계층은 Controller, View, Business Layer, Persistent Layer 이다.
    - 일반적인 DTO는 로직을 갖고 있지 않는 순수한 데이터 객체이며, 속성과 그 속성에 접근하기 위한 getter, setter 메소드만 가진 클래스이다.
    - VO(Value Object) 라고도 불린다.
        - DTO와 동일한 개념이지만 read only 속성을 가진다.

> :arrow_double_up:[Top](#8-spring)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#9-spring)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)

## :house: [Home](https://github.com/WeareSoft/tech-interview)

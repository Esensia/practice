# 6. Design Pattern
**:book: Contents**
* [Singleton 패턴](#singleton-패턴)
* [Strategy 패턴](#strategy-패턴)
* [Template Method 패턴](#template-method-패턴)
* [Factory Method 패턴](#factory-method-패턴)
* [MVC1 패턴과 MVC2 패턴](#mvc1-패턴과-mvc2-패턴)

---
### Singleton 패턴
* 개념
  * 전역 변수를 사용하지 않고 **객체를 하나만 생성** 하도록 하며, 생성된 객체를 **어디에서든지 참조할 수 있도록** 하는 패턴
  * '생성(Creational) 패턴'의 하나
* <img src="./images/singleton-example.png" width="25%" height="25%">
* 역할이 수행하는 작업
  * Singleton
    * 하나의 인스턴스만을 생성하는 책임이 있으며 getInstance 메서드를 통해 모든 클라이언트에게 동일한 인스턴스를 반환하는 작업을 수행한다.
* 예시
  * 프린터 관리자 만들기

> :arrow_double_up:[Top](#5-design-pattern)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#5-design-pattern)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [https://gmlwjd9405.github.io/2018/07/06/singleton-pattern.html](https://gmlwjd9405.github.io/2018/07/06/singleton-pattern.html)

### Strategy 패턴
* 개념
  * **행위를 클래스로 캡슐화해** 동적으로 행위를 자유롭게 바꿀 수 있게 해주는 패턴
    * 같은 문제를 해결하는 여러 알고리즘이 클래스별로 캡슐화되어 있고 이들이 필요할 때 교체할 수 있도록 함으로써 동일한 문제를 다른 알고리즘으로 해결할 수 있게 하는 디자인 패턴
  * '행위(Behavioral) 패턴'의 하나
  * 즉, **전략을 쉽게 바꿀 수 있도록** 해주는 디자인 패턴이다.
    * 전략이란
      * 어떤 목적을 달성하기 위해 일을 수행하는 방식, 비즈니스 규칙, 문제를 해결하는 알고리즘 등
  * 특히 게임 프로그래밍에서 게임 캐릭터가 자신이 처한 상황에 따라 공격이나 행동하는 방식을 바꾸고 싶을 때 스트래티지 패턴은 매우 유용하다.
* <img src="./images/strategy-pattern.png" width="60%" height="60%">
* 역할이 수행하는 작업
  * Strategy
    * 인터페이스나 추상 클래스로 외부에서 동일한 방식으로 알고리즘을 호출하는 방법을 명시
  * ConcreteStrategy
    * 스트래티지 패턴에서 명시한 알고리즘을 실제로 구현한 클래스
  * Context
    * 스트래티지 패턴을 이용하는 역할을 수행한다.
    * 필요에 따라 동적으로 구체적인 전략을 바꿀 수 있도록 setter 메서드('집약 관계')를 제공한다.
* 예시
  * 로봇 만들기

> :arrow_double_up:[Top](#5-design-pattern)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#5-design-pattern)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [https://gmlwjd9405.github.io/2018/07/06/strategy-pattern.html](https://gmlwjd9405.github.io/2018/07/06/strategy-pattern.html)

### Template Method 패턴
* 개념
  * 어떤 작업을 처리하는 일부분을 **서브 클래스로 캡슐화해** 전체 일을 수행하는 구조는 바꾸지 않으면서 특정 단계에서 수행하는 내역을 바꾸는 패턴
    * 즉, **전체적으로는 동일하면서 부분적으로는 다른 구문으로 구성된 메서드의 코드 중복을 최소화** 할 때 유용하다.
    * 다른 관점에서 보면 동일한 기능을 상위 클래스에서 정의하면서 확장/변화가 필요한 부분만 서브 클래스에서 구현할 수 있도록 한다.
    * 예를 들어, 전체적인 알고리즘은 상위 클래스에서 구현하면서 다른 부분은 하위 클래스에서 구현할 수 있도록 함으로써 전체적인 알고리즘 코드를 재사용하는 데 유용하도록 한다.
  * '행위(Behavioral) 패턴'의 하나
* <img src="./images/template-method-pattern.png" width="40%" height="40%">
* 역할이 수행하는 작업
  * AbstractClass
    * 템플릿 메서드를 정의하는 클래스
    * 하위 클래스에 공통 알고리즘을 정의하고 하위 클래스에서 구현될 기능을 primitive 메서드 또는 hook 메서드로 정의하는 클래스
  * ConcreteClass
    * 물려받은 primitive 메서드 또는 hook 메서드를 구현하는 클래스
    * 상위 클래스에 구현된 템플릿 메서드의 일반적인 알고리즘에서 하위 클래스에 적합하게 primitive 메서드나 hook 메서드를 오버라이드하는 클래스
* 예시
  * 여러 회사의 모터 지원하기

> :arrow_double_up:[Top](#5-design-pattern)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#5-design-pattern)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [https://gmlwjd9405.github.io/2018/07/13/template-method-pattern.html](https://gmlwjd9405.github.io/2018/07/13/template-method-pattern.html)

### Factory Method 패턴
* 개념
  * **객체 생성 처리를 서브 클래스로 분리** 해 처리하도록 캡슐화하는 패턴
    * 즉, 객체의 생성 코드를 별도의 클래스/메서드로 분리함으로써 객체 생성의 변화에 대비하는 데 유용하다.
    * 특정 기능의 구현은 개별 클래스를 통해 제공되는 것이 바람직한 설계다.
      * 기능의 변경이나 상황에 따른 기능의 선택은 해당 객체를 생성하는 코드의 변경을 초래한다.
      * 상황에 따라 적절한 객체를 생성하는 코드는 자주 중복될 수 있다.
      * 객체 생성 방식의 변화는 해당되는 모든 코드 부분을 변경해야 하는 문제가 발생한다.
    * [스트래티지 패턴](https://gmlwjd9405.github.io/2018/07/06/strategy-pattern.html), [싱글턴 패턴](https://gmlwjd9405.github.io/2018/07/06/singleton-pattern.html), [템플릿 메서드 패턴](https://gmlwjd9405.github.io/2018/07/13/template-method-pattern.html)을 사용한다.
  * '생성(Creational) 패턴'의 하나
* <img src="./images/factory-method-pattern.png" width="60%" height="60%">
* 역할이 수행하는 작업
  * Product
    * 팩토리 메서드로 생성될 객체의 공통 인터페이스
  * ConcreteProduct
    * 구체적으로 객체가 생성되는 클래스
  * Creator
    * 팩토리 메서드를 갖는 클래스
  * ConcreteCreator
    * 팩토리 메서드를 구현하는 클래스로 ConcreteProduct 객체를 생성
* 팩토리 메서드 패턴의 개념과 적용 방법
  1. 객체 생성을 전담하는 별도의 **Factory 클래스 이용**
      * 스트래티지 패턴과 싱글턴 패턴을 이용한다.
      * 해당 Post에서는 이 방법을 기준으로 팩토리 메서드 패턴을 적용한다.
  2. **상속 이용**: 하위 클래스에서 적합한 클래스의 객체를 생성
      * 스트래티지 패턴, 싱글턴 패턴과 템플릿 메서드 패턴을 이용한다.
      * 해당 Post의 맨 하단에 '다른 방법으로 팩토리 메서드 패턴 적용하기'를 확인한다.
* 예시
  * 여러 가지 방식의 엘리베이터 스케줄링 방법 지원하기

> :arrow_double_up:[Top](#5-design-pattern)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#5-design-pattern)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
> - [https://gmlwjd9405.github.io/2018/08/07/factory-method-pattern.html](https://gmlwjd9405.github.io/2018/08/07/factory-method-pattern.html)

### MVC1 패턴과 MVC2 패턴

> :arrow_double_up:[Top](#5-design-pattern)    :leftwards_arrow_with_hook:[Back](https://github.com/WeareSoft/tech-interview#5-design-pattern)    :information_source:[Home](https://github.com/WeareSoft/tech-interview#tech-interview)
* MVC1
* <img src="./images/mvc1.png" width="60%" height="60%">
  - 웹브라우저 요청을 JSP가 처리, JSP가 Controller와 view 기능 모두 담당
  - jsp페이지 내에서 controller는 자바, view는 html, css 이벤트는 자바스크립트를 사용하고 Model은 jdbc 인터페이스로 DB 조작하면서 class를 정의
* MVC2
* <img src="./images/mvc2.png" width="60%" height="60%">
  - 웹 브라우저 요청을 controller에서 처리 controller는 요청에 대한 로직처리를 model로 보내고, model은 결과를 view로 보내여 사용자에게 응답
  - model은 mvc1, mvc2 모두 동일. view는 jsp로 구성되어 있으며, 자바는 포함되지 않고 jstl을 사용해 결과를 표현합니다.

---

## Reference
> - [JAVA 객체지향 디자인 패턴, 한빛미디어](http://www.kyobobook.co.kr/product/detailViewKor.laf?mallGb=KOR&ejkGb=KOR&barcode=9788968480911&orderClick=JAj)


## :house: [Home](https://github.com/WeareSoft/tech-interview)

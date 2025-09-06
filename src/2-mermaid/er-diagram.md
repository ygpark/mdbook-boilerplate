# ER 다이어그램

> 개체-관계 모델(ER 모델)은 특정 지식 영역에서 관심 있는 상호 관련된 사물들을 설명합니다. 기본적인 ER 모델은 개체 타입(관심 대상을 분류)으로 구성되며, 개체들(해당 개체 타입의 인스턴스) 간에 존재할 수 있는 관계를 명시합니다.

ER 모델링 실무자들은 거의 항상 *개체 타입*을 단순히 *개체*라고 지칭한다는 점에 주목하세요. 예를 들어 `CUSTOMER` 개체 *타입*은 단순히 `CUSTOMER` 개체라고 불립니다. 이는 매우 일반적이어서 다르게 하는 것은 바람직하지 않지만, 기술적으로 개체는 개체 타입의 추상적인 *인스턴스*이며, 이것이 ER 다이어그램이 보여주는 것입니다 - 추상적 인스턴스들과 그들 간의 관계입니다. 이것이 개체가 항상 단수 명사를 사용하여 명명되는 이유입니다.

Mermaid는 `erDiagram` 구문을 사용하여 ER 다이어그램을 렌더링할 수 있습니다.

## 문법

### 개체와 관계

Mermaid의 ER 다이어그램 문법은 PlantUML과 호환되며, 관계에 레이블을 지정하는 확장 기능이 있습니다. 각 명령문은 다음 부분들로 구성됩니다:

```text
<첫-번째-개체> [<관계> <두-번째-개체> : <관계-레이블>]
```

여기서:

- `첫-번째-개체`는 개체의 이름입니다
- `관계`는 두 개체가 서로 연관되는 방식을 설명합니다
- `두-번째-개체`는 다른 개체의 이름입니다
- `관계-레이블`은 첫 번째 개체의 관점에서 관계를 설명합니다

### 기본 예제

````text
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```
````

```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

## 관계 문법

`관계` 부분은 세 개의 하위 구성 요소로 나눌 수 있습니다:

- 두 번째 개체에 대한 첫 번째 개체의 카디널리티
- 관계가 '자식' 개체에게 식별성을 부여하는지 여부
- 첫 번째 개체에 대한 두 번째 개체의 카디널리티

### 카디널리티

| 값 (왼쪽) | 값 (오른쪽) | 의미         |
| --------- | ----------- | ------------ |
| `\|o`     | `o\|`       | 0개 또는 1개 |
| `\| `     | `\|\|`      | 정확히 1개   |
| `}o`      | `o{`        | 0개 이상     |
| `}\|`     | `\|{`       | 1개 이상     |

### 식별 관계

| 값   | 의미        |
| ---- | ----------- |
| `--` | 식별 관계   |
| `..` | 비식별 관계 |

## 속성

개체에 대한 속성은 개체 이름 뒤에 중괄호 `{}` 안에 속성 정의를 지정하여 정의할 수 있습니다. 각 속성은 타입과 이름으로 정의됩니다.

### 기본 속성 문법

````text
```mermaid
erDiagram
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER {
        int orderNumber
        string deliveryAddress
        datetime orderDate
    }
    CUSTOMER ||--o{ ORDER : places
```
````

```mermaid
erDiagram
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER {
        int orderNumber
        string deliveryAddress
        datetime orderDate
    }
    CUSTOMER ||--o{ ORDER : places
```

### 속성 키와 주석

속성을 키로 지정하고 주석을 포함할 수 있습니다:

````text
```mermaid
erDiagram
    CUSTOMER {
        string name
        string custNumber PK "기본키"
        string sector
    }
    ORDER {
        int orderNumber PK
        string deliveryAddress
        datetime orderDate
        string custNumber FK "외래키"
    }
    PRODUCT {
        string productName PK
        int productPrice
        string category
    }
    ORDER-ITEM {
        int quantity
        int orderNumber FK
        string productName FK
    }

    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER-ITEM : contains
    PRODUCT ||--|{ ORDER-ITEM : "주문됨"
```
````

```mermaid
erDiagram
    CUSTOMER {
        string name
        string custNumber PK "기본키"
        string sector
    }
    ORDER {
        int orderNumber PK
        string deliveryAddress
        datetime orderDate
        string custNumber FK "외래키"
    }
    PRODUCT {
        string productName PK
        int productPrice
        string category
    }
    ORDER-ITEM {
        int quantity
        int orderNumber FK
        string productName FK
    }

    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER-ITEM : contains
    PRODUCT ||--|{ ORDER-ITEM : "주문됨"
```

### 키 타입

- `PK` - 기본키(Primary Key)
- `FK` - 외래키(Foreign Key)
- `UK` - 유니크키(Unique Key)

## 완전한 예제

````text
```mermaid
erDiagram
    CUSTOMER {
        string name "고객명"
        string custNumber PK "고객ID"
        string sector "업종"
        string address
        string phoneNumber
        string email UK
    }
    ORDER {
        int orderNumber PK "주문ID"
        string deliveryAddress "배송주소"
        datetime orderDate "주문일자"
        decimal totalAmount "총주문금액"
        string status "주문상태"
        string custNumber FK "고객ID"
    }
    PRODUCT {
        string productName PK "상품명"
        decimal productPrice "단가"
        string category "상품분류"
        string description
        int stockQuantity "재고수량"
    }
    ORDER-ITEM {
        int quantity "주문수량"
        decimal unitPrice "주문시단가"
        int orderNumber FK "주문ID"
        string productName FK "상품명"
    }
    SUPPLIER {
        int supplierID PK "공급업체ID"
        string name "공급업체명"
        string contactPerson
        string phoneNumber
        string email UK
        string address
    }
    PRODUCT-SUPPLIER {
        int supplierID FK "공급업체ID"
        string productName FK "상품명"
        decimal supplierPrice "공급업체단가"
        int leadTime "리드타임(일)"
    }

    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER-ITEM : contains
    PRODUCT ||--|{ ORDER-ITEM : "주문됨"
    SUPPLIER ||--|{ PRODUCT-SUPPLIER : supplies
    PRODUCT ||--o{ PRODUCT-SUPPLIER : "공급받음"
```
````

```mermaid
erDiagram
    CUSTOMER {
        string name "고객명"
        string custNumber PK "고객ID"
        string sector "업종"
        string address
        string phoneNumber
        string email UK
    }
    ORDER {
        int orderNumber PK "주문ID"
        string deliveryAddress "배송주소"
        datetime orderDate "주문일자"
        decimal totalAmount "총주문금액"
        string status "주문상태"
        string custNumber FK "고객ID"
    }
    PRODUCT {
        string productName PK "상품명"
        decimal productPrice "단가"
        string category "상품분류"
        string description
        int stockQuantity "재고수량"
    }
    ORDER-ITEM {
        int quantity "주문수량"
        decimal unitPrice "주문시단가"
        int orderNumber FK "주문ID"
        string productName FK "상품명"
    }
    SUPPLIER {
        int supplierID PK "공급업체ID"
        string name "공급업체명"
        string contactPerson
        string phoneNumber
        string email UK
        string address
    }
    PRODUCT-SUPPLIER {
        int supplierID FK "공급업체ID"
        string productName FK "상품명"
        decimal supplierPrice "공급업체단가"
        int leadTime "리드타임(일)"
    }

    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ ORDER-ITEM : contains
    PRODUCT ||--|{ ORDER-ITEM : "주문됨"
    SUPPLIER ||--|{ PRODUCT-SUPPLIER : supplies
    PRODUCT ||--o{ PRODUCT-SUPPLIER : "공급받음"
```

## 개체명

개체명은 종종 대문자로 표기되지만, 이에 대한 공인된 표준은 없으며 Mermaid에서 필수는 아닙니다.

개체명은 다음과 같아야 합니다:

- 단수 명사
- 대문자로 작성 (일반적인 관례)
- 나타내는 것을 명확히 설명

## 스타일링

### 커스텀 스타일링

CSS를 사용하여 개별 개체를 스타일링할 수 있습니다:

````
```mermaid
erDiagram
    CUSTOMER {
        string name
        string custNumber PK
    }
    ORDER {
        int orderNumber PK
        string deliveryAddress
    }
    CUSTOMER ||--o{ ORDER : places

    %% 커스텀 스타일링
    classDef customerClass fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef orderClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px

    class CUSTOMER customerClass
    class ORDER orderClass
```
````

```mermaid
erDiagram
    CUSTOMER {
        string name
        string custNumber PK
    }
    ORDER {
        int orderNumber PK
        string deliveryAddress
    }
    CUSTOMER ||--o{ ORDER : places

    %% 커스텀 스타일링
    classDef customerClass fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef orderClass fill:#f3e5f5,stroke:#4a148c,stroke-width:2px

    class CUSTOMER customerClass
    class ORDER orderClass
```

## 모범 사례

### 명명 규칙

- 개체명에 단수 명사 사용
- 개체가 나타내는 것을 명확하게 식별할 수 있는 설명적인 이름 사용
- 다이어그램 전체에서 일관된 명명 패턴 유지

### 관계 설계

- 각 관계에 대해 카디널리티를 명확하게 정의
- 의미 있는 관계 레이블 사용
- 관계가 식별 관계인지 비식별 관계인지 고려

### 속성 정의

- 각 개체에 대한 모든 관련 속성 포함
- 기본키와 외래키를 명확하게 표시
- 복잡한 속성에 대해 주석 추가

## 일반적인 패턴

### 일대다 관계

````text
```mermaid
erDiagram
    DEPARTMENT ||--o{ EMPLOYEE : employs
    DEPARTMENT {
        int deptId PK
        string deptName
        string location
    }
    EMPLOYEE {
        int empId PK
        string firstName
        string lastName
        int deptId FK
    }
```
````

```mermaid
erDiagram
    DEPARTMENT ||--o{ EMPLOYEE : employs
    DEPARTMENT {
        int deptId PK
        string deptName
        string location
    }
    EMPLOYEE {
        int empId PK
        string firstName
        string lastName
        int deptId FK
    }
```

### 다대다 관계

````text
```mermaid
erDiagram
    STUDENT ||--o{ ENROLLMENT : enrolls
    ENROLLMENT ||--|| COURSE : "수강함"

    STUDENT {
        int studentId PK
        string firstName
        string lastName
        string email UK
    }
    COURSE {
        string courseCode PK
        string courseName
        int credits
        string department
    }
    ENROLLMENT {
        int studentId FK
        string courseCode FK
        date enrollmentDate
        string grade
    }
```
````

```mermaid
erDiagram
    STUDENT ||--o{ ENROLLMENT : enrolls
    ENROLLMENT ||--|| COURSE : "수강함"

    STUDENT {
        int studentId PK
        string firstName
        string lastName
        string email UK
    }
    COURSE {
        string courseCode PK
        string courseName
        int credits
        string department
    }
    ENROLLMENT {
        int studentId FK
        string courseCode FK
        date enrollmentDate
        string grade
    }
```

### 자기참조 관계

````text
```mermaid
erDiagram
    EMPLOYEE ||--o{ EMPLOYEE : manages
    EMPLOYEE {
        int empId PK
        string name
        string position
        int managerId FK "empId 참조"
    }
```
````

```mermaid
erDiagram
    EMPLOYEE ||--o{ EMPLOYEE : manages
    EMPLOYEE {
        int empId PK
        string name
        string position
        int managerId FK "empId 참조"
    }
```

## 복합 예제: 전자상거래 시스템

````text
```mermaid
erDiagram
    CUSTOMER {
        int customerId PK
        string firstName
        string lastName
        string email UK
        string phone
        date registrationDate
    }

    ADDRESS {
        int addressId PK
        string street
        string city
        string state
        string zipCode
        string country
        int customerId FK
    }

    CATEGORY {
        int categoryId PK
        string categoryName
        string description
    }

    PRODUCT {
        int productId PK
        string productName
        string description
        decimal price
        int stockQuantity
        int categoryId FK
    }

    ORDER {
        int orderId PK
        datetime orderDate
        string status
        decimal totalAmount
        int customerId FK
        int shippingAddressId FK
    }

    ORDER_ITEM {
        int orderId FK
        int productId FK
        int quantity
        decimal unitPrice
    }

    PAYMENT {
        int paymentId PK
        int orderId FK
        decimal amount
        datetime paymentDate
        string paymentMethod
        string status
    }

    REVIEW {
        int reviewId PK
        int productId FK
        int customerId FK
        int rating
        string comment
        datetime reviewDate
    }

    CUSTOMER ||--o{ ADDRESS : "보유"
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ REVIEW : writes

    CATEGORY ||--o{ PRODUCT : contains

    ORDER ||--|| ADDRESS : "배송지"
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER ||--o{ PAYMENT : "결제됨"

    PRODUCT ||--|{ ORDER_ITEM : "포함됨"
    PRODUCT ||--o{ REVIEW : "리뷰됨"
```
````

```mermaid
erDiagram
    CUSTOMER {
        int customerId PK
        string firstName
        string lastName
        string email UK
        string phone
        date registrationDate
    }

    ADDRESS {
        int addressId PK
        string street
        string city
        string state
        string zipCode
        string country
        int customerId FK
    }

    CATEGORY {
        int categoryId PK
        string categoryName
        string description
    }

    PRODUCT {
        int productId PK
        string productName
        string description
        decimal price
        int stockQuantity
        int categoryId FK
    }

    ORDER {
        int orderId PK
        datetime orderDate
        string status
        decimal totalAmount
        int customerId FK
        int shippingAddressId FK
    }

    ORDER_ITEM {
        int orderId FK
        int productId FK
        int quantity
        decimal unitPrice
    }

    PAYMENT {
        int paymentId PK
        int orderId FK
        decimal amount
        datetime paymentDate
        string paymentMethod
        string status
    }

    REVIEW {
        int reviewId PK
        int productId FK
        int customerId FK
        int rating
        string comment
        datetime reviewDate
    }

    CUSTOMER ||--o{ ADDRESS : "보유"
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ REVIEW : writes

    CATEGORY ||--o{ PRODUCT : contains

    ORDER ||--|| ADDRESS : "배송지"
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER ||--o{ PAYMENT : "결제됨"

    PRODUCT ||--|{ ORDER_ITEM : "포함됨"
    PRODUCT ||--o{ REVIEW : "리뷰됨"
```

이 포괄적인 예제는 ER 다이어그램이 여러 개체와 다양한 유형의 관계를 가진 복잡한 실세계 시스템을 어떻게 모델링할 수 있는지를 보여줍니다.

## 효과적인 ER 다이어그램 작성을 위한 팁

1. **단순하게 시작하기**: 핵심 개체와 관계부터 시작한 후 세부사항을 추가하세요
2. **명확한 이름 사용**: 개체, 속성, 관계에 대해 설명적인 이름을 선택하세요
3. **가정 문서화**: 주석을 사용하여 비즈니스 규칙과 제약 조건을 명확히 하세요
4. **이해관계자와 검증**: 도메인 전문가와 다이어그램을 검토하세요
5. **반복과 개선**: ER 다이어그램은 종종 여러 번의 수정이 필요합니다
6. **성능 고려**: 모델이 실제로 어떻게 구현될지 고려하세요

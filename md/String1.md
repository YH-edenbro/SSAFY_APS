# String(문자열)

## 컴퓨터에서의 문자표현

- 글자 A를 메모리에 저장하는 방법에 대해서 생각해보자.
- 네트워크가 발전되기 전 지역별로 정해놓고 사용
- 네트워크가 발전하면서 서로간에 정보를 주고 받을 때 정보를 달리 해석한다는 문제가 생겼다.
- 혼동을 피하기 위한 표준안 제작
  
    -> **ASCII 코드**

- 다국어 처리를 위해 **유니코드**

- big-endian : 높은자리 먼저 저장
- little-endian : 낮은자리 먼저 저장

### 유니코드 인코딩(UTF : Unicode Transformation Format)

- UTF-8(in web)
  - MIN : 8bit, MAX: 32bit(1 Byte * 4)
- UTF-16(in windows, java)
  - MIN : 16bit, MAX: 32bit(2 Byte * 2)
- UTF-32(in unix)
  - MIN : 32bit, MAX : 32bit(4 Byte * 1)

## 문자열의 분류
- 문자열(string)
  - fixed length
  - variable length
    - length controlled(java 언어에서의 문자열)
    - delimited(c 언어에서의 문자열)
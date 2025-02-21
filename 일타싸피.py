import math

start = (1,1)
end = (2,2)

a = abs(end[0] - start[0])  # x 좌표의 차이
b = abs(end[1] - start[1])  # y 좌표의 차이

r = math.sqrt(a**2 + b**2)

# 아크탄젠트는 math.atan 함수를 이용하면 계산할 수 있음
# math.atan의 결과는 radian으로 나옴 (degree가 아님)
radian = math.atan(b / a)

# radian을 degree로 변경을 해야 실제 각도를 얻을 수 있음
print(r, math.degrees(radian))


"""
결국 알면 되는것은

math 함수 쓰는법.
arctan 쓰는법.
거리 구하는 방법.
끝

이거 알면 그냥 세기만 잘 조절하면 되는거 아닐까?
"""

# 정사영까지 이동하기

PI = 3.141592

def calculate_theta(x1, y1, x2, y2):
    # 1) my ball(내 공)과 정사영까지의 x 거리 a
    a = x2 - x1
    # 2) my nall(내 공)과 정사영까지의 y 거리 b
    b = y2 - y1
    # 3) my ball(내 공)이 법선과 벽의 교차점으로 이동하기 위한 방향 (세타)
    tan_theta = a / b
    theta = math.atan(tan_theta)
    return theta

x1, y1 = 1.0, 2.0  # my ball 초기 위치
x2, y2 = 5.0, 1.0

# 세타 계산
alpha = calculate_theta(x1,y1,x2,y2)

# 출력 (라디안 및 도 단위 변환)
print(f"my ball의 출발 각도 (라디안): {alpha}")
print(f"my ball의 출발 각도: {alpha * 180.0 / PI} 도")        
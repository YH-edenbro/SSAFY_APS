import math

def calculate_shot(white_ball, target_ball, pocket):
    """
    흰 공(white_ball)에서 목적구(target_ball)를 포켓(pocket)으로 넣기 위한 샷 계산
    :param white_ball: (x, y) 흰 공 좌표
    :param target_ball: (x, y) 목적구 좌표
    :param pocket: (x, y) 포켓 좌표
    :return: 조준해야 할 각도(도)와 거리
    """
    # 목적구에서 포켓 방향의 각도 계산
    dx = pocket[0] - target_ball[0]
    dy = pocket[1] - target_ball[1]
    angle_to_pocket = math.atan2(dy, dx)

    # 흰 공에서 목적구 방향의 각도 계산
    dx = target_ball[0] - white_ball[0]
    dy = target_ball[1] - white_ball[1]
    angle_to_target = math.atan2(dy, dx)

    # 샷의 최적 각도 계산 (라디안을 도 단위로 변환)
    shot_angle = math.degrees(angle_to_target)

    # 거리 계산
    distance = math.sqrt(dx**2 + dy**2)

    return shot_angle, distance

# 예제 좌표 (당구대는 1000x500 기준)
white_ball = (500, 250)  # 중앙에 위치한 흰 공
target_ball = (700, 300)  # 목적구 위치
pocket = (1000, 0)  # 우측 아래 포켓

angle, dist = calculate_shot(white_ball, target_ball, pocket)
print(f"샷 각도: {angle:.2f}도, 거리: {dist:.2f}")

# 기본 코드 ---------------------------------------------------


import pygame
import math
import random

# Pygame 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("일타싸피 - 쿠션 반사 및 다수의 공 처리")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 100, 0)

# 공의 반지름
RADIUS = 10
FRICTION = 0.98  # 마찰 계수

# 포켓 반경 (공보다 약간 큼)
POCKET_RADIUS = RADIUS * 1.5

# 포켓 위치 (코너 4개 + 중간 2개)
pockets = [(0, 0), (WIDTH//2, 0), (WIDTH, 0), (0, HEIGHT), (WIDTH//2, HEIGHT), (WIDTH, HEIGHT)]

# 공 클래스 정의
class Ball:
    def __init__(self, x, y, color, is_white=False):
        self.x = x
        self.y = y
        self.color = color
        self.radius = RADIUS
        self.velocity = [0, 0]
        self.is_white = is_white  # 흰 공 여부

    def move(self):
        # 공 이동
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # 쿠션 반사 (벽에 충돌 시 반사)
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.velocity[0] *= -1  # x축 반전
        if self.y - self.radius <= 0 or self.y + self.radius >= HEIGHT:
            self.velocity[1] *= -1  # y축 반전

        # 마찰 효과
        self.velocity[0] *= FRICTION
        self.velocity[1] *= FRICTION

        # 속도 낮으면 멈춤
        if abs(self.velocity[0]) < 0.1:
            self.velocity[0] = 0
        if abs(self.velocity[1]) < 0.1:
            self.velocity[1] = 0

    def check_collision(self, other):
        """다른 공과 충돌 감지 및 반응"""
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx**2 + dy**2)

        if distance <= self.radius * 2:  # 충돌 발생
            # 충돌 방향 벡터 정규화
            angle = math.atan2(dy, dx)
            sin_a, cos_a = math.sin(angle), math.cos(angle)

            # 공의 속도를 상대 좌표계로 변환
            v1 = cos_a * self.velocity[0] + sin_a * self.velocity[1]
            v2 = cos_a * other.velocity[0] + sin_a * other.velocity[1]

            # 충돌 후 속도 교환 (운동량 보존)
            self.velocity[0] = cos_a * v2 - sin_a * self.velocity[1]
            self.velocity[1] = sin_a * v2 + cos_a * self.velocity[1]

            other.velocity[0] = cos_a * v1 - sin_a * other.velocity[1]
            other.velocity[1] = sin_a * v1 + cos_a * other.velocity[1]

            # 충돌 후 중첩 방지 (조금 밀어내기)
            overlap = (self.radius * 2 - distance) / 2
            self.x -= overlap * cos_a
            self.y -= overlap * sin_a
            other.x += overlap * cos_a
            other.y += overlap * sin_a

    def is_in_pocket(self):
        """포켓에 들어갔는지 확인 (공의 중심이 포켓 반경 + 공 반경보다 안쪽이면 제거)"""
        for px, py in pockets:
            if math.sqrt((self.x - px)**2 + (self.y - py)**2) <= (POCKET_RADIUS + self.radius):
                return True
        return False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# 공 리스트 초기화
balls = [
    Ball(500, 250, WHITE, is_white=True),  # 흰 공
    Ball(600, 250, RED),  # 목적구 1
    Ball(650, 300, RED),  # 목적구 2
    Ball(700, 200, RED),  # 목적구 3
]

# 흰 공 샷 설정
white_ball = balls[0]
shot_angle = math.radians(25)  # 샷 방향
shot_power = 60 # 샷 세기
white_ball.velocity = [shot_power * math.cos(shot_angle), shot_power * math.sin(shot_angle)]

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GREEN)  # 당구대 배경

    # 공 이동 및 충돌 처리
    for ball in balls:
        ball.move()

    # 공끼리 충돌 확인
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].check_collision(balls[j])

    # 포켓 감지 (목적구만 삭제)
    balls = [ball for ball in balls if not (ball.is_in_pocket() and not ball.is_white)]

    # 공 그리기
    for ball in balls:
        ball.draw(screen)

    # 포켓 그리기
    for px, py in pockets:
        pygame.draw.circle(screen, BLUE, (px, py), POCKET_RADIUS)

    # 이벤트 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)  # 60 FPS 유지

pygame.quit()



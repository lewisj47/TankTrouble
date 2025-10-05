#Tank Trouble Environment
import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Movement")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Tank Movement")

shoot_sound = pygame.mixer.Sound("sound.wav")
move_forward_sound = pygame.mixer.Sound("move_forward.wav")

#Screen Dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

#Tank sprite class
class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_tank_image = pygame.image.load("tank.png").convert_alpha()
        self.tank_image = pygame.transform.scale(self.original_tank_image, (50,30))
        self.image = self.tank_image
        self.rect = self.tank_image.get_rect(center=(x,y))
        self.angle = 0
        self.tip_offset = 30
        self.gun_length = 40
        self.speed = 0
        self.rotation_speed = 0

        self.original_gun_length = self.gun_length
        self.can_shoot = 200
        self.shoot_cooldown = 0
        self.cooldown_duration = 3000
        self.last_update_time = pygame.time.get_ticks()
    
    def update(self):
        keys = pygame.ket.get_pressed()

        if keys[pygame.K_UP]:
            self.speed = 3
        elif keys[pygame.K_DOWN]:
            self.speed = -2
        else:
            self.speed = 0
        
        if keys[pygame.K_LEFT]:
            self.rotation_speed = 2
        elif keys[pygame.K_RIGHT]:
            self.rotation_speed = -2
        else:
            self.rotation_speed = 0
        
        self.angle += self.rotation_speed
        self.angle %= 360

        self.image = pygame.transform.rotate(self.original_tank_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        angle_rad = math.radians(self.angle)
        dx = math.cos(angle_rad) * self.speed
        dy = math.sin(angle_rad) * self.speed

        self.rect.x += dx
        self.rect.y -+ dy

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init()
        self.original_bullet_image = pygame.image.load("bullet.png").convert_alpha()
        self.bullet_image = pygame.transform.scale(self.original_bullet_image,(20,20))
        self.image = self.bullet_image
        self.angle = angle
        self.speed = 10

        angle_rad = math.radians(self.angle)

        dx = (tank.gun_length + tank.tip_offset - 32) * math.cos(angle_rad)

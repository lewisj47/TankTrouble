#Tank Trouble Environment
import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
BOUNCELIMIT = 3
SPEED = 1.8
ROT_SPEED = 1.5
BULLET_SPEED = 1.5

tank_length = 100
tank_scalar = 1

map_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Movement")
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Tank Movement")

shoot_sound = pygame.mixer.Sound("sound.wav")

#Screen Dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

#Tank sprite class
class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_tank_image = pygame.image.load("tank.png").convert_alpha()
        self.tank_image = pygame.transform.scale(self.original_tank_image, (tank_length * tank_scalar, tank_length * tank_scalar))
        self.image = self.tank_image
        self.rect = self.tank_image.get_rect(center=(x,y))
        # Fixed-size collision rectangle (e.g., 40x24)
        self.collision_rect = pygame.Rect(0, 0, 80, 80)
        self.rect.x += 10
        self.angle = 0
        self.tip_offset = 30
        self.gun_length = 40
        self.speed = 0
        self.rotation_speed = 0

        self.original_gun_length = self.gun_length
        self.gun_back_start_time = 0
        self.gun_back_duration = 200
        self.can_shoot = True
        self.shot_time = 0
        self.cooldown_duration = 200
        self.reload_speed = 3500
        self.magazine = 5
        self.last_update_time = pygame.time.get_ticks()
    
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.speed = 3 * SPEED
        elif keys[pygame.K_DOWN]:
            self.speed = -2 * SPEED
        else:
            self.speed = 0

        if keys[pygame.K_LEFT]:
            self.rotation_speed = 2 * ROT_SPEED
        elif keys[pygame.K_RIGHT]:
            self.rotation_speed = -2 * ROT_SPEED
        else:
            self.rotation_speed = 0

        self.angle += self.rotation_speed
        self.angle %= 360

        self.image = pygame.transform.rotate(self.tank_image, self.angle)
        old_rect = self.rect.copy()
        self.rect = self.image.get_rect(center=self.rect.center)
        # Keep collision rect centered on tank
        self.collision_rect.center = self.rect.center

        angle_rad = math.radians(self.angle)
        dx = math.cos(angle_rad) * self.speed
        dy = math.sin(angle_rad) * self.speed

        # Simulate x movement
        next_collision_rect_x = self.collision_rect.copy()
        next_collision_rect_x.x += dx
        collision_x = False
        for row in range(len(map_data)):
            for col in range(len(map_data[row])):
                if map_data[row][col] == 1:
                    wall_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if next_collision_rect_x.colliderect(wall_rect):
                        collision_x = True
                        break
            if collision_x:
                break
        if not collision_x:
            self.collision_rect.x += dx
            self.rect.centerx = self.collision_rect.centerx

        # Simulate y movement
        next_collision_rect_y = self.collision_rect.copy()
        next_collision_rect_y.y -= dy
        collision_y = False
        for row in range(len(map_data)):
            for col in range(len(map_data[row])):
                if map_data[row][col] == 1:
                    wall_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if next_collision_rect_y.colliderect(wall_rect):
                        collision_y = True
                        break
            if collision_y:
                break
        if not collision_y:
            self.collision_rect.y -= dy
            self.rect.centery = self.collision_rect.centery

    def collides_with_wall(self):
        # Check for collision with wall tiles using fixed collision rect
        for row in range(len(map_data)):
            for col in range(len(map_data[row])):
                if map_data[row][col] == 1:
                    wall_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if self.collision_rect.colliderect(wall_rect):
                        return True
        return False

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()  # Correct parent constructor call
        self.original_bullet_image = pygame.image.load("bullet.png").convert_alpha()
        self.bullet_image = pygame.transform.scale(self.original_bullet_image, (20, 20))
        self.image = self.bullet_image
        self.angle = angle
        self.speed = 3 * BULLET_SPEED
        self.bounced = False  # Track if bullet has bounced

        angle_rad = math.radians(self.angle)
        dx = (tank.gun_length + tank.tip_offset - 32) * math.cos(angle_rad)
        dy = -(tank.gun_length + tank.tip_offset - 32) * math.sin(angle_rad)
        self.rect = self.bullet_image.get_rect(center=(x + dx, y + dy))
        self.collision_rect = pygame.Rect(0, 0, 20, 20)
        self.start_x = self.rect.centerx
        self.start_y = self.rect.centery

    def collides_with_wall(self):
        for row in range(len(map_data)):
            for col in range(len(map_data[row])):
                if map_data[row][col] == 1:
                    wall_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if self.rect.colliderect(wall_rect):
                        return True
        return False

    def update(self):
        angle_rad = math.radians(self.angle)
        dx = self.speed * math.cos(angle_rad)
        dy = -self.speed * math.sin(angle_rad)

        # Try to move in x direction
        self.rect.x += dx
        if self.collides_with_wall():
            self.rect.x -= dx
            if self.bounced < BOUNCELIMIT:
                self.angle = (180 - self.angle) % 360
                self.bounced += 1
            else:
                self.kill()
                return

        # Try to move in y direction
        self.rect.y += dy
        if self.collides_with_wall():
            self.rect.y -= dy
            if self.bounced < BOUNCELIMIT:
                self.angle = (-self.angle) % 360
                self.bounced +=1
            else:
                self.kill()
                return

# Color the map walls
def draw_map():
    WALL_COLOR = (100, 100, 100)  # Gray
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            if map_data[row][col] == 1:
                pygame.draw.rect(screen, WALL_COLOR, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))







#MAIN LOOP
tank = Tank(150, 150)
all_sprites = pygame.sprite.Group()
all_obstacles = pygame.sprite.Group()
all_sprites.add(tank)
bullet_sprites = pygame.sprite.Group()

running = True

while running:

    # Restart game if tank is destroyed
    if not tank.alive():
        # Draw a box and message in the center
        box_width, box_height = 400, 150
        box_x = SCREEN_WIDTH // 2 - box_width // 2
        box_y = SCREEN_HEIGHT // 2 - box_height // 2
        pygame.draw.rect(screen, (50, 50, 50), (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, (200, 0, 0), (box_x, box_y, box_width, box_height), 4)
        font = pygame.font.SysFont(None, 60)
        text = font.render("u suck", True, (255, 255, 255))
        screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
        pygame.display.flip()
        pygame.time.wait(2000)
        all_sprites.empty()
        bullet_sprites.empty()
        tank = Tank(150, 150)
        all_sprites.add(tank)
        continue

    # Check if tank is hit by any bullet and destroy both
    hit_bullet = pygame.sprite.spritecollideany(tank, bullet_sprites)
    if hit_bullet:
        tank.kill()
        hit_bullet.kill()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()

    keys = pygame.key.get_pressed()

    if tank.can_shoot and keys[pygame.K_SPACE] and tank.magazine > 0:
        tank.shot_time = pygame.time.get_ticks()

        bullet_angle = tank.angle

        bullet_x = tank.rect.centerx + (tank.gun_length + tank.tip_offset) * math.cos(math.radians(bullet_angle))
        bullet_y = tank.rect.centery - (tank.gun_length + tank.tip_offset) * math.sin(math.radians(bullet_angle))
        bullet = Bullet(bullet_x, bullet_y, bullet_angle)

        tank.magazine -= 1
        all_sprites.add(bullet)
        bullet_sprites.add(bullet)
        shoot_sound.play()
        tank.can_shoot = False
    
    bullet_sprites.update()

    if pygame.time.get_ticks() - tank.shot_time > tank.cooldown_duration:
        tank.can_shoot = True
    if tank.magazine == 0:
        if pygame.time.get_ticks() - tank.shot_time > tank.reload_speed:
            tank.magazine = 5

    screen.fill((255, 255, 255))
    draw_map()
    all_sprites.draw(screen)
    bullet_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
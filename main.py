import pygame
from constants import *
from player import Player
from AsteroidField import *
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    player_timer = 0
    

 

    print(f"""Starting asteroids! 
Screen width: {SCREEN_WIDTH} 
Screen height: {SCREEN_HEIGHT}""")
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((1, 1, 1))
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print(f"Game Over!")
                sys.exit()
                
        pygame.display.flip()

        dt = clock.tick(60) / 1000
   
   
    pygame.quit()

if __name__ == "__main__":
    main()
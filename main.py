from constants import * # pyright: ignore[reportMissingImports]
import pygame
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # type: ignore
    print(f"Screen height: {SCREEN_HEIGHT}")  # type: ignore
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore
    game_clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()



    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        updatable.update(dt)

        screen.fill("black")

        for rock in asteroids:
            for bullet in shots:
                if bullet.collide(rock):
                    bullet.kill()
                    rock.split()

        for rock in asteroids:
            if player.collide(rock):
                print("Game Over!")
                raise SystemExit

        for item in drawable:
            item.draw(screen)
    
        pygame.display.flip()

        # limit the framerate to 60 FPS

        dt = game_clock.tick(60)/1000
  
        

if __name__ == "__main__":
    main()
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #creates a new player object centered on screen
    x = SCREEN_WIDTH / 2 
    y = SCREEN_HEIGHT / 2
    player1 = Player(x, y)

    #creates a new clock object
    clock = pygame.time.Clock()
    dt = 0

    #creates a new AsteroidField object
    asteroidfield1 = AsteroidField()

    # infinite game loop
    running = True
    while running:
        log_state()
        # make the "X" button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update player movement, asteroids, and shots
        updatable.update(dt)
        #check collision
        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                return SystemExit       
        # draw everything
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        # limit frame rate
        dt = clock.tick(60) / 1000
        # show the frame
        pygame.display.flip()
        


if __name__ == "__main__":
    main()

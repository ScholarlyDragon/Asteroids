import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #creates a new clock object
    clock = pygame.time.Clock()
    dt = 0

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
        
    #creates a new player object centered on screen
    x = SCREEN_WIDTH / 2 
    y = SCREEN_HEIGHT / 2
    player1 = Player(x, y)

    # infinite game loop
    while True:
        log_state()
        # make the "X" button work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update player movement, asteroids, and shots
        updatable.update(dt)
        # draw everything
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        # limit frame rate
        dt = clock.tick(60) / 1000
        # show the frame
        pygame.display.flip()
        


if __name__ == "__main__":
    main()

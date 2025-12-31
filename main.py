import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    ## groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2), PLAYER_RADIUS)
    
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    

    exit = False

    while not exit:
        
        
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            print(event)
        screen.fill("black")
        updatable.update(dt)
        for p in drawable:
            p.draw(screen)
        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()

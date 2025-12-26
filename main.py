import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        pygame.display.flip()
    
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()

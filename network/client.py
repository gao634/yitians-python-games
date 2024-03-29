import pygame

#this function is called every tick of the loop to update the window
def redraw_window(window):
    window.fill((255, 255, 255))
    pygame.display.update()

def main():
    #sets up window
    height = 500
    width = 500
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")

    #client number will keep track of different clients
    client_number = 0

    #main loop
    run = True
    while run:
        redraw_window(window)
        #checks if the x is pressed, this part at the end of the while loop so code exits cleanly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
main()
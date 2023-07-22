import pygame
import random
pygame.init()

clock = pygame.time.Clock()
speed = 100

display_width = 800
display_height= 600

x = 100
y = 100
radius = 10

x_1 =  3
y_1 = 3

paddle_x = 10
paddle_y = 10 
paddle_width = 15
paddle_height = 60

play_score = 0

def randomize_start():
    global x,y,y_1 
    x = random.randint(int(display_width/4), display_width - 20)
    y = random.randint(10, display_height-10)
    if random.randint(0,2)%2==0:
        y_1 *=1 

def hit_back():
    if x + radius > display_width:
        return True
    return False

def hit_sides():
    if y - radius < 0 :
        return True
    if y + radius > display_height:
        return True
    return False 

def hit_paddle():
    global play_score
    if x - radius <= paddle_x + paddle_width and y > paddle_y and y < paddle_y + paddle_height:
        play_score += 100
        return True
    return False

def game_over():
    global play_score
    end_game = True
    screen.fill ((0,150,0))
    font_title = pygame.font.Font(None, 36)
    font_instructions = pygame.font.Font(None, 24)
    announcement = font_title.render("Game over", True, (255,255,255))
    announcement_rect = announcement.get_rect(center = (int(display_width/2), int(display_height/3)))
    screen.blit(announcement, announcement_rect)

    qinstructions = font_instructions.render("Press q to quit", True, (255,255,255))
    qinstructions_rect = qinstructions.get_rect(center = (int(display_width/2), int(display_height/1.5)))
    screen.blit(qinstructions,qinstructions_rect)

    rinstructions = font_instructions.render("Press r to resume",True, (255,255,255))
    rinstructions_rect = rinstructions.get_rect(center = (int(display_width/2), int(display_height/1.3)))
    screen.blit(rinstructions, rinstructions_rect)

    final_score = "final score: " + str(play_score)
    score_announce = font_instructions.render(final_score, True, (255,255,255))
    score_announce_rect = score_announce.get_rect(center= (int(display_width/2), int (display_height/2)))
    screen.blit(score_announce, score_announce_rect)

    pygame.display.flip()
    while (end_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()
                if event.key == pygame.K_r:
                    end_game = False


screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("ping pong game")

screen.fill((0,150,0))
welcome_screen = pygame.font.Font(None, 30)
welcome = welcome_screen.render("Let's play pin_pon", True, (255,255,255))
welcome_rect = welcome.get_rect(center = (int(display_width/2), int(display_height/3)))

startmsg = welcome_screen.render("Hit 'y' to start, or autostart in 10 seconds", True, (255,255, 255))
startmsg_rect = startmsg.get_rect(center= (int(display_width/2), int(display_height/4)))

screen.blit(welcome, welcome_rect)
screen.blit(startmsg, startmsg_rect)
pygame.display.flip()
pygame.time.set_timer(pygame.USEREVENT, 10000)

timer_active = True
while (timer_active):
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            timer_active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                timer_active = False
randomize_start() 


while True:
    clock.tick(speed)

    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
        if paddle_y + paddle_height + 10 <= display_height:
            paddle_y += 10
    if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
        if paddle_y >= 0:
            paddle_y -= 10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((100, 80, 255))
    x += x_1
    y += y_1

    pygame.draw.rect(screen, (255, 0, 255), (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(screen, (255, 255, 0), (x, y), radius)
    if x < radius:
        game_over()
        randomize_start()
        x_1 = abs(x_1)
        play_score = 0

    if hit_back() or hit_paddle():
        x_1 *= -1
    if hit_sides():
        y_1 *= -1

    pygame.display.update()


# while True:
#     clock.tick(speed)

#     pressed_key = pygame.key.get_pressed()
#     if pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
#         if paddle_y + paddle_height + 10 <= display_height:
#             paddle_y += 10
#         if pressed_key[pygame.K_UP] or pressed_key[pygame.K_w]:
#             if paddle_y >= 0:
#                 paddle_y -= 10




#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit() 
#     screen.fill((0,0,0))
#     x+= x_1
#     y+= y_1

#     pygame.draw.rect(screen, (255,255,255), (paddle_x, paddle_y, paddle_width,paddle_height))
#     pygame.draw.circle(screen, (255,255,255), (x,y), radius )
#     if x < radius:
#         game_over()
#         randomize_start()
#         x_1 = abs(x_1)
#         play_score = 0

#     if hit_back() or hit_paddle():
#         x_1 *= -1
#     if hit_sides():
#         y_1 *= -1 
#     pygame.display.update() 






   









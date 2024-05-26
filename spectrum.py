import pygame
import random
import sys
import time
from maze_layout import *

level = 1
key_index = 0
current_cheese_score = 0
current_player_ammo = 0
current_player_color = (0,255,0)
def start_menu():
    pygame.init()
    start_box_running_2 = True
    start_box_running = True
    while start_box_running:
        # Constants
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        HIGHLIGHT_COLOR = (200, 200, 200)
        # Colors
        red = (255, 0, 0)
        dark_red = (139, 0, 0)
        light_red = (255, 99, 71)
        orange = (255, 165, 0)
        dark_orange = (255, 140, 0)
        light_orange = (255, 179, 71)
        yellow = (255, 255, 0)
        dark_yellow = (184, 134, 11)
        light_yellow = (255, 255, 153)
        green = (0, 255, 0)
        dark_green = (0, 100, 0)
        light_green = (144, 238, 144)
        blue = (0, 0, 255)
        dark_blue = (0, 0, 139)
        light_blue = (173, 216, 230)
        indigo = (75, 0, 130)
        dark_indigo = (54, 0, 93)
        light_indigo = (125, 60, 152)
        purple = (148, 0, 211)
        dark_violet = (128, 0, 128)
        light_violet = (204, 153, 255)
        # Neutral Colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        # Gray Colors
        gray = (128, 128, 128)
        dark_gray = (64, 64, 64)
        light_gray = (192, 192, 192)
        FONT_SIZE = 36

        # Initialize screen
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Set fullscreen
        pygame.display.set_caption("Game Menu")
        # Load background image
        # background_image = pygame.image.load("playerStuff\Cheese.PNG")  
        # background_image2 = pygame.image.load("playerStuff\Chicken.PNG")  
        # background_image2_width, background_image2_height = background_image2.get_size()
        # Function to draw text on the screen
        def draw_text(text, font, color, surface, x, y):
            text_obj = font.render(text, True, color)
            text_rect = text_obj.get_rect(center=(x, y))
            surface.blit(text_obj, text_rect)

        # Main game loop
        while start_box_running_2:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    # Check if any button is clicked
                    if play_button_rect.collidepoint(x, y):
                        print("Play button clicked")
                        return
                    elif leaderboards_button_rect.collidepoint(x, y):
                        leaderboard_menu()
                        print("LeaderBoards button clicked")
                    elif quit_button_rect.collidepoint(x, y):
                        print("Quit button clicked")
                        pygame.quit()
                        exit()

            # Clear the screen
            screen.fill(WHITE)
            # Draw background image
            # screen.blit(background_image, (0, 0))
            # screen.blit(background_image2, (screen_width - background_image2_width, screen_height - background_image2_height))
            pygame.draw.circle(screen, red, (screen_width // 3, screen_height // 10), screen_width // 20)
            pygame.draw.circle(screen, purple, (screen_width - (screen_width // 3), screen_height // 10), screen_width // 20)
            pygame.draw.circle(screen, orange, (screen_width // 4, screen_height // 2), screen_width // 20)
            pygame.draw.circle(screen, blue, (screen_width - (screen_width // 4), screen_height // 2), screen_width // 20)
            pygame.draw.circle(screen, yellow, (screen_width // 3, screen_height - (screen_height // 10)), screen_width // 20)
            pygame.draw.circle(screen, green, (screen_width - (screen_width // 3), screen_height - (screen_height // 10)), screen_width // 20)
            # Draw buttons with highlighting when mouse hovers over them
            button_width, button_height = 200, 100
            button_x = (screen_width - button_width) // 2
            button_padding = (screen_height // 6.5)

            # Define button rectangles
            play_button_rect = pygame.Rect(button_x, button_padding, button_width, button_height)
            leaderboards_button_rect = pygame.Rect(button_x, 2 * button_padding + button_height, button_width, button_height)
            quit_button_rect = pygame.Rect(button_x, 3 * button_padding + 2 * button_height, button_width, button_height)

            # Draw buttons
            pygame.draw.rect(screen, HIGHLIGHT_COLOR if play_button_rect.collidepoint(pygame.mouse.get_pos()) else BLACK, play_button_rect)
            pygame.draw.rect(screen, HIGHLIGHT_COLOR if leaderboards_button_rect.collidepoint(pygame.mouse.get_pos()) else BLACK, leaderboards_button_rect)
            pygame.draw.rect(screen, HIGHLIGHT_COLOR if quit_button_rect.collidepoint(pygame.mouse.get_pos()) else BLACK, quit_button_rect)

            # Draw button text
            font = pygame.font.Font(None, FONT_SIZE)
            draw_text("Play", font, WHITE, screen, screen_width // 2, button_padding + button_height // 2)
            draw_text("LeaderBoards", font, WHITE, screen, screen_width // 2, 2 * button_padding + 3 * button_height // 2)
            draw_text("Quit", font, WHITE, screen, screen_width // 2, 3 * button_padding + 5 * button_height // 2)

            # Update the display
            pygame.display.flip()

            # Limit frames per second
            pygame.time.Clock().tick(30)

def leaderboard_menu():
    pygame.mouse.set_visible(False)
    LB_running = True
    while LB_running:
        def timeconvert(elapsed_time):
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            # Print the elapsed time in the desired format
            time = "Elapsed Time: " f"{hours:02}:{minutes:02}:{seconds:02}"
            return time
        # Neutral Colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        # Gray Colors
        gray = (128, 128, 128)
        font = pygame.font.Font(None, 30)
        filelb = "Greenman\Leaderboard.txt"
        readfilelb = open(filelb,"r")
        lb_temp = readfilelb.read()
        LB = lb_temp.split(",")
        lb1 = LB[0]
        lb2 = LB[1]
        lb3 = LB[2]
        lb4 = LB[3]
        lb5 = LB[4]
        LB1 = str(timeconvert(int(round(float(lb1)))))
        LB2 = str(timeconvert(int(round(float(lb2)))))
        LB3 = str(timeconvert(int(round(float(lb3)))))
        LB4 = str(timeconvert(int(round(float(lb4)))))
        LB5 = str(timeconvert(int(round(float(lb5)))))
       
        screen_info = pygame.display.Info()
        screen_width = screen_info.current_w
        screen_height = screen_info.current_h
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Set fullscreen
        box_width = 2*screen_width // 3
        box_height = 2*screen_height // 3
        box_x = (screen_width - box_width) // 2
        box_y = (screen_height - box_height) // 2
        pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
        # Calculate the position to center the text
        def draw_text(text, font, color, surface, x, y):
            text_obj = font.render(text, True, color)
            text_rect = text_obj.get_rect(center=(x, y))
            surface.blit(text_obj, text_rect)
        draw_text(LB1, font, white, screen, screen_width // 2, screen_height // 4)
        draw_text(LB2, font, white, screen, screen_width // 2, screen_height // 2 - screen_height // 8)
        draw_text(LB3, font, white, screen, screen_width // 2, screen_height // 2)
        draw_text(LB4, font, white, screen, screen_width // 2, screen_height // 2 + screen_height // 8)
        draw_text(LB5, font, white, screen, screen_width // 2, screen_height - screen_height // 4)
        pygame.display.flip()
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.mouse.set_visible(True)
            LB_running = False
        # Limit frames per second
        pygame.time.Clock().tick(10)
def maze_level(maze_number):
    string1 = "maze"
    maze_string = string1 + str(maze_number)
#total_score = 0
def switch_maze(maze_index, player_ammo, player_color, cheese_score):
    global current_player_ammo
    global maze_str
    global maze
    global current_player_color
    global current_cheese_score
    current_cheese_score = cheese_score
    current_player_color = player_color
    current_player_ammo = player_ammo
    if maze_index == 1:
        maze1 = [list(row) for row in maze_layout1]
        maze = maze1
        maze_str = "maze1"
        main_game_loop(maze1)
    if maze_index == 2:
        maze2 = [list(row) for row in maze_layout2]
        maze = maze2
        maze_str = "maze2"
        main_game_loop(maze2)
    elif maze_index == 3:
        maze3 = [list(row) for row in maze_layout3]
        maze = maze3
        maze_str = "maze3"
        main_game_loop(maze3)
    elif maze_index == 4:
        maze4 = [list(row) for row in maze_layout4]
        maze = maze4
        maze_str = "maze4"
        main_game_loop(maze4)
    elif maze_index == 5:
    #Traingle bob map
        maze_trianglebob = [list(row) for row in maze_layout_trianglebob]
        maze = maze_trianglebob
        maze_str = "maze_trianglebob"
        main_game_loop(maze_trianglebob)
    elif maze_index == 100:
        maze100 = [list(row) for row in maze_layout100]
        maze = maze100
        maze_str = "maze100"
        main_game_loop(maze100)
    


# Function to generate random teleport points
def generate_random_teleport_points(maze, num_points):
    walkable_spaces = []
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == ".":
                walkable_spaces.append((row, col))
    if len(walkable_spaces) < num_points:
        return None
    return random.sample(walkable_spaces, num_points)

# Projectile class
class Projectile:
    def __init__(self, x, y, direction, color):
        self.x = x
        self.y = y
        self.direction = direction
        self.color = color
        self.speed = 60  # Adjust the speed as needed
def get_mouse_direction(mouse_pos, player_pos):
    dx = mouse_pos[0] - player_pos[0]
    dy = mouse_pos[1] - player_pos[1]
    if abs(dx) > abs(dy):
        return "right" if dx > 0 else "left"
    else:
        return "down" if dy > 0 else "up"

# Get the current time when the script starts
start_time = time.time()

def main_game_loop(maze):
    # Initialize Pygame's mixer module
    pygame.mixer.init()
    # Load the music file
    pygame.mixer.music.load("Greenman\LSdenstist.mp3")
    pygame.mixer.music.set_volume(0.5)
    # Play the music on loop
    pygame.mixer.music.play(-1)
    
    # Initialize the player's score
    score = 0
    pygame.mouse.set_visible(False)
    # Initialize Pygame
    pygame.init()

    # Hide the mouse cursor
    
    # Get the current screen dimensions
    screen_info = pygame.display.Info()
    screen_width = screen_info.current_w
    screen_height = screen_info.current_h
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Set fullscreen
    pygame.display.set_caption("Adventures of Spectrum")
    # Colors
    red = (255, 0, 0)
    dark_red = (139, 0, 0)
    light_red = (255, 99, 71)
    orange = (255, 165, 0)
    dark_orange = (255, 140, 0)
    light_orange = (255, 179, 71)
    yellow = (255, 255, 0)
    dark_yellow = (184, 134, 11)
    light_yellow = (255, 255, 153)
    green = (0, 255, 0)
    dark_green = (0, 100, 0)
    light_green = (144, 238, 144)
    blue = (0, 0, 255)
    dark_blue = (0, 0, 139)
    light_blue = (173, 216, 230)
    indigo = (75, 0, 130)
    dark_indigo = (54, 0, 93)
    light_indigo = (125, 60, 152)
    purple = (148, 0, 211)
    dark_violet = (128, 0, 128)
    light_violet = (204, 153, 255)
    # Neutral Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    # Gray Colors
    gray = (128, 128, 128)
    dark_gray = (64, 64, 64)
    light_gray = (192, 192, 192)
    
    
    # Calculate the size of each cell and the number of visible rows/columns
    cell_size_number = 25
    cell_size = screen_width // cell_size_number
    num_visible_rows = 20
    num_visible_cols = 20

    #print(cell_size)
    # player (Pacman)
    player_radius = cell_size // 4
    player_speed = int(cell_size)
    player_x = (cell_size * (len(maze[0]) // 2)) + (cell_size // 2)
    player_y = 0
    green_trail = []
    green_projectiles = []
    player_ammo = current_player_ammo #this is for the length of the trail and for projectiles
    cheese_score = current_cheese_score
    # Redman (Bot)
    redman_radius = cell_size // 2
    redman_speed = int(cell_size)
    redman_x = (cell_size * (len(maze[0]) // 2)) - (cell_size // 2)
    redman_y = (cell_size * (len(maze) // 2)) + (cell_size // 2)
    redman_color = red
    red_trail = []  # List to store the red trail position
    redman_life = 0
    # Chicken (Bot)
    chicken_radius = cell_size // 2 
    chicken_speed = int(cell_size)
    chicken_x = (cell_size * 32) - (cell_size // 2)
    chicken_y = (cell_size * 18) - (cell_size // 2)

    #Gray_stone (Bot)
    gray_stone_x = (cell_size * 32) - (cell_size // 2)
    gray_stone_y = (cell_size * 24) - (cell_size // 2)
    
    rocket_score = 0

    #print(maze_str)
    last_movement_direction = None
    projectile_radius = cell_size // 5
    projectile_cooldown = 300  # Cooldown time in milliseconds (adjust as needed)
    last_shot_time = pygame.time.get_ticks()  # Initialize the last shot time

    key_score = 0

    # Find the lowest available starting position for the player
    for row in range(len(maze) - 1, -1, -1):
        if maze[row][player_x // cell_size] != "#" and maze[row][player_x // cell_size] != "T":
            player_y = row * cell_size + cell_size // 2
            break

    # Generate random teleport points
    num_teleport_points = 100  # Change this to the number of teleport points you want
    teleport_points = generate_random_teleport_points(maze, num_teleport_points)
    if teleport_points is None:
        print("Not enough walkable spaces to generate teleport points.")
        pygame.quit()
        sys.exit()
    current_tp_index = 0

    # Game loop
    clock = pygame.time.Clock()
    running = True
    current_maze = maze
    #print(maze)
    def get_space_in_direction(maze, x, y, direction):
        if direction == "up":
            face_x, face_y = x, y - (cell_size)
        elif direction == "down":
            face_x, face_y = x, y + (cell_size)
        elif direction == "left":
            face_x, face_y = x - (cell_size), y
        elif direction == "right":
            face_x, face_y = x + (cell_size), y
        else:
           return None  # Invalid direction
            
        # Check if the new coordinates are within the maze boundaries
        if 0 <= face_x // cell_size < (len(maze)) and 0 <= face_y // cell_size < len(maze):
            return maze[face_y // cell_size][face_x // cell_size]
        #else:
            # print("Error In get_space function")  # Coordinates are outside the maze
            # print(face_x, face_y, direction)
# Get the space in the 'right' direction from (3, 1)
# result = get_space_in_direction(current_maze, 3, 1, 'right')
# print(result)  # This will print '.' since it's an empty space in that direction.
    def rocket_special():
         # Body of the rocket
        pygame.draw.rect(screen, gray, (x + (cell_size // 4), y + (cell_size // 3), cell_size // 2, cell_size - (cell_size // 3)))
            # Top of the rocket (triangle)
        top_left = (x + (cell_size // 4), y + (cell_size // 3))
        top_right = (x + 3 * (cell_size // 4), y + (cell_size // 3))
        bottom = (x + cell_size // 2, y)
        pygame.draw.polygon(screen, gray, [top_left, top_right, bottom])
        # Rocket's wings (triangles)
        wing1_top = (x +(cell_size // 2), y + (cell_size // 2))
        wing1_bottom_left = (x, y + cell_size)
        wing1_bottom_right = (x +(cell_size // 2), y + cell_size)
        pygame.draw.polygon(screen, gray, [wing1_top, wing1_bottom_left, wing1_bottom_right])
        wing2_top = (x + (cell_size // 2), y + (cell_size // 2))
        wing2_bottom_left = (x + (cell_size // 2), y + cell_size)
        wing2_bottom_right = (x + (cell_size - 1), y + cell_size)
        pygame.draw.polygon(screen, gray, [wing2_top, wing2_bottom_left, wing2_bottom_right])
    #write to leaderboard file
    def write_leaderboard(elapsed_time):
        #read and write leaderboard
        file = "C:\VSCode\GreenmanStuff\Leaderboard.txt"
        readfile = open(file, "r")
        checkNum = elapsed_time
        LE_temp = readfile.read()
        LE = LE_temp.split(",")
        for i in range(5):
            if int(round(float(LE[i]))) > int(round(float(checkNum))):
                replace_num = i
        if int(round(float(checkNum))) < int(round(float(LE[4]))):
            LE.pop(replace_num)
            LE.append(checkNum)
        LE = [int(round(float((x)))) for x in LE]
        LE.sort()
        LES_temp = str(LE)
        LES = LES_temp.strip("[]")
        readfile.close()

        writefile = open(file, "w")
        writefile.writelines(LES)
        writefile.close()
    def game_over():
        print("Game Over")
        end_time = time.time()
        elapsed_time = end_time - start_time
        # Convert elapsed time to hours, minutes, and seconds
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        # Print the elapsed time in the desired format
        print("Elapsed Time:", f"{hours:02}:{minutes:02}:{seconds:02}")
        
        # Display "Game Over" message
        font = pygame.font.Font(None, 50)
        message = font.render("Game Over", True, red)
        # Create a black rectangular text box with white outline
        box_width = 900
        box_height = 300
        box_x = (screen_width - box_width) // 2
        box_y = (screen_height - box_height) // 2
        pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
        # Calculate the position to center the text
        text_x = box_x + (box_width - message.get_width()) // 2
        text_y = box_y + (box_height - message.get_height()) // 2
        # Blit the message text onto the screen
        screen.blit(message, (text_x, text_y))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait for 3 seconds                    
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
        quit()
    def You_Won():
        print("You Won")
        end_time = time.time()
        elapsed_time = end_time - start_time
        # Convert elapsed time to hours, minutes, and seconds
        hours = int(elapsed_time // 3600)
        minutes = int((elapsed_time % 3600) // 60)
        seconds = int(elapsed_time % 60)
        # Print the elapsed time in the desired format
        print("Elapsed Time:", f"{hours:02}:{minutes:02}:{seconds:02}")
        #read and write to leaderboard
        write_leaderboard(elapsed_time)
        # Display "Game Over" message
        font = pygame.font.Font(None, 50)
        message = font.render("You Won", True, yellow)
        # Create a black rectangular text box with white outline
        box_width = 900
        box_height = 300
        box_x = (screen_width - box_width) // 2
        box_y = (screen_height - box_height) // 2
        pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
        # Calculate the position to center the text
        text_x = box_x + (box_width - message.get_width()) // 2
        text_y = box_y + (box_height - message.get_height()) // 2
        # Blit the message text onto the screen
        screen.blit(message, (text_x, text_y))
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait for 3 seconds                    
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()
        quit()
    def flew_to_close():
        print("You Flew To Close Too The Sun")
        # Display "Game Over" message
        font = pygame.font.Font(None, 40)
        message = font.render("You Flew Too Close To The Sun", True, yellow)
        # Create a black rectangular text box with white outline
        box_width = 600
        box_height = 200
        box_x = (screen_width - box_width) // 2
        box_y = (screen_height - box_height) // 2
        pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
        # Calculate the position to center the text
        text_x = box_x + (box_width - message.get_width()) // 2
        text_y = box_y + (box_height - message.get_height()) // 2
        # Blit the message text onto the screen
        screen.blit(message, (text_x, text_y))
        pygame.display.flip()
        pygame.time.wait(2000)
        player_ammo = 0
        cheese_score = 0
        switch_maze(1, player_ammo, player_color, cheese_score)
    def display_menu(screen):
        menu_running = True
        running = True
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Draw your menu here
            # You can use pygame.draw.rect(), pygame.draw.text(), etc.
            # Display "Game Over" message
            font = pygame.font.Font(None, 36)
            message = font.render("Main Menu", True, green)
            message2 = font.render("Press (p) to resume", True, white)
            message3 = font.render("Press (z) to quit", True, white)
            # Create a black rectangular text box with white outline
            box_width = 900
            box_height = 300
            box_x = (screen_width - box_width) // 2
            box_y = (screen_height - box_height) // 2
            pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
            pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
            # Calculate the position to center the text
            text_x = box_x + (box_width - message.get_width()) // 2
            text_x2 = box_x + (box_width - message2.get_width()) // 2
            text_x3 = box_x + (box_width - message3.get_width()) // 2
            text_y = box_y + (box_height - message.get_height()) // 2
            text_y2 = text_y + message2.get_height()
            text_y3 = text_y2 + message3.get_height()

            # Blit the message text onto the screen
            screen.blit(message, (text_x, text_y))
            screen.blit(message2, (text_x2, text_y2))
            screen.blit(message3, (text_x3, text_y3))            
            pygame.display.flip()
            pygame.display.update()
            # Handle key events
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                menu_running = False
            if keys[pygame.K_z]:
                game_over()
        return running  # Return the game state flag
    def text_box(talker_color,message):
        text_box_running = True
        running = True
        while text_box_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Draw your menu here
            font = pygame.font.Font(None, 36)
            fixed_message = font.render(message, True, talker_color)
           # Create a black rectangular text box with white outline
            box_width = num_visible_cols * cell_size
            box_height = 3*cell_size
            box_x = 0
            box_y = (num_visible_rows * cell_size) - box_height
            pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
            pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
            # Calculate the position to center the text
            text_x = box_x + (box_width - fixed_message.get_width()) // 2
            text_y = box_y + (box_height - fixed_message.get_height()) // 2
            # Blit the message text onto the screen
            screen.blit(fixed_message, (text_x, text_y))
            pygame.display.flip()
            pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                text_box_running = False
            

        return running
    def question_box(talker_color,message, first_message, second_message):
        question_box_running = True
        running = True
        while question_box_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Draw your menu here
            font = pygame.font.Font(None, 36)
            fixed_message = font.render(message, True, talker_color)
           # Create a black rectangular text box with white outline
            box_width = num_visible_cols * cell_size
            box_height = 3*cell_size
            box_x = 0
            box_y = (num_visible_rows * cell_size) - box_height
            pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
            pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
            # Calculate the position to center the text
            text_x = box_x + (box_width - fixed_message.get_width()) // 2
            text_y = box_y + (box_height - fixed_message.get_height()) // 2
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                question_box_running = False
                return option 
            if keys[pygame.K_y]:
                option =1
                text_box(talker_color, first_message)
            if keys[pygame.K_n]:
                option = 2
                text_box(talker_color, second_message)
            
            screen.blit(fixed_message, (text_x, text_y))
            pygame.display.flip()
            pygame.display.update()
            

        return running

    def player_color_selection_box():
        question_box_running = True
        running = True
        while question_box_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            # Draw your menu here
            message = "Red(1), Orange(2), Yellow(3), Green(4), Blue(5), Purple(6)."
            talker_color = white
            font = pygame.font.Font(None, 36)
            fixed_message = font.render(message, True, talker_color)
           # Create a black rectangular text box with white outline
            box_width = num_visible_cols * cell_size
            box_height = 3*cell_size
            box_x = 0
            box_y = (num_visible_rows * cell_size) - box_height
            pygame.draw.rect(screen, black, (box_x, box_y, box_width, box_height))
            pygame.draw.rect(screen, white, (box_x, box_y, box_width, box_height), 3)  # White outline
            # Calculate the position to center the text
            text_x = box_x + (box_width - fixed_message.get_width()) // 2
            text_y = box_y + (box_height - fixed_message.get_height()) // 2
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                text_box(talker_color, "You are now red.")
                current_player_color = red
                question_box_running = False
                return current_player_color
            if keys[pygame.K_2]:
                text_box(talker_color, "You are now orange.")
                current_player_color = orange
                question_box_running = False
                return current_player_color
            if keys[pygame.K_3]:
                text_box(talker_color, "You are now yellow.")
                current_player_color = yellow
                question_box_running = False
                return current_player_color
            if keys[pygame.K_4]:
                text_box(talker_color, "You are now green.")
                current_player_color = green
                question_box_running = False
                return current_player_color
            if keys[pygame.K_5]:
                text_box(talker_color, "You are now blue.")
                current_player_color = blue
                question_box_running = False
                return current_player_color
            if keys[pygame.K_6]:
                text_box(talker_color, "You are now purple.")
                current_player_color = purple
                question_box_running = False
                return current_player_color
            
            screen.blit(fixed_message, (text_x, text_y))
            pygame.display.flip()
            pygame.display.update()

        return running
    player_color = current_player_color 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    # Check if the player is on a key e (k)
                    if current_maze[player_y // cell_size][player_x // cell_size] == "k":
                        key_score += 1

                        current_maze[player_y // cell_size][player_x // cell_size] = "."
                    # Check if the player is on a door space (K) with the key
                    if current_maze[player_y // cell_size][player_x // cell_size] == "K" and key_score == 0:
                        text_box(purple, "Need purple circle to advance.")
                    if current_maze[player_y // cell_size][player_x // cell_size] == "K" and key_score > 0:
                        global level
                        level += 1
                        switch_maze(level, player_ammo, player_color, cheese_score)
                if player_color == blue: 
                    if player_ammo != 0:
                        if event.key == pygame.K_t:
                            current_tp_index = (current_tp_index + 1) % len(teleport_points)
                            new_tp_row, new_tp_col = teleport_points[current_tp_index]
                            while current_maze[new_tp_row][new_tp_col] != ".":
                                current_tp_index = (current_tp_index + 1) % len(teleport_points)
                                new_tp_row, new_tp_col = teleport_points[current_tp_index]
                            player_x = new_tp_col * cell_size + cell_size // 2
                            player_y = new_tp_row * cell_size + cell_size // 2
                            player_ammo -= 1
                if maze_str == "maze3":
                    if event.key == pygame.K_e:
                        if current_maze[player_y // cell_size][player_x // cell_size] == "|":
                            rocket_score += 1
                            current_maze[player_y // cell_size][player_x // cell_size] = "."
                        
                # Interaction with chicken and no cheese
                if maze_str == "maze1":
                    if event.key == pygame.K_e:
                        # Check if the player is on a key e (k)
                        if current_maze[player_y // cell_size][player_x // cell_size] == "C":
                            cheese_score += 1
                            current_maze[player_y // cell_size][player_x // cell_size] = "."
                    if event.key == pygame.K_e and (
                        abs(player_x - chicken_x) < (cell_size*2) and abs(player_y - chicken_y) < (cell_size*2)):
                        if cheese_score == 0:
                            text_box(yellow, "Chicken with no cheese, cheese with no chicken.")  # Replace this with code to display a text box
                    if event.key == pygame.K_e and (
                        abs(player_x - chicken_x) < (cell_size*2) and abs(player_y - chicken_y) < (cell_size*2)):
                        if cheese_score > 0:
                            text_box(yellow, "Chicken with cheese, cheese with chicken, the balance is restored, and the chicken cheese is finally free.")  # Replace this with code to display a text box
                #Gray Stone (Bot) that asks questions to pass

                    if event.key == pygame.K_e and (
                        abs(player_x - gray_stone_x) < (cell_size*2) and abs(player_y - gray_stone_y) < (cell_size*2)):
                            option_color = question_box(gray, "Would you like to change colors?                      (y or n)", "Here are your options.", "Come back if you change your mind.")
                            if option_color == 1:
                                player_color = player_color_selection_box()

                elif current_maze[player_y // cell_size][player_x // cell_size] == "S":
                    print("I am speed")
                


        if player_y < 0:
            current_maze = maze
            player_y = (len(current_maze) - 1) * cell_size - cell_size // 2
        elif player_y >= len(current_maze) * cell_size:
            current_maze = maze
            player_y = cell_size // 2
        
        # Update the green trail list with the current position of the player
        green_trail.append((player_x, player_y))
        # Ensure player_ammo doesn't go below 0
        player_ammo = max(player_ammo, 0)

        current_time = pygame.time.get_ticks()  # Get the current time
        # Handle user input
        if 0 <= player_y // cell_size < len(current_maze) and 0 <= player_x // cell_size < len(current_maze[0]):
            if current_maze[player_y // cell_size][player_x // cell_size] != "#":
            # Your movement logic here
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x // cell_size - 1 >= 0 and current_maze[player_y // cell_size][player_x // cell_size - 1] != "#" and current_maze[player_y // cell_size][player_x // cell_size - 1] != "&":
                    player_x -= player_speed
                    last_movement_direction = "left"
                if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x // cell_size + 1 < len(current_maze[0]) and current_maze[player_y // cell_size][player_x // cell_size + 1] != "#" and current_maze[player_y // cell_size][player_x // cell_size + 1] != "&":
                    player_x += player_speed
                    last_movement_direction = "right"
                if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y // cell_size - 1 >= 0 and current_maze[player_y // cell_size - 1][player_x // cell_size] != "#" and player_y // cell_size - 1 >= 0 and current_maze[player_y // cell_size - 1][player_x // cell_size] != "&":
                    player_y -= player_speed
                    last_movement_direction = "up"
                if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_y // cell_size + 1 < len(current_maze) and current_maze[player_y // cell_size + 1][player_x // cell_size] != "#" and current_maze[player_y // cell_size + 1][player_x // cell_size] != "&":
                    player_y += player_speed
                    last_movement_direction = "down"
                if current_time - last_shot_time >= projectile_cooldown:
                    if player_ammo > 0:
                        if player_color == green:
                            if keys[pygame.K_t]:
                                if last_movement_direction:
                                    new_projectile = Projectile(player_x, player_y, last_movement_direction, player_color)
                                    green_projectiles.append(new_projectile)
                                else:
                                    new_projectile = Projectile(player_x, player_y, "up", player_color)
                                    green_projectiles.append(new_projectile)
                                # Update the last shot time
                                last_shot_time = current_time
                                player_ammo -= 1
                if keys[pygame.K_ESCAPE]:
                    # Calculate the elapsed time when the game loop ends
                    #print(current_player_ammo)
                    #game_over()
                    display_menu(screen)
                if maze_str == "maze1" or maze_str == "maze2" or maze_str == "maze3":
                    if redman_life == 0:
                        # if random.randint(0, 1) == 0:  # 50% chance to move
                        redman_directions = ["up", "down", "left", "right"]  # Up, Down, Left, Right
                        redman_direction = random.choice(redman_directions)
                        redman_face = get_space_in_direction(maze, redman_x, redman_y, redman_direction)
                        if redman_face != "#" and redman_face != "D":
                            if redman_direction == "up":
                                redman_new_y = redman_y - redman_speed
                                redman_new_x = redman_x
                            elif redman_direction == "down":
                                redman_new_y = redman_y + redman_speed
                                redman_new_x = redman_x
                            elif redman_direction == "left":
                                redman_new_x = redman_x - redman_speed
                                redman_new_y = redman_y
                            elif redman_direction == "right":
                                redman_new_x = redman_x + redman_speed
                                redman_new_y = redman_y
                            if maze_str == "maze1" or maze_str == "maze2" or maze_str == "maze3":
                                if 0 <= redman_new_y // cell_size < len(current_maze) and 0 <= redman_new_x // cell_size < len(current_maze[0]) and current_maze[redman_new_y // cell_size][redman_new_x // cell_size] != "#":
                                    redman_x = redman_new_x
                                    redman_y = redman_new_y
                                else:
                                    redman_x = 2*(cell_size) - (cell_size // 2)
                                    redman_y = 2*(cell_size) - (cell_size // 2)
                            
                    
        
        # Update the red trail list with the current position of the redman
        red_trail.append((redman_x, redman_y))

            # Keep the red trail list's length no more than 10
        if len(red_trail) > 20:
            red_trail.pop(0)
        # Calculate the top-left position of the visible area
        # Calculate the top-left position of the visible area
        top_row = max(0, min((player_y // cell_size) - num_visible_rows // 2, len(current_maze) - num_visible_rows))
        left_col = max(0, min((player_x // cell_size) - num_visible_cols // 2, len(current_maze[0]) - num_visible_cols))
        # Calculate the number of visible rows and columns based on screen dimensions and player's position
        num_visible_rows = screen_height // cell_size
        num_visible_cols = screen_width // cell_size        
        # Clear the screen
        screen.fill(black)
        # Keep the green trail list's length no more than 20
        if len(green_trail) > player_ammo:
            green_trail.pop(0)
    # Draw the visible portion of the maze
        for row in range(top_row, top_row + num_visible_rows):
            for col in range(left_col, left_col + num_visible_cols):
                x = (col - left_col) * cell_size
                y = (row - top_row) * cell_size

                # Check if the row and column indices are within the valid range
                if 0 <= row < len(current_maze) and 0 <= col < len(current_maze[row]):
                    if current_maze[row][col] == "k":
                        pygame.draw.circle(screen, purple, (x + cell_size // 2, y + cell_size // 2), cell_size // 8)
                    elif current_maze[row][col] == "K":
                        pygame.draw.rect(screen, purple, (x, y, cell_size, cell_size))
                    elif current_maze[row][col] == "#":
                        pygame.draw.rect(screen, white, (x, y, cell_size, cell_size))
                    elif current_maze[row][col] == ".":
                        pygame.draw.rect(screen, black, (x, y, cell_size, cell_size))
                    elif current_maze[row][col] == "T":
                        pygame.draw.rect(screen, blue, (x, y, cell_size, cell_size))
                    elif current_maze[row][col] == "&":
                        pygame.draw.rect(screen, red, (x, y, cell_size, cell_size))
                    elif current_maze[row][col] == "o":
                        pygame.draw.circle(screen, yellow, (x + cell_size // 2, y + cell_size // 2), cell_size // 8)
                    elif current_maze[row][col] == "S":
                        pygame.draw.rect(screen, yellow, (x, y, cell_size, cell_size))
                    elif current_maze[row][col] == "D":
                        pygame.draw.rect(screen,light_blue, (x, y, cell_size, cell_size))
                    elif current_maze[row][col] == "C":
                        if maze_str == "maze1" or (maze_str == "maze_trianglebob" and cheese_score != 0):
                            pygame.draw.rect(screen,yellow, (x + (cell_size // 4), y + (cell_size // 4), (cell_size // 2), (cell_size // 2)))
                            pygame.draw.circle(screen, white, (x + cell_size // 3, y + cell_size // 3), cell_size // 11)
                            pygame.draw.circle(screen, white, (x + cell_size // 3, y + 2*cell_size // 3), cell_size // 11)
                            pygame.draw.circle(screen, white, (x + 2*cell_size // 3, y + 2*cell_size // 3), cell_size // 11)
                            pygame.draw.circle(screen, white, (x + 2*cell_size // 3, y + cell_size // 3), cell_size // 11)
                            pygame.draw.circle(screen, white, (x + cell_size // 2, y + cell_size // 2), cell_size // 11)
                    elif maze_str == "maze3":
                        if rocket_score == 0:
                            if current_maze[row][col] == "|":
                                rocket_special()
                    elif maze_str == "maze1":
                        #if gray_stone_score == 0:
                            if current_maze[row][col] == "G":
                                pygame.draw.rect(screen, gray, (x ,y ,cell_size ,cell_size))
                                pygame.draw.rect(screen, white, (x + cell_size // 5 ,y + cell_size // 4 ,cell_size // 4 ,cell_size // 4))
                                pygame.draw.rect(screen, white, (x + cell_size - (cell_size // 3 + cell_size // 10) ,y + cell_size // 4 ,cell_size // 4 ,cell_size // 4))
                                pygame.draw.rect(screen, white, (x + cell_size // 4, y + cell_size - (cell_size // 4), cell_size // 2 , cell_size // 9))
                            #triangleBob
                            elif current_maze[row][col] == "g":
                                                    pygame.draw.polygon(screen, yellow, [(x, y + cell_size), (x + cell_size, y + cell_size), (x + (cell_size // 2), y) ])
                                                    pygame.draw.circle(screen, white, (x + cell_size // 2, y + cell_size // 2), cell_size // 4)
                                                    pygame.draw.circle(screen, black, (x + cell_size // 2, y + cell_size // 2), cell_size // 4, 2)

                                                    if (player_x // cell_size) > col and (player_y // cell_size) == row:
                                                        eye_pos = (x + (cell_size  - cell_size*0.4), y + cell_size // 2)
                                                        #right
                                                    elif (player_x // cell_size) < col and (player_y // cell_size) == row:
                                                        eye_pos = ( x + cell_size*0.4, y + cell_size // 2)
                                                        #left
                                                    elif (player_x // cell_size) == col and (player_y // cell_size) < row:
                                                        eye_pos = (x + cell_size // 2, y + cell_size*0.4)
                                                        #up
                                                    elif (player_x // cell_size) == col and (player_y // cell_size) > row:
                                                        eye_pos = (x + cell_size // 2, y + (cell_size - cell_size*0.4))
                                                        #down
                                                    elif (player_x // cell_size) > col and (player_y // cell_size) < row:
                                                        eye_pos = ( x + (cell_size - cell_size*0.45), y + cell_size*0.45)
                                                        #upright
                                                    elif (player_x // cell_size) < col and (player_y // cell_size) < row:
                                                        eye_pos = ( x + cell_size*0.45, y + cell_size*0.45)
                                                        #upleft
                                                    elif (player_x // cell_size) > col and (player_y // cell_size) > row:
                                                        eye_pos = ( x + (cell_size - cell_size*0.45), y + (cell_size - cell_size*0.45))
                                                        #downright
                                                    elif (player_x // cell_size) < col and (player_y // cell_size) > row:
                                                        eye_pos = ( x + cell_size*0.45, y + (cell_size - cell_size*0.45))
                                                        #downleft
                                                    else:
                                                        eye_pos = (x + cell_size // 2, y + cell_size // 2)
                                                        

                                                    pygame.draw.circle(screen, black, eye_pos, cell_size // 8)
                                                    pygame.draw.rect(screen, black, (x + cell_size // 4, y + (cell_size - (cell_size // 5)), cell_size // 2, cell_size // 8))
        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if cheese_score != 2:
                    if maze_str == "maze_trianglebob":
                        x = (col - left_col) * cell_size
                        y = (row - top_row) * cell_size
                        trianglebob_real_x = 20*cell_size + (cell_size // 2)
                        trianglebob_real_y = 16*cell_size + (cell_size // 2)
                        
                        if current_maze[row][col] == "g":
                            trianglebob_eye_x = x - 10*cell_size + (cell_size // 2)
                            trianglebob_eye_y = y - 7*cell_size + cell_size // 2
                            pygame.draw.polygon(screen, yellow, [(x - 20*cell_size, y + cell_size), (x + cell_size, y + cell_size), (x - 10*cell_size + (cell_size // 2), y - 13*cell_size) ])
                            pygame.draw.circle(screen, white, (trianglebob_eye_x, trianglebob_eye_y), cell_size * 3)
                            pygame.draw.circle(screen, black, (trianglebob_eye_x, trianglebob_eye_y), cell_size * 3, 2)

                            if (player_x // cell_size) > (trianglebob_real_x // cell_size) and (player_y // cell_size) == (trianglebob_real_y // cell_size):
                                eye_pos = (trianglebob_eye_x + cell_size, trianglebob_eye_y)
                                #right
                            elif (player_x // cell_size) < (trianglebob_real_x // cell_size) and (player_y // cell_size) == (trianglebob_real_y // cell_size):
                                eye_pos = ( trianglebob_eye_x - cell_size, trianglebob_eye_y)
                                #left
                            elif (player_x // cell_size) == (trianglebob_real_x // cell_size) and (player_y // cell_size) < (trianglebob_real_y // cell_size):
                                eye_pos = (trianglebob_eye_x, trianglebob_eye_y - cell_size)
                                #up
                            elif (player_x // cell_size) == (trianglebob_real_x // cell_size) and (player_y // cell_size) > (trianglebob_real_y // cell_size):
                                eye_pos = (trianglebob_eye_x, trianglebob_eye_y + cell_size)
                                #down
                            elif (player_x // cell_size) > (trianglebob_real_x // cell_size) and (player_y // cell_size) < (trianglebob_real_y // cell_size):
                                eye_pos = ( trianglebob_eye_x + (2*cell_size // 3), trianglebob_eye_y - (2*cell_size // 3))
                                #upright
                            elif (player_x // cell_size) < (trianglebob_real_x // cell_size) and (player_y // cell_size) < (trianglebob_real_y // cell_size):
                                eye_pos = (trianglebob_eye_x - (2*cell_size // 3), trianglebob_eye_y - (2*cell_size // 3))
                                #upleft
                            elif (player_x // cell_size) > (trianglebob_real_x // cell_size) and (player_y // cell_size) > (trianglebob_real_y // cell_size):
                                eye_pos = ( trianglebob_eye_x + (2*cell_size // 3), trianglebob_eye_y + (2*cell_size // 3))
                                #downright
                            elif (player_x // cell_size) < (trianglebob_real_x // cell_size) and (player_y // cell_size) > (trianglebob_real_y // cell_size):
                                eye_pos = ( trianglebob_eye_x - (2*cell_size // 3), trianglebob_eye_y + (2*cell_size // 3))
                                #downleft
                            else:
                                eye_pos = (trianglebob_eye_x, trianglebob_eye_y)
                                
                            #eye_pos = (trianglebob_eye_x, trianglebob_eye_y)
                            pygame.draw.circle(screen, black, eye_pos, cell_size *2 )
                            pygame.draw.rect(screen, black, (trianglebob_eye_x - 5*cell_size, trianglebob_eye_y + 6*cell_size, cell_size*10, cell_size))
            # Update player projectiles positions and draw them
            # Update and draw player projectiles
        for projectile in green_projectiles:
            if projectile.direction == "up":
                projectile.y -= projectile.speed
            elif projectile.direction == "down":
                projectile.y += projectile.speed
            elif projectile.direction == "left":
                projectile.x -= projectile.speed
            elif projectile.direction == "right":
                projectile.x += projectile.speed

            # Check if the projectile is still within the bounds of the map
            if 0 <= projectile.x < len(current_maze[0]) * cell_size and 0 <= projectile.y < len(current_maze) * cell_size:
                # Calculate the projectile's position relative to the visible area
                projectile_screen_x = projectile.x - left_col * cell_size
                projectile_screen_y = projectile.y - top_row * cell_size

                row = int(projectile.y / cell_size)
                col = int(projectile.x / cell_size)
                # Draw the projectile with its color and a white outline
                pygame.draw.circle(screen, projectile.color, (projectile_screen_x, projectile_screen_y), projectile_radius)
                pygame.draw.circle(screen, white, (projectile_screen_x, projectile_screen_y), projectile_radius, 2)
                projectile_facing = get_space_in_direction(maze, projectile.x // cell_size, projectile.y // cell_size, last_movement_direction)
                # print(projectile_facing)  # This will print
                if maze[row][col] == "&":
                    maze[row][col] = "."
                    green_projectiles.remove(projectile)

                if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == "#":
                    green_projectiles.remove(projectile)
            else:
                # If projectile is out of bounds, remove it from the list
                green_projectiles.remove(projectile)
            # Calculate the distance between the projectile and redman
            distance = ((projectile.x - redman_x) ** 2 + (projectile.y - redman_y) ** 2) ** 0.5
            if distance < projectile_radius + redman_radius:
                # Collision detected, reset redman
                #print("test hit redman")
                redman_x = (cell_size * (len(maze[0]) // 2)) - (cell_size // 2)
                redman_y = (cell_size * (len(maze) // 2)) + (cell_size // 2)
                #reset_redman()
                # Remove the projectile
                green_projectiles.remove(projectile)
            if maze_str == "maze3":
                if rocket_score != 0:
                    if distance < projectile_radius + redman_radius:
                        redman_x = (cell_size * (len(maze[0]) // 2)) - (cell_size // 2)
                        redman_y = (cell_size * (len(maze) // 2)) + (cell_size // 2)
                        # Remove the projectile
                        redman_life = 1
                        key_score += 1

         # Keep the green trail list's length no more than 20
        if len(green_trail) > player_ammo:
            green_trail.pop(0)
        # Draw the green trail
        for x, y in green_trail:
            pygame.draw.circle(screen, player_color, (x - left_col * cell_size, y - top_row * cell_size), player_radius // 3)
        
        
        if current_maze[player_y // cell_size][player_x // cell_size] == "D":
            if (player_x // cell_size) == 40:
                player_x = (cell_size + (cell_size // 2))
            elif (player_x // cell_size) == 0:
                player_x = ((len(maze)) * cell_size) + ((cell_size // 2)) #2133
        if current_maze[player_y // cell_size][player_x // cell_size] == "o":
                    score += 1
                    # Increase player_ammo when a coin is picked up
                    player_ammo += 1
                    current_maze[player_y // cell_size][player_x // cell_size] = "."

        # Draw player (player) if it's not over a wall
        if current_maze[player_y // cell_size][player_x // cell_size] != "#":
            pygame.draw.circle(screen, player_color, (player_x - left_col * cell_size, player_y - top_row * cell_size), player_radius)
            pygame.draw.circle(screen, white, (player_x - left_col * cell_size, player_y - top_row * cell_size), player_radius, 2)
            if rocket_score != 0:
                if last_movement_direction == "left" or last_movement_direction == "right":
                    pygame.draw.rect(screen, gray,((player_x - left_col * cell_size) - (cell_size // 2),player_y - top_row * cell_size, cell_size, cell_size // 5))
                    pygame.display.flip()
                elif last_movement_direction == "up" or last_movement_direction == "down":
                    pygame.draw.rect(screen, gray,((player_x - left_col * cell_size) ,(player_y - top_row * cell_size) - (cell_size // 2), cell_size // 5, cell_size))
                    pygame.display.flip()
        # Draw Redman (Bot) if it's not over a wall
        if redman_life == 0:
            if maze_str == "maze1" or maze_str == "maze2" or maze_str == "maze3":
                # Keep the red trail list's length no more than 20
                if len(red_trail) > 10:
                    red_trail.pop(0)
                    # Draw the red trail (using red color)
                    for x, y in red_trail:
                        pygame.draw.circle(screen, red, (x - left_col * cell_size, y - top_row * cell_size), redman_radius // 2)
                        pygame.draw.circle(screen, white, (x - left_col * cell_size, y - top_row * cell_size), redman_radius // 2, 2)
                    for i in range(len(red_trail)):
                        if player_color != red:
                            if (player_x, player_y) == red_trail[i]:
                                level = 1
                                flew_to_close()
                    if current_maze[redman_y // cell_size][redman_x // cell_size] != "#":
                                    pygame.draw.circle(screen, redman_color, (redman_x - left_col * cell_size, redman_y - top_row * cell_size), redman_radius)
                                    # Update the display
                                    pygame.display.flip()
        # Draw Chicken
        if maze_str == "maze1":
            if current_maze[chicken_y // cell_size][chicken_x // cell_size] != "#":
                pygame.draw.circle(screen, yellow, (chicken_x - left_col * cell_size, chicken_y - top_row * cell_size),chicken_radius // 2)
                pygame.draw.ellipse(screen, yellow, ((chicken_x - (cell_size // 2)) - left_col * cell_size, chicken_y - top_row * cell_size, cell_size, (cell_size // 2)))
                pygame.draw.circle(screen, white, ((chicken_x + (cell_size // 7)) - left_col * cell_size, chicken_y - top_row * cell_size),chicken_radius // 6)
                pygame.draw.circle(screen, white, ((chicken_x - (cell_size // 7)) - left_col * cell_size, chicken_y - top_row * cell_size),chicken_radius // 6)
                pygame.draw.polygon(screen, dark_orange, [((chicken_x - (cell_size // 7)) - left_col * cell_size, (chicken_y + (cell_size // 10)) - top_row * cell_size), (chicken_x - left_col * cell_size, (chicken_y + (cell_size // 6)) - top_row * cell_size), ((chicken_x + (cell_size // 7)) - left_col * cell_size, (chicken_y + (cell_size // 10)) - top_row * cell_size)])
                pygame.display.flip()
        # Draw Chicken at boss fight
        if maze_str == "maze_trianglebob":
            if cheese_score == 1:
                if abs((player_x - trianglebob_eye_x)) // cell_size <= 10 and abs((player_y - trianglebob_eye_y)) // cell_size <= 10:
                    if current_maze[chicken_y // cell_size][chicken_x // cell_size] != "#":
                        pygame.draw.circle(screen, yellow, (chicken_x - left_col * cell_size, chicken_y - top_row * cell_size),chicken_radius // 2)
                        pygame.draw.ellipse(screen, yellow, ((chicken_x - (cell_size // 2)) - left_col * cell_size, chicken_y - top_row * cell_size, cell_size, (cell_size // 2)))
                        pygame.draw.circle(screen, white, ((chicken_x + (cell_size // 7)) - left_col * cell_size, chicken_y - top_row * cell_size),chicken_radius // 6)
                        pygame.draw.circle(screen, white, ((chicken_x - (cell_size // 7)) - left_col * cell_size, chicken_y - top_row * cell_size),chicken_radius // 6)
                        pygame.draw.polygon(screen, dark_orange, [((chicken_x - (cell_size // 7)) - left_col * cell_size, (chicken_y + (cell_size // 10)) - top_row * cell_size), (chicken_x - left_col * cell_size, (chicken_y + (cell_size // 6)) - top_row * cell_size), ((chicken_x + (cell_size // 7)) - left_col * cell_size, (chicken_y + (cell_size // 10)) - top_row * cell_size)])
                        pygame.display.flip()
        if maze_str == "maze3":
            if rocket_score != 0:
                pygame.mouse.set_visible(True)
                left_mouse_button, _, _ = pygame.mouse.get_pressed()
                if left_mouse_button:
                    mouse_direction = get_mouse_direction((pygame.mouse.get_pos()), (player_x,player_y))
                    new_projectile = Projectile(player_x, player_y, mouse_direction, gray)
                    green_projectiles.append(new_projectile)
        # orange special moves
        if player_color == orange:
            projectile_radius = cell_size
        if player_color == orange:
            projectile_cooldown = 1000
        # fail safe for green
        if player_color == green:
            projectile_radius = cell_size // 5
        if player_color == green:
            projectile_cooldown = 300
        if player_color == purple:
            key_score = 1
        if maze_str == "maze_trianglebob":
            if abs((player_x - trianglebob_eye_x)) // cell_size <= 10 and abs((player_y - trianglebob_eye_y)) // cell_size <= 10:
                if cheese_score != 0:
                    number_index_tri = 0
                    message_tri_1 = "What!!! Chicken why are you here?!?"
                    message_tri_2 = "Noo! The cheese"
                    message_tri_3 = "Ahhh Chicken and Cheese my worst enemies"
                    if number_index_tri == 0:
                        text_box(yellow , message_tri_1)
                        pygame.time.wait(1000)
                        number_index_tri = 1
                        if number_index_tri == 1:
                            text_box(yellow , message_tri_2)
                            pygame.time.wait(1000)
                            number_index_tri = 2
                            if number_index_tri == 2:
                                pygame.time.wait(1000)
                                text_box(yellow , message_tri_3)
                                pygame.time.wait(1000)
                                You_Won()
                elif cheese_score == 0:
                    number_index_tri = 0
                    message_tri_1 = "It is impressive you made it this far."
                    message_tri_2 = "But you are no match for me."
                    message_tri_3 = "Begone!"
                    if number_index_tri == 0:
                        text_box(red , message_tri_1)
                        pygame.time.wait(500)
                        number_index_tri = 1
                        if number_index_tri == 1:
                            text_box(red , message_tri_2)
                            pygame.time.wait(500)
                            number_index_tri = 2
                            if number_index_tri == 2:
                                pygame.time.wait(500)
                                text_box(red , message_tri_3)
                                pygame.time.wait(500)
                                flew_to_close()

        
        pygame.display.flip()
        clock_tick = 16
        if player_color == yellow:
            clock_tick = 60
        # Cap the frame rate
        clock.tick(clock_tick)


# Clean up
pygame.quit()

start_menu()
# Convert the maze layout to a list of lists
maze1 = [list(row) for row in maze_layout1]
maze = maze1
maze_str = "maze1"
main_game_loop(maze1)
# Calculate the elapsed time when the game loop ends
end_time = time.time()
elapsed_time = end_time - start_time

# Convert elapsed time to hours, minutes, and seconds
hours = int(elapsed_time // 3600)
minutes = int((elapsed_time % 3600) // 60)
seconds = int(elapsed_time % 60)

# Print the elapsed time in the desired format
print("Elapsed Time:", f"{hours:02}:{minutes:02}:{seconds:02}")
print(time)
time = (hours, minutes, seconds)
file = open("C:\VSCode\TextTest.txt", "r+")
file.write(time)
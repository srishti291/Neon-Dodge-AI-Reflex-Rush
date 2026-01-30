import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Dodge: AI Reflex Rush")

# Colors (Vibrant Palette)
VIBRANT_RED = (255, 69, 58)
VIBRANT_BLUE = (0, 122, 255)
VIBRANT_GREEN = (52, 199, 89)
VIBRANT_YELLOW = (255, 204, 0)
VIBRANT_PURPLE = (175, 82, 222)
BLACK = (0, 0, 0)

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10
player_color = VIBRANT_BLUE  # Player color

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_colors = [VIBRANT_RED, VIBRANT_GREEN, VIBRANT_YELLOW, VIBRANT_PURPLE]  # List of enemy colors
enemy_color = random.choice(enemy_colors)  # Random enemy color

# Fonts
font = pygame.font.SysFont("arial", 30, bold=True)
title_font = pygame.font.SysFont("arial", 60, bold=True)
score_font = pygame.font.SysFont("arial", 40, bold=True)

# Clock to control frame rate
clock = pygame.time.Clock()

# File to store the highest score
HIGHEST_SCORE_FILE = "highest_score.txt"

# Load the highest score from the file
def load_highest_score():
    if os.path.exists(HIGHEST_SCORE_FILE):
        with open(HIGHEST_SCORE_FILE, "r") as file:
            return int(file.read())
    return 0  # Default highest score if the file doesn't exist

# Save the highest score to the file
def save_highest_score(score):
    with open(HIGHEST_SCORE_FILE, "w") as file:
        file.write(str(score))

# Gradient background
def draw_gradient_background():
    for i in range(HEIGHT):
        color = (
            135 + (216 - 135) * i // HEIGHT,
            206 + (191 - 206) * i // HEIGHT,
            250 + (216 - 250) * i // HEIGHT,
        )
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))

# Render a button with hover effect
def render_button(button, mouse_pos):
    color = VIBRANT_GREEN if button["rect"].collidepoint(mouse_pos) else VIBRANT_RED
    pygame.draw.rect(screen, color, button["rect"], border_radius=10)
    text = font.render(button["text"], True, BLACK)
    screen.blit(text, (button["rect"].x + button["rect"].width // 2 - text.get_width() // 2,
                       button["rect"].y + button["rect"].height // 2 - text.get_height() // 2))

# Difficulty selection screen
def select_difficulty_ui():
    while True:
        draw_gradient_background()

        # Render title
        title_text = title_font.render("Select Difficulty", True, BLACK)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        # Render buttons
        buttons = [
            {"text": "Easy", "rect": pygame.Rect(WIDTH // 2 - 100, 150, 200, 50), "speed": 5},
            {"text": "Medium", "rect": pygame.Rect(WIDTH // 2 - 100, 250, 200, 50), "speed": 8},
            {"text": "Hard", "rect": pygame.Rect(WIDTH // 2 - 100, 350, 200, 50), "speed": 12},
            {"text": "Advanced", "rect": pygame.Rect(WIDTH // 2 - 100, 450, 200, 50), "speed": 16},
        ]

        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            render_button(button, mouse_pos)

        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for button in buttons:
                    if button["rect"].collidepoint(mouse_pos):
                        return button["speed"]

# Game Over Screen
def game_over_ui(score, highest_score):
    while True:
        draw_gradient_background()

        # Render Game Over text
        game_over_text = title_font.render("Game Over!", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 150))

        # Render score
        score_text = score_font.render(f"Your Score: {score}", True, BLACK)
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 250))

        # Render highest score
        highest_score_text = score_font.render(f"Highest Score: {highest_score}", True, BLACK)
        screen.blit(highest_score_text, (WIDTH // 2 - highest_score_text.get_width() // 2, 300))

        # Render Restart button
        restart_button = pygame.Rect(WIDTH // 2 - 100, 400, 200, 50)
        pygame.draw.rect(screen, VIBRANT_GREEN, restart_button, border_radius=10)
        restart_text = font.render("Restart", True, BLACK)
        screen.blit(restart_text, (restart_button.x + restart_button.width // 2 - restart_text.get_width() // 2,
                                   restart_button.y + restart_button.height // 2 - restart_text.get_height() // 2))

        pygame.display.update()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return  # Exit the game over screen and restart the game

# Draw the player with a border and stripes
def draw_player():
    # Draw the outer border
    pygame.draw.rect(screen, VIBRANT_GREEN, (player_pos[0] - 2, player_pos[1] - 2, player_size + 4, player_size + 4))

    # Draw the player square
    pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

    # Add diagonal stripes inside the player square
    stripe_color = VIBRANT_YELLOW
    stripe_spacing = 10
    for i in range(0, player_size, stripe_spacing):
        pygame.draw.line(screen, stripe_color, (player_pos[0] + i, player_pos[1]),
                         (player_pos[0], player_pos[1] + i), 2)
        pygame.draw.line(screen, stripe_color, (player_pos[0] + player_size - i, player_pos[1]),
                         (player_pos[0] + player_size, player_pos[1] + i), 2)

# Main game loop
def main():
    global player_pos, enemy_pos, enemy_color

    # Load the highest score
    highest_score = load_highest_score()

    while True:  # Restartable game loop
        # Select difficulty
        enemy_speed = select_difficulty_ui()

        # Initialize game variables
        score = 0
        player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
        enemy_color = random.choice(enemy_colors)

        running = True
        while running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_pos[0] > 0:
                player_pos[0] -= player_speed
            if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
                player_pos[0] += player_speed

            # Enemy movement
            enemy_pos[1] += enemy_speed
            if enemy_pos[1] > HEIGHT:
                enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
                enemy_pos[1] = 0
                enemy_color = random.choice(enemy_colors)  # Change color
                score += 1
                enemy_speed += 0.5  # Increase speed as the player survives longer

            # Collision detection
            if (enemy_pos[0] < player_pos[0] < enemy_pos[0] + enemy_size or
                enemy_pos[0] < player_pos[0] + player_size < enemy_pos[0] + enemy_size) and \
               (enemy_pos[1] < player_pos[1] < enemy_pos[1] + enemy_size or
                enemy_pos[1] < player_pos[1] + player_size < enemy_pos[1] + enemy_size):
                # Update the highest score if the current score is greater
                if score > highest_score:
                    highest_score = score
                    save_highest_score(highest_score)
                game_over_ui(score, highest_score)
                break  # Exit the current game loop to restart the game

            # Drawing everything
            draw_gradient_background()
            draw_player()  # Draw the player as a square
            pygame.draw.rect(screen, enemy_color, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))  # Enemy as a square
            score_text = font.render(f"Score: {score}", True, BLACK)
            highest_score_text = font.render(f"Highest: {highest_score}", True, BLACK)
            screen.blit(score_text, (10, 10))  # Display the score
            screen.blit(highest_score_text, (10, 50))  # Display the highest score

            # Update the screen
            pygame.display.update()

            # Control the frame rate
            clock.tick(30)

if __name__ == "__main__":
    main()
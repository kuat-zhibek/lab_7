import pygame
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.font.init()
font = pygame.font.Font(None, 36)  


music_FOLDER = r"C:\Users\Zhibek\OneDrive\Desktop\lab_7"
playlist = [os.path.join(music_FOLDER, f) for f in os.listdir(music_FOLDER) if f.endswith(".mp3")]

current_song_index = 0


def play_music():
    pygame.mixer.music.load(playlist[current_song_index])
    pygame.mixer.music.play()


def draw_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (x, y))


if playlist:
    play_music()
else:
    print("No music files found in 'music' folder.")


running = True
paused = False

while running:
    screen.fill(WHITE)
    

    if playlist:
        song_name = os.path.basename(playlist[current_song_index])
        draw_text(f"Now Playing: {song_name}", 50, 100)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    play_music()
            
            elif event.key == pygame.K_s: 
                pygame.mixer.music.stop()
                paused = False

            elif event.key == pygame.K_n:  
                current_song_index = (current_song_index + 1) % len(playlist)
                play_music()

            elif event.key == pygame.K_p:  
                current_song_index = (current_song_index - 1) % len(playlist)
                play_music()

pygame.quit()
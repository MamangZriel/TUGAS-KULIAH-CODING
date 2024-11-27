import pygame
import time

# Inisialisasi pygame
pygame.init()

# Konfigurasi layar
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lirik Lagu Beranimasi")

# Warna
black = (0, 0, 0)
white = (255, 255, 255)

# Font
font = pygame.font.Font(None, 74)

# Lirik lagu
lyrics = [
    "Ayo Ayo Ganyank Fufufafa",
    "Ganyank Fufufafa Sekarang Juga",
    "Ayo Ayo Ganyank Fufufafa",
    "Ganyank Fufufafa Sekarang Juga",
]

# Fungsi untuk menampilkan teks
def display_text(text, y_position):
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(screen_width // 2, y_position))
    screen.blit(text_surface, text_rect)

# Loop utama
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    # Menampilkan lirik dengan animasi
    for i, line in enumerate(lyrics):
        display_text(line, 100 + i * 100)  # Mengatur posisi y untuk setiap baris
        pygame.display.flip()  # Memperbarui tampilan
        time.sleep(1)  # Menunggu 1 detik sebelum menampilkan baris berikutnya

    pygame.display.flip()  # Memperbarui tampilan terakhir
    time.sleep(2)  # Menunggu sebelum keluar

pygame.quit()
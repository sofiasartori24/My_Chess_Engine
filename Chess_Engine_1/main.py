# main.py

from game import Game
import pygame

def load_images():
    images = {}
    pieces = ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']
    colors = ['white', 'black']
    for color in colors:
        for piece in pieces:
            image = pygame.image.load(f'images/{color}_{piece}.png')
            images[f'{color}_{piece}'] = pygame.transform.scale(image, (50, 50))
    return images

def draw_board(screen, board, images):
    colors = [pygame.Color("white"), pygame.Color("pink")]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col*60, row*60, 60, 60))
            piece = board[row][col]
            if piece:
                piece.draw_piece(screen, images)
                pass

def main():
    images = load_images()
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
    game = Game()
    piece = None
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // 60, pos[0] // 60
                if piece:
                    game.move_piece(piece, row, col)
                    piece.draw_piece(screen, images)
                    piece = None
                else:
                    piece = game.board[row][col]
        
        draw_board(screen, game.board, images)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

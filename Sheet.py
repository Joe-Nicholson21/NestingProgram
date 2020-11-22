# GUI.py
import pygame

pygame.font.init()

#def redraw_window(win):
    # win.fill((255,255,255))
    # fnt = pygame.font.SysFont("comicsans", 30)
    
    # text = fnt.render("Part Size:", 1, (0,0,0))
    # win.blit(text, (0, 10))
    # pygame.draw.rect(win,(0,0,00),(110,5,50,30),3)
    # pygame.draw.rect(win,(0,0,00),(200,5,50,30),3)
    # text = fnt.render("X", 1, (0,0,0))
    # win.blit(text, (175, 10))
    
    # clear = fnt.render("Sheet Border:", 1, (0,0,0))
    # win.blit(clear, (0, 60))
    # pygame.draw.rect(win,(0,0,00),(160,55,50,30),3)
    # pygame.draw.rect(win,(0,0,00),(250,55,50,30),3)
    # text = fnt.render("X", 1, (0,0,0))
    # win.blit(text, (205, 110))
    
    # clear = fnt.render("Part Border:", 1, (0,0,0))
    # win.blit(clear, (0, 110))
    # pygame.draw.rect(win,(0,0,00),(140,105,50,30),3)
    # pygame.draw.rect(win,(0,0,00),(230,105,50,30),3)
    # text = fnt.render("X", 1, (0,0,0))
    # win.blit(text, (225, 60))
    
    
    # pygame.draw.rect(win,(0,0,00),(50,200,500,250),3)
    


# def main():
 
    
    
    
#     win = pygame.display.set_mode((600,500))
#     pygame.display.set_caption("Sudoku Solver")
#     redraw_window(win)
#     pygame.display.update()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
            
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pos = pygame.mouse.get_pos()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     pos = pygame.mouse.get_pos()
#                     print(pos)



def main():
    
    sheetx=500
    sheety=250
    
    partx = 70
    party = 70
    
    sheetbordx=20
    sheetbordy=20
    
    partbordx=50
    partbordy=75
    
    numberx = int(((sheetx *5) - (2*sheetbordx)) / (partx+partbordx))
    numbery = int(((sheety *5) - (2*sheetbordy)) / (party+partbordy))
    
    
    win = pygame.display.set_mode((600,500))
    pygame.display.set_caption("Sheet arranger")

    win.fill((255,255,255))
    fnt = pygame.font.SysFont("comicsans", 30)
    
    text = fnt.render("Part Size:", 1, (0,0,0))
    win.blit(text, (0, 10))
    pygame.draw.rect(win,(0,0,00),(110,5,50,30),3)
    pygame.draw.rect(win,(0,0,00),(200,5,50,30),3)
    text = fnt.render("X", 1, (0,0,0))
    win.blit(text, (175, 10))
    
    clear = fnt.render("Sheet Border:", 1, (0,0,0))
    win.blit(clear, (0, 60))
    pygame.draw.rect(win,(0,0,00),(160,55,50,30),3)
    pygame.draw.rect(win,(0,0,00),(250,55,50,30),3)
    text = fnt.render("X", 1, (0,0,0))
    win.blit(text, (205, 110))
    
    clear = fnt.render("Part Border:", 1, (0,0,0))
    win.blit(clear, (0, 110))
    pygame.draw.rect(win,(0,0,00),(140,105,50,30),3)
    pygame.draw.rect(win,(0,0,00),(230,105,50,30),3)
    text = fnt.render("X", 1, (0,0,0))
    win.blit(text, (225, 60))
    print(numberx)
    for i in range(numberx):
        for j in range(numbery):
            pygame.draw.rect(win,(0,0,0),(50+sheetbordx/5+partbordx/5*i+i*partx/5,200+sheetbordy/5+partbordy/5*j+j*party/5,partx/5,party/5),0)
            pygame.draw.rect(win,(150,150,150),(52+sheetbordx/5+partbordx/5*i+i*partx/5,202+sheetbordy/5+partbordy/5*j+j*party/5,partx/5-4,party/5-4),0)
    
    pygame.draw.rect(win,(0,0,255),(50,200,500,250),5)
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)





main()

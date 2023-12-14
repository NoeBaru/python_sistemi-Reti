import pygame #raggruppa una serie di funzioni che controllano la visualizzazione della finestra principale

pygame.init() #serve ad inizializzare tutti i sottomoduli
screen = pygame.display.set_mode((800, 600)) #prende come parametro una tuple di due numeri (larghezza ed altezza) e crea la finestra principale con le dimensioni assegnate
pygame.display.set_caption("Il mio primo programma")
screen.fill((255, 255, 255))
pygame.display.flip()
import pygame
from sys import exit
import os
from cards import Card


class Game:
    def __init__(self, PokerGame):
        pygame.init()
        pygame.display.set_caption("Poker Odds")

        self.ds = pygame.display.set_mode((1200, 800))
        self.game = PokerGame(4)
        self.card_images = {}
        self.init_card_images()

    def init_card_images(self):
        for img in os.listdir(r'Images'):
            suit, value = img[:-4].split('_')
            new_value = str(int(value)) if value.isnumeric() else \
                {"A": "Ace", "K": "King", "Q": "Queen", "J": "Jack"}[value]

            self.card_images[Card(new_value, suit)] = pygame.image.load(fr"Images/{suit}_{value}.png").convert_alpha()

    def update(self):
        self.ds.blit(self.card_images[Card("King", "Spades")], (0, 0))

    def run(self):
        while True:
            events = pygame.event.get()
            for ev in events:
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.update()

            pygame.display.update()

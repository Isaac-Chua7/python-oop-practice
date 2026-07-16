from abc import ABC, abstractmethod

class Card(ABC):
    
    @abstractmethod
    def inspect(self):
        pass

    @abstractmethod
    def play(self):
        pass

class Heart(Card):

    def inspect(self):
        print("This card is a heart")

    def play(self):
        print("You played a heart")

heart = Heart()
heart.inspect()
heart.play()


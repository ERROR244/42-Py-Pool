from abc import ABC, abstractmethod

class Character(ABC):
    """Your docstring for Class"""
    
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name  = first_name
        self.is_alive    = is_alive
        self.family_name = self.family_name
        self.eyes        = self.eyes
        self.hairs       = self.hairs

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
    

    @abstractmethod
    def func():
        pass

class Stark(Character):
    """Your docstring for Class"""
    def func():
        return "I'm Iron Man!"



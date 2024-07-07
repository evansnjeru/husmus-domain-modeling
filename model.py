from enum import Enum


class Alignment(Enum):
    """
    Models character alignments
    """
    GOOD = 1
    NEUTRAL = 2
    EVIL = 3
    

class Character:
    """
    Models a character. 

    character_id: since character is an entity, we generate a unique id for persistence. 
    _name: private attribute tracking character's name.
    _alignment: private attribute tracking character's alignment.
    _hp: private attribute tracking character's hitpoints
    """
    def __init__(self, name: str, alignment: Alignment, hitpoints: int = 5, armor_class: int = 10, attributes: dict = {"strength": 10, "dexterity": 10, "constitution": 10, "wisdom": 10, "intelligence": 10, "charisma": 10}) -> None:
        #self.id = 
        self.name = name
        self.alignment = alignment
        self.hp = hitpoints
        self._ac = armor_class
        self.attributes = attributes

    @property
    def name(self) -> str:
        """
        Gets name of character
        """
        return self._name 

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets name of character
        """
        self._name = name

    @property
    def alignment(self) -> Alignment:
        """
        Gets character's alignment
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment: Alignment) -> None:
        """
        Sets character's alignment
        """
        self._alignment = alignment

    @property
    def hp(self) -> int:
        """
        Gets character's hp
        """
        return self._hp

    @hp.setter
    def hp(self, hitpoints: int) -> None:
        """
        Sets character's hitpoints
        """
        if hitpoints < 1:
            raise CharacterDead(f'{self._name} is DEAD! Better luck next time!')
        else:
            self._hp = hitpoints

    @property
    def ac(self) -> int:
        """
        Sets character's armor class
        """
        return self._ac

    def take_damage(self, roll: int) -> None:
        """
        Reduces character's hp after an attack or debilitating effect.
        """ 
        damage = 1

        if roll > self._ac:
            self.hp -= damage 
        elif roll == 20:
            self.hp -= damage * 2 




def attack(attacker: Character, defender: Character, roll: int) -> None:
    """
    Simulates an attack workflow between two combatants 
    """
    defender.take_damage(roll)


class CharacterDead(Exception):
    pass

# setup eq and hash for character entity

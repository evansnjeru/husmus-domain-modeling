import pytest

from model import Character, Alignment, attack, CharacterDead


def test_getter_can_fetch_character_name():
    """
    Tests the get character's name feature.
    """
    character1 = Character("Bob", Alignment.GOOD)
    character2 = Character("Alice", Alignment.NEUTRAL)

    assert character1.name == "Bob" and character2.name == "Alice"


def test_setter_can_change_character_name():
    """
    Tests the set character's name feature
    """
    character = Character("Bob", Alignment.GOOD)

    character.name = "Alice"

    assert character.name == "Alice"


def test_getter_can_fetch_character_alignment():
    """
    Tests the get character's alignment feature
    """
    character = Character("Bob", Alignment.GOOD)

    assert character.alignment == Alignment.GOOD


def test_setter_can_change_character_alignment():
    """
    Tests the set character's alignment feature
    """
    character = Character("Bob", Alignment.GOOD)

    character.alignment = Alignment.NEUTRAL

    assert character.alignment == Alignment.NEUTRAL


def test_character_hitpoints_defaults_to_5_on_creation():
    """
    Tests new character hitpoints as 5  
    """
    character = Character("Bob", Alignment.GOOD)

    assert character.hp == 5


def test_character_can_get_damaged():
    """
    Tests character can take damage
    """
    character = Character("Bob", Alignment.GOOD)

    character.take_damage(11)

    assert character.hp == 4
    

def test_character_armor_class_defaults_to_10_on_creation():
    """
    Tests new character armor class as 10 
    """
    character = Character("Bob", Alignment.GOOD)

    assert character.ac == 10


def test_one_character_can_attack_another():
    """
    Tests for a successful attack by one character on another
    """
    character1 = Character("Bob", Alignment.GOOD)
    character2 = Character("Alice", Alignment.NEUTRAL)

    attack(character1, character2, 11)

    assert character1.hp == 5 and character2.hp == 4


def test_rolling_a_20_always_hits_double_damage():
    """
    Tests for critical hit on a 20 roll
    """
    character = Character("Bob", Alignment.GOOD, armor_class = 21)

    character.take_damage(20)

    assert character.hp == 3


def test_raises_character_dead_exception_when_hitpoints_reach_zero():
    """
    Tests for character's death
    """
    character1 = Character("Bob", Alignment.GOOD)
    character2 = Character("Alice", Alignment.NEUTRAL, hitpoints = 1)

    with pytest.raises(CharacterDead, match="Alice"):
        attack(character1, character2, 11)
        

def test_character_has_attributes():
    """
    Tests character's attributes
    """
    character = Character("Bob", Alignment.GOOD, armor_class = 21)
    attributes = ["strength", "dexterity", "constitution", "wisdom", "intelligence", "charisma"]
    all_attributes_available = True

    for attribute in attributes:
        all_attributes_available = all_attributes_available and attribute in character.attributes.keys()

    assert all_attributes_available


def test_new_character_has_default_attribute_scores_of_10():
    """
    Tests character's attributes scores
    """
    character = Character("Bob", Alignment.GOOD, armor_class = 21)
    attributes_default_to_10 = []

    for score in character.attributes.values():
        attributes_default_to_10.append(score == 10)

    assert all(attributes_default_to_10)

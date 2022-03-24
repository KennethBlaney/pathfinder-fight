import random
import json


def load_character_json(name: str):
    """
    This loads the json files for a character into a dict for the character.

    :param name: name of the json to be loaded (be sure to append the `.json` when opening it.
    :return: a dictionary for the requested character, a boolean value indicating a character was successfully loaded
    """
    return {}, True


def make_attack(to_hit: int, weapon_damage: str, target_ac: int):
    """
    This makes and resolves an attack between two characters by rolling a d20 to determine if it hits,
    then rolling damage on a successful hit

    :param to_hit: the attack bonus of the attacker
    :param weapon_damage: the damage done by the attacker's weapon, passed into `roll_damage`
    :param target_ac: the target's armor class
    :return: a boolean value indicating a hit, an integer value for the amount of damage done
    """
    return True, roll_damage(weapon_damage)


def roll_damage(damage_string: str):
    """
    Damage is usually given as a string in the format XdY+Z. We extract X, Y, and Z from this format and then roll the
    necessary dice

    :param damage_string: XdY+Z
    :return: the amount of damage done with this attack
    """
    return 0


if __name__ == "__main__":
    good_guy = {}
    bad_guy = {}

    # Character selection
    while True:
        good_guy['name'] = input("Which character are you?")
        good_guy, success = load_character_json(good_guy.get('name'))
        if success:
            break
        print(f"{good_guy['name']} is not a valid character sheet. Please choose again.")
    while True:
        bad_guy['name'] = input("Which character are you fighting?")
        bad_guy, success = load_character_json(bad_guy.get('name'))
        if success:
            break
        print(f"{bad_guy['name']} is not a valid character sheet. Please choose again.")

    # Character fight
    good_guy_hits, damage_to_bad_guy = make_attack(good_guy["to_hit"], good_guy["weapon_damage"], bad_guy["ac"])
    bad_guy_hits, damage_to_good_guy = make_attack(bad_guy["to_hit"], bad_guy["weapon_damage"], good_guy["ac"])
    print(f"{good_guy['name']} swings their {good_guy['weapon']} at {bad_guy['name']}.")
    if good_guy_hits:
        print(f"They hit for {damage_to_bad_guy} damage.")
    else:
        print(f"{bad_guy['name']} dodges out of the way.")
    print(f"{bad_guy['name']} counters with their {bad_guy['weapon']}.")
    if bad_guy_hits:
        print(f"They hit for {damage_to_good_guy} damage.")
    else:
        print(f"{good_guy['name']} dodges out of the way.")

def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    for card, card_type in args:
        if card_type == "monster":
            monster_cards.append("  ***" + card)
        elif card_type == "spell":
            spell_cards.append("  $$$" + card)
    for card, card_type in kwargs.items():
        if card_type == "monster":
            monster_cards.append("  ***" + card)
        elif card_type == "spell":
            spell_cards.append("  $$$" + card)

    monster_cards = sorted(monster_cards, key=lambda x: x, reverse=True)
    spell_cards = sorted(spell_cards)
    result = ""
    if monster_cards and spell_cards:
        result = "Monster cards:"
        result += "\n" + "\n".join(monster_cards)
        result += "\nSpell cards:"
        result += "\n" + "\n".join(spell_cards)
    elif spell_cards:
        result += "Spell cards:"
        result += "\n" + "\n".join(spell_cards)
    elif monster_cards:
        result = "Monster cards:"
        result += "\n" + "\n".join(monster_cards)

    return result
def cookbook(*menu):
    my_cookbook = {}
    for first_group in menu:
        name, cuisine, ingredients = first_group
        if cuisine not in my_cookbook:
            my_cookbook[cuisine] = []
        my_cookbook[cuisine].append((name, ingredients))

    for cuisine in my_cookbook:
        my_cookbook[cuisine].sort()
    sorted_cookbook = sorted(my_cookbook.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []
    for cuisine, recipes in sorted_cookbook:
        result.append(f"{cuisine} cuisine contains {len(recipes)} recipes:\n")
        for name, ingredients in recipes:
            result.append(f"  * {name} -> Ingredients: {', '.join(ingredients)}\n")

    return ''.join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))
# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
#     ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
#     ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
#     ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
#     ))

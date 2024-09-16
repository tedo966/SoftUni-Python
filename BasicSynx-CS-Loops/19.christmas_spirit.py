quantity_decorations = int(input())
days_left = int(input())

ornament_set = 0
tree_skirt = 0
tree_garland = 0
tree_lights = 0

improved_points = 0

for day in range(1, days_left + 1):
    # Every eleventh day: increase quantity by 2
    if day % 11 == 0:
        quantity_decorations += 2

    # Every second day: buy Ornament Sets
    if day % 2 == 0:
        ornament_set += quantity_decorations
        improved_points += 5

    # Every third day: buy Tree Skirts and Tree Garlands
    if day % 3 == 0:
        tree_skirt += quantity_decorations
        tree_garland += quantity_decorations
        improved_points += 13

    # Every fifth day: buy Tree Lights
    if day % 5 == 0:
        tree_lights += quantity_decorations
        improved_points += 17
        # If it's also the third day, increase spirit by an additional 30
        if day % 3 == 0:
            improved_points += 30

    # Every tenth day: the cat ruins decorations
    if day % 10 == 0:
        improved_points -= 20  # Cat ruins decorations, lose 20 spirit points
        # Buy one piece of Tree Skirt, Garland, and Lights
        tree_skirt += 1
        tree_garland += 1
        tree_lights += 1

    # If the last day is the tenth day, the cat ruins the Christmas turkey
    if day == days_left and day % 10 == 0:
        improved_points -= 30


# Calculate total cost
total_price = (ornament_set * 2) + (tree_skirt * 5) + (tree_garland * 3) + (tree_lights * 15)

# Output the total cost and total spirit
print(f"Total cost: {total_price}")
print(f"Total spirit: {improved_points}")

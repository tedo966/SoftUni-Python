def sorting_cheeses(**cheses_dict):
    cheses_dict = sorted(cheses_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for chesse_name, quantities in cheses_dict:
        result.append(chesse_name)
        quantity_list = sorted(quantities, reverse=True)
        result += quantity_list

    return "\n".join([str(x) for x in result])





print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
number_of_pieces = int(input())
list_of_favorite_pieces = {}
for _ in range(number_of_pieces):
    command = input().split("|")
    piece, composer, note = command[0], command[1], command[2]
    if piece not in list_of_favorite_pieces:
        list_of_favorite_pieces[piece] = {"composer":"" , "note":"" }
    list_of_favorite_pieces[piece]["composer"] = composer
    list_of_favorite_pieces[piece]["note"] = note

while True:
    command = input().split("|")
    if command[0] == "Stop":
        break
    if command[0] == "Add":
        piece, composer, note = command[1], command[2], command[3]
        if piece not in list_of_favorite_pieces:
            list_of_favorite_pieces[piece] = {"composer": "", "note": ""}
            list_of_favorite_pieces[piece]["composer"] = composer
            list_of_favorite_pieces[piece]["note"] = note
            print(f"{piece} by {composer} in {note} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif command[0] == "Remove":
        piece = command[1]
        if piece in list_of_favorite_pieces:
            del list_of_favorite_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command[0] == "ChangeKey":
        piece, note = command[1], command[2]
        if piece in list_of_favorite_pieces:
            list_of_favorite_pieces[piece]["note"] = note
            print(f"Changed the key of {piece} to {note}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, pieces_list in list_of_favorite_pieces.items():
    composer = list_of_favorite_pieces[piece]["composer"]
    note = list_of_favorite_pieces[piece]["note"]
    print(f"{piece} -> Composer: {composer}, Key: {note}")









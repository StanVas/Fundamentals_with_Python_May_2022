def manage_dict(numb_of_pieces, pieces_dict):
    for num in range(numb_of_pieces):
        piece, composer, key = input().split('|')
        pieces_dict[piece] = {'composer': composer, 'key': key}

    return pieces_dict


def manage_pieces(pieces_dict):
    while True:
        command = input()
        if command == 'Stop':
            break
        else:
            command = command.split('|')
            action = command[0]
        if action == 'Add':
            piece = command[1]
            composer = command[2]
            key = command[3]
            if piece in pieces_dict:
                print(f"{piece} is already in the collection!")
            else:
                pieces_dict[piece] = {'composer': composer, 'key': key}
                print(f"{piece} by {composer} in {key} added to the collection!")

        elif action == 'Remove':
            piece = command[1]
            if piece not in pieces_dict:
                print(f"Invalid operation! {piece} does not exist in the collection.")
            else:
                del pieces_dict[piece]
                print(f"Successfully removed {piece}!")

        elif action == 'ChangeKey':
            piece = command[1]
            new_key = command[2]
            if piece not in pieces_dict:
                print(f"Invalid operation! {piece} does not exist in the collection.")
            else:
                pieces_dict[piece]['key'] = new_key
                print(f"Changed the key of {piece} to {new_key}!")

    return pieces_dict


def print_function(pieces_dict):
    for piece in pieces_dict:
        composer = pieces_dict[piece]['composer']
        key = pieces_dict[piece]['key']
        print(f"{piece} -> Composer: {composer}, Key: {key}")


def the_pianist(numb_of_pieces):
    pieces_dict = {}
    manage_dict(numb_of_pieces, pieces_dict)
    manage_pieces(pieces_dict)
    print_function(pieces_dict)


number_of_pieces = int(input())
the_pianist(number_of_pieces)

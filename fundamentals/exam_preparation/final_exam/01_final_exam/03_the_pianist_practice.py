def greate_list(number, pieces_dict):
    for piece in range(number):
        piece_info = input().split('|')
        piece = piece_info[0]
        composer = piece_info[1]
        key = piece_info[2]
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


def additional_print(pieces_dict):
    for piece in pieces_dict:
        print(f"{piece} -> Composer: {pieces_dict[piece]['composer']}, Key: {pieces_dict[piece]['key']}")


def the_pianist(number):
    pieces_dict = {}
    greate_list(number, pieces_dict)
    manage_pieces(pieces_dict)
    additional_print(pieces_dict)


number_of_pieces = int(input())
the_pianist(number_of_pieces)

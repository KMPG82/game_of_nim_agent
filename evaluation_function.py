def evaluation_function(state):
    xor_sum = 0
    for pile in state.board:
        pile_int = int(pile)
        xor_sum ^= pile_int

    return 1 if xor_sum != 0 else -1

def evaluation_function(state):
    piles = [pile for pile in state.board if pile > 0]
    
    if len(piles) == 0:
        if state.to_move == 'MAX':
            return 1000
        else:
            return -1000

    xor_sum = 0
    num_ones = 0
    num_non_ones = 0

    for pile in piles:
        xor_sum ^= pile
        if pile == 1:
            num_ones += 1
        else:
            num_non_ones += 1

    total_non_zero = len(piles)
    
    if total_non_zero == 1 and piles[0] == 1:
        if state.to_move == 'MAX':
            return -1000
        else:
            return 1000

    if num_non_ones == 0:
        if num_ones % 2 == 1:
            return -500
        else:
            return 500

    # # If there's exactly 1 pile with size > 1 and 1 pile with size 1
    if sorted(piles) == [1, 2]:
        return 600  # Favor moving to [0, 1] because opponent will lose
    if sorted(piles) == [1, 1]:
        return -400  # Don't want to create [1, 1] for the opponent

    # Midgame: Evaluate using XOR logic (standard Nim behavior)
    if xor_sum == 0:
        return -50
    else:
        return 50 + sum(piles)

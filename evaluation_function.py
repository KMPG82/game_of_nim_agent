
def evaluation_function(state):
    groups = [group for group in state.board if group > 0]
    
    if len(groups) == 0:
        if state.to_move == 'MAX':
            return 1000
        else:
            return -1000

    nim_sum = 0
    number_of_ones = 0
    number_of_non_ones = 0

    for group in groups:
        nim_sum ^= group
        if group == 1:
            number_of_ones += 1
        else:
            number_of_non_ones += 1

    total_non_zero = len(groups)
    
    if total_non_zero == 1 and groups[0] == 1:
        if state.to_move == 'MAX':
            return -1000
        else:
            return 1000

    if number_of_non_ones == 0:
        if number_of_ones % 2 == 1:
            return -500
        else:
            return 500

    if nim_sum == 0:
        return -50
    else:
        return 50 + sum(groups)

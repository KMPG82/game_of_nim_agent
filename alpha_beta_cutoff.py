from games import *
from evaluation_function import *

def alpha_beta_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state=state, game=game, d=3, eval_fn=evaluation_function)

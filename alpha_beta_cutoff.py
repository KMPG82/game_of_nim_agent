from evaluation_function import *
from alpha_beta_cutoff_search import *

def alpha_beta_cutoff_player(game, state):
    return alpha_beta_cutoff_search(state=state, game=game, d=3, eval_fn=evaluation_function)

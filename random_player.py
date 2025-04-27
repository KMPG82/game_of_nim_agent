"""Games or Adversarial Search (Chapter 5)"""

import random

def random_player(game, state):
    """A player that chooses a legal move at random."""
    return random.choice(game.actions(state)) if game.actions(state) else None

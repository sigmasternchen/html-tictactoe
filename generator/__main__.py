from jinja2 import Environment, select_autoescape, FileSystemLoader

from generator.model import Board, NOT_DETERMINED, WIN, Move
from generator.tictactoe import calculate_best_move

import random

env = Environment(
    loader=FileSystemLoader(["./generator"]),
    autoescape=select_autoescape()
)
template = env.get_template("template.html")

taunts = [
    "Looks like you're just one step away from defeat! Better luck next time!",
    "You might want to start practicing your 'congratulations' speech for me!",
    "I hope you're ready to accept your fate - because it's coming fast!",
    "You can almost hear the victory music playing for me, can't you?",
    "You're about to witness a masterclass in losing - starring you!",
    "You're on the express train to defeat, and I'm the conductor!"
]

random.seed(1337)

def get_taunt(board, outcome):
    if outcome == WIN and board.winner() == NOT_DETERMINED:
        return random.choice(taunts)
    else:
        return ""


def render_board(prefix, old_board, board, outcome):
    with open("output/" + prefix + old_board.getId() + ".html", "w") as file:
        file.write(
	    template.render(
                board=board, 
                prefix=prefix,
                reset=prefix + ".html",
                msg=get_taunt(board, outcome),
                Move=Move,
             )
        )


def generate_options(prefix, old_board, board, outcome):
    render_board(prefix, old_board, board, outcome)

    if board.winner() == NOT_DETERMINED:
        for move in board.moves():
            future = board.apply(move)
            response, outcome = calculate_best_move(future)

            print(board.getId(), move, response)

            generate_options(
                prefix,
                future,
                future.apply(response) if response else future,
		        outcome
            )


if __name__ == "__main__":
    board = Board()

    generate_options("index", board, board, NOT_DETERMINED)

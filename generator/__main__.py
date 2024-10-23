from jinja2 import Environment, select_autoescape, FileSystemLoader

from generator.model import Board, NOT_DETERMINED
from generator.tictactoe import calculate_best_move

env = Environment(
    loader=FileSystemLoader(["./generator"]),
    autoescape=select_autoescape()
)
template = env.get_template("template.html")


def render_board(initial_prefix, prefix, board):
    with open("output/" + prefix + ".html", "w") as file:
        file.write(template.render(board=board, prefix=prefix, reset=initial_prefix + ".html"))
        pass


def generate_options(initial_prefix, prefix, board):
    render_board(initial_prefix, prefix, board)

    if board.winner() == NOT_DETERMINED:
        for move in board.moves():
            future = board.apply(move)
            response, _ = calculate_best_move(future)

            print(prefix, move, response)

            generate_options(
                initial_prefix,
                prefix + str(move),
                future.apply(response) if response else future
            )


if __name__ == "__main__":
    board = Board()

    generate_options("g", "g", board)

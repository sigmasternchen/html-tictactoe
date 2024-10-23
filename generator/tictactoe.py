from generator.model import DRAW, NOT_DETERMINED, WIN, LOSS


def transform_board_to_result(board):
    winner = board.winner()
    if winner == DRAW:
        return DRAW
    elif winner == NOT_DETERMINED:
        return NOT_DETERMINED
    elif winner == board.current:
        return WIN
    else:
        return LOSS


def calculate_best_move(board):
    player = board.current
    candidates = []

    winner = board.winner()
    if winner != NOT_DETERMINED:
        return None, transform_board_to_result(board)

    for move in board.moves():
        future = board.apply(move)

        winner = future.winner()

        if winner == player:
            return move, WIN
        elif winner == DRAW:
            candidates.append((move, DRAW))
        elif winner == NOT_DETERMINED:
            opponent_move = calculate_best_move(future)

            if opponent_move[1] == DRAW:
                candidates.append((move, DRAW))
            if opponent_move[1] == WIN:
                candidates.append((move, LOSS))
            if opponent_move[1] == LOSS:
                candidates.append((move, WIN))

    candidates.sort(key=lambda candidate: candidate[1], reverse=True)
    return candidates[0]

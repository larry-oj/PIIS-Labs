import eval

def negascout(depth, board, alpha, beta):
    if (depth == 0):
        return eval.getEvaluation(board)
    
    for move in board.legal_moves:
        a = alpha
        b = beta
        for i in range(1, board.legal_moves.count()):
            board.push(move)
            t = -negascout(depth - 1, board, -b, -a)
            if (t > a) and (t < beta) and (i > 1) and (depth < eval.maxDepth()-1):
                a = -negascout(depth - 1, board, -beta, -t)
            board.pop()
            a = max(a, t)
            if a >= beta:
                return a
            b = a + 1
    return a


def controller(depth, board):
    best = None
    bv = -9998
    alpha = -9999
    beta = 9999

    for move in board.legal_moves:
        board.push(move)
        value = -negascout(depth - 1, board, -beta, -alpha, )

        if value > bv:
            bv = value
            best = move
        alpha = max(value, alpha)

        board.pop()

    return best
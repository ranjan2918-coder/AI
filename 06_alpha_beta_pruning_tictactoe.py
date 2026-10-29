# 6. Alpha-Beta Pruning for Tic-Tac-Toe

def winner(b):
    lines = [b[:3], b[3:6], b[6:]]
    lines += [[b[i], b[i+3], b[i+6]] for i in range(3)]
    lines += [[b[0], b[4], b[8]], [b[2], b[4], b[6]]]
    for line in lines:
        if line == ['X']*3: return 10
        if line == ['O']*3: return -10
    return 0

def minimax(b, maximizing, alpha, beta):
    score = winner(b)
    if score or ' ' not in b: return score
    best = -float('inf') if maximizing else float('inf')
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if maximizing else 'O'
            v = minimax(b, not maximizing, alpha, beta)
            b[i] = ' '
            if maximizing:
                best = max(best, v)
                alpha = max(alpha, best)
            else:
                best = min(best, v)
                beta = min(beta, best)
            if beta <= alpha: break
    return best

board = ['X','O','X','O','X',' ',' ',' ','O']
moves = []
for i in range(9):
    if board[i] == ' ':
        board[i] = 'X'
        moves.append((minimax(board, False, -float('inf'),
                              float('inf')), i))
        board[i] = ' '

if moves:
    print("Best move:", max(moves)[1] + 1)

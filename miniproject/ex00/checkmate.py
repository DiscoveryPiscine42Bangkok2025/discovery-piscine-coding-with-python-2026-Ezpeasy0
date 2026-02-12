def checkmate(board):
    if not board:
        print("Error")
        return
    
    rows = board.splitlines()
    if not rows:
        print("Error")
        return
        
    height = len(rows)
    width = len(rows[0])

    if height != width:
        print("Error")
        return

    for r in rows:
        if len(r) != width:
            print("Error")
            return

    grid = [list(r) for r in rows]
    
    king_r, king_c = None, None
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 'K':
                king_r, king_c = r, c
                break
        if king_r is not None:
            break
            
    if king_r is None:
        print("Error")
        return
    
    king_count = sum(row.count('K') for row in rows)
    if king_count != 1:
        print("Error")
        return


    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    def is_in_bound(r, c):
        return 0 <= r < height and 0 <= c < width

    def scan_threat(dirs, threat_types, is_pawn_check=False):
        for dr, dc in dirs:
            r, c = king_r + dr, king_c + dc
            distance = 0
            
            while is_in_bound(r, c):
                distance += 1
                piece = grid[r][c]
                
                if piece in "PBRQ":
                    if piece in threat_types:
                        if piece == 'P':
                            if distance == 1 and is_pawn_check:
                                return True
                            else:
                                break 
                        else:
                            return True
                    else:
                        break
                
                elif piece == 'K': 
                    break 
           
                r += dr
                c += dc
        return False

    if scan_threat(straight_dirs, "RQ"):
        print("Success")
        return

    if scan_threat(diag_dirs, "BQ"):
        print("Success")
        return

    pawn_attack_dirs = [(1, -1), (1, 1)]
    if scan_threat(pawn_attack_dirs, "P", is_pawn_check=True):
        print("Success")
        return

    print("Fail")
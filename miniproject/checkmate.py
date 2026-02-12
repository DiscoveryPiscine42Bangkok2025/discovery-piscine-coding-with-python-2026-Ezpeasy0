def checkmate(board_str):
    # 1. แยกบรรทัดและกำจัดช่องว่าง (รองรับบอร์ดทุกขนาดที่เป็นจัตุรัส)
    lines = [line.strip() for line in board_str.strip().split('\n') if line.strip()]
    if not lines:
        return
    
    size = len(lines)
    grid = [list(line) for line in lines]
    
    # 2. หาตำแหน่งของ King (K)
    king_pos = None
    for r in range(size):
        for c in range(size):
            if grid[r][c] == 'K':
                king_pos = (r, c)
                break
    
    # กรณีไม่มี King ในบอร์ด (Undefined behavior)
    if not king_pos:
        return

    kr, kc = king_pos

    # 3. กำหนดทิศทางการเดินของหมากแต่ละชนิด
    directions = {
        'orthogonal': [(0, 1), (0, -1), (1, 0), (-1, 0)], # Rook และ Queen
        'diagonal': [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Bishop และ Queen
    }

    def in_bounds(r, c):
        return 0 <= r < size and 0 <= c < size

    # เช็คแนวตรงและแนวนอน (Rook / Queen)
    for dr, dc in directions['orthogonal']:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            piece = grid[r][c]
            if piece != '.':
                if piece in ('R', 'Q'):
                    print("Success")
                    return
                break # มีหมากอื่นขวางทาง
            r += dr
            c += dc

    # เช็คแนวทแยง (Bishop / Queen)
    for dr, dc in directions['diagonal']:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            piece = grid[r][c]
            if piece != '.':
                if piece in ('B', 'Q'):
                    print("Success")
                    return
                break # มีหมากอื่นขวางทาง
            r += dr
            c += dc

    # เช็ค Pawn (P) - กินทแยงมุมจากด้านบน 1 ช่อง (ตามภาพประกอบ)
    pawn_checks = [(kr - 1, kc - 1), (kr - 1, kc + 1)]
    for r, c in pawn_checks:
        if in_bounds(r, c) and grid[r][c] == 'P':
            print("Success")
            return

    # หากไม่มีหมากตัวใดโจมตีได้
    print("Fail")
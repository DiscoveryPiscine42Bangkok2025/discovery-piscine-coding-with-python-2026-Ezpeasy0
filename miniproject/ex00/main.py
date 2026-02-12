from checkmate import checkmate

def main():
    print("Test 1")
    board1 = """\
R...
.K..
..P.
....\
"""
    checkmate(board1)
    print("-" * 20)

    print("Test 2")
    board2 = """\
..
.K\
"""
    checkmate(board2)
 
if __name__ == "__main__":
    main()
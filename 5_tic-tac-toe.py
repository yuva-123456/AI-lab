b = [' '] * 9

def show():
    print(b[:3], '\n', b[3:6], '\n', b[6:])

def win(p):
    return any(b[i]==b[j]==b[k]==p for i,j,k in
               [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

for t in range(9):
    show()
    p = 'X' if t % 2 == 0 else 'O'
    m = int(input(f"{p} move (0-8): "))
    if b[m] == ' ':
        b[m] = p
        if win(p):
            show()
            print(p, "wins")
            break
    else:
        print("Invalid")
else:
    show()
    print("Draw")

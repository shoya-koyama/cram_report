n = list(map(int, input().split()))


if ((n[0] == 1) and (n[1] == 2)) or ((n[0] == 2) and (n[1] == 3)) or ((n[0] == 4) and (n[1] == 5)) or ((n[0] == 5) and (n[1] == 6)) or ((n[0] == 7) and (n[1] == 8)) or ((n[0] == 8) and (n[1] == 9)):
    print("Yes")
else:
    print("No")

"""def is_adjacent(A, B):
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for i in range(3):
        for j in range(3):
            if board[i][j] == A:
                if j < 2 and board[i][j + 1] == B:
                    return "YES"
                if j > 0 and board[i][j - 1] == B:
                    return "YES"
    
    return "NO"


A, B = map(int, input().split())
print(is_adjacent(A, B))
"""

"""function isAdjacent($A, $B) {
    $board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ];

    for ($i = 0; $i < 3; $i++) {
        for ($j = 0; $j < 3; $j++) {
            if ($board[$i][$j] == $A) {
                if ($j < 2 && $board[$i][$j + 1] == $B) {
                    return "YES";
                }
                if ($j > 0 && $board[$i][$j - 1] == $B) {
                    return "YES";
                }
            }
        }
    }

    return "NO";
}

$AB = explode(' ', trim(fgets(STDIN)));
$A = intval($AB[0]);
$B = intval($AB[1]);

echo isAdjacent($A, $B);
"""
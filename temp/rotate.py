def rotate_matrix(matrix):
    N = len(matrix)
    rotated_matrix = [row.copy() for row in matrix]

    # Top row
    for i in range(N - 1):
        rotated_matrix[0][i + 1] = matrix[0][i]

    # Rightmost column
    for i in range(N - 1):
        rotated_matrix[i + 1][N - 1] = matrix[i][N - 1]

    # Bottom row
    for i in range(N - 1, 0, -1):
        rotated_matrix[N - 1][i - 1] = matrix[N - 1][i]

    # Leftmost column
    for i in range(N - 1, 0, -1):
        rotated_matrix[i - 1][0] = matrix[i][0]

    # Corners
    rotated_matrix[0][0] = matrix[N - 1][0]
    rotated_matrix[N - 1][N - 1] = matrix[0][N - 1]
    rotated_matrix[0][N - 1] = matrix[0][0]
    rotated_matrix[N - 1][0] = matrix[N - 1][N - 1]

    return rotated_matrix

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
rotated_matrix = rotate_matrix(matrix)

for row in rotated_matrix:
    print(' '.join(map(str, row)))

"""function rotate_matrix($matrix) {
    $N = count($matrix);
    $rotated_matrix = $matrix; // PHPは値で配列をコピーします

    // 上行
    for ($i = 0; $i < $N - 1; $i++) {
        $rotated_matrix[0][$i + 1] = $matrix[0][$i];
    }

    // 右列
    for ($i = 0; $i < $N - 1; $i++) {
        $rotated_matrix[$i + 1][$N - 1] = $matrix[$i][$N - 1];
    }

    // 下行
    for ($i = $N - 1; $i > 0; $i--) {
        $rotated_matrix[$N - 1][$i - 1] = $matrix[$N - 1][$i];
    }

    // 左列
    for ($i = $N - 1; $i > 0; $i--) {
        $rotated_matrix[$i - 1][0] = $matrix[$i][0];
    }

    // 角
    $rotated_matrix[0][0] = $matrix[$N - 1][0];
    $rotated_matrix[$N - 1][$N - 1] = $matrix[0][$N - 1];
    $rotated_matrix[0][$N - 1] = $matrix[0][0];
    $rotated_matrix[$N - 1][0] = $matrix[$N - 1][$N - 1];

    return $rotated_matrix;
}

$N = intval(fgets(STDIN));
$matrix = array();
for ($i = 0; $i < $N; $i++) {
    $matrix[$i] = explode(' ', trim(fgets(STDIN)));
}

$rotated_matrix = rotate_matrix($matrix);

for ($i = 0; $i < $N; $i++) {
    echo implode(' ', $rotated_matrix[$i]) . "\n";
}
"""

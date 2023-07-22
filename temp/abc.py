n = int(input())
s = input()

def abc(n,s):
    count = []
    for i in range(len(s)):
        count.append(s[i])
    if 'A' in count and 'B' in count and 'C' in count:
        return i 
print(abc(n, s))

n = int(input())
s = input()

def abc2(n,s):
    count = {'A': 0, 'B': 0, 'C': 0}
    for i in range(len(s)):
        count[s[i]] += 1
        if count['A'] > 0 and count['B'] > 0 and count['C'] > 0:
            return i + 1 # pythonのインデックスは0から始まるので1を足す
    return -1 # A, B, Cが全て出現しなかった場合

print(abc2(n, s))

n = int(input())
s = input()

def abc3(n,s):
    count_a = 0
    count_b = 0
    count_c = 0
    for i in range(n): 
        if s[i] == 'A':
            count_a += 1
        elif s[i] == 'B':
            count_b += 1
        elif s[i] == 'C':
            count_c += 1
        if count_a >= 1 and count_b >= 1 and count_c >= 1: 
            return i + 1 # Pythonのインデックスは0から始まるので1を足す
    return -1 # A, B, Cが全て出現しなかった場合

print(abc3(n, s))


"""<?php

function abc($s) {
    $count_a = 0;
    $count_b = 0;
    $count_c = 0;
    $n = strlen($s);
    for ($i = 0; $i < $n; $i++) {
        if ($s[$i] == 'A') {
            $count_a += 1;
        } elseif ($s[$i] == 'B') {
            $count_b += 1;
        } elseif ($s[$i] == 'C') {
            $count_c += 1;
        }
        if ($count_a >= 1 && $count_b >= 1 && $count_c >= 1) {
            // PHPのインデックスも0から始まるので1を足す
            return $i + 1;
        }
    }
    // A, B, Cが全て出現しなかった場合
    return -1;
}

$s = trim(fgets(STDIN));
echo abc($s), "\n";
?>
"""
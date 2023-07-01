"""s = [int(input()) for _ in range(8)]

def new_scheme():
    if (s[0] >= 100) and (s[0] <= 675) and (s[0] % 25 == 0):
        for i in range(1,9):
            if (s[i] < 100) and (s[i] > 675) and (s[i] % 25 != 0) and (s[i] < s[i-1]):
                return 'No'
            else: 
                return 'Yes'
    else:
        return 'No'
    
print(new_scheme())

def new_scheme():
     for i in s:
          if (i < 100) and (i > 675) and (i % 25 != 0) and (s.sort):
              return 'No'
          else: 
              return 'Yes'
    
print(new_scheme())
"""
def check_conditions(numbers):
    if numbers != sorted(numbers):
        return 'No'

    if not all(100 <= num <= 675 for num in numbers):
        return 'No'

    if not all(num % 25 == 0 for num in numbers):
        return 'No'
    
    return 'Yes'

numbers = list(map(int, input().split()))

print(check_conditions(numbers))

"""
php

<?php

// 関数check_conditionsを定義します。この関数は、引数として配列numbersを受け取ります。
function check_conditions($numbers) {
    // 配列numbersのコピーを作ります。
    $sortedNumbers = $numbers;
    // コピーした配列をソートします。
    sort($sortedNumbers);
    // もしソート前の配列とソート後の配列が一致しなければ、'No'を返します。
    // これは配列が単調増加であることを確認するためのステップです。
    if ($numbers !== $sortedNumbers) {
        return 'No';
    }
    
    // すべての数が100以上675以下であることを確認します。
    // 違反があれば、'No'を返します。
    foreach ($numbers as $num) {
        if ($num < 100 || $num > 675) {
            return 'No';
        }
    }
    
    // すべての数が25の倍数であることを確認します。
    // 違反があれば、'No'を返します。
    foreach ($numbers as $num) {
        if ($num % 25 != 0) {
            return 'No';
        }
    }
    
    // すべてのチェックがパスすれば、'Yes'を返します。
    return 'Yes';
}

// 標準入力から数値を受け取ります。
$numbers = explode(" ", trim(fgets(STDIN)));

// 受け取った数値を整数に変換します。
foreach ($numbers as $index => $num) {
    $numbers[$index] = (int) $num;
}

// check_conditions関数を呼び出し、その結果を出力します。
echo check_conditions($numbers);

?>


"""

"""
c++

#include <iostream>
#include <vector>
#include <algorithm>

// 条件をチェックする関数を定義します。
bool check_conditions(std::vector<int> &numbers) {
    // 配列が単調増加であることを確認します。
    if (!std::is_sorted(numbers.begin(), numbers.end())) {
        return false;
    }

    // すべての数が100以上675以下であることを確認します。
    for (int num : numbers) {
        if (num < 100 || num > 675) {
            return false;
        }
    }

    // すべての数が25の倍数であることを確認します。
    for (int num : numbers) {
        if (num % 25 != 0) {
            return false;
        }
    }

    // すべてのチェックがパスした場合はtrueを返します。
    return true;
}

int main() {
    std::vector<int> numbers(8);  // 8つの整数を格納するためのベクトルを定義します。

    // 標準入力から8つの整数を読み取ります。
    for (int i = 0; i < 8; i++) {
        std::cin >> numbers[i];
    }

    // check_conditions関数を呼び出します。
    if (check_conditions(numbers)) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }

    return 0;
}

"""

"""
java

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 標準入力から8つの整数を読み込むためのScannerを作成します。
        Scanner scanner = new Scanner(System.in);
        int[] numbers = new int[8];

        // 標準入力から8つの整数を読み込みます。
        for (int i = 0; i < 8; i++) {
            numbers[i] = scanner.nextInt();
        }

        // checkConditionsメソッドを呼び出します。
        if (checkConditions(numbers)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

    // 条件をチェックする関数を定義します。
    public static boolean checkConditions(int[] numbers) {
        // 配列が単調増加であることを確認します。
        for (int i = 0; i < numbers.length - 1; i++) {
            if (numbers[i] > numbers[i + 1]) {
                return false;
            }
        }

        // すべての数が100以上675以下であることを確認します。
        for (int num : numbers) {
            if (num < 100 || num > 675) {
                return false;
            }
        }

        // すべての数が25の倍数であることを確認します。
        for (int num : numbers) {
            if (num % 25 != 0) {
                return false;
            }
        }

        // すべてのチェックがパスした場合はtrueを返します。
        return true;
    }
}
"""
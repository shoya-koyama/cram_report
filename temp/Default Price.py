def calculate_total_price(N, M, C, D, P):
    total_price = 0  # 合計金額を0で初期化

    # 高橋くんが食べた各皿について
    for i in range(N):
        # その皿の色が価格が定義されている色かどうかを確認
        if C[i] in D:
            # 定義されている色ならその価格を合計に加える
            color_index = D.index(C[i])
            total_price += P[color_index + 1]  # P[0]は定義されていない色なので +1 する
        else:
            # 定義されていない色ならP[0]を合計に加える
            total_price += P[0]

    return total_price


"""
php

<?php

function calculate_total_price($N, $M, $C, $D, $P) {
    $total_price = 0;  // 合計金額を0で初期化

    // 高橋くんが食べた各皿について
    for ($i = 0; $i < $N; $i++) {
        // その皿の色が価格が定義されている色かどうかを確認
        $color_index = array_search($C[$i], $D);
        if ($color_index !== false) {
            // 定義されている色ならその価格を合計に加える
            $total_price += $P[$color_index + 1];  // $P[0]は定義されていない色なので +1 する
        } else {
            // 定義されていない色なら$P[0]を合計に加える
            $total_price += $P[0];
        }
    }

    return $total_price;
}

?>
"""

import numpy as np
import matplotlib.pyplot as plt

f = 800 
hm = 1.5  
hb = [30, 120, 180] 
d = np.linspace(1, 10, 100)

def okumura_hata(d, f, hb, hm):
    ahr = (1.1 * np.log10(f) - 0.7) * hm - (1.56 * np.log10(f) - 0.8)
    return 69.55 + 26.16 * np.log10(f) - 13.82 * np.log10(hb) + (44.9 - 6.55 * np.log10(hb)) * np.log10(d) - ahr

# Calculate loss for each base station antenna height
l = [okumura_hata(d, f, h, hm) for h in hb]

# Plot
plt.figure(figsize=(10, 6))
for i, loss in enumerate(l):
    plt.plot(d, loss, label=f'hb = {hb[i]} m')
plt.xscale('log')
plt.xlabel('d (km)')
plt.ylabel('Loss (dB)')
plt.title('Loss : d Okumura-Hata')
plt.legend()
plt.grid(True)
plt.show()

# 商品情報を設定する
products = [
    {"name": "ヤクルト", "price": 120, "stock": 5},
    {"name": "ポテチ", "price": 100, "stock": 8},
    {"name": "ショコラ", "price": 150, "stock": 3}
]

# 合計金額を初期化する
total_price = 0

# レジを開始する
while True:
    # 入力された商品番号を取得する
    print("商品番号を選択してください")
    for i, product in enumerate(products):
        print("{0}: {1} ({2}円, 在庫{3}個)".format(i, product["name"], product["price"], product["stock"]))
    choice = input("> ")

    # 終了する
    if choice == "q":
        print("合計金額は{0}円です。".format(total_price))
        break

    # 選択された商品の情報を取得する
    try:
        choice = int(choice)
        product = products[choice]
    except:
        print("商品番号が正しくありません。")
        continue

    # 在庫を確認する
    if product["stock"] <= 0:
        print("在庫がありません。別の商品を選択してください。")
        continue

    # 商品を購入する
    product["stock"] -= 1
    total_price += product["price"]
    print("{0}を購入しました。合計金額は{1}円です。".format(product["name"], total_price))
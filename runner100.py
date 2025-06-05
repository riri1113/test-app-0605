import random

# 日本人の名前リスト（例）
japanese_names = [
    "佐藤 大輔", "鈴木 一郎", "高橋 健太", "田中 翔太", "伊藤 直樹",
    "渡辺 拓海", "山本 大地", "中村 亮", "小林 悠斗", "加藤 颯太",
    "吉田 陸", "山田 智也", "佐々木 海斗", "山口 直人", "松本 優",
    "井上 大和", "木村 颯", "林 智樹", "斎藤 陽斗", "清水 直樹",
    "山崎 悠真", "森 拓真", "池田 陸斗", "橋本 智也", "阿部 大輔",
    "石川 颯太", "山下 拓海", "中島 大地", "小川 直樹", "前田 健太",
    "藤田 亮", "岡田 悠斗", "後藤 陸", "近藤 智也", "村上 大和",
    "遠藤 颯", "青木 智樹", "坂本 陽斗", "福田 直樹", "西村 優",
    "太田 大輔", "三浦 颯太", "藤井 拓海", "岡本 大地", "松田 直樹"
]

# 外国人の名前リスト（例）
foreign_names = [
    "John Smith", "Michael Johnson", "Usain Bolt", "Justin Gatlin", "Andre De Grasse"
]

# 選手リスト作成
athletes = []

# 日本人45人
for name in japanese_names[:45]:
    time = round(random.uniform(9.56, 12.99), 2)
    age = random.randint(20, 30)
    athletes.append({
        "name": name,
        "time": time,
        "age": age,
        "nationality": "日本"
    })

# 外国人5人
for name in foreign_names:
    time = round(random.uniform(9.56, 12.99), 2)
    age = random.randint(20, 30)
    athletes.append({
        "name": name,
        "time": time,
        "age": age,
        "nationality": "外国"
    })

# タイムが良い順に並び替え
athletes_sorted = sorted(athletes, key=lambda x: x["time"])

# 結果表示
print("順位 | 名前             | 国籍 | 年齢 | タイム")
print("-----------------------------------------------")
for i, athlete in enumerate(athletes_sorted, 1):
    print(f"{i:2d}   | {athlete['name']:<15} | {athlete['nationality']} | {athlete['age']}歳 | {athlete['time']}秒")
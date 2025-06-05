import random

# 英検1級レベルの単語リスト（例：単語, 正解, 選択肢3つ）
questions = [
    {"word": "aberration", "answer": "逸脱", "choices": ["逸脱", "模倣", "進化", "抑制"]},
    {"word": "acquiesce", "answer": "黙認する", "choices": ["黙認する", "拒否する", "説明する", "促進する"]},
    {"word": "belligerent", "answer": "好戦的な", "choices": ["好戦的な", "平和的な", "怠惰な", "誠実な"]},
    {"word": "cajole", "answer": "おだてる", "choices": ["おだてる", "非難する", "拒絶する", "許す"]},
    {"word": "debilitate", "answer": "衰弱させる", "choices": ["衰弱させる", "強化する", "修復する", "拡大する"]},
    {"word": "elucidate", "answer": "解明する", "choices": ["解明する", "隠す", "縮小する", "混乱させる"]},
    {"word": "fastidious", "answer": "気難しい", "choices": ["気難しい", "寛大な", "陽気な", "無関心な"]},
    {"word": "garrulous", "answer": "おしゃべりな", "choices": ["おしゃべりな", "無口な", "短気な", "慎重な"]},
    {"word": "harangue", "answer": "長々とした演説", "choices": ["長々とした演説", "短い挨拶", "秘密の会話", "歌"]},
    {"word": "iconoclast", "answer": "因習打破主義者", "choices": ["因習打破主義者", "伝統主義者", "平和主義者", "現実主義者"]},
    {"word": "juxtapose", "answer": "並べて置く", "choices": ["並べて置く", "隠す", "壊す", "混ぜる"]},
    {"word": "laconic", "answer": "簡潔な", "choices": ["簡潔な", "冗長な", "曖昧な", "明確な"]},
    {"word": "magnanimous", "answer": "寛大な", "choices": ["寛大な", "狭量な", "冷淡な", "短気な"]},
    {"word": "nefarious", "answer": "極悪な", "choices": ["極悪な", "善良な", "普通の", "愚かな"]},
    {"word": "obfuscate", "answer": "曖昧にする", "choices": ["曖昧にする", "明確にする", "強調する", "削除する"]},
    {"word": "palpable", "answer": "明白な", "choices": ["明白な", "不明な", "微妙な", "隠れた"]},
    {"word": "quixotic", "answer": "非現実的な", "choices": ["非現実的な", "現実的な", "論理的な", "冷静な"]},
    {"word": "rancor", "answer": "憎しみ", "choices": ["憎しみ", "愛情", "友情", "尊敬"]},
    {"word": "sagacious", "answer": "賢明な", "choices": ["賢明な", "愚かな", "無知な", "怠惰な"]},
    {"word": "tantamount", "answer": "同等の", "choices": ["同等の", "異なる", "劣る", "優れる"]},
    {"word": "ubiquitous", "answer": "至る所にある", "choices": ["至る所にある", "珍しい", "限定的な", "隠れた"]},
    {"word": "vacillate", "answer": "ためらう", "choices": ["ためらう", "決断する", "進む", "止まる"]},
    {"word": "wary", "answer": "用心深い", "choices": ["用心深い", "無防備な", "大胆な", "怠惰な"]},
    {"word": "yoke", "answer": "束縛する", "choices": ["束縛する", "解放する", "助ける", "隠す"]},
    {"word": "zealous", "answer": "熱心な", "choices": ["熱心な", "冷淡な", "怠惰な", "無関心な"]},
    # ... 必要に応じて追加 ...
]

# 50問に満たない場合はランダムに重複して出題
while len(questions) < 50:
    q = random.choice(questions)
    questions.append(q.copy())

random.shuffle(questions)
score = 0

for i, q in enumerate(questions[:50], 1):
    choices = q["choices"].copy()
    random.shuffle(choices)
    print(f"\n第{i}問: {q['word']} の意味は？")
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")
    ans = input("番号で答えてください: ")
    try:
        if choices[int(ans)-1] == q["answer"]:
            print("正解！")
            score += 1
        else:
            print(f"不正解。正解は「{q['answer']}」です。")
    except:
        print(f"入力エラー。正解は「{q['answer']}」です。")

print(f"\nあなたの正解数: {score}/50")
if score >= 35:
    print("合格です！おめでとうございます。")
else:
    print("不合格です。再挑戦しましょう。")
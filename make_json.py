import os
import json

# 設定：現在の総問題数
TOTAL_QUESTIONS = 11

quiz_list = []

for i in range(1, TOTAL_QUESTIONS + 1):
    q_id = i
    folder_name = f"q{q_id}"
    
    # 各ファイルのパスを設定
    text_path = os.path.join(folder_name, f"q{q_id}_text.txt")
    hint1_path = os.path.join(folder_name, f"q{q_id}_hint1.txt")
    hint2_path = os.path.join(folder_name, f"q{q_id}_hint2.txt")
    
    # デフォルト値（ファイルがない場合の保険）
    question_text = f"もんだい {q_id} のテキストがみつかりません。"
    hint1_text = "よくよんでみよう！"
    hint2_text = "もういちどチャレンジ！"
    
    # 問題文の読み込み
    if os.path.exists(text_path):
        with open(text_path, "r", encoding="utf-8") as f:
            question_text = f.read().strip()
            
    # ヒント1の読み込み
    if os.path.exists(hint1_path):
        with open(hint1_path, "r", encoding="utf-8") as f:
            hint1_text = f.read().strip()
            
    # ヒント2の読み込み
    if os.path.exists(hint2_path):
        with open(hint2_path, "r", encoding="utf-8") as f:
            hint2_text = f.read().strip()
            
    # 新しいデータ構造のオブジェクトを組み立て
    quiz_data = {
        "id": q_id,
        "questionText": question_text,
        "hint1": hint1_text,
        "hint2": hint2_text,
        "choices": {
            "correct": f"q{q_id}/correct_q{q_id}.png",
            "wrong1": f"q{q_id}/wrong1_q{q_id}.png",
            "wrong2": f"q{q_id}/wrong2_q{q_id}.png"
        }
    }
    
    quiz_list.append(quiz_data)

# 新しい構造の quiz.json として上書き保存
output_path = "quiz.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(quiz_list, f, ensure_ascii=False, indent=2)

print(f"✨ 成功しました！ {TOTAL_QUESTIONS}問分のデータを集計して 'quiz.json' を新しく作成しました。")

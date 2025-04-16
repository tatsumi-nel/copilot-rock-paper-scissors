import random

def play_game():
    """
    じゃんけんゲームをプレイする関数
    """
    choices = ["グー", "チョキ", "パー"]
    
    print("じゃんけんゲームへようこそ！")
    print("0: グー, 1: チョキ, 2: パー, q: 終了")
    
    while True:
        # ユーザーの選択を取得
        user_input = input("\nあなたの選択は？ (0/1/2/q): ")
        
        # 終了条件
        if user_input.lower() == 'q':
            print("ゲームを終了します。また遊んでね！")
            break
        
        # 入力の検証
        if user_input not in ["0", "1", "2"]:
            print("無効な入力です。0, 1, 2, または q を入力してください。")
            continue
        
        # 選択を数値に変換
        user_choice = int(user_input)
        
        # コンピューターの選択
        computer_choice = random.randint(0, 2)
        
        # 選択を表示
        print(f"\nあなた: {choices[user_choice]}")
        print(f"コンピューター: {choices[computer_choice]}")
        
        # 勝者を決定
        if user_choice == computer_choice:
            print("引き分けです！")
        elif (user_choice == 0 and computer_choice == 1) or \
             (user_choice == 1 and computer_choice == 2) or \
             (user_choice == 2 and computer_choice == 0):
            print("あなたの勝ちです！")
        else:
            print("コンピューターの勝ちです！")

if __name__ == "__main__":
    play_game()
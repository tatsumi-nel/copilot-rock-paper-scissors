import random

def get_user_choice():
    """
    ユーザーの選択を取得する関数
    """
    print("じゃんけんゲーム - Rock, Paper, Scissors, Lizard, Spock")
    print("以下から選択してください:")
    print("1. Rock (グー)")
    print("2. Paper (パー)")
    print("3. Scissors (チョキ)")
    print("4. Lizard")
    print("5. Spock")
    
    while True:
        choice = input("選択肢を入力してください (1-5): ")
        choices = {
            '1': 'rock',
            '2': 'paper',
            '3': 'scissors',
            '4': 'lizard',
            '5': 'spock'
        }
        
        if choice in choices:
            return choices[choice]
        else:
            print("無効な選択です。1から5の数字を入力してください。")

def get_computer_choice():
    """
    コンピューターの選択をランダムに生成する関数
    """
    return random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])

def determine_winner(user_choice, computer_choice):
    """
    勝敗を判定する関数
    """
    if user_choice == computer_choice:
        return "引き分け"
    
    # 勝敗ルール
    winning_rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['rock', 'scissors']
    }
    
    if computer_choice in winning_rules[user_choice]:
        return "あなたの勝ち"
    else:
        return "コンピューターの勝ち"

def display_result(user_choice, computer_choice, result):
    """
    結果を表示する関数
    """
    choice_jp = {
        'rock': 'グー (Rock)',
        'paper': 'パー (Paper)',
        'scissors': 'チョキ (Scissors)',
        'lizard': 'リザード (Lizard)',
        'spock': 'スポック (Spock)'
    }
    
    print(f"\nあなたの選択: {choice_jp[user_choice]}")
    print(f"コンピューターの選択: {choice_jp[computer_choice]}")
    print(f"結果: {result}\n")

def play_game():
    """
    ゲームのメイン関数
    """
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    
    play_again = input("もう一度プレイしますか？ (y/n): ").lower()
    if play_again == 'y':
        play_game()

if __name__ == "__main__":
    play_game()

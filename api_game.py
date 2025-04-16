import random
from datetime import datetime

# 選択肢とその表示名
CHOICES = {
    'rock': 'グー (Rock)',
    'paper': 'パー (Paper)',
    'scissors': 'チョキ (Scissors)',
    'lizard': 'リザード (Lizard)',
    'spock': 'スポック (Spock)'
}

# 勝敗ルール
RULES = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

def get_computer_choice():
    """
    コンピューターの選択をランダムに生成する関数
    
    Returns:
        str: コンピュータの選択（rock, paper, scissors, lizard, spock）
    """
    return random.choice(list(CHOICES.keys()))

def determine_winner(user_choice, computer_choice):
    """
    勝敗を判定する関数
    
    Args:
        user_choice (str): ユーザーの選択
        computer_choice (str): コンピュータの選択
    
    Returns:
        str: 勝敗結果（"あなたの勝ち", "コンピューターの勝ち", "引き分け"）
    """
    if user_choice == computer_choice:
        return "引き分け"
    
    if computer_choice in RULES[user_choice]:
        return "あなたの勝ち"
    else:
        return "コンピューターの勝ち"

def play_game(user_choice):
    """
    ゲームを実行する関数
    
    Args:
        user_choice (str): ユーザーの選択
    
    Returns:
        dict: ゲーム結果を含む辞書
    """
    # 選択肢の検証
    if user_choice not in CHOICES:
        raise ValueError(f"無効な選択です: {user_choice}。有効な選択: {', '.join(CHOICES.keys())}")
    
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    
    # 結果を辞書形式で返す
    return {
        "player_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
        "timestamp": datetime.now().isoformat()
    }

def get_choices():
    """
    選択肢の一覧を取得する関数
    
    Returns:
        list: 選択肢のリスト（辞書形式）
    """
    return [{"id": key, "name": value} for key, value in CHOICES.items()]

def get_rules():
    """
    ゲームルールを取得する関数
    
    Returns:
        dict: ゲームルールを含む辞書
    """
    return {
        "rules": RULES,
        "description": "各選択肢は、配列内の選択肢に対して勝利します"
    }
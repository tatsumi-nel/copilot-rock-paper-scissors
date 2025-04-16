import pytest
from unittest.mock import patch
import game

def test_determine_winner_draw():
    """引き分けのケースをテスト"""
    assert game.determine_winner('rock', 'rock') == "引き分け"
    assert game.determine_winner('paper', 'paper') == "引き分け"
    assert game.determine_winner('scissors', 'scissors') == "引き分け"
    assert game.determine_winner('lizard', 'lizard') == "引き分け"
    assert game.determine_winner('spock', 'spock') == "引き分け"

def test_determine_winner_rock():
    """Rockの勝ち負けのケースをテスト"""
    # Rockが勝つケース
    assert game.determine_winner('rock', 'scissors') == "あなたの勝ち"
    assert game.determine_winner('rock', 'lizard') == "あなたの勝ち"
    
    # Rockが負けるケース
    assert game.determine_winner('rock', 'paper') == "コンピューターの勝ち"
    assert game.determine_winner('rock', 'spock') == "コンピューターの勝ち"

def test_determine_winner_paper():
    """Paperの勝ち負けのケースをテスト"""
    # Paperが勝つケース
    assert game.determine_winner('paper', 'rock') == "あなたの勝ち"
    assert game.determine_winner('paper', 'spock') == "あなたの勝ち"
    
    # Paperが負けるケース
    assert game.determine_winner('paper', 'scissors') == "コンピューターの勝ち"
    assert game.determine_winner('paper', 'lizard') == "コンピューターの勝ち"

def test_determine_winner_scissors():
    """Scissorsの勝ち負けのケースをテスト"""
    # Scissorsが勝つケース
    assert game.determine_winner('scissors', 'paper') == "あなたの勝ち"
    assert game.determine_winner('scissors', 'lizard') == "あなたの勝ち"
    
    # Scissorsが負けるケース
    assert game.determine_winner('scissors', 'rock') == "コンピューターの勝ち"
    assert game.determine_winner('scissors', 'spock') == "コンピューターの勝ち"

def test_determine_winner_lizard():
    """Lizardの勝ち負けのケースをテスト"""
    # Lizardが勝つケース
    assert game.determine_winner('lizard', 'paper') == "あなたの勝ち"
    assert game.determine_winner('lizard', 'spock') == "あなたの勝ち"
    
    # Lizardが負けるケース
    assert game.determine_winner('lizard', 'rock') == "コンピューターの勝ち"
    assert game.determine_winner('lizard', 'scissors') == "コンピューターの勝ち"

def test_determine_winner_spock():
    """Spockの勝ち負けのケースをテスト"""
    # Spockが勝つケース
    assert game.determine_winner('spock', 'rock') == "あなたの勝ち"
    assert game.determine_winner('spock', 'scissors') == "あなたの勝ち"
    
    # Spockが負けるケース
    assert game.determine_winner('spock', 'paper') == "コンピューターの勝ち"
    assert game.determine_winner('spock', 'lizard') == "コンピューターの勝ち"

@patch('random.choice')
def test_get_computer_choice(mock_choice):
    """コンピュータの選択をテスト"""
    mock_choice.return_value = 'rock'
    assert game.get_computer_choice() == 'rock'
    mock_choice.assert_called_with(['rock', 'paper', 'scissors', 'lizard', 'spock'])

@patch('builtins.input')
def test_get_user_choice(mock_input):
    """ユーザー入力をテスト"""
    # 正常入力のケース
    mock_input.return_value = '1'
    assert game.get_user_choice() == 'rock'
    
    mock_input.return_value = '2'
    assert game.get_user_choice() == 'paper'
    
    mock_input.return_value = '3'
    assert game.get_user_choice() == 'scissors'
    
    mock_input.return_value = '4'
    assert game.get_user_choice() == 'lizard'
    
    mock_input.return_value = '5'
    assert game.get_user_choice() == 'spock'

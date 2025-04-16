// APIエンドポイントの基本URL（必要に応じて変更してください）
const API_BASE_URL = 'http://localhost:3000';

// DOM要素の参照
const choiceButtonsContainer = document.getElementById('choice-buttons');
const playerChoiceText = document.getElementById('player-choice-text');
const computerChoiceText = document.getElementById('computer-choice-text');
const resultText = document.getElementById('result-text');
const playerImage = document.getElementById('player-image');
const computerImage = document.getElementById('computer-image');
const errorMessage = document.getElementById('error-message');
const rulesButton = document.getElementById('rules-btn');
const rulesModal = document.getElementById('rules-modal');
const rulesText = document.getElementById('rules-text');
const closeButton = document.querySelector('.close');

// 選択肢の情報を保持するオブジェクト
let choices = {};

// ページ読み込み時の初期化
document.addEventListener('DOMContentLoaded', () => {
    // 選択肢情報を取得する
    fetchChoices();
    
    // ルール情報を取得する
    fetchRules();
    
    // モーダルのイベントリスナーを設定
    setupModalListeners();
});

// 選択肢を取得して表示する関数
async function fetchChoices() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/choices`);
        
        if (!response.ok) {
            throw new Error('選択肢情報の取得に失敗しました');
        }
        
        const data = await response.json();
        choices = data.choices;
        
        // 選択肢ボタンを生成
        createChoiceButtons(choices);
    } catch (error) {
        console.error('エラー:', error);
        showError('選択肢情報の読み込みに失敗しました。ページを再読み込みしてください。');
    }
}

// ルール情報を取得する関数
async function fetchRules() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/rules`);
        
        if (!response.ok) {
            throw new Error('ルール情報の取得に失敗しました');
        }
        
        const data = await response.json();
        displayRules(data);
    } catch (error) {
        console.error('エラー:', error);
        // ルールの取得に失敗してもゲームは続行できるため、エラー表示はしない
    }
}

// 選択肢ボタンを生成する関数
function createChoiceButtons(choices) {
    choiceButtonsContainer.innerHTML = '';
    
    choices.forEach(choice => {
        const button = document.createElement('button');
        button.className = 'choice-button';
        button.dataset.choice = choice.id;
        
        const img = document.createElement('img');
        // アセットファイルパスを修正
        img.src = `assets/images/${choice.id}.jpg`;
        img.alt = choice.name;
        
        const span = document.createElement('span');
        span.textContent = choice.name;
        
        button.appendChild(img);
        button.appendChild(span);
        
        button.addEventListener('click', () => playGame(choice.id));
        
        choiceButtonsContainer.appendChild(button);
    });
}

// ゲームをプレイする関数
async function playGame(playerChoice) {
    try {
        // 結果テキストをリセット
        resultText.textContent = '処理中...';
        resultText.className = '';
        
        // プレイヤーの選択を表示
        const playerChoiceObj = choices.find(c => c.id === playerChoice);
        playerChoiceText.textContent = playerChoiceObj.name;
        playerImage.src = `assets/images/${playerChoice}.jpg`;
        playerImage.alt = playerChoiceObj.name;
        playerImage.style.display = 'block';
        
        // コンピューターの選択をリセット
        computerChoiceText.textContent = '選択中...';
        computerImage.style.display = 'none';
        
        // APIに選択を送信
        const response = await fetch(`${API_BASE_URL}/api/play`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ choice: playerChoice })
        });
        
        if (!response.ok) {
            throw new Error('ゲームの実行に失敗しました');
        }
        
        const gameResult = await response.json();
        
        // 結果表示
        displayResult(gameResult);
    } catch (error) {
        console.error('エラー:', error);
        showError('ゲームの実行中にエラーが発生しました。再度お試しください。');
    }
}

// 結果を表示する関数
function displayResult(result) {
    // コンピューターの選択を表示
    const computerChoiceObj = choices.find(c => c.id === result.computer_choice);
    computerChoiceText.textContent = computerChoiceObj.name;
    computerImage.src = `assets/images/${result.computer_choice}.jpg`;
    computerImage.alt = computerChoiceObj.name;
    computerImage.style.display = 'block';
    
    // 勝敗結果を表示
    resultText.textContent = result.result;
    
    // 勝敗に応じたクラスを設定
    if (result.result.includes('あなたの勝ち')) {
        resultText.className = 'win';
    } else if (result.result.includes('コンピューターの勝ち')) {
        resultText.className = 'lose';
    } else {
        resultText.className = 'draw';
    }
}

// ルール情報を表示する関数
function displayRules(rulesData) {
    const rulesHtml = `
        <p>各選択肢は以下の選択肢に対して勝利します：</p>
        <ul class="rules-list">
            ${Object.entries(rulesData.rules).map(([key, defeats]) => `
                <li><strong>${getChoiceName(key)}</strong> は ${defeats.map(d => getChoiceName(d)).join(' と ')} に勝ちます</li>
            `).join('')}
        </ul>
        <p>${rulesData.description}</p>
    `;
    
    rulesText.innerHTML = rulesHtml;
}

// 選択肢IDから名前を取得する関数
function getChoiceName(id) {
    const choice = choices.find(c => c.id === id);
    return choice ? choice.name : id;
}

// エラーを表示する関数
function showError(message) {
    errorMessage.querySelector('p').textContent = message;
    errorMessage.style.display = 'block';
    
    // 5秒後に非表示にする
    setTimeout(() => {
        errorMessage.style.display = 'none';
    }, 5000);
}

// モーダルウィンドウのイベントリスナーを設定する関数
function setupModalListeners() {
    // ルールボタンクリックでモーダルを表示
    rulesButton.addEventListener('click', () => {
        rulesModal.style.display = 'block';
    });
    
    // 閉じるボタンでモーダルを非表示
    closeButton.addEventListener('click', () => {
        rulesModal.style.display = 'none';
    });
    
    // モーダル外クリックで非表示
    window.addEventListener('click', (event) => {
        if (event.target === rulesModal) {
            rulesModal.style.display = 'none';
        }
    });
}

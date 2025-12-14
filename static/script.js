// Переменные состояния
let startTimeStamp = null;
let wasRunning = null;

// DOM элементы
const mainBtn = document.getElementById('mainBtn');
const reloadBtn = document.getElementById('reloadBtn');
const btnText = mainBtn.querySelector('.btn-text');
const btnIcon = mainBtn.querySelector('.btn-icon');
const statusIndicator = document.getElementById('statusIndicator');
const statusText = document.getElementById('statusText');
const messageLog = document.getElementById('messageLog');
const timerDisplay = document.getElementById('sessionTimer');
const launchCountDisplay = document.getElementById('launchCount');
const pingStat = document.getElementById('pingStat');

// Добавляем новый элемент для управления
const serverStatus = document.getElementById('serverStatus'); 

// --- ОСНОВНОЙ ЦИКЛ ---
document.addEventListener('DOMContentLoaded', () => {
    fetchStatus();
    setInterval(fetchStatus, 2000);
    setInterval(updateLocalTimer, 1000);
});

// Обработчик кнопки перезагрузки
reloadBtn.addEventListener('click', () => {
    window.location.reload();
});

async function fetchStatus() {
    try {
        const response = await fetch('/get-status');
        
        if (!response.ok) throw new Error("Server Error");
        
        const data = await response.json();

        // СВЯЗЬ УСПЕШНА: Убираем режим ошибки
        disableErrorMode(); 

        launchCountDisplay.textContent = data.launches;
        pingStat.textContent = data.ping;
        startTimeStamp = data.start_time;

        // Логика обновления статуса игры
        if (wasRunning === null) {
            if (data.running) {
                updateLog("Сессия активна");
                setUiRunning();
            } else {
                updateLog("Готов к запуску...");
                setUiStopped();
            }
        } else if (wasRunning !== data.running) {
            if (data.running) {
                updateLog("CS2 успешно запущена");
                setUiRunning();
            } else {
                updateLog("Игра закрыта. Готов к запуску...");
                setUiStopped();
            }
        }
        wasRunning = data.running;

    } catch (error) {
        console.error("Ошибка связи:", error);
        // СВЯЗЬ ПОТЕРЯНА: Включаем режим ошибки
        enableErrorMode();
    }
}

// --- РЕЖИМЫ ИНТЕРФЕЙСА ---

function enableErrorMode() {
    // Обновление общего статуса
    statusText.textContent = "CONN. ERROR";
    pingStat.textContent = "ERR";
    
    // Обновление карточки "Статус Сервера"
    serverStatus.textContent = "ERROR"; 
    
    // Блокируем и меняем вид главной кнопки
    mainBtn.disabled = true;
    btnText.textContent = "НЕТ СВЯЗИ";
    
    // Показываем кнопку перезагрузки
    reloadBtn.style.display = 'flex';
    
    updateLog("Потеряна связь с сервером");
    statusIndicator.classList.remove('active');
    document.querySelector('.dot').style.backgroundColor = '#ef4444';
}

function disableErrorMode() {
    // Если мы выходим из режима ошибки
    if (statusText.textContent === "CONN. ERROR") {
        mainBtn.disabled = false;
        reloadBtn.style.display = 'none'; 
        document.querySelector('.dot').style.backgroundColor = '';
        
        // Устанавливаем статус сервера как ACTIVE (т.к. запрос успешно прошел)
        serverStatus.textContent = 'ACTIVE'; 
    } else if (serverStatus.textContent !== 'ACTIVE') {
         // Устанавливаем ACTIVE при первой успешной загрузке
         serverStatus.textContent = 'ACTIVE';
    }
}

// --- ОБРАБОТЧИК ГЛАВНОЙ КНОПКИ ---
mainBtn.addEventListener('click', async () => {
    mainBtn.disabled = true; 
    
    const isStopAction = mainBtn.classList.contains('stop');
    const endpoint = isStopAction ? '/stop-cs2' : '/start-cs2';

    updateLog(isStopAction ? "Завершение процесса..." : "Отправка команды запуска...");

    try {
        const response = await fetch(endpoint, { method: 'POST' });
        const result = await response.json();
        
        if (!result.success) {
            updateLog("Ошибка: " + (result.message || result.error));
        }
    } catch (e) {
        enableErrorMode();
    }
    
    setTimeout(() => { 
        if (statusText.textContent !== "CONN. ERROR") {
            mainBtn.disabled = false; 
        }
    }, 500);
});

// --- ОСТАЛЬНЫЕ ФУНКЦИИ UI (БЕЗ ИЗМЕНЕНИЙ) ---

function setUiRunning() {
    if (mainBtn.classList.contains('stop')) return;
    mainBtn.classList.remove('start');
    mainBtn.classList.add('stop');
    btnText.textContent = "ОСТАНОВИТЬ ИГРУ";
    btnIcon.textContent = "■";
    statusIndicator.classList.add('active');
    statusText.textContent = "ONLINE";
}

function setUiStopped() {
    if (mainBtn.classList.contains('start')) return;
    mainBtn.classList.remove('stop');
    mainBtn.classList.add('start');
    btnText.textContent = "ЗАПУСТИТЬ CS2";
    btnIcon.textContent = "▶";
    statusIndicator.classList.remove('active');
    statusText.textContent = "OFFLINE";
    timerDisplay.textContent = "00:00:00";
}

function updateLocalTimer() {
    if (!startTimeStamp) {
        timerDisplay.textContent = "00:00:00";
        return;
    }
    const now = Date.now() / 1000;
    const diff = Math.floor(now - startTimeStamp);
    if (diff < 0) return;

    const h = Math.floor(diff / 3600).toString().padStart(2, '0');
    const m = Math.floor((diff % 3600) / 60).toString().padStart(2, '0');
    const s = Math.floor(diff % 60).toString().padStart(2, '0');
    timerDisplay.textContent = `${h}:${m}:${s}`;
}

function updateLog(msg) {
    if (messageLog.textContent === msg) return;
    messageLog.style.opacity = 0;
    setTimeout(() => {
        messageLog.textContent = msg;
        messageLog.style.opacity = 1;
    }, 200);
}
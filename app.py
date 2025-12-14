import os
import json
import time
import subprocess
import re
import secrets
from functools import wraps
from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '97aszfg6h0ßa97hfAUSD7fghaü0f'  # ВАЖНО: Смените на случайную строку

STATS_FILE = 'stats.json'
CODES_FILE = 'codes.json'
ADMIN_PASSWORD = 'f5asd76gz8uh'  # ВАЖНО: Пароль для входа в админку

# --- Работа с данными ---

def load_json(filename, default):
    if not os.path.exists(filename):
        return default
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return default

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_codes():
    return load_json(CODES_FILE, {"codes": []})

def save_codes(data):
    save_json(CODES_FILE, data)

# --- Декоратор авторизации ---

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'authenticated' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin_auth' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- Системные функции (без изменений) ---

def get_real_ping():
    try:
        output = subprocess.check_output("ping -n 1 -w 1000 8.8.8.8", shell=True).decode('cp866', errors='ignore')
        match = re.search(r'(время|time)[=<](\d+)м?s?', output)
        if match:
            return f"{match.group(2)} ms"
        return "TIMEOUT"
    except Exception:
        return "OFFLINE"

def is_cs2_running():
    try:
        output = subprocess.check_output('tasklist /FI "IMAGENAME eq cs2.exe"', shell=True).decode('cp866', errors='ignore')
        return "cs2.exe" in output
    except:
        return False

# --- Маршруты Авторизации ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        code = request.form.get('code')
        
        # Проверка админа
        if code == ADMIN_PASSWORD:
            session['authenticated'] = True
            session['admin_auth'] = True
            return redirect(url_for('admin_panel'))
        
        # Проверка кодов доступа
        data = get_codes()
        valid_codes = [c['code'] for c in data['codes']]
        
        if code in valid_codes:
            session['authenticated'] = True
            session['user_code'] = code # Запоминаем, под каким кодом вошли
            return redirect(url_for('index'))
        else:
            error = "Неверный код доступа"
            
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# --- Админ Панель ---

@app.route('/admin')
@admin_required
def admin_panel():
    data = get_codes()
    return render_template('admin.html', codes=data['codes'])

@app.route('/admin/generate', methods=['POST'])
@admin_required
def generate_code():
    data = get_codes()
    # Генерируем красивый код вида XXXX-XXXX
    new_code = f"{secrets.token_hex(2).upper()}-{secrets.token_hex(2).upper()}"
    note = request.json.get('note', 'Друг')
    
    data['codes'].append({
        "code": new_code,
        "note": note,
        "created_at": time.strftime("%Y-%m-%d %H:%M")
    })
    save_codes(data)
    return jsonify({"success": True, "code": new_code})

@app.route('/admin/delete', methods=['POST'])
@admin_required
def delete_code():
    code_to_delete = request.json.get('code')
    data = get_codes()
    data['codes'] = [c for c in data['codes'] if c['code'] != code_to_delete]
    save_codes(data)
    return jsonify({"success": True})

# --- Основные Маршруты (Защищены) ---

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/get-status', methods=['GET'])
@login_required
def get_status():
    stats = load_json(STATS_FILE, {"launches": 0, "start_time": None})
    is_running = is_cs2_running()
    current_ping = get_real_ping()
    
    if is_running and stats['start_time'] is None:
        stats['start_time'] = time.time()
        save_json(STATS_FILE, stats)
    elif not is_running and stats['start_time'] is not None:
        stats['start_time'] = None
        save_json(STATS_FILE, stats)

    return jsonify({
        "running": is_running,
        "ping": current_ping,
        "launches": stats['launches'],
        "start_time": stats['start_time']
    })

@app.route('/start-cs2', methods=['POST'])
@login_required
def start_cs2():
    if is_cs2_running():
        return jsonify({"success": False, "message": "Игра уже запущена"})
    try:
        os.system("start steam://run/730")
        stats = load_json(STATS_FILE, {"launches": 0, "start_time": None})
        stats['launches'] += 1
        stats['start_time'] = time.time()
        save_json(STATS_FILE, stats)
        return jsonify({"success": True, "message": "Команда запуска отправлена"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route('/stop-cs2', methods=['POST'])
@login_required
def stop_cs2():
    try:
        os.system("taskkill /f /im cs2.exe")
        return jsonify({"success": True, "message": "Процесс завершен"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3654, threaded=True)
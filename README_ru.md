<h1 align="center">CS Launch</h1>
<div align="center">

[English](./README.md) | Русский

Небольшая утилита для запуска и мониторинга CS2 через веб-интерфейс.

![Release Download](https://img.shields.io/github/downloads/megatocha/cslaunch/total?style=for-the-badge&labelColor=fae5c0&color=%234caf50&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPg0KPHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0xNyAxN0gxNy4wMU0xNy40IDE0SDE4QzE4LjkzMTkgMTQgMTkuMzk3OCAxNCAxOS43NjU0IDE0LjE1MjJDMjAuMjU1NCAxNC4zNTUyIDIwLjY0NDggMTQuNzQ0NiAyMC44NDc4IDE1LjIzNDZDMjEgMTUuNjAyMiAyMSAxNi4wNjgxIDIxIDE3QzIxIDE3LjkzMTkgMjEgMTguMzk3OCAyMC44NDc4IDE4Ljc2NTRDMjAuNjQ0OCAxOS4yNTU0IDIwLjI1NTQgMTkuNjQ0OCAxOS43NjU0IDE5Ljg0NzhDMTkuMzk3OCAyMCAxOC45MzE5IDIwIDE4IDIwSDZDNS4wNjgxMiAyMCA0LjYwMjE4IDIwIDQuMjM0NjMgMTkuODQ3OEMzLjc0NDU4IDE5LjY0NDggMy4zNTUyMyAxOS4yNTU0IDMuMTUyMjQgMTguNzY1NEMzIDE4LjM5NzggMyAxNy45MzE5IDMgMTdDMyAxNi4wNjgxIDMgMTUuNjAyMiAzLjE1MjI0IDE1LjIzNDZDMy4zNTUyMyAxNC43NDQ2IDMuNzQ0NTggMTQuMzU1MiA0LjIzNDYzIDE0LjE1MjJDNC42MDIxOCAxNCA1LjA2ODEyIDE0IDYgMTRINi42TTEyIDE1VjRNMTIgMTVMOSAxMk0xMiAxNUwxNSAxMiIgc3Ryb2tlPSIjMDAwMDAwIiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIvPg0KPC9zdmc+)
[![GitHub License](https://img.shields.io/github/license/megatocha/cslaunch?style=for-the-badge&labelColor=fae5c0&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPg0KPHN2ZyB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4NCjxwYXRoIGQ9Ik0xOSAzSDlWM0M3LjExNDM4IDMgNi4xNzE1NyAzIDUuNTg1NzkgMy41ODU3OUM1IDQuMTcxNTcgNSA1LjExNDM4IDUgN1YxMC41VjE3IiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+DQo8cGF0aCBkPSJNMTQgMTdWMTlDMTQgMjAuMTA0NiAxNC44OTU0IDIxIDE2IDIxVjIxQzE3LjEwNDYgMjEgMTggMjAuMTA0NiAxOCAxOVY5VjQuNUMxOCAzLjY3MTU3IDE4LjY3MTYgMyAxOS41IDNWM0MyMC4zMjg0IDMgMjEgMy42NzE1NyAyMSA0LjVWNC41QzIxIDUuMzI4NDMgMjAuMzI4NCA2IDE5LjUgNkgxOC41IiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+DQo8cGF0aCBkPSJNMTYgMjFINUMzLjg5NTQzIDIxIDMgMjAuMTA0NiAzIDE5VjE5QzMgMTcuODk1NCAzLjg5NTQzIDE3IDUgMTdIMTQiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4NCjxwYXRoIGQ9Ik05IDdIMTQiIHN0cm9rZT0iIzAwMDAwMCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4NCjxwYXRoIGQ9Ik05IDExSDE0IiBzdHJva2U9IiMwMDAwMDAiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIi8+DQo8L3N2Zz4=)](LICENSE)
[![GitHub Star](https://img.shields.io/github/stars/megatocha/cslaunch?style=for-the-badge&labelColor=fae5c0&color=yellow&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPgo8c3ZnIHdpZHRoPSI4MDBweCIgaGVpZ2h0PSI4MDBweCIgdmlld0JveD0iMCAwIDM2IDM2IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiBhcmlhLWhpZGRlbj0idHJ1ZSIgcm9sZT0iaW1nIiBjbGFzcz0iaWNvbmlmeSBpY29uaWZ5LS10d2Vtb2ppIiBwcmVzZXJ2ZUFzcGVjdFJhdGlvPSJ4TWlkWU1pZCBtZWV0Ij48cGF0aCBmaWxsPSIjRkZBQzMzIiBkPSJNMjcuMjg3IDM0LjYyN2MtLjQwNCAwLS44MDYtLjEyNC0xLjE1Mi0uMzcxTDE4IDI4LjQyMmwtOC4xMzUgNS44MzRhMS45NyAxLjk3IDAgMCAxLTIuMzEyLS4wMDhhMS45NzEgMS45NzEgMCAwIDEtLjcyMS0yLjE5NGwzLjAzNC05Ljc5MmwtOC4wNjItNS42ODFhMS45OCAxLjk4IDAgMCAxLS43MDgtMi4yMDNhMS45NzggMS45NzggMCAwIDEgMS44NjYtMS4zNjNMMTIuOTQ3IDEzbDMuMTc5LTkuNTQ5YTEuOTc2IDEuOTc2IDAgMCAxIDMuNzQ5IDBMMjMgMTNsMTAuMDM2LjAxNWExLjk3NSAxLjk3NSAwIDAgMSAxLjE1OSAzLjU2NmwtOC4wNjIgNS42ODFsMy4wMzQgOS43OTJhMS45NyAxLjk3IDAgMCAxLS43MiAyLjE5NGExLjk1NyAxLjk1NyAwIDAgMS0xLjE2LjM3OXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/megatocha/cslaunch/stargazers)
![GitHub Repo size](https://img.shields.io/github/repo-size/megatocha/cslaunch?style=for-the-badge&color=3cb371&labelColor=fae5c0&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz48IS0tIFVwbG9hZGVkIHRvOiBTVkcgUmVwbywgd3d3LnN2Z3JlcG8uY29tLCBHZW5lcmF0b3I6IFNWRyBSZXBvIE1peGVyIFRvb2xzIC0tPg0KPHN2ZyBmaWxsPSIjMDAwMDAwIiB3aWR0aD0iODAwcHgiIGhlaWdodD0iODAwcHgiIHZpZXdCb3g9IjAgMCAzMiAzMiIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPg0KICAgIDxwYXRoIGQ9Ik0xMS45NzUgMTAuODM4bC0wLjAyMS03LjIxOWMtMC4wMDktMC40MDQtMC4zNDQtMC42NDQtMC43NDgtMC42NTRsLTAuNTEzLTAuMDAxYy0wLjQwNS0wLjAwOS0wLjcyNSAwLjM0My0wLjcxNiAwLjc0N2wwLjAyOCA0Ljg1MS04LjMyMS04LjI0MmMtMC4zOTEtMC4zOTEtMS4wMjQtMC4zOTEtMS40MTQgMHMtMC4zOTEgMS4wMjQgMCAxLjQxNGw4LjI4NSA4LjIwNy00LjcyMSAwLjAxMmMtMC40MDQtMC4wMDktMC43NzkgMC4yNy0wLjg0IDAuNzQ2bDAuMDAxIDAuNTEzYzAuMDEwIDAuNDA1IDAuMzQ0IDAuNzM5IDAuNzQ4IDAuNzQ4bDcuMTcyLTAuMDMxYzAuMDA4IDAuMDAxIDAuMDEzIDAuMDAzIDAuMDIwIDAuMDAzbDAuMzY2IDAuMDA4YzAuMjAxIDAuMDA1IDAuMzgzLTAuMDc0IDAuNTEyLTAuMjA1IDAuMTMyLTAuMTMgMC4xNzgtMC4zMTEgMC4xNzUtMC41MTRsLTAuMDQwLTAuMzY2YzAuMDAxLTAuMDA3IDAuMDI3LTAuMDEyIDAuMDI3LTAuMDE5ek0yMC4xODcgMTEuNzM2YzAuMTI5IDAuMTMgMC4zMTEgMC4yMSAwLjUxMiAwLjIwNWwwLjM2Ni0wLjAwOGMwLjAwNyAwIDAuMDEyLTAuMDAyIDAuMDIwLTAuMDA0bDcuMTcyIDAuMDMxYzAuNDA0LTAuMDA5IDAuNzM4LTAuMzQ0IDAuNzQ3LTAuNzQ4bDAuMDAxLTAuNTEzYy0wLjA2MS0wLjQ3Ni0wLjQzNi0wLjc1NS0wLjg0LTAuNzQ2bC00LjcyMS0wLjAxMiA4LjI4NS04LjIwN2MwLjM5MS0wLjM5MSAwLjM5MS0xLjAyNCAwLTEuNDE0cy0xLjAyMy0wLjM5MS0xLjQxNCAwbC04LjMyIDguMjQxIDAuMDI3LTQuODUxYzAuMDA5LTAuNDA0LTAuMzExLTAuNzU2LTAuNzE1LTAuNzQ3bC0wLjUxMyAwLjAwMWMtMC40MDUgMC4wMTAtMC43MzkgMC4yNS0wLjc0OCAwLjY1NGwtMC4wMjEgNy4yMTljMCAwLjAwNyAwLjAyNyAwLjAxMiAwLjAyNyAwLjAyMGwtMC4wNDAgMC4zNjZjLTAuMDA1IDAuMjAzIDAuMDQzIDAuMzg0IDAuMTc0IDAuNTE0ek0xMS44MTMgMjAuMjMyYy0wLjEzLTAuMTMxLTAuMzExLTAuMjEtMC41MTItMC4yMDVsLTAuMzY2IDAuMDA5Yy0wLjAwNyAwLTAuMDEyIDAuMDAzLTAuMDIwIDAuMDAzbC03LjE3My0wLjAzMmMtMC40MDQgMC4wMDktMC43MzggMC4zNDMtMC43NDggMC43NDdsLTAuMDAxIDAuNTE0YzAuMDYyIDAuNDc2IDAuNDM2IDAuNzU1IDAuODQgMC43NDVsNC43MjcgMC4wMTItOC4yOSA4LjIzOGMtMC4zOTEgMC4zOS0wLjM5MSAxLjAyMyAwIDEuNDE0czEuMDI0IDAuMzkgMS40MTQgMGw4LjMyMS04LjI2OC0wLjAyOCA0Ljg3OGMtMC4wMDkgMC40MDQgMC4zMTIgMC43NTYgMC43MTYgMC43NDdsMC41MTMtMC4wMDFjMC40MDUtMC4wMTAgMC43MzktMC4yNSAwLjc0OC0wLjY1NGwwLjAyMS03LjIxOWMwLTAuMDA3LTAuMDI3LTAuMDExLTAuMDI3LTAuMDE5bDAuMDQwLTAuMzk3YzAuMDA1LTAuMjAzLTAuMDQzLTAuMzg0LTAuMTc0LTAuNTE0ek0yMy40MzkgMjIuMDI4bDQuNzI3LTAuMDEyYzAuNDA0IDAuMDA5IDAuNzc5LTAuMjcgMC44NC0wLjc0NWwtMC4wMDEtMC41MTRjLTAuMDEwLTAuNDA0LTAuMzQ0LTAuNzM5LTAuNzQ4LTAuNzQ4aC03LjE3MmMtMC4wMDgtMC0wLjAxMy0wLjAwMy0wLjAyMC0wLjAwM2wtMC40MjgtMC4wMDljLTAuMjAxLTAuMDA2LTAuMzg0IDAuMTM2LTAuNTEyIDAuMjY3LTAuMTMxIDAuMTMtMC4xNzggMC4zMTEtMC4xNzQgMC41MTRsMC4wNDAgMC4zNjZjMCAwLjAwOC0wLjAyNyAwLjAxMi0wLjAyNyAwLjAxOWwwLjAyMSA3LjIxOWMwLjAwOSAwLjQwNCAwLjM0MyAwLjY0NCAwLjc0OCAwLjY1NGwwLjU0NCAwLjAwMWMwLjQwNCAwLjAwOSAwLjcyNS0wLjM0MyAwLjcxNS0wLjc0N2wtMC4wMjctNC44MjkgOC4zNTIgOC4yMmMwLjM5IDAuMzkxIDEuMDIzIDAuMzkxIDEuNDE0IDBzMC4zOTEtMS4wMjMgMC0xLjQxNHoiPjwvcGF0aD4NCjwvc3ZnPg==)
[![Release Version](https://img.shields.io/github/v/release/megatocha/cslaunch?style=for-the-badge&labelColor=fae5c0&logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBVcGxvYWRlZCB0bzogU1ZHIFJlcG8sIHd3dy5zdmdyZXBvLmNvbSwgR2VuZXJhdG9yOiBTVkcgUmVwbyBNaXhlciBUb29scyAtLT4NCjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+DQo8c3ZnIGZpbGw9IiMwMDAwMDAiIHZlcnNpb249IjEuMSIgaWQ9IkNhcGFfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgDQoJIHdpZHRoPSI4MDBweCIgaGVpZ2h0PSI4MDBweCIgdmlld0JveD0iMCAwIDQ2IDQ2IiB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxnPg0KCTxnPg0KCQk8cGF0aCBkPSJNMzYuNDU1LDE3LjA1NmgtMC4xNzRjLTEuNTc3LTYtNi44ODUtMTAuMTEzLTEzLjIwNy0xMC4xMTNzLTExLjYzLDQuMTEzLTEzLjIwNywxMC4xMTNIOS42OTMNCgkJCUM0LjM4MSwxNy4wNTYsMCwyMS42NzYsMCwyNi45ODl2Mi43NjJjMCw1LjMxMiw0LjM4MSw5LjMwNiw5LjY5Myw5LjMwNmgyNi43NjJjNS4zMTIsMCw5LjU0NS0zLjk5NCw5LjU0NS05LjMwN3YtMi43NjINCgkJCUM0NiwyMS42NzYsNDEuNzY4LDE3LjA1NiwzNi40NTUsMTcuMDU2eiBNMzEuNzM4LDIyLjU4M2wtOS42MjcsOS42MjhjLTAuODUxLDAuODUyLTIuMjI5LDAuODUyLTMuMDgsMGwtNC43NzItNC43NzENCgkJCWMtMC44NTEtMC44NTItMC44NTEtMi4yMjksMC4wMDEtMy4wOGMwLjg1LTAuODUyLDIuMjI5LTAuODUyLDMuMDc4LDBsMi44NDUsMi44NDRjMC4xMDMsMC4xMDQsMC4yNDMsMC4xNjEsMC4zODksMC4xNjENCgkJCXMwLjI4Ni0wLjA2LDAuMzg5LTAuMTYxbDcuNjk5LTcuN2MwLjQwOC0wLjQwOCwwLjk2Mi0wLjYzOCwxLjU0LTAuNjM4YzAuNTc3LDAsMS4xMzIsMC4yMjksMS41NCwwLjYzOQ0KCQkJQzMyLjU5LDIwLjM1NCwzMi41OSwyMS43MzMsMzEuNzM4LDIyLjU4M3oiLz4NCgk8L2c+DQo8L2c+DQo8L3N2Zz4=)](https://github.com/megatocha/cslaunch/releases/latest)

</div>

## ⚠️ Требования

- **Python 3.8+** (рекомендуется 3.11)
- **Docker & Docker Compose** (опционально, рекомендуется)
- Зависимости из `requirements.txt`

## 🚀 Быстрый старт

### Вариант 1: Docker (Рекомендуется)

```bash
# 1. Клонируйте репозиторий
git clone <repository-url>
cd cs2-controller

# 2. Скопируйте пример окружения
copy example.env .env  # Windows
cp example.env .env    # Linux/Mac

# 3. Отредактируйте .env файл со своими значениями
# Установите SECRET_KEY и ADMIN_PASSWORD

# 4. Запустите через Docker Compose
docker-compose up -d

# 5. Проверьте логи
docker-compose logs -f

# Доступно по адресу http://localhost:4242
```

### Вариант 2: Локальная установка

```bash
# 1. Создайте виртуальное окружение
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 2. Скопируйте пример окружения
copy example.env .env  # Windows
cp example.env .env    # Linux/Mac

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Запустите приложение
python main.py
# или
uvicorn main:app --reload --host 0.0.0.0 --port 4242

# Доступно по адресу http://localhost:4242
```

## ⚙️ Конфигурация (.env)

```env
# Безопасность (ОБЯЗАТЕЛЬНО)
SECRET_KEY=ваш-супер-секретный-ключ-измените-это
ADMIN_PASSWORD=ваш-пароль-администратора

# Конфигурация сервера
HOST=0.0.0.0
PORT=8000
DEBUG=True  # Установите False для продакшена
```

### Переменные окружения

- `SECRET_KEY` — Секретный ключ для шифрования сессий (обязательно)
- `ADMIN_PASSWORD` — Пароль администратора для доступа к `/admin` (обязательно)
- `HOST` — Хост сервера (по умолчанию: 0.0.0.0)
- `PORT` — Порт сервера (по умолчанию: 8000)
- `DEBUG` — Режим отладки (по умолчанию: True, установите False в продакшене)

## 🔗 Маршруты

### Публичные маршруты

- `GET /login` — Страница входа (по коду доступа или админ-паролю)
- `POST /login` — Аутентификация
- `GET /logout` — Выход

### Защищенные маршруты (требуется авторизация)

- `GET /` — Главная панель управления
- `GET /get-status` — Статус сервера (JSON)
- `POST /start-cs2` — Запустить CS2
- `POST /stop-cs2` — Остановить CS2

### Админ-маршруты (требуется доступ администратора)

- `GET /admin` — Админ-панель для управления кодами
- `POST /admin/generate` — Сгенерировать новый код доступа
- `POST /admin/delete` — Удалить код доступа

## 📚 Документация API

После запуска сервера:

- **Swagger UI**: <http://localhost:4242/docs>
- **ReDoc**: <http://localhost:4242/redoc>

## 🐳 Docker команды

```bash
# Собрать образ
docker-compose build

# Запустить контейнеры
docker-compose up -d

# Остановить контейнеры
docker-compose down

# Просмотреть логи
docker-compose logs -f

# Перезапустить контейнеры
docker-compose restart

# Удалить все данные
docker-compose down -v

# Открыть shell в контейнере
docker-compose exec cs2-controller /bin/bash
```

Или используйте Makefile:

```bash
make build    # Собрать образ
make up       # Запустить контейнеры
make down     # Остановить контейнеры
make logs     # Просмотреть логи
make restart  # Перезапустить
make clean    # Очистить все данные
```

## 📁 Структура проекта

```
cs2-controller/
│
├── app/
│   ├── __init__.py
│   ├── config.py          # Конфигурация приложения
│   ├── models.py          # Pydantic модели
│   ├── services.py        # Бизнес-логика
│   ├── dependencies.py    # FastAPI зависимости
│   │
│   └── routers/
│       ├── __init__.py
│       ├── auth.py        # Авторизация
│       ├── admin.py       # Админ-панель
│       └── control.py     # Управление CS2
│
├── templates/
│   ├── index.html         # Главная страница
│   ├── login.html         # Страница входа
│   └── admin.html         # Админ-панель
│
├── static/
│   ├── style.css          # Стили
│   └── script.js          # Фронтенд логика
│
├── data/                  # Создается автоматически
│   ├── stats.json         # Статистика
│   └── codes.json         # Коды доступа
│
├── main.py                # Точка входа приложения
├── requirements.txt       # Python зависимости
├── Dockerfile             # Docker образ
├── docker-compose.yml     # Docker Compose конфиг
├── .dockerignore          # Docker ignore файл
├── example.env            # Пример окружения
├── Makefile               # Быстрые команды
└── README.md              # Этот файл
```

## ✨ Ключевые возможности

### 1. **Модульная архитектура**

- Разделенные роутеры (auth, admin, control)
- Бизнес-логика в сервисах
- Четкое разделение ответственности

### 2. **Pydantic валидация**

- Автоматическая валидация входных данных
- Типобезопасные ответы
- Автоматически генерируемая документация

### 3. **Dependency Injection**

- Переиспользуемые проверки авторизации
- Чистый код без дублирования
- Легкое тестирование

### 4. **Сервисы**

- `DataService` - операции с JSON файлами
- `CodeService` - управление кодами доступа
- `StatsService` - отслеживание статистики
- `CS2Service` - управление игровым процессом

### 5. **Поддержка Docker**

- Развертывание одной командой
- Изолированная среда
- Легкое масштабирование
- Готовность к продакшену

## 🔒 Функции безопасности

- Аутентификация на основе сессий
- Pydantic валидация входных данных
- Защита админ-маршрутов
- Безопасная обработка паролей
- Готовность к HTTPS (настройте reverse proxy)

## 🚦 Развертывание в продакшене

### 1. Использование Docker (Рекомендуется)

```bash
# Установите продакшен окружение
echo "DEBUG=False" >> .env

# Используйте надежные секреты
echo "SECRET_KEY=$(openssl rand -hex 32)" >> .env

# Запустите с продакшен настройками
docker-compose up -d
```

### 2. За Nginx (Reverse Proxy)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:4242;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### 3. Использование systemd (Linux)

```ini
# /etc/systemd/system/cs2-controller.service
[Unit]
Description=CS2 Controller
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/path/to/cs2-controller
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/uvicorn main:app --host 0.0.0.0 --port 4242
Restart=always

[Install]
WantedBy=multi-user.target
```

## 🛠️ Разработка

```bash
# Установите dev зависимости
pip install -r requirements.txt

# Запустите с авто-перезагрузкой
uvicorn main:app --reload

# Запустите тесты (если доступны)
pytest

# Форматирование кода
black .
isort .

# Проверка типов
mypy .
```

## 📊 Мониторинг

### Health Check

```bash
curl http://localhost:4242/login
```

### Docker Health

```bash
docker-compose ps
```

### Логи

```bash
# Docker логи
docker-compose logs -f

# Логи приложения (если настроено)
tail -f logs/app.log
```

## 🐛 Устранение неполадок

### Порт уже используется

```bash
# Измените PORT в .env файле
PORT=6969

# И остановите конфликтующий сервис
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Linux
sudo lsof -i :8000
kill -9 <PID>
```

### Отказано в доступе (Docker)

```bash
# Исправьте права доступа к директории data
sudo chown -R $USER:$USER data/
chmod 755 data/
```

### Контейнер не запускается

```bash
# Проверьте логи
docker-compose logs

# Пересоберите образ
docker-compose build --no-cache
docker-compose up -d
```

## 📝 Лицензия

Этот проект предоставляется как есть в образовательных целях.

## 🤝 Вклад

Вклады приветствуются! Пожалуйста, не стесняйтесь отправлять pull requests.

## 📧 Поддержка

По вопросам и проблемам, пожалуйста, откройте issue на GitHub.

---

Сделано с ❤️ для CS2 сообщества

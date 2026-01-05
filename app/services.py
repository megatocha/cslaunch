import json
import os
import subprocess
import re
import secrets
import time
from typing import Optional, List
from pathlib import Path

from app.models import AccessCode, Stats
from app.config import settings


class DataService:
    """Сервис для работы с JSON данными"""
    
    @staticmethod
    def _ensure_dir(filepath: str):
        """Создать директорию, если не существует"""
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def load_json(filepath: str, default: dict) -> dict:
        """Загрузить JSON файл"""
        DataService._ensure_dir(filepath)
        
        if not os.path.exists(filepath):
            return default
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return default
    
    @staticmethod
    def save_json(filepath: str, data: dict):
        """Сохранить в JSON файл"""
        DataService._ensure_dir(filepath)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


class CodeService:
    """Сервис управления кодами доступа"""
    
    @staticmethod
    def get_codes() -> List[AccessCode]:
        """Получить все коды"""
        data = DataService.load_json(settings.CODES_FILE, {"codes": []})
        return [AccessCode(**code) for code in data.get("codes", [])]
    
    @staticmethod
    def save_codes(codes: List[AccessCode]):
        """Сохранить коды"""
        data = {"codes": [code.model_dump() for code in codes]}
        DataService.save_json(settings.CODES_FILE, data)
    
    @staticmethod
    def generate_code(note: str = "Друг") -> str:
        """Сгенерировать новый код"""
        return f"{secrets.token_hex(2).upper()}-{secrets.token_hex(2).upper()}"
    
    @staticmethod
    def add_code(note: str = "Друг") -> AccessCode:
        """Добавить новый код"""
        codes = CodeService.get_codes()
        new_code = AccessCode(
            code=CodeService.generate_code(),
            note=note
        )
        codes.append(new_code)
        CodeService.save_codes(codes)
        return new_code
    
    @staticmethod
    def delete_code(code_to_delete: str) -> bool:
        """Удалить код"""
        codes = CodeService.get_codes()
        filtered = [c for c in codes if c.code != code_to_delete]
        
        if len(filtered) == len(codes):
            return False
        
        CodeService.save_codes(filtered)
        return True
    
    @staticmethod
    def validate_code(code: str) -> bool:
        """Проверить валидность кода"""
        codes = CodeService.get_codes()
        return any(c.code == code for c in codes)


class StatsService:
    """Сервис статистики"""
    
    @staticmethod
    def get_stats() -> Stats:
        """Получить статистику"""
        data = DataService.load_json(settings.STATS_FILE, {
            "launches": 0,
            "start_time": None
        })
        return Stats(**data)
    
    @staticmethod
    def save_stats(stats: Stats):
        """Сохранить статистику"""
        DataService.save_json(settings.STATS_FILE, stats.model_dump())
    
    @staticmethod
    def increment_launches():
        """Увеличить счетчик запусков"""
        stats = StatsService.get_stats()
        stats.launches += 1
        stats.start_time = time.time()
        StatsService.save_stats(stats)
    
    @staticmethod
    def set_start_time(start_time: Optional[float]):
        """Установить время старта"""
        stats = StatsService.get_stats()
        stats.start_time = start_time
        StatsService.save_stats(stats)


class CS2Service:
    """Сервис управления CS2"""
    
    @staticmethod
    def is_running() -> bool:
        """Проверить, запущена ли игра"""
        try:
            output = subprocess.check_output(
                'tasklist /FI "IMAGENAME eq cs2.exe"',
                shell=True
            ).decode('cp866', errors='ignore')
            return "cs2.exe" in output
        except Exception:
            return False
    
    @staticmethod
    def start() -> bool:
        """Запустить CS2"""
        try:
            os.system("start steam://run/730")
            StatsService.increment_launches()
            return True
        except Exception:
            return False
    
    @staticmethod
    def stop() -> bool:
        """Остановить CS2"""
        try:
            os.system("taskkill /f /im cs2.exe")
            StatsService.set_start_time(None)
            return True
        except Exception:
            return False
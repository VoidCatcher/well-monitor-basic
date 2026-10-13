"""Вывод паспорта условной нефтяной скважины.""" 
 
from well_monitor import __version__ 
 
 
WELL_NAME = "Скважина № 101" 
FIELD_NAME = "Учебное месторождение" 
DEPTH_M = 2850 
DAILY_RATE_T = 12.5 
 
 
def main() -> None: 
    print("ПАСПОРТ НЕФТЯНОЙ СКВАЖИНЫ") 
    print("-" * 32) 
    print(f"Проект: Well Monitor v{__version__}") 
    print(f"Название: {WELL_NAME}") 
    print(f"Месторождение: {FIELD_NAME}") 
    print(f"Глубина: {DEPTH_M} м") 
    print(f"Дебит: {DAILY_RATE_T} т/сут") 
 
 
if __name__ == "__main__": 
    main() 
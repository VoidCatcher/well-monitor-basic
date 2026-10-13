"""Консольный прототип мониторинга скважины.""" 
 
from well_monitor import __version__ 
from well_monitor.config import ( 
    DAILY_RATE_T, 
    DEPTH_M, 
    FIELD_NAME, 
    PROJECT_NAME, 
    WELL_ID, 
) 
 
 
def print_well_card() -> None: 
    print("=" * 42) 
    print(f"{PROJECT_NAME} v{__version__}") 
    print("КАРТОЧКА ТЕХНОЛОГИЧЕСКОГО ОБЪЕКТА") 
    print("=" * 42) 
    print(f"Идентификатор: {WELL_ID}") 
    print(f"Месторождение: {FIELD_NAME}") 
    print(f"Глубина: {DEPTH_M} м") 
    print(f"Дебит: {DAILY_RATE_T} т/сут") 
    print("=" * 42) 
 
 
if __name__ == "__main__": 
    print_well_card() 

WELL_STATUS = "В работе" 
print(f"Статус: {WELL_STATUS}") 
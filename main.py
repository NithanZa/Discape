from bot_manager import run
from interactives.user_data_manager import clear_all_data

if __name__ == '__main__':
    clear_data = input("Do you want to clear previous data? (y/N): ")
    while clear_data.lower() not in ['y', 'n']:
        print("Invalid input, answer with (y/N)")
        clear_data = input("Do you want to clear previous data? (y/N): ")
    if clear_data == 'y':
        clear_all_data()
    run()

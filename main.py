import os
os.system("clear")
print("Запуск МодЛаунчера")
try:
    os.mkdir("modpacks")
except FileExistsError:
    print("\n")
import shutil
import sys
import time
try:
    from rich import print
    print("[bold green](✓)Успешный импорт библиотеки[/bold green]")
except ImportError:
    print("(x)Не удалось импортировать библиотеку , она будет установлена")
    time.sleep(1)
    os.system("sudo apt install python3-pip -y")
    os.system("pip3 install rich")
    from rich import print
    os.system("clear")
    print("Перезапустите")
    exit()
try:
    from tkinter import *
    from tkinter import ttk
    from tkinter.ttk import Combobox
    from tkinter import messagebox
    print("[bold green](✓)Успешный импорт библиотеки[/bold green]")
except ImportError:
    print("[bold red](x)Не удалось импортировать библиотеку, она будет установлена[/bold red]")
    os.system("sudo apt-get install python3-tk -y")
    os.system("clear")
    print("Перезапустите")
    exit()
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
print("[bold green](✓)Все библиотеки импортированы успешно![/bold green]")
config = configparser.ConfigParser()
config.read('config.ini')
window = Tk()
window.title("ModsLauncher")
window.geometry('320x200')
window.configure(bg='gray')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Лаунчер')
tab_control.add(tab2, text='Настройки')
tab_control.pack(expand=1, fill='both')
text = Label(tab2, text="Выберите сборку")
text.grid(column=0, row=0)
print("Поиск модпаков...")
dirname = 'modpacks/'
files = os.listdir(dirname)
temp = map(lambda name: os.path.join(dirname, name), files)
modpacks = list(temp)
i = 0
while i < len(modpacks):
    print("[bold green](✓)Найден модпак[/bold green]")
    print(modpacks[i])    # применяем индекс для получения элемента
    i += 1
if i==0:
    print("[bold red](x)Не найдено модпаков[/bold red]")
else:
    print("[bold green](✓)Успешно найдено " + str(i) + " модпаков[/bold green]")
combo2 = Combobox(tab2)
combo2['values'] = modpacks
combo2.grid(column=0, row=1)
text_two = Label(tab2, text="Выберите лаунчер")
text_two.grid(column=0, row=2)
combo = Combobox(tab2)
combo['values'] = ("Minecraft launcher", "Другой")
combo.current(1)  # установите вариант по умолчанию
combo.grid(column=0, row=3)
def clicked():
    game_folder = config["settings"]["directory"]
    folder = game_folder
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    print("[bold magenta]Подключение модпака и запуск игры[/bold magenta]")
    modpack = combo2.get()
    for f in os.listdir(modpack):
        if os.path.isfile(os.path.join(modpack, f)):
            shutil.copy(os.path.join(modpack, f), os.path.join(game_folder, f))
    launcher = combo.get()
    laucher_cfg = config["settings"]["command"]
    if launcher == "Другой" and laucher_cfg == "":
        messagebox.showinfo('Краш нахуй', 'Укажите команду для запуска лаунчера')
        print("[bold red](x)Краш (не введена команда запуска стороннего лаунчера)[/bpld red]")
        sys.exit()
    elif launcher == "Minecraft launcher":
        os.system("minecraft-launcher")
        print("[bold red](х)Игра закрыта[/bold red]")
        sys.exit()
    elif launcher == "Другой":
        os.system(laucher_cfg)
def create_sh():
    print("Определяю директорию")
    os.system("pwd")
    pwd = os.getcwd()
    print("Создаю скрипт")
    with open("ModsLauncher.sh", "w") as file:
        file.write("sudo python3 " + pwd + " /main.py")
    print("Проверка")
    print("")
    os.system("cat ModsLauncher.sh")
    print("")
    print("[bold green](✓)Успешно создано! Находится в [/bold green]" + pwd + "/ModsLauncher.sh")
btn = Button(tab1, text="Запуск", bg="green", command=clicked)
txt2 = Label(tab2, text="Вы можете создать .sh скрипт на запуск лаунчера")
txt2.grid(column=0, row=4)
btn2 = Button(tab2, text="Создать", command=create_sh)
btn2.grid(column=0, row=5)
btn.grid(column=0, row=4)
window.mainloop() #эту хуйню не трогать

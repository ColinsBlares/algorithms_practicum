import tkinter as tk
from tkinter import messagebox
import subprocess


def run_python_script(input_value, script_name):
    try:
        result = subprocess.run(['python', script_name, str(input_value)], capture_output=True, text=True)
        messagebox.showinfo("Результат", result.stdout)
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при выполнении скрипта: {e}")


def on_button_click(script_name):
    input_value = entry.get()
    if input_value.isdigit():
        run_python_script(input_value, script_name)
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, введите число.")


# Создание основного окна
root = tk.Tk()
root.title("Задачи по вычислению чисел Фибоначчи")

# Настройка внешнего вида окна
root.geometry("400x350")  # Размер окна
root.config(bg="#f0f0f0")  # Цвет фона окна

# Настройка шрифта и стилей
label_font = ("Arial", 12, "bold")
button_font = ("Arial", 10, "bold")
entry_font = ("Arial", 12)

# Добавление инпута
entry_label = tk.Label(root, text="Введите число:", font=label_font, bg="#f0f0f0")
entry_label.pack(pady=(20, 10))

entry = tk.Entry(root, font=entry_font, width=20, bd=2, relief="solid")
entry.pack(pady=(0, 20))

# Кнопки для запуска различных скриптов
button_style = {'font': button_font, 'width': 20, 'height': 2, 'bd': 2, 'relief': "raised", 'bg': "#4CAF50",
                'fg': "white"}

button_1 = tk.Button(root, text="Запустить скрипт 1", command=lambda: on_button_click('fib_recursive.py'),
                     **button_style)
button_1.pack(pady=5)

button_2 = tk.Button(root, text="Запустить скрипт 2", command=lambda: on_button_click('fib_loop.py'), **button_style)
button_2.pack(pady=5)

button_3 = tk.Button(root, text="Запустить скрипт 3", command=lambda: on_button_click('fib_array.py'), **button_style)
button_3.pack(pady=5)

button_4 = tk.Button(root, text="Запустить скрипт 4", command=lambda: on_button_click('fib_binet.py'), **button_style)
button_4.pack(pady=5)

button_5 = tk.Button(root, text="Запустить скрипт 5", command=lambda: on_button_click('fib_big_even_odd.py'),
                     **button_style)
button_5.pack(pady=5)

# Запуск главного цикла Tkinter
root.mainloop()

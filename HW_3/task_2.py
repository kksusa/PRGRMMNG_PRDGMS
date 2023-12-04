# Задача
# Написать игру в “Крестики-нолики”. Можете использовать любые парадигмы, которые посчитаете наиболее подходящими.
# Можете реализовать доску как угодно - как одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё усмотрение.
# Главное, чтобы в игру можно было поиграть через терминал с вашего компьютера.

# Вариант 2. Самописное решение с использованием библиотеки Tkinter. Доработан вариант игры, созданный на курсе
# "Знакомство с Python".
# В основном используется процедурная парадигма. Алгоритм работы полностью контролируется и доступен для модификации.
# GUI реализован с помощью встроенной в Python библиотеки Tkinter (используется декларативная парадигма).
# Настройка виджетов реализована с помощью структурной парадигмы (простое описание).

from random import randint
import tkinter as tk
from random import getrandbits
from random import randint


def check_winner(matrix: list[list]) -> list:
    """
    Проверка строк, столбцов, диагоналей
    :param matrix: игровое поле
    :return: вариант заполнения матрицы для победы
    """
    var_win = []
    # варианты победы
    for i in range(3):
        # Строки
        if matrix[i][0]['text'] == matrix[i][1]['text'] == matrix[i][2]['text'] != '':
            var_win = [i, 0, i, 1, i, 2]
        # Столбцы
        if matrix[0][i]['text'] == matrix[1][i]['text'] == matrix[2][i]['text'] != '':
            var_win = [0, i, 1, i, 2, i]
    # Главная диагональ
    if matrix[0][0]['text'] == matrix[1][1]['text'] == matrix[2][2]['text'] != '':
        var_win = [0, 0, 1, 1, 2, 2]
    # Второстепенная диагональ
    if matrix[0][2]['text'] == matrix[1][1]['text'] == matrix[2][0]['text'] != '':
        var_win = [0, 2, 1, 1, 2, 0]
    return var_win


def iq_move(matrix):
    """
    Определение координаты хода IQ AI
    :param matrix: игровое поле
    :return: координаты следующего хода
    """
    win_lines = {
        0: ((0, 0), (0, 1), (0, 2)),
        1: ((1, 0), (1, 1), (1, 2)),
        2: ((2, 0), (2, 1), (2, 2)),
        3: ((0, 0), (1, 0), (2, 0)),
        4: ((0, 1), (1, 1), (2, 1)),
        5: ((0, 2), (1, 2), (2, 2)),
        6: ((0, 0), (1, 1), (2, 2)),
        7: ((0, 2), (1, 1), (2, 0)),
    }
    # если центр не занят, ставим туда
    if matrix[1][1]['text'] == '':
        return [1, 1]
    # вариант, чтобы человек мог сыграть только вничью или проиграть - занять центр первым ходом и один из углов вторым ходом
    line_two_0 = -1
    for line in win_lines.keys():
        count_X = 0
        count_0 = 0
        for cell in win_lines[line]:
            if matrix[cell[0]][cell[1]]['text'] == 'X':
                count_X += 1
            elif matrix[cell[0]][cell[1]]['text'] == '0':
                count_0 += 1
        if count_X == 2 and count_0 == 0:
            row, col = find_empty_cell(win_lines[line], matrix)
            return [row, col]
        elif count_0 == 2 and count_X == 0:
            line_two_0 = line
    if line_two_0 != -1:
        row, col = find_empty_cell(win_lines[line_two_0], matrix)
        return [row, col]
    else:
        while True:
            row = randint(0, 2)
            col = randint(0, 2)
            # если поле свободно, ставим маркер бота
            if matrix[row][col]['text'] == '':
                return [row, col]


def find_empty_cell(line, matrix):
    """
    Нахождение пустой ячейки в линии
    :param line: линия игрового поля
    :param matrix: игровое поле
    :return: координаты пустой ячейки
    """
    for cell in line:
        if matrix[cell[0]][cell[1]]['text'] == '':
            return [cell[0], cell[1]]


def start_game():
    field = []
    attempt = True
    attempt_count = 0
    players = []
    # определение маркера в зависимости от bool-попытки
    marker = lambda x: 'X' if x else '0'
    # определение цвета в зависимости от bool-попытки
    color = lambda x: 'blue' if x else 'green'

    def ai_move():
        """
        ход ai
        :return:
        """
        global attempt_count
        global attempt
        attempt_count += 1
        # если бот с интеллектом
        if aq.get():
            row, col = iq_move(field)
        # иначе бот ходит случайно
        else:
            # random ищем пустую ячейку на поле и ставим marker
            while True:
                row = randint(0, 2)
                col = randint(0, 2)
                # если поле свободно, ставим маркер бота
                if field[row][col]['text'] == '':
                    break
        field[row][col]['foreground'] = color(attempt)
        field[row][col]['text'] = marker(attempt)

    def check_status():
        """
        Проверяем статус игры, победу
        :return:
        """
        global attempt_count
        global attempt
        global players
        var_win = check_winner(field)
        # если есть выигрышный вариант
        if len(var_win):
            r0, c0, r1, c1, r2, c2 = var_win
            field[r0][c0]['background'] = color(not attempt)
            field[r1][c1]['background'] = color(not attempt)
            field[r2][c2]['background'] = color(not attempt)
            lbl_progress['foreground'] = color(attempt)
            lbl_progress['text'] = f'attempt_count {attempt_count} attempt {attempt} '
            lbl_progress['text'] = f'Выиграл {players[attempt]} ({marker(attempt)})'
            attempt_count = 9
        else:
            if attempt_count == 9:
                lbl_progress['foreground'] = 'black'
                lbl_progress['text'] = 'Боевая ничья!'
            else:
                lbl_progress['foreground'] = color(not attempt)
                lbl_progress['text'] = f'Очередь {players[not attempt]} ({marker(not attempt)})'
                attempt = not attempt

    def click(row: int, col: int):
        """
        Нажатие кнопок поля
        :param row: номер строки
        :param col: номер столбца
        :return:
        """
        global attempt
        global attempt_count
        global players
        # если пользователь начнёт нажимать кнопки на поле до инициализации глобальных переменных
        try:
            if field[row][col]['text'] == '' and attempt_count < 9:
                field[row][col]['foreground'] = color(attempt)
                field[row][col]['text'] = marker(attempt)
                attempt_count += 1
                # проверка статуса
                check_status()
                # если играет ai и его ход
                if ai.get() and attempt:
                    ai_move()
                    check_status()
        except:
            pass

    def new_game():
        """
        Новая игра
        :return:
        """
        global players
        global attempt
        global attempt_count
        # играет человек и компьютер
        if ai.get():
            ent_player_1.delete(0, tk.END)
            ent_player_1.insert(0, 'Компьютер')
            ent_player_0.delete(0, tk.END)
            ent_player_0.insert(0, 'Человек')
        # играют два человека
        else:
            ent_player_1.delete(0, tk.END)
            ent_player_1.insert(0, 'Второй игрок')
        players = [ent_player_0.get(), ent_player_1.get()]
        # очистка игрового поля
        for row in range(3):
            for col in range(3):
                field[row][col]['background'] = 'light gray'
                field[row][col]['text'] = ''
        # случайный выбор первого хода
        attempt = bool(getrandbits(1))
        attempt_count = 0
        if ai.get() and attempt:
            ai_move()
            attempt = not attempt
        lbl_progress['foreground'] = color(attempt)
        lbl_progress['text'] = f'Очередь {players[attempt]} ({marker(attempt)})'

    def make_field():
        """
        задание игрового поля. 3 списка 3 списков Button
        :return:
        """
        for row in range(3):
            line = []
            for col in range(3):
                # кнопка с командой
                # Виджеты Button нужны для создания кликабельных кнопок.
                # Их можно настроить таким образом, чтобы при нажатии вызывалась определенная функция.
                button = tk.Button(master=frame_field, text='', width=6, height=3,
                                   font=('Arial', 20, 'bold'), background='light gray',
                                   command=lambda row=row, col=col: click(row, col))
                # размещение кнопки
                button.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
                # добавляем кнопку на линию игрового поля
                line.append(button)
            # добавляем линию на игровое поле
            field.append(line)

    # создаём новое окно (экземпляр класса Tkinter)
    ttt = tk.Tk()
    # название окна
    ttt.title("Игра крестики-нолики")
    # размеры окна
    ttt.geometry('350x500')

    # для checkbutton (выбор AI)
    ai = tk.BooleanVar()
    # для checkbutton (выбор IQ)
    aq = tk.BooleanVar()

    # Виджет рамки
    # Рамки лучше всего рассматривать как контейнеры для других виджетов.
    frame_players = tk.Frame(ttt)
    # Самым популярным менеджером геометрии в Tkinter является .grid().
    # Он обладает всей мощностью .pack(), будучи намного более простым в использовании.
    # Менеджер .grid() работает путем разделения окна или рамки на строки и столбцы (на сетку).
    # Указыввется местоположение виджета, вызывая метод .grid() и передавая индексы row и column (строки и столбца)
    # в ключевые аргументы строки и столбца соответственно.
    # Индексы строк и столбцов начинаются с 0, поэтому индекс строки 1 и индекс столбца 2 указывают методу .grid(),
    # что виджет нужно разместить в третьем столбце второй строки.
    frame_players.grid(row=0, column=0)

    # Виджеты Label используется для отображения текста или картинок.
    # Текст на виджете Label, не может редактироваться пользователем. Он только показывается.
    # Можно вставить любой виджет в рамку, установив атрибут master:
    lbl_player_0 = tk.Label(master=frame_players, text='Первый игрок')
    # В случаях, когда требуется получить текстовую информацию от пользователя, используется виджет Entry.
    # Он отображает небольшой текстовый бокс, куда пользователь может ввести текст.
    ent_player_0 = tk.Entry(master=frame_players)
    # Вставка нового текста через .insert()
    ent_player_0.insert(0, 'Первый игрок')
    lbl_player_0.grid(row=0, column=0, sticky='w')
    ent_player_0.grid(row=1, column=0)

    lbl_player_1 = tk.Label(master=frame_players, text='Второй игрок')
    ent_player_1 = tk.Entry(master=frame_players)
    ent_player_1.insert(0, 'Второй игрок')
    lbl_player_1.grid(row=0, column=1, sticky='e')
    ent_player_1.grid(row=1, column=1)

    chbtn_ai = tk.Checkbutton(master=frame_players, text='AI', variable=ai)
    chbtn_ai.grid(row=1, column=2)
    chbtn_iq = tk.Checkbutton(master=frame_players, text='IQ', variable=aq)
    chbtn_iq.grid(row=1, column=3)

    frame_field = tk.Frame(ttt)
    frame_progress = tk.Frame(ttt)
    # Кнопка "Новая игра" (команда new_game)
    btn_start = tk.Button(master=frame_progress, text='Новая игра', width=20,
                          font=('Arial', 20, 'bold'), background='orange',
                          command=new_game)
    btn_start.grid(row=1, column=0)
    lbl_progress = tk.Label(master=frame_progress, text='Для начала игры нажмите кнопку', image='',
                            font=('Arial', 15, 'bold'))
    lbl_progress.grid(row=0, column=0)

    # разметка рамок
    frame_field.grid(row=1, column=0)
    frame_progress.grid(row=2, column=0)

    # делаем игровое поле
    make_field()

    # Вечный цикл для экземпляра класса Tkinter
    # Данный метод требуется для событий вроде нажатий на клавиши или кнопки,
    # он также блокирует запуск кода, что следует после, пока окно, на котором оно было вызвано, не будет закрыто.
    # Если не добавлять .mainloop() в конец программы в Python файле, тогда приложение Tkinter не запустится вообще,
    # и ничего не будет отображаться.
    ttt.mainloop()
    # print("Игра окончена")


if __name__ == '__main__':
    start_game()
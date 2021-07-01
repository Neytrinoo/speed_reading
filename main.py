from tkinter import *
from forming_array_of_words import *
from styles import *

word_ind = 0
is_start = False
last_after = 0


def change_label_text(label, text):
    label.set(text)


def start_reading(wind, label, words, ms_for_word, event=None):
    global word_ind, is_start, last_after
    if event is not None:
        is_start = not is_start
    if not is_start:
        wind.after_cancel(last_after)
        word_ind -= 1
        return
    if word_ind == 0:
        change_label_text(label, words[word_ind])
    if word_ind == len(words) - 2:
        last_after = wind.after(ms_for_word, lambda: change_label_text(label, words[word_ind] + '\nНажмите Esc, чтобы закрыть окно'))
    else:
        last_after = wind.after(ms_for_word, lambda: change_label_text(label, words[word_ind]))
    word_ind += 1
    if word_ind < len(words) - 1:
        wind.after(ms_for_word, lambda: start_reading(wind, label, words, ms_for_word))


def close_wind(wind):
    wind.destroy()


def start_speed_reading():
    global word_ind
    word_ind = 0
    try:
        speed = int(words_per_min.get())
        ms_for_word = int(60000 / speed)
    except Exception:
        return

    text = text_area.get('1.0', 'end')
    words = get_array_of_words(text)
    speed_reading_window = Toplevel(window)
    speed_reading_window.attributes('-fullscreen', True)
    speed_reading_window.config(bg='black')
    now_word = StringVar()
    now_word.set('Пробел - старт/пауза')
    text_label = Label(speed_reading_window, textvariable=now_word, bg='black', fg=SPEED_TEXT_COLOR, width=SPEED_TEXT_WIDTH,
                       font=SPEED_TEXT_FONT)
    text_label.pack(padx=10, ipady=200)
    speed_reading_window.bind('<space>', lambda start: start_reading(speed_reading_window, now_word, words, ms_for_word, start))
    speed_reading_window.bind('<Escape>', lambda event: close_wind(speed_reading_window))

    speed_reading_window.mainloop()


window = Tk()
window.geometry('520x200')
window.maxsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

words_per_min_label = Label(text='Слов в минуту: ')
words_per_min_label.pack()
words_per_min = Entry()
words_per_min.pack()

text_area = Text()
scroll_bar = Scrollbar()
scroll_bar.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.pack(expand=YES)

button_start_speed_reading = Button(text='Прочитать', command=start_speed_reading)
button_start_speed_reading.pack()

window.mainloop()

from tkinter import *
import tkinter as tk
from datetime import datetime, date

class typing_speed_app:
    def __init__(self):
        self.master = Tk()
        self.master.geometry('1000x500+100+50')
        self.master.title('Typing Speed App')
        self.master.resizable(width=False, height=False)
        self.main_program()
        self.master.grid_columnconfigure(5, weight=1)
        self.master.mainloop()

    def main_program(self):
        def exit_work():
            self.master.destroy()
            exit()

        self.work = []

        def result_work():
            self.end_time = datetime.now().time()
            self.final_time = (datetime.combine(date.min, self.end_time) - datetime.combine(date.min, self.start_time))

            def gross_wpm(chr, tim, e):
                tim_sec = str(tim).split(':')
                tim_sec = tim_sec[2].split('.')[0]

                tim_min = str(tim).split(':')[1]

                if float(tim_sec) > 0:
                    out = float(tim_sec) / 60
                    self.ff = float(tim_min) + out

                wpm = (chr / 5) / self.ff
                net_wpm = (wpm - e) / self.ff
                net_wpm = format(net_wpm, '.2f')

                self.result_win = Toplevel(self.master)
                self.result_win.title('RESULT (WPM)')
                self.result_win.geometry('300x300+200+150')
                self.result_win.resizable(width=False, height=False)

                self.r_heading = Label(self.result_win, text='RESULT', font=('Arial', 20))
                self.r_heading.grid(column=2, row=0)

                self.dummy = Label(self.result_win)
                self.dummy.grid(column=2, row=1)

                self.type_char = Label(self.result_win, text='TYPE CHAR', font=('Arial', 14))
                self.type_char.grid(column=1, row=2, sticky=W)

                self.type_char_r = Label(self.result_win, text=str(chr), font=('Arial', 14))
                self.type_char_r.grid(column=2, row=2, sticky=W)

                self.dummy = Label(self.result_win)
                self.dummy.grid(column=2, row=3)

                self.er_char = Label(self.result_win, text='ERRORS', font=('Arial', 14))
                self.er_char.grid(column=1, row=4, sticky=W)

                self.er_char_r = Label(self.result_win, text=str(e), font=('Arial', 14))
                self.er_char_r.grid(column=2, row=4, sticky=W)

                self.dummy = Label(self.result_win)
                self.dummy.grid(column=2, row=5)

                self.time_l = Label(self.result_win, text='TIME', font=('Arial', 14))
                self.time_l.grid(column=1, row=6, sticky=W)

                self.ff = format(self.ff, '.2f')

                self.time_l_r = Label(self.result_win, text=f'{self.ff}, min', font=('Arial', 14))
                self.time_l_r.grid(column=2, row=6, sticky=W)

                self.dummy = Label(self.result_win)
                self.dummy.grid(column=2, row=7)

                self.wpn_char = Label(self.result_win, text='WPM', font=('Arial', 14))
                self.wpn_char.grid(column=1, row=8, sticky=W)

                self.wpn_char_c = Label(self.result_win, text=f'{net_wpm}WPM', font=('Arial', 14))
                self.wpn_char_c.grid(column=2, row=8, sticky=W)

                if net_wpm <= "35":
                    self.bing = Label(self.result_win, text='Turtle', font=('Arial', 30), fg='RED')
                    self.bing.grid(column=2, row=9)
                elif net_wpm > "35":
                    self.bing = Label(self.result_win, text='Rabbit', font=('Arial', 30), fg='Blue')
                    self.bing.grid(column=2, row=9)

                self.result_win.grid_columnconfigure(4, weight=1)
                self.result_win.mainloop()

            p2_txt = self.ty_work.get(1.0,'end-1c').lower()

            para1 = []
            para2 = p2_txt.split()
            errors = 0
            time = self.final_time

            for i in self.work:
                for r in i.split():
                    para1.append(r.lower())

            for e in range(len(para1)):
                if para1[e] == para2[e]:
                    continue
                else:
                    errors += 1

            gross_wpm(len(p2_txt), time, errors)

        def start_work():
            self.ty_work.focus()
            self.start_time = datetime.now().time()

            count = 0
            var = tk.IntVar()
            def call_back(event):
                var.set(1)
            for i in range(len(self.work)):
                self.type_work['text'] = self.work[count]
                self.type_work.update()
                self.ty_work.bind('<Return>', call_back)
                self.ty_work.wait_variable(var)
                count +=1
                if count == len(self.work):
                    result_work()

        with open('out.txt', 'r') as file:
            out = file.read()
            for i in out.split('\n'):
                self.work.append(i)

        self.dummy = Label(self.master)
        self.dummy.grid(column=2, row=0)

        self.heading = Label(self.master, text='TYPING SPEED', font=('Arial', 30), bg='light green', fg='white',
                             width=40)
        self.heading.grid(column=4, row=1, columnspan=2)

        self.dummy = Label(self.master)
        self.dummy.grid(column=2, row=2)

        self.type_work = Label(self.master, text='*****', font=('Arial', 24), bg='Black', fg='white',width=70,
                               pady=10)
        self.type_work.grid(column=3, row=3, columnspan=3)

        self.dummy = Label(self.master)
        self.dummy.grid(column=2, row=4)

        self.ty_work = Text(self.master, font=('Arial', 16), width=80, bd=5, relief=GROOVE, height=14)
        self.ty_work.grid(column=3, row=5, columnspan=3)

        self.dummy = Label(self.master)
        self.dummy.grid(column=3, row=6)

        self.start_btn = Button(self.master, font=('Arial', 14), text='START', command=start_work, width=40)
        self.start_btn.grid(column=5, row=7)

        self.stop_btn = Button(self.master, font=('Arial', 14), text='EXIT', command=exit_work, width=10)
        self.stop_btn.grid(column=5, row=7, sticky=W)

        self.result_btn = Button(self.master, font=('Arial', 14), text='RESULT', command=result_work, width=10)
        self.result_btn.grid(column=5, row=7, sticky=E)

app = typing_speed_app()

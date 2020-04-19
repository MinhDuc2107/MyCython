from tkinter import *
import tkinter.messagebox as box
import fractions as frac


class main():
    def __init__(self):
        super().__init__()# Chỗ này làm việc gì ?
        self.win = Tk()
        self.set_mode()
        self.x1 = Label(self.win, text = 'X', font = ('Times', '15'))
        self.y1 = Label(self.win, text = 'Y =', font = ('Times', '15'))
        self.x2 = Label(self.win, text = 'X', font = ('Times', '15'))
        self.y2 = Label(self.win, text = 'Y =', font = ('Times', '15'))
        self.a1 = Entry(self.win, justify = 'right', font = ('Times', '15'))
        self.a2 = Entry(self.win, justify = 'right', font = ('Times', '15'))
        self.b1 = Entry(self.win, justify = 'right', font = ('Times', '15'))
        self.b2 = Entry(self.win, justify = 'right', font = ('Times', '15'))
        self.c1 = Entry(self.win, justify = 'left', font = ('Times', '15'))
        self.c2 = Entry(self.win, justify = 'left', font = ('Times', '15'))
        self.solve = Button(self.win, text = 'Solve', font = ('Times', '15'), command = self.solve)
        self.clear = Button(self.win, text = 'Clear', font = ('Times', '15'), command = self.clear)
        self.out = Label(self.win, text = '', font = ('Times', '15'), anchor = E, bg = 'black', fg = 'white')
        self.pack()
        self.mainloop()

    def set_mode(self):
        self.win.title('Giải hệ PT 2 ẩn')
        self.win.geometry('310x150+400+200')
        self.win.resizable(0, 0)

    def pack(self):
        self.a1.place(x = 10, y = 10, width = 50, height = 20)
        self.x1.place(x = 70, y = 10, width = 50, height = 20)
        self.b1.place(x = 130, y = 10, width = 50, height = 20)
        self.y1.place(x = 190, y = 10, width = 50, height = 20)
        self.c1.place(x = 250, y = 10, width = 50, height = 20)
        self.a2.place(x = 10, y = 40, width = 50, height = 20)
        self.x2.place(x = 70, y = 40, width = 50, height = 20)
        self.b2.place(x = 130, y = 40, width = 50, height = 20)
        self.y2.place(x = 190, y = 40, width = 50, height = 20)
        self.c2.place(x = 250, y = 40, width = 50, height = 20)
        self.solve.place(x = 230, y = 70, width = 70, height = 30)
        self.clear.place(x = 10, y = 70, width = 70, height = 30)
        self.out.place(x = 10, y = 105, width = 290, height = 40)

    def clear(self):
        self.a1.delete(0, END)
        self.a2.delete(0, END)
        self.b1.delete(0, END)
        self.b2.delete(0, END)
        self.c1.delete(0, END)
        self.c2.delete(0, END)

    def isdigit(self, text):
        if (text == ''): return False
        if (text.count('.') > 1 or text.count('/') > 1 or text.count('-') > 1 or text.find('-') not in [-1,
                                                                                                        0] or text.count(
            '.') + text.count('/') > 1): return False
        database = '1234567890./-'
        for ch in text:
            if (ch not in database): return False
        return True

    def get_value(self):
        a1 = self.a1.get()
        a2 = self.a2.get()
        b1 = self.b1.get()
        b2 = self.b2.get()
        c1 = self.c1.get()
        c2 = self.c2.get()
        lst = [a1, a2, b1, b2, c1, c2]
        for text in lst:
            if self.isdigit(text):
                pass
            else:
                box.showerror('Lỗi chức năng', '...Vui lòng điền số đầy đủ...')
                return
        return lst

    def solve(self):
        v = self.get_value()
        if (v != None):
            for i in range(6):
                if ('/' not in v[i]):
                    v[i] = float(v[i])
                else:
                    v[i] = frac.Fraction(v[i])
            # Condition 1
            if (v[0] ** 2 + v[2] ** 2 == 0 or v[1] ** 2 + v[3] ** 2 == 0):
                box.showerror('Lỗi chức năng', '...Hai hệ số ko thể đồng thời bằng 0...\n...Hãy nhập lại...')
                return
            # Condition 2
            if (v[0] == 0 and v[3] == 0):
                x = str(v[5] / v[1])
                y = str(v[4] / v[2])
                self.out.config(text = 'x = ' + x + '\ny = ' + y)
                return
            if (v[2] == 0 and v[1] == 0):
                x = str(v[4] / v[0])
                y = str(v[5] / v[3])
                self.out.config(text = 'x = ' + x + '\ny = ' + y)
                return
            # condition 3
            if (v[0] == 0 and v[1] == 0):
                if (v[4] / v[2] != v[5] / v[3]):
                    self.out.config(text = 'PT vô nghiệm')
                    return
                else:
                    self.out.config(text = 'PT có vô số nghiệm')
                    return
            if (v[2] == 0 and v[3] == 0):
                if (v[4] / v[0] != v[5] / v[1]):
                    self.out.config(text = 'PT vô nghiệm')
                    return
                else:
                    self.out.config(text = 'PT có vô số nghiệm')
                    return
            # condition 4
            if (v[0] == 0 and v[3] != 0):
                y = v[4] / v[2]
                x = str((v[5] - v[3] * y) / v[1])
                y = str(y)
                self.out.config(text = 'x = ' + x + '\ny = ' + y)
                return
            if (v[2] == 0 and v[1] != 0):
                x = v[4] / v[0]
                y = str((v[5] - v[1] * x) / v[3])
                x = str(x)
                self.out.config(text = 'x = ' + x + '\ny = ' + y)
                return
            if (v[1] == 0 and v[2] != 0):
                y = v[5] / v[3]
                x = str((v[4] - v[2] * y) / v[0])
                y = str(y)
                self.out.config(text = 'x = ' + x + '\ny = ' + y)
                return
            if (v[3] == 0 and v[0] != 0):
                x = v[5] / v[1]
                y = str((v[4] - v[0] * x) / v[2])
                x = str(x)
                self.out.config(text = 'x = ' + x + '\ny = ' + y)
                return
            # condition 5
            if (v[4] == 0 and v[5] == 0):
                if (v[0] / v[1] == v[2] / v[3]):
                    self.out.config(text = 'PT có vô số nghiệm')
                    return
                else:
                    self.out.config(text = 'x = 0, y = 0')
                    return
            elif (v[4] == 0 and v[5] != 0):
                if (v[0] / v[1] == v[2] / v[3]):
                    self.out.config(text = 'PT vô nghiệm')
                    return
                else:
                    x = v[5] / (v[1] - v[3] * v[0] / v[2])
                    y = - (v[0] / v[2]) * x
                    x = str(x)
                    y = str(y)
                    self.out.config(text = 'x = ' + x + '\ny = ' + y)
                    return
            elif (v[4] != 0 and v[5] == 0):
                if (v[0] / v[1] == v[2] / v[3]):
                    self.out.config(text = 'PT vô nghiệm')
                    return
                else:
                    x = v[4] / (v[0] - v[2] * v[1] / v[3])
                    y = - (v[1] / v[3]) * x
                    x = str(x)
                    y = str(y)
                    self.out.config(text = 'x = ' + x + '\ny = ' + y)
                    return
            else:
                a = v[0] / v[1]
                b = v[2] / v[3]
                c = v[4] / v[5]
                if ((a == b and b != c) or (a == c and b != c) or (b == c and a != b)):
                    self.out.config(text = 'PT vô nghiệm')
                    return
                elif (a == b and b == c):
                    self.out.config(text = 'PT có vô số nghiệm')
                    return
                else:
                    x = (v[5] * v[2] - v[3] * v[4]) / (v[1] * v[2] - v[3] * v[0])
                    y = v[4] / v[2] - (v[0] / v[2]) * x
                    x = str(x)
                    y = str(y)
                    self.out.config(text = 'x = ' + x + '\ny = ' + y)
                    return

    def mainloop(self):
        self.win.mainloop()


app = main()

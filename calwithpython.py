#http://www.jb51.net/article/77326.htm
from Tkinter import *
#create framework
def frame(root, side):
    w = Frame(root)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w
#create button
def button(root, side, text, command = None):
    w = Button(root, text = text, command = command)
    w.pack(side = side, expand = YES, fill = BOTH)
    return w
#
class Calculator(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title('Simple Calculater')
        display = StringVar()
  #input
        Entry(self, relief = SUNKEN,
              textvariable = display).pack(side = TOP, expand = YES,
                                           fill = BOTH)
  #
        for key in('123', '456', '789', '-0.'):
            keyF = frame(self, TOP)
            for char in key:
                button(keyF, LEFT, char, lambda w = display, c = char:w.set(w.get() + c))
                #add + - * /
            opsF = frame(self, TOP)
            for char in '+-*/=':
                if char == '=':
                    btn = button(opsF, LEFT, char)
                    btn.bind('<ButtonRelease - 1>', lambda e, s = self, w = display:s.calc(w), '+')
                else:
                    btn = button(opsF, LEFT, char, lambda w = display, s = '%s' %char:w.set(w.get() + s))
                    #add claer button
            clearF = frame(self, BOTTOM)
            button(clearF, LEFT, 'clear', lambda w = display:w.set(''))
            #eval to the value
    def calc(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("ERROR")
            #pro entrance
            if __name__ == '__main__':
                print('ok')
                Calculator().mainloop()

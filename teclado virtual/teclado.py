import tkinter as Tkinter
import buttons as b
#classe principal
class Moving_Screen():
    #classe construtor
    def __init__(self, root, label):
        self.root = root
        self.label = label

    def motion_activate(self, kwargs):
        w, h = (self.root.winfo_reqwidth(), self.root.winfo_reqheight())
        (x, y) = (kwargs.x_root, kwargs.y_root)

        self.root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        return


# Criando a tela principal
def main():
    root = Tkinter.Tk()

    #objeto do buttons
    k = b.Keyboard(root, bg="cornflowerblue")
    #ola@eejj{ym
    #faz a janela não fechar
    root.overrideredirect(True)
    root.wait_visibility(root)
    #transparencia do app
    root.wm_attributes('-alpha', 0.7)

    f = Tkinter.Frame(root)
    t_bar = Tkinter.Label(f, text='Virtual Keyboard', bg="skyblue")
    t_bar.pack(side='left', expand="yes", fill="both")
    mechanism = Moving_Screen(root, t_bar)
    t_bar.bind("<B1-Motion>", mechanism.motion_activate)
    Tkinter.Button(f, text="[X]", command=root.destroy).pack(side='right')
    f.pack(side='top', expand='yes', fill='both')
    k.pack(side='top')
    root.mainloop()
    return

if __name__ == '__main__':
    main()
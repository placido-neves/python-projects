import tkinter as Tkinter
import pyautogui
import KeysConst as kc
class Keyboard(Tkinter.Frame):
    def __init__(self, *args, **kwargs):
        Tkinter.Frame.__init__(self, *args, **kwargs)
        self.create_buttons()


    #criando o evento dos botoes
    def button_command(self, event):
        pyautogui.press(event)
        return

    def create_buttons(self):
        #criando um loop para percorre as teclas
        for key_section in kc.keys:
            #criando frame por cima melhor pra organização
            store_section = Tkinter.Frame(self)
            store_section.pack(side='left', expand='yes', fill='both', padx=9, pady=10, ipadx=10, ipady=10)
            #criando um loop em key section
            for layer_name, layer_properties, layer_keys in key_section:
                #criando um labelframe para cada frame
                store_layer = Tkinter.LabelFrame(store_section)
                store_layer.pack(layer_properties)
                #criando loop em layer_keys
                for key_bunch in layer_keys:
                    store_key_frame = Tkinter.Frame(store_layer)
                    store_key_frame.pack(side='top', expand='yes', fill='both')
                    #loop pra criação dos butoes
                    for k in key_bunch:
                        #pegar o primeira letra e deixa em maiusculo
                        k = k.capitalize()
                        #ver o tamanho da letra pra ve o tamanho da letra pra ve o tamanho do botão
                        if len(k) <= 2:
                            store_button = Tkinter.Button(store_key_frame, text=k, width=1, height=2)
                        else:
                            store_button = Tkinter.Button(store_key_frame, text=k.center(4, ' '), height=2)
                        #se tiver algum botão null e não fucionar
                        if " " in k:
                            store_button['state'] = 'disable'
                        #configurao do estilo do botão
                        store_button['relief'] ='flat'
                        store_button['bg'] = 'black'
                        store_button['fg'] = 'white'

                        store_button['command'] = lambda q=k.lower(): self.button_command(q)
                        store_button.pack(side='left', fill='both', expand='yes')
        return




#virtual keybord5
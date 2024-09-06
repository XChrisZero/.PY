import tkinter

def clique ():
    print ( "Click" )
        
    janela = tkinter.Tk ()
    janela.geometry ( " 400x300 " )

    texto0 = tkinter.Label ( janela, text = "Login", font = "times new roman 15 italic", fg = "blue" )
    texto0.pack ( padx = 10, pady = 5 )

    email = tkinter.Entry( janela )
    email.pack ( padx = 10, pady = 5 )

    texto1 = tkinter.Label ( janela, text = "Senha", font = "times new roman 15 italic", fg = "blue" )
    texto1.pack ( padx = 10, pady = 5 )

    senha = tkinter.Entry ( janela, show = '*' )
    senha.pack ( padx = 10, pady = 5 )

    botao = tkinter.Button ( janela, text = "LOGIN", command = clique )
    botao.pack ( padx = 10, pady = 5 )

    checkbox = tkinter.Checkbutton ( janela, text = "Manter-me conectado?" )
    checkbox.pack ( padx = 10, pady = 5 )

    janela.mainloop ()

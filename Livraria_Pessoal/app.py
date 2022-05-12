from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import sqlite3 as lite
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk, Image  # Pillow
from tkinter import ttk
from tkinter import messagebox


# Criando conexao
conexao = lite.connect('library.db')


# * FAZENDO CRUD NO BANCO DE DADOS

## Create = Criar/Inserir

"""
with conexao:
    cursor = conexao.cursor()
    cursor.execute("CREATE TABLE Library(id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, autor TEXT, editora TEXT, genero TEXT, nome_alugador TEXT, alugado_em DATE, data_de_retorno DATE, paginas INTEGER)")
"""

# Inserindo informações


def inserir_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "INSERT INTO Library(titulo, autor, editora, genero, nome_alugador, alugado_em, data_de_retorno, paginas) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, i)


# Read = Mostrando informações da tabela

def mostrar_info(titulo=None):
    lista = []

    with conexao:
        cursor = conexao.cursor()
        selector = f"WHERE titulo = '{titulo}'" if titulo else ''
        query = f"SELECT * FROM Library {selector}"
        cursor.execute(query)
        informacao = cursor.fetchall()

        for i in informacao:
            lista.append(i)

        print(lista)

    return lista

# atualizar informações


def atualizar_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "UPDATE Library SET titulo=?, autor=?, editora=?, genero=?, nome_alugador=?, alugado_em=?, data_de_retorno=?, paginas=? WHERE id=?"
        cursor.execute(query, i)


# Função Deletar

def deletar_info(i):
    with conexao:
        cursor = conexao.cursor()
        query = "DELETE FROM Library WHERE id=?"
        cursor.execute(query, i)


# cores
cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#4fa882"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"  # letra / letters
cor5 = "#38576b"  # Azul macho / forte
cor6 = '#48337d'  # Rocho / purple
cor7 = "#038cfc"   # azul
cor8 = "#ef5350"   # vermelha
cor9 = "#263238"   # + verde


janela = Tk()
janela.title('Login')
# janela.geometry('310x300')
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)
janela.iconbitmap('login.ico')


# style = ttk.Style(janela)
# style.theme_use('clam')


# ----- Dividindo a janela com Frames -------

frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


# ----- Configurando o frame cima -------

label_nome = Label(frame_cima, text='LOGIN', anchor=NE,
                   font=('Ivy 25'), bg=cor1, fg=cor4)
label_nome.place(x=10, y=5)

# Linha azul
label_linha = Label(frame_cima, text='', width=275,
                    anchor=NW, font=('Ivy 1'), bg=cor6, fg=cor4)
label_linha.place(x=14, y=45)


credenciais = ['Lisa', 'Library']


def verificar_senha():
    nome = entry_nome.get()
    senha = entry_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login', 'Senha bem vindo Admin !!!')
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo(
            'Login', 'Seja bem-vinda de volta ' + credenciais[0])
        
        # limpa o que esta dentro do frame_baixo e cima
        for widget in frame_baixo.winfo_children():
            widget.destroy()

        for widget in frame_baixo.winfo_children():
            widget.destroy()

        nova_janela()

    else:
        messagebox.showwarning('Login', 'Verifique o nome ou a senha !!!')


def nova_janela():  # verificado
    # * Centralizando o arquivo
    janela.iconbitmap('library.ico')
    janela.title('Library')
    # Dimensoes da janela
    largura = 1204
    altura = 490

    # Resolução do nosso sistema
    largura_screen = janela.winfo_screenwidth()
    altura_screen = janela.winfo_screenwidth()
    # print(largura_screen, altura_screen)  # para saber as dimensoes do monitor

    # Posição da janela
    posx = largura_screen/2 - largura/2
    posy = altura_screen/5 - altura/5

    # Definir a geometria
    janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    # * ----- Dividindo a janela em Frames -----

    frame_cima2 = Frame(janela, width=310, height=50,
                        bg=cor7, relief='flat')
    frame_cima2.grid(row=0, column=0)

    frame_baixo2 = Frame(janela, width=310, height=434, bg=cor1, relief='flat')
    frame_baixo2.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

    frame_direita = Frame(janela, width=588, height=430,
                          bg=cor1, relief='flat')
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

    # Imagem

    img = Image.open('library2.ico')
    img = img.resize((60, 50), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    app_logo = Label(frame_cima2, height=60, image=img, compound=LEFT,
                     padx=10, relief='flat', anchor='nw', bg=cor7)
    app_logo.place(x=205, y=-4)

    # *----- Configurando frame_cima com o nome do app -----

    app_nome = Label(frame_cima2, text='Biblioteca Pessoal',
                     anchor=NW, font=('Ivy 13 bold'), bg=cor7, fg=cor1, relief='flat')
    app_nome.place(x=12, y=16)

    # * Variaveis globais

    global tree

    # * Função inserir

    def inserir():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        editora = entry_editora.get()
        genero = combo_generos.get()
        nome_alugador = entry_nome_alugador.get()
        alugado_em = entry_alugado_em.get()
        data_de_retorno = entry_data_de_retorno.get()
        paginas = spin.get()

        lista = [titulo, autor, editora, genero, nome_alugador,
                 alugado_em, data_de_retorno, paginas]

        if titulo == '' or autor == '' or editora == '' or genero == '' or paginas == '':
            messagebox.showwarning(
                'Atenção!', 'Preencha os campos obrigatórios*')
        else:
            inserir_info(lista)
            messagebox.showinfo(
                'Sucesso!', 'Os novos dados foram inseridos com sucesso')

            entry_titulo.delete(0, 'end')
            entry_autor.delete(0, 'end')
            entry_editora.delete(0, 'end')
            combo_generos.delete(0, 'end')
            entry_nome_alugador.delete(0, 'end')
            entry_alugado_em.delete(0, 'end')
            entry_data_de_retorno.delete(0, 'end')
            spin.delete(0, 'end')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    # * Função atualizar

    def atualizar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = tree_lista[0]

            entry_titulo.delete(0, 'end')
            entry_autor.delete(0, 'end')
            entry_editora.delete(0, 'end')
            combo_generos.delete(0, 'end')
            entry_nome_alugador.delete(0, 'end')
            entry_alugado_em.delete(0, 'end')
            entry_data_de_retorno.delete(0, 'end')
            spin.delete(0, 'end')

            entry_titulo.insert(0, tree_lista[1])
            entry_autor.insert(0, tree_lista[2])
            entry_editora.insert(0, tree_lista[3])
            combo_generos.insert(0, tree_lista[4])
            entry_nome_alugador.insert(0, tree_lista[5])
            entry_alugado_em.insert(0, tree_lista[6])
            entry_data_de_retorno.insert(0, tree_lista[7])
            spin.insert(0, tree_lista[8])

            def update():
                titulo = entry_titulo.get()
                autor = entry_autor.get()
                editora = entry_editora.get()
                genero = combo_generos.get()
                nome_alugador = entry_nome_alugador.get()
                alugado_em = entry_alugado_em.get()
                data_de_retorno = entry_data_de_retorno.get()
                paginas = spin.get()

                lista = [titulo, autor, editora, genero, nome_alugador,
                         alugado_em, data_de_retorno, paginas, valor_id]

                if titulo == '':
                    messagebox.showwarning(
                        'Atenção!', 'Primeiro é necessario selecionar um item da tabela e atualizar para depois confirmar')
                else:
                    atualizar_info(lista)
                    messagebox.showinfo(
                        'Sucesso!', 'Os dados foram atualizados com sucesso')

                    entry_titulo.delete(0, 'end')
                    entry_autor.delete(0, 'end')
                    entry_editora.delete(0, 'end')
                    combo_generos.delete(0, 'end')
                    entry_nome_alugador.delete(0, 'end')
                    entry_alugado_em.delete(0, 'end')
                    entry_data_de_retorno.delete(0, 'end')
                    spin.delete(0, 'end')

                for widget in frame_direita.winfo_children():
                    widget.destroy()

                    botao_confirmar.destroy()

                mostrar()

            # botao atualizar
            botao_confirmar = Button(frame_baixo2, command=update, text='Confirmar', width=10, anchor=NW, font=(
                'Ivy 7 bold'), bg='#0f944d', fg='#ffffff', relief='raised', overrelief='ridge')
            botao_confirmar.place(x=116, y=397)

        except IndexError:
            messagebox.showinfo(
                'Erro!', 'Selecione um dos dados da tabela para poder atualizar')

    # Função atualizar

    def deletar():
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = [tree_lista[0]]

            deletar_info(valor_id)
            messagebox.showinfo(
                'Sucesso!', 'Os dados foram deletados com sucesso')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

        except IndexError:
            messagebox.showerror(
                'Erro!', 'Selecione um dos dados da tabela para poder deletar')

    # * ----- Configurando frame_baixo com labels e entrys.... -----

    # * FAZER
    # titulo == '' or autor == '' or editora == '' or genero == '' or paginas == ''
    # Label e entry do Título do livro

    label_titulo = Label(frame_baixo2, text='Título*', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_titulo.place(x=10, y=10)

    entry_titulo = Entry(frame_baixo2, width=45, justify='left',
                         relief='solid', highlightthickness=1)
    entry_titulo.place(x=14, y=40)

    # Label e entry do Autor do livro

    label_autor = Label(frame_baixo2, text='Autor*', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_autor.place(x=10, y=70)

    entry_autor = Entry(frame_baixo2, width=45, justify='left',
                        relief='solid', highlightthickness=1)
    entry_autor.place(x=14, y=100)

    # Label e entry da Editora do livro

    label_editora = Label(frame_baixo2, text='Editora*', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_editora.place(x=10, y=130)

    entry_editora = Entry(frame_baixo2, width=15, justify='left',
                          relief='solid', highlightthickness=1)
    entry_editora.place(x=14, y=160)

    # Label e Combobox do Gênero do livro

    generos = ['Ficção científica', 'Fantasia', 'Horror', 'Ação e aventura', 'Suspense', 'Romance',
               'Conto', 'Ficção Policial', 'Biografia', 'Gastronomia', 'Humor', 'Tecnologia', 'Ciência']

    label_genero = Label(frame_baixo2, text='Gênero do livro*', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_genero.place(x=170, y=130)

    # Combobox

    combo_generos = ttk.Combobox(frame_baixo2, width=14,
                                 justify=CENTER, font=('Ivy 10'))

    combo_generos.place(x=167, y=159)

    combo_generos['values'] = (generos)

    # Label e entry de quem alugou o livro
    label_nome_alugador = Label(frame_baixo2, text='Pessoa que alugou:', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_nome_alugador.place(x=11, y=260)

    entry_nome_alugador = Entry(
        frame_baixo2, justify='left', relief='solid', highlightthickness=1)
    entry_nome_alugador.place(x=14, y=290)

    # Label e entry da DATA EM QUE FOI ALUGADO O LIVRO

    label_alugado_em = Label(frame_baixo2, text='Alugado em:', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_alugado_em.place(x=11, y=190)

    entry_alugado_em = DateEntry(
        frame_baixo2, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
    entry_alugado_em.place(x=14, y=220)

    # Label e entry da DATA DE RETORNO DO LIVRO ALUGADO

    label_data_de_retorno = Label(frame_baixo2, text='Retorno em:', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_data_de_retorno.place(x=177, y=190)

    entry_data_de_retorno = DateEntry(
        frame_baixo2, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
    entry_data_de_retorno.place(x=181, y=220)

    # Label e spinbox da quantidade de Páginas do livro

    label_paginas = Label(frame_baixo2, text='Páginas*', anchor=NW, font=(
        'Ivy 10 bold'), bg=cor1, fg=cor4, relief='flat')
    label_paginas.place(x=200, y=260)

    var = IntVar()
    var.set(0)
    spin = Spinbox(frame_baixo2, from_=0, to=10000, width=6, textvariable=var,
                   justify='left', relief='solid', highlightthickness=1)
    spin.place(x=205, y=290)

    #### * FUNÇÃO procurar dados #####

    def procurar():
        titulo = entry_pesquisar.get()

        lista = mostrar_info(titulo)

        tree.delete(*tree.get_children())

        for item in lista:
            tree.insert('', 'end', values=item)

        entry_pesquisar.delete(0, 'end')

    #### * BOTAO PROCURAR #####
    entry_pesquisar = Entry(frame_baixo2, width=21, justify='left',
                            relief='solid', highlightthickness=1)
    entry_pesquisar.place(x=157, y=325)

    botao_pesquisar = Button(frame_baixo2, command=procurar, text='Procurar Título/Ver dados', width=22, anchor=NW, font=(
        'Verdana 7 bold'), bg='white', fg='black', relief='raised', overrelief='ridge')
    botao_pesquisar.place(x=12, y=325)

    # * ----- Botões -----

    # Botão inserir

    botao_inserir = Button(frame_baixo2, command=inserir, text='Adicionar', width=10, anchor=NW, font=(
        'Ivy 9 bold'), bg=cor7, fg=cor1, relief='raised', overrelief='ridge')
    botao_inserir.place(x=14, y=360)

    # Botão Atualizar

    botao_atualizar = Button(frame_baixo2, command=atualizar, text='Atualizar', width=10, anchor=NW, font=(
        'Ivy 9 bold'), bg=cor2, fg=cor1, relief='raised', overrelief='ridge')
    botao_atualizar.place(x=110, y=360)

    # Botão Deletar

    botao_deletar = Button(frame_baixo2, command=deletar, text='Deletar', width=10, anchor=NW, font=(
        'Ivy 9 bold'), bg=cor8, fg=cor1, relief='raised', overrelief='ridge')
    botao_deletar.place(x=205, y=360)

    # * ------------------- codigo para tabela Frame Direita ----------------

    def mostrar():

        global tree

        lista = mostrar_info()

        # lista para cabecario
        tabela_head = ['ID', 'Título', 'Autor', 'Editora',
                       'Gênero', 'Nome', 'Alugado Em', 'Data Retorno', 'Páginas']

        # criando a tabela
        tree = ttk.Treeview(frame_direita, selectmode="extended",
                            columns=tabela_head, show="headings")

        # vertical scrollbar
        vsb = ttk.Scrollbar(
            frame_direita, orient="vertical", command=tree.yview)

        # horizontal scrollbar
        hsb = ttk.Scrollbar(
            frame_direita, orient="horizontal", command=tree.xview)

        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew')
        vsb.grid(column=1, row=0, sticky='ns')
        hsb.grid(column=0, row=1, sticky='ew')

        frame_direita.grid_rowconfigure(0, weight=12)

        hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw", "center", "center"]
        h = [35, 180, 155, 70, 110, 80, 90, 90, 60]
        n = 0

        for col in tabela_head:
            tree.heading(col, text=col.title(), anchor=CENTER)
            tree.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in lista:
            tree.insert('', 'end', values=item)

    # Chamando a função mostrar

    mostrar()

    janela.mainloop()

# ----- Configurando o frame baixo -------


# nome e entrada do nome
label_nome = Label(frame_baixo, text='Nome: ', anchor=NW,
                   font=('Ivy 10'), bg=cor1, fg=cor4)
label_nome.place(x=10, y=20)
entry_nome = Entry(frame_baixo, width=25, justify='left',
                   font=('', 15), highlightthickness=1, relief='solid')
entry_nome.place(x=14, y=50)


# Senha e entrada da senha
label_pass = Label(frame_baixo, text='Senha: ', anchor=NW,
                   font=('Ivy 10'), bg=cor1, fg=cor4)
label_pass.place(x=10, y=95)
entry_pass = Entry(frame_baixo, width=25, justify='left', show='*',
                   font=('', 15), highlightthickness=1, relief='solid')
entry_pass.place(x=14, y=130)


# Botao

botao_confirmar = Button(frame_baixo, command=verificar_senha, text='Entrar', width=39, height=2, font=(
    'Ivy 8 bold'), bg=cor6, fg=cor1, relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)


# * Centralizando o arquivo

# Dimensoes da janela
largura = 310
altura = 295

# Resolução do nosso sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()
# print(largura_screen, altura_screen)  # para saber as dimensoes do monitor


# Posição da janela
posx = largura_screen/2 - largura/1.8
posy = altura_screen/5 - altura/5

# Definir a geometria
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))


janela.mainloop()

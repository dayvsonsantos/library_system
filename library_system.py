from datetime import date
from tkinter import *
from tkinter import ttk

livros = {
    '4111113244': {'isbn': '4111113244', 'Titulo': 'O pequeno princepe', 'Gênero': 'Literatura Infatil', 'Ano': 2012,
                   'Autor': 'Paulo Coelho'},
    '8768686878': {'isbn': '8768686878', 'Titulo': 'A hora da verdade', 'Gênero': 'Literatura juvenil', 'Ano': 1999,
                   'Autor': 'Paulo Coelho'},
    '6464564456': {'isbn': '6464564456', 'Titulo': 'Dom Casmurro', 'Gênero': 'Literatura moderna', 'Ano': 1985,
                   'Autor': 'Paulo Coelho'},
    '7667754545': {'isbn': '7667754545', 'Titulo': 'Iracema', 'Gênero': 'Literatura naturalista', 'Ano': 1975,
                   'Autor': 'Paulo Coelho'}
}

alunos = {
    '2458582384': {'Matricula': '2458582384', 'Nome': 'Josiel', 'Unidade': 'EST', 'Curso': 'Engenharia Mecanica'},
    '9569749466': {'Matricula': '9569749466', 'Nome': 'Falcão', 'Unidade': 'EST', 'Curso': 'Engenharia Computação'},
    '5482890344': {'Matricula': '5482890344', 'Nome': 'Josefina', 'Unidade': 'ESA', 'Curso': ' Educação Fisica'},
    '2749235752': {'Matricula': '2749235752', 'Nome': 'Isabele', 'Unidade': 'ESAT', 'Curso': 'Dança'},
    '2348057295': {'Matricula': '2348057295', 'Nome': 'Maria Eduarda', 'Unidade': 'ESO', 'Curso': 'Direito '}
}

emprestimos = {
    '2458582384#4111113244': {'data_entrega': date.fromordinal(date.today().toordinal() - 30),
                              'data_devolucao': date.fromordinal(date.today().toordinal() - 3), 'data_devolvida': None,
                              'qtd_dias': 27, 'entregue': False}
}

punicoes = {
    '5748582384': {'dias_sem_emprestimo': 6, 'emprestimo': '2458582384#4111113244'}
}


############################# cadastro
def criar_livro(isbn, titulo, genero, ano, autor):
    livro = {'isbn': isbn, 'Titulo': titulo, 'Gênero': genero, 'Ano': ano, 'Autor': autor}
    return isbn, livro


def adicionar_livro(isbn, livro):
    if isbn in livros:
        return False
    else:
        livros[isbn] = livro
        return True


def criar_aluno(matricula, nome, unidade, curso):
    aluno = {'Matricula': matricula, 'Nome': nome, 'Unidade': unidade, 'Curso': curso}
    return matricula, aluno


def adicionar_alunos(matricula, aluno):
    if matricula in alunos:
        return False
    else:
        alunos[matricula] = aluno
        return True


############################# emprestimo
def atualizar_punicoes(matricula):
    if matricula in punicoes:
        hoje = date.today()
        chave_emprestimo = punicoes[matricula]['emprestimo']
        data_devolvida = emprestimos[chave_emprestimo]['data_devolvida']
        intervalo = (hoje - data_devolvida).days
        if intervalo > punicoes[matricula]['dias_sem_emprestimo']:
            del punicoes[matricula]


def devolver_livro(matricula, isbn):
    chave = matricula + "#" + isbn
    hoje = date.today()
    emprestimos[chave]['data_devolvida'] = hoje
    emprestimos[chave]['entregue'] = True
    data_devolucao = emprestimos[chave]['data_devolucao']
    intervalo = (hoje - data_devolucao).days
    if intervalo > 0:
        punicoes[matricula] = {'dias_sem_emprestimo': intervalo * 2, 'emprestimo': chave}
        print(punicoes)
        return True
    else:
        return False


def emprestar_livro(matricula, isbn, qtd_dias):
    atualizar_punicoes(matricula)
    if matricula in punicoes:
        return False
    else:
        chave = matricula + "#" + isbn
        hoje = date.today()
        entrega = date.fromordinal(date.today().toordinal() + int(qtd_dias))
        emprestimos[chave] = {'data_emprestimo': hoje, 'data_devolucao': entrega, 'data_devolvido': None,
                              'qtd_dias': int(qtd_dias), 'entregue': False}
        return True


############################## Janelas
def janela_cadastrar_livro():
    janela = Tk()
    janela.title("Cadastrar Livro")
    janela.geometry("600x500")

    ctn_cadastro = Frame(janela, padx=20, pady=20)
    ctn_cadastro.pack()

    # =============isbn=============
    lbl_isbn = Label(ctn_cadastro, text="ISBN")
    lbl_isbn.grid(row=0, column=0, pady=20)
    etr_isbn = Entry(ctn_cadastro, width=40)
    etr_isbn.grid(row=0, column=1, padx=3, pady=20)

    # =============titulo============
    lbl_titulo = Label(ctn_cadastro, text="Titulo")
    lbl_titulo.grid(row=1, column=0, pady=20)
    etr_titulo = Entry(ctn_cadastro, width=40)
    etr_titulo.grid(row=1, column=1, padx=3, pady=20)

    # =============genero============
    lbl_titulo = Label(ctn_cadastro, text="Genero")
    lbl_titulo.grid(row=2, column=0, pady=20)
    etr_genero = Entry(ctn_cadastro, width=40)
    etr_genero.grid(row=2, column=1, padx=3, pady=20)

    # =============ano===============
    lbl_ano = Label(ctn_cadastro, text="Ano")
    lbl_ano.grid(row=3, column=0, pady=20)
    etr_ano = Entry(ctn_cadastro, width=40)
    etr_ano.grid(row=3, column=1, padx=3, pady=20)

    # =============autor=============
    lbl_autor = Label(ctn_cadastro, text="Autor")
    lbl_autor.grid(row=4, column=0, pady=20)
    etr_autor = Entry(ctn_cadastro, width=40)
    etr_autor.grid(row=4, column=1, padx=3, pady=20)

    def feedback(msg):
        janela_in = Tk()
        janela_in.title("Feedback")
        janela_in.geometry("300x300")
        cont = Frame(janela_in, padx=20, pady=20)
        cont.pack()
        Label(cont, text=msg).pack()
        def sair(): janela_in.destroy(), janela.destroy()
        Button(cont, text="OK", width=12, command=sair).pack()
        janela_in.mainloop()

    def cadastrar_livro():
        isbn_, livro = criar_livro(etr_isbn.get(), etr_titulo.get(), etr_genero.get(), etr_ano.get(), etr_autor.get())
        if adicionar_livro(isbn_, livro):
            feedback("Livro Cadastrado!!!")
        else:
            feedback("Livro Não Cadastrado!!!")

    btn_cadastrar = Button(ctn_cadastro, text="Cadastrar", width=12, command=cadastrar_livro)
    btn_cadastrar.grid(row=5, column=1, pady=20)

    janela.mainloop()


def janela_cadastrar_aluno():
    janela = Tk()
    janela.title("Cadastrar Aluno")
    janela.geometry("600x500")

    ctn_cadastro = Frame(janela, padx=20, pady=20)
    ctn_cadastro.pack()

    # =============matricula==============
    lbl_matricula = Label(ctn_cadastro, text="Matricula")
    lbl_matricula.grid(row=0, column=0, pady=20)
    etr_matricula = Entry(ctn_cadastro, width=40)
    etr_matricula.grid(row=0, column=1, padx=3, pady=20)

    # =============nome==============
    lbl_nome = Label(ctn_cadastro, text="Nome")
    lbl_nome.grid(row=2, column=0, pady=20)
    etr_nome = Entry(ctn_cadastro, width=40)
    etr_nome.grid(row=2, column=1, padx=3, pady=20)

    # =============unidade==============
    lbl_unidade = Label(ctn_cadastro, text="Unidade")
    lbl_unidade.grid(row=3, column=0, pady=20)
    cbx_unidade = ttk.Combobox(ctn_cadastro, width=40)
    cbx_unidade['values'] = ("EST", "ENS", "ESAT", "ESA", "ESO")
    cbx_unidade.grid(row=3, column=1, padx=3, pady=20)

    # =============curso==============
    lbl_curso = Label(ctn_cadastro, text="Curso")
    lbl_curso.grid(row=4, column=0, pady=20)
    etr_curso = Entry(ctn_cadastro, width=40)
    etr_curso.grid(row=4, column=1, padx=3, pady=20)

    def feedback(msg):
        janela_in = Tk()
        janela_in.title("Feedback")
        janela_in.geometry("300x300")
        cont = Frame(janela_in, padx=20, pady=20)
        cont.pack()
        Label(cont, text=msg).pack()
        def sair(): janela_in.destroy(), janela.destroy()
        Button(cont, text="OK", width=12, command=sair).pack()
        janela_in.mainloop()

    def cadastrar_aluno():
        matricula_, aluno = criar_aluno(etr_matricula.get(), etr_nome.get(), cbx_unidade.get(), etr_curso.get())
        if adicionar_alunos(matricula_, aluno):
            feedback("Aluno Cadastrado!!!")
        else:
            feedback("Aluno Não Cadastrado!!!")

    btn = Button(ctn_cadastro, text="Cadastrar", width=12, command=cadastrar_aluno)
    btn.grid(row=5, column=1, padx=3, pady=20)

    janela.mainloop()


def janela_mostrar_livros():
    janela = Tk()
    janela.title("Mostrar Livros")
    janela.geometry("900x900")

    scr_bar = Scrollbar(janela)
    text_ = Text(janela, height=600, width=500)

    scr_bar.pack(side=RIGHT, fill=Y)
    text_.pack(side=LEFT, fill=Y)

    scr_bar.config(command=text_.yview)
    text_.config(yscrollcommand=scr_bar.set)

    s = ""
    for isbn, livro in livros.items():
        s += str(livro) + "\n" + "====================================================\n"
    text_.insert(END, s)
    janela.mainloop()


def janela_mostrar_alunos():
    janela = Tk()
    janela.title("Mostrar Alunos")
    janela.geometry("900x900")

    scr_bar = Scrollbar(janela)
    text_ = Text(janela, height=600, width=500)

    scr_bar.pack(side=RIGHT, fill=Y)
    text_.pack(side=LEFT, fill=Y)

    scr_bar.config(command=text_.yview)
    text_.config(yscrollcommand=scr_bar.set)

    s = ""
    for matricula, aluno in alunos.items():
        s += str(aluno) + "\n" + "====================================================\n"
    text_.insert(END, s)
    janela.mainloop()


def janela_ajuda():
    janela=Tk()
    janela.title("Tela de Ajuda")
    janela.geometry("600x600")
    text = Text(janela)
    text.pack()
    text.insert('insert', 'Com o software é possível: \n'
                          '- Cadastrar Aluno\n'
                          '- Remover Aluno\n'
                          '- Consultar Aluno\n'
                          '- Consultar livro\n'
                          '- Cadastrar Livro\n'
                          '- Remover Livro\n')
    janela.mainloop()


def janela_emprestimo():
    janela = Tk()
    janela.title("Emprestimo")
    janela.geometry("600x500")

    ctn_cadastro = Frame(janela, padx=20, pady=20)
    ctn_cadastro.pack()

    # ==============matricula===================
    lbl_matricula = Label(ctn_cadastro, text="Matricula")
    lbl_matricula.grid(row=0, column=0, pady=20)
    etr_matricula = Entry(ctn_cadastro, width=40)
    etr_matricula.grid(row=0, column=1, padx=3, pady=20)

    # ===============isbn========================
    lbl_isbn = Label(ctn_cadastro, text="ISBN")
    lbl_isbn.grid(row=1, column=0, pady=20)
    etr_isbn = Entry(ctn_cadastro, width=40)
    etr_isbn.grid(row=1, column=1, padx=3, pady=20)

    # ===================dias=========================
    lbl_qtd_dias = Label(ctn_cadastro, text="QTD Dias")
    lbl_qtd_dias.grid(row=2, column=0, pady=20)
    cbx_qtd_dias = ttk.Combobox(ctn_cadastro, width=40)
    cbx_qtd_dias['values'] = (1, 2, 3, 4, 5, 6, 7)
    cbx_qtd_dias.grid(row=2, column=1, padx=3, pady=20)

    def feedback(msg):
        janela_in = Tk()
        janela_in.title("Sucesso")
        janela_in.geometry("300x300")
        cont = Frame(janela_in, padx=20, pady=20)
        cont.pack()
        Label(cont, text=msg).pack()
        def sair(): janela_in.destroy(), janela.destroy()
        Button(cont, text="OK", width=12, command=sair).pack()
        janela_in.mainloop()

    def add_livro():
        chave = etr_matricula.get() + "#" + etr_isbn.get()
        if not (chave in emprestimos) and etr_matricula.get() != "" and etr_isbn.get() != "" and cbx_qtd_dias.get() != "":
            if emprestar_livro(etr_matricula.get(), etr_isbn.get(), cbx_qtd_dias.get()):
                feedback("Livro Emprestado!!!")
            else:
                feedback("Livro Não Emprestado!!!")
        else:
            feedback("Livro Não Emprestado!!!")

    btn_emprestar = Button(ctn_cadastro, text="Emprestar", width=12, command=add_livro)
    btn_emprestar.grid(row=3, column=0, pady=3)

    janela.mainloop()


def janela_devolver():
    janela = Tk()
    janela.title("Devolver livro")
    janela.geometry("600x500")

    ctn_cadastro = Frame(janela, padx=20, pady=20)
    ctn_cadastro.pack()

    lbl_matricula = Label(ctn_cadastro, text="Matricula")
    lbl_matricula.grid(row=0, column=0, pady=20)

    etr_matricula = Entry(ctn_cadastro, width=40)
    etr_matricula.grid(row=0, column=1, padx=3, pady=20)

    lbl_isbn = Label(ctn_cadastro, text="ISBN")
    lbl_isbn.grid(row=1, column=0, pady=20)

    etr_isbn = Entry(ctn_cadastro, width=40)
    etr_isbn.grid(row=1, column=1, padx=3, pady=20)

    def feedback(msg):
        aluno_cad = Tk()
        aluno_cad.title("Sucesso")
        aluno_cad.geometry("300x300")
        cont = Frame(aluno_cad, padx=20, pady=20)
        cont.pack()
        Label(cont, text=msg).pack()

        def sair(): aluno_cad.destroy(), janela.destroy()

        Button(cont, text="OK", width=12, command=sair).pack()
        aluno_cad.mainloop()

    def dev_livro():
        chave = etr_matricula.get() + "#" + etr_isbn.get()
        if (chave in emprestimos) and etr_matricula.get() != "" and etr_isbn.get() != "":
            if devolver_livro(etr_matricula.get(), etr_isbn.get()):
                feedback("Livro Devolvido!!!")
            else:
                feedback("Livro Não Devolvido!!!")
        else:
            feedback("Livro Não Devolvido!!!")

    btn_devolver = Button(ctn_cadastro, text="Devolver", width=12, command=dev_livro)
    btn_devolver.grid(row=3, column=0, pady=3)

    janela.mainloop()


def janela_principal():
    root = Tk()
    root.title("Gerenciamento de Biblioteca")
    root.geometry("1000x700")

    menubar = Menu(root)
    root.config(menu=menubar)

    menu1 = Menu(menubar)
    menu2 = Menu(menubar)
    menu3 = Menu(menubar)
    menu4 = Menu(menubar)

    menubar.add_cascade(label='Livros', menu=menu1)
    menubar.add_cascade(label='Alunos', menu=menu2)
    menubar.add_cascade(label='Emprestimos', menu=menu3)
    menubar.add_cascade(label='Ajuda', menu=menu4)

    menu1.add_command(label='Cadastrar Livro', command=janela_cadastrar_livro)
    menu1.add_command(label='Mostrar Livros Cadastrados', command=janela_mostrar_livros)
    menu2.add_command(label='Cadastrar Aluno', command=janela_cadastrar_aluno)
    menu2.add_command(label='Mostrar Alunos Cadastrados', command=janela_mostrar_alunos)
    menu3.add_command(label='Emprestar livro', command=janela_emprestimo)
    menu3.add_command(label='Devolver livro', command=janela_devolver)
    menu4.add_command(label='Ajuda', command=janela_ajuda)

    root.mainloop()

if __name__ == "__main__":
    janela_principal()




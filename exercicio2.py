import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

class funcs():
    def criar_lista(self):
        self.elementos = self.codigo_entry.get()
        self.elementos_lista = self.elementos.split(',')
        self.minha_lista = list(self.elementos_lista)
        messagebox.showinfo("Lista", f"A Lista é: {self.minha_lista}")
    
    def criar_e_mostrar_tupla(self):
        self.elementos = self.codigo_entry.get()
        self.elementos_tupla = self.elementos.split(',')
        self.minha_tupla = tuple(self.elementos_tupla)
        messagebox.showinfo("Tupla", f"A tupla é: {self.minha_tupla}")

    def substituir_espacos_por_virgulas(self):
        self.entrada_texto = self.codigo_entry.get()
        self.saida_texto = self.entrada_texto.replace(" ", ",")
        self.codigo_entry.delete(0, tk.END)
        self.codigo_entry.insert(0, self.saida_texto)

    def fechar_tudo(self):
        root.destroy()
        return
    
    def limpar_confg(self):
        self.codigo_entry.delete(0, tk.END)

    def texto_tupla(self, frame):
        textbox = tk.Text(frame, width=102, height=15, bd=2, relief="solid")
        textbox.grid(row=0, column=0)
        scrollbar = tk.Scrollbar(frame, command=textbox.yview, bg="blue")
        scrollbar.place(relx =0.98, rely = 0, relwidth = 0.02, relheight = 0.40)
        textbox.config(yscrollcommand=scrollbar.set)
        textbox.insert("1.0", 'Tupla\n\n' + "Tupla é um tipo de estrutura de dados utilizada em Python que funciona de modo semelhante a uma lista, entretanto, com a característica principal de ser imutável. Isso significa que quando uma tupla é criada não é possível adicionar, alterar ou remover seus elementos. Geralmente, ela é utilizada para adicionar tipos diferentes de informações, porém, com a quantidade de elementos definidos.Podemos utilizar uma tupla de dois elementos, por exemplo, para indicar a sigla do estado em uma posição e o nome dele em outra. Portanto, ela é uma boa opção quando queremos trabalhar com informações diferentes em uma mesma variável e quando queremos que esses dados não sofram alterações.Sua característica de imutabilidade oferece segurança nas informações armazenadas. Por isso, uma das finalidades da tupla é armazenar uma sequência de dados que não será modificada em outras partes do código.Entretanto, ela não é completamente imutável, pois quando armazena outro objeto, como uma lista, os dados armazenados nesse elemento podem ser modificados. É preciso entender, porém, que nesse caso não é alterado a estrutura da tupla, apenas o conteúdo desse objeto, que é passado por referência.Imagine que temos uma tupla que contém dois elementos, uma string com o nome de uma pessoa, e uma lista com os nomes de seus filhos. Perceba que a lista de filhos pode e deve sofrer alterações, caso a pessoa tenha um novo filho. Entretanto, a estrutura da tupla não foi alterada, pois ela continua com os mesmos elementos e função.\n\n")
        return
    
    def texto_lista(self, frame):
        textbox = tk.Text(frame, width=102, height=10, bd=2, relief="solid")
        textbox.grid(row=8, column=0)
        scrollbar = tk.Scrollbar(frame, command=textbox.yview, bg="blue")
        scrollbar.place(relx = 0.98, rely = 0.41, relwidth = 0.02, relheight = 0.27)
        textbox.config(yscrollcommand=scrollbar.set)
        textbox.insert("1.0", 'Lista\n\n' + "Em Python, list é uma estrutura de dados utilizada para armazenar elementos de forma sequencial e ordenada. As listas são acessadas por meio de um índice que inicia com o valor 0 para o primeiro elemento e é incrementada com 1 a cada novo item. Além disso, o último item da lista é representado pelo índice “–1”.Em Python, a lista é um tipo de dado mutável. Isso significa que elas podem ser modificadas, ou seja, é possível sobrescrever os valores atribuídos a ela. Isso não é possível com tipos de dados imutáveis, como as strings e as tuplas. Por sua característica mutável, é preciso atenção ao manipular os dados de uma lista para evitar a perda de informações.\n\n")
        return

class Application(funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        root.mainloop()

    def tela(self):
        self.root.title("Estrutura de Dados")
        self.root.configure(background= '#DCDCDC')
        self.root.geometry('900x650')
        self.root.resizable(False, True)
    
    def frames_da_tela(self):
        self.frame_1 = tk.Frame(self.root, bd= 4, bg='#708090', 
                                highlightbackground='#DAA520',highlightthickness= 3)
        self.frame_1.place(relx = 0.025, rely = 0.02, relwidth = 0.95, relheight = 0.95)

    def widgets_frame1(self):
        self.texto_tupla(self.frame_1)
        self.texto_lista(self.frame_1)

        self.btn_tupla = tk.Button(self.frame_1, text="Tupla", bd=3, bg='#C0C0C0', fg='black',
                                   font=('Arial', 11, 'bold'), command=self.criar_e_mostrar_tupla,)
        self.btn_tupla.place(relx=0.01, rely=0.92, relwidth=0.1, relheight=0.08)

        self.btn_lista = tk.Button(self.frame_1, text="Lista", bd=3, bg='#C0C0C0', fg='black',
                                   font=('Arial', 11, 'bold'), command=self.criar_lista)
        self.btn_lista.place(relx=0.12, rely=0.92, relwidth=0.1, relheight=0.08)

        self.btn_fecharbc = tk.Button(self.frame_1, text="Fechar", bd=3, bg='#C0C0C0', fg='black',
                                      font=('Arial', 11, 'bold'), command=self.fechar_tudo)
        self.btn_fecharbc.place(relx=0.90, rely=0.92, relwidth=0.1, relheight=0.08)

        self.btn_substituir = tk.Button(self.frame_1, text="Formatar", bd=3, bg='#C0C0C0', fg='black',
                                        font=('Arial', 11, 'bold'), command=self.substituir_espacos_por_virgulas)
        self.btn_substituir.place(relx=0.71, rely=0.80, relwidth=0.1, relheight=0.08)

        self.btn_limpar_tudo = tk.Button(self.frame_1, text="Limpar", bd=3, bg='#C0C0C0', fg='black',
                                         font=('Arial', 11, 'bold'), command=self.limpar_confg)
        self.btn_limpar_tudo.place(relx=0.34, rely=0.92, relwidth=0.1, relheight=0.08)

        self.codigo_lb = tk.Label(self.frame_1, text="Coloque os valores usando Espaço (Space) logo em seguida aperte o botão Formatar ", font=('Arial', 13, 'bold'),bg='#708090' )
        self.codigo_lb.place(relx=0.0, rely=0.72, relwidth=0.81, relheight=0.08)
        
        self.codigo_entry = tk.Entry(self.frame_1, font=('Arial', 15, 'bold'))
        self.codigo_entry.place(relx=0.0, rely=0.80, relwidth=0.70, relheight=0.08)

Application()
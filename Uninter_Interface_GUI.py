import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os


# ==================== FUNÇÕES DE ARQUIVO ====================

def ler_linhas(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt', encoding='utf-8') as a:
            return [linha.strip() for linha in a if linha.strip()]
    except FileNotFoundError:
        return []


def dividir_campos(linha):
    return [campo.strip() for campo in linha.split(';')]


def formatar_resumo(linha):
    campos = dividir_campos(linha)
    if len(campos) >= 3:
        return f'{campos[0]} - {campos[1]} - {campos[2]}'
    return ' - '.join(campos)


def cadastrarVaga(nomeArquivo, nomeEmpresa, nomeVaga, tipoVaga, detalhes=''):
    try:
        a = open(nomeArquivo, 'at', encoding='utf-8')
    except:
        return False
    else:
        linha = f'{nomeEmpresa}; {nomeVaga}; {tipoVaga}'
        if detalhes:
            linha += f'; {detalhes}'
        a.write(linha + '\n')
        a.close()
        return True


def cadastrarTreinamento(nomeArquivo, nomeEmpresa, nomeTreinamento, tipoTreinamento, detalhes=''):
    try:
        a = open(nomeArquivo, 'at', encoding='utf-8')
    except:
        return False
    else:
        linha = f'{nomeEmpresa}; {nomeTreinamento}; {tipoTreinamento}'
        if detalhes:
            linha += f'; {detalhes}'
        a.write(linha + '\n')
        a.close()
        return True


def existeArquivo(nomeArquivo):
    return os.path.exists(nomeArquivo)


def criarArquivo(nome):
    try:
        open(nome, 'wt+', encoding='utf-8').close()
        return True
    except:
        return False


# ==================== JANELA PRINCIPAL ====================

class AplicacaoUninter:
    def __init__(self, root):
        self.root = root
        self.root.title('Rede Social - Uninter')
        self.root.geometry('600x500')
        self.root.config(bg="#CACACA")
        
        self.arquivo_vagas = 'vagas.txt'
        self.arquivo_treinamentos = 'treinamentos.txt'
        
        # Criar arquivos se não existirem
        if not existeArquivo(self.arquivo_vagas):
            criarArquivo(self.arquivo_vagas)
        if not existeArquivo(self.arquivo_treinamentos):
            criarArquivo(self.arquivo_treinamentos)
        
        self.criar_menu_principal()
    
    def limpar_janela(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def criar_menu_principal(self):
        self.limpar_janela()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        titulo = ttk.Label(frame, text='REDE SOCIAL - UNINTER', font=('Poppins', 16, 'bold'))
        titulo.pack(pady=20)
        
        botoes = [
            ('Postar Vaga', self.janela_postar_vaga),
            ('Postar Treinamento', self.janela_postar_treinamento),
            ('Consultar Vagas', self.janela_consultar_vagas),
            ('Consultar Treinamentos', self.janela_consultar_treinamentos),
            ('Sair', self.root.quit),
        ]
        
        for texto, comando in botoes:
            btn = ttk.Button(frame, text=texto, command=comando, width=30)
            btn.pack(pady=10)
    
    def janela_postar_vaga(self):
        self.limpar_janela()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text='Postar Vaga', font=('Poppins', 14, 'bold')).pack(pady=10)
        
        ttk.Label(frame, text='Empresa:').pack(anchor='w')
        empresa = ttk.Entry(frame, width=40)
        empresa.pack(pady=5)
        
        ttk.Label(frame, text='Nome da Vaga:',).pack(anchor='w', pady=(10, 0))
        vaga = ttk.Entry(frame, width=40)
        vaga.pack(pady=5)
        
        ttk.Label(frame, text='Tipo de Vaga:').pack(anchor='w', pady=(10, 0))
        tipo = ttk.Entry(frame, width=40)
        tipo.pack(pady=5)
        
        ttk.Label(frame, text='Informações Adicionais:').pack(anchor='w', pady=(10, 0))
        detalhes = ttk.Entry(frame, width=40)
        detalhes.pack(pady=5)
        
        def salvar():
            if not empresa.get() or not vaga.get() or not tipo.get():
                messagebox.showwarning('Aviso', 'Preencha todos os campos obrigatórios!')
                return
            
            if cadastrarVaga(self.arquivo_vagas, empresa.get(), vaga.get(), tipo.get(), detalhes.get()):
                messagebox.showinfo('Sucesso', 'Vaga cadastrada com sucesso!')
                self.criar_menu_principal()
            else:
                messagebox.showerror('Erro', 'Erro ao cadastrar vaga.')
        
        frame_botoes = ttk.Frame(frame)
        frame_botoes.pack(pady=20)
        
        ttk.Button(frame_botoes, text='Salvar', command=salvar).pack(side='left', padx=5)
        ttk.Button(frame_botoes, text='Voltar', command=self.criar_menu_principal).pack(side='left', padx=5)
    
    def janela_postar_treinamento(self):
        self.limpar_janela()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text='Postar Treinamento', font=('Arial', 14, 'bold')).pack(pady=10)
        
        ttk.Label(frame, text='Empresa/Fornecedor:').pack(anchor='w')
        empresa = ttk.Entry(frame, width=40)
        empresa.pack(pady=5)
        
        ttk.Label(frame, text='Nome do Treinamento:').pack(anchor='w', pady=(10, 0))
        treinamento = ttk.Entry(frame, width=40)
        treinamento.pack(pady=5)
        
        ttk.Label(frame, text='Tipo de Treinamento:').pack(anchor='w', pady=(10, 0))
        tipo = ttk.Entry(frame, width=40)
        tipo.pack(pady=5)
        
        ttk.Label(frame, text='Informações Adicionais:').pack(anchor='w', pady=(10, 0))
        detalhes = ttk.Entry(frame, width=40)
        detalhes.pack(pady=5)
        
        def salvar():
            if not empresa.get() or not treinamento.get() or not tipo.get():
                messagebox.showwarning('Aviso', 'Preencha todos os campos obrigatórios!')
                return
            
            if cadastrarTreinamento(self.arquivo_treinamentos, empresa.get(), treinamento.get(), tipo.get(), detalhes.get()):
                messagebox.showinfo('Sucesso', 'Treinamento cadastrado com sucesso!')
                self.criar_menu_principal()
            else:
                messagebox.showerror('Erro', 'Erro ao cadastrar treinamento.')
        
        frame_botoes = ttk.Frame(frame)
        frame_botoes.pack(pady=20)
        
        ttk.Button(frame_botoes, text='Salvar', command=salvar).pack(side='left', padx=5)
        ttk.Button(frame_botoes, text='Voltar', command=self.criar_menu_principal).pack(side='left', padx=5)
    
    def janela_consultar_vagas(self):
        self.limpar_janela()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text='Consultar Vagas', font=('Arial', 14, 'bold')).pack(pady=10)
        
        vagas = ler_linhas(self.arquivo_vagas)
        
        if not vagas:
            ttk.Label(frame, text='Nenhuma vaga cadastrada.').pack(pady=20)
        else:
            # Frame com scrollbar
            frame_lista = ttk.Frame(frame)
            frame_lista.pack(fill='both', expand=True, pady=10)
            
            listbox = tk.Listbox(frame_lista, height=10)
            scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=listbox.yview)
            
            listbox.config(yscrollcommand=scrollbar.set)
            
            for i, vaga in enumerate(vagas, 1):
                listbox.insert(tk.END, f'{i} - {formatar_resumo(vaga)}')
            
            listbox.pack(side='left', fill='both', expand=True)
            scrollbar.pack(side='right', fill='y')
            
            def mostrar_detalhes():
                selecao = listbox.curselection()
                if not selecao:
                    messagebox.showwarning('Aviso', 'Selecione uma vaga!')
                    return
                
                indice = selecao[0]
                self.janela_detalhes_vaga(vagas[indice])
            
            ttk.Button(frame, text='Ver Detalhes', command=mostrar_detalhes).pack(pady=10)
        
        ttk.Button(frame, text='Voltar', command=self.criar_menu_principal).pack(pady=5)
    
    def janela_consultar_treinamentos(self):
        self.limpar_janela()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text='Consultar Treinamentos', font=('Arial', 14, 'bold')).pack(pady=10)
        
        treinamentos = ler_linhas(self.arquivo_treinamentos)
        
        if not treinamentos:
            ttk.Label(frame, text='Nenhum treinamento cadastrado.').pack(pady=20)
        else:
            frame_lista = ttk.Frame(frame)
            frame_lista.pack(fill='both', expand=True, pady=10)
            
            listbox = tk.Listbox(frame_lista, height=10)
            scrollbar = ttk.Scrollbar(frame_lista, orient='vertical', command=listbox.yview)
            
            listbox.config(yscrollcommand=scrollbar.set)
            
            for i, treinamento in enumerate(treinamentos, 1):
                listbox.insert(tk.END, f'{i} - {formatar_resumo(treinamento)}')
            
            listbox.pack(side='left', fill='both', expand=True)
            scrollbar.pack(side='right', fill='y')
            
            def mostrar_detalhes():
                selecao = listbox.curselection()
                if not selecao:
                    messagebox.showwarning('Aviso', 'Selecione um treinamento!')
                    return
                
                indice = selecao[0]
                self.janela_detalhes_treinamento(treinamentos[indice])
            
            ttk.Button(frame, text='Ver Detalhes', command=mostrar_detalhes).pack(pady=10)
        
        ttk.Button(frame, text='Voltar', command=self.criar_menu_principal).pack(pady=5)
    
    def janela_detalhes_vaga(self, linha):
        self.limpar_janela()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text='Detalhes da Vaga', font=('Arial', 14, 'bold')).pack(pady=10)
        
        campos = dividir_campos(linha)
        
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        if len(campos) > 0:
            ttk.Label(info_frame, text=f"Empresa: {campos[0]}", font=('Arial', 11)).pack(anchor='w', pady=5)
        if len(campos) > 1:
            ttk.Label(info_frame, text=f"Vaga: {campos[1]}", font=('Arial', 11)).pack(anchor='w', pady=5)
        if len(campos) > 2:
            ttk.Label(info_frame, text=f"Tipo: {campos[2]}", font=('Arial', 11)).pack(anchor='w', pady=5)
        
        if len(campos) > 3:
            ttk.Label(info_frame, text="Informações Adicionais:", font=('Arial', 11, 'bold')).pack(anchor='w', pady=(15, 5))
            for extra in campos[3:]:
                if extra:
                    ttk.Label(info_frame, text=f"• {extra}", font=('Arial', 10)).pack(anchor='w', padx=20, pady=2)
        
        ttk.Button(frame, text='Voltar', command=self.janela_consultar_vagas).pack(pady=10)
    
    def janela_detalhes_treinamento(self, linha):
        self.limpar_janela()
        
        frame = ttk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        ttk.Label(frame, text='Detalhes do Treinamento', font=('Arial', 14, 'bold')).pack(pady=10)
        
        campos = dividir_campos(linha)
        
        info_frame = ttk.Frame(frame)
        info_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        if len(campos) > 0:
            ttk.Label(info_frame, text=f"Fornecedor: {campos[0]}", font=('Arial', 11)).pack(anchor='w', pady=5)
        if len(campos) > 1:
            ttk.Label(info_frame, text=f"Treinamento: {campos[1]}", font=('Arial', 11)).pack(anchor='w', pady=5)
        if len(campos) > 2:
            ttk.Label(info_frame, text=f"Tipo: {campos[2]}", font=('Arial', 11)).pack(anchor='w', pady=5)
        
        if len(campos) > 3:
            ttk.Label(info_frame, text="Informações Adicionais:", font=('Arial', 11, 'bold')).pack(anchor='w', pady=(15, 5))
            for extra in campos[3:]:
                if extra:
                    ttk.Label(info_frame, text=f"• {extra}", font=('Arial', 10)).pack(anchor='w', padx=20, pady=2)
        
        ttk.Button(frame, text='Voltar', command=self.janela_consultar_treinamentos).pack(pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    app = AplicacaoUninter(root)
    root.mainloop()

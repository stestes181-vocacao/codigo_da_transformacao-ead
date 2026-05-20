import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

# --- FUNÇÃO LOGICA DA API E TRATAMENTO DE ERROS ---
def buscar_feriados():
    # Captura o ano que o usuário digitou no campo de entrada
    ano = entrada_ano.get().strip()
    
    # Validação básica: verifica se o campo está vazio
    if not ano:
        messagebox.showwarning("Aviso", "Por favor, digite um ano!")
        return
        
    # Limpa a área de texto antes de exibir o novo resultado
    area_texto.delete(1.0, tk.END)
    area_texto.insert(tk.END, f"Buscando feriados para o ano {ano}...\n\n")
    
    # URL da API brasileira de feriados
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    
    try:
        # Tentativa de requisição HTTP
        resposta = requests.get(url)
        
        # Se a API retornar erro 404 (ano não encontrado)
        if resposta.status_code == 404:
            messagebox.showerror("Erro", "Ano não encontrado ou fora do limite do sistema!")
            area_texto.delete(1.0, tk.END)
            return
            
        # Força o disparo de exceção para outros erros HTTP (ex: 500)
        resposta.raise_for_status()
        
        # Converte a resposta em formato JSON (Lista de Dicionários)
        feriados = resposta.json()
        
        # Limpa o texto de "Buscando..." para colocar o resultado final
        area_texto.delete(1.0, tk.END)
        area_texto.insert(tk.END, f"🎉 Feriados Nacionais em {ano}:\n")
        area_texto.insert(tk.END, "="*40 + "\n\n")
        
        # Filtragem e exibição dos dados específicos
        for feriado in feriados:
            # Formatando a exibição da data e nome do feriado
            texto_feriado = f"📅 Data: {feriado['date']} | 🎈 {feriado['name']}\n"
            area_texto.insert(tk.END, texto_feriado)
            
    except requests.exceptions.ConnectionError:
        # Se houver falha na conexão de internet
        messagebox.showerror("Erro de Conexão", "Não foi possível conectar à internet!")
        area_texto.delete(1.0, tk.END)
        
    except Exception as e:
        # Captura qualquer outra exceção inesperada
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")
        area_texto.delete(1.0, tk.END)

# --- CONSTRUÇÃO DA INTERFACE GRÁFICA (TELA) ---
# 1. Criando a janela principal
janela = tk.Tk()
janela.title("Buscador de Feriados Brasileiros")
janela.geometry("500x450")

# 2. Rótulo explicativo (Label)
rotulo = tk.Label(janela, text="Digite o ano desejado (ex: 2026):", font=("Arial", 11))
rotulo.pack(pady=10)

# 3. Campo de entrada de texto (Entry)
entrada_ano = tk.Entry(janela, font=("Arial", 12), width=15, justify="center")
entrada_ano.pack(pady=5)

# 4. Botão de comando (Button) ligado à nossa função
botao_buscar = tk.Button(janela, text="Buscar Feriados", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=buscar_feriados)
botao_buscar.pack(pady=10)

# 5. Área de texto com barra de rolagem integrada (ScrolledText) para os resultados
area_texto = scrolledtext.ScrolledText(janela, width=55, height=18, font=("Courier New", 10))
area_texto.pack(pady=10)

# Inicializa e mantém a tela aberta esperando interações
janela.mainloop()
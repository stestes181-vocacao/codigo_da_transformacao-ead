import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

def buscar_feriados():
    
    ano = entrada_ano.get().strip()
    
    
    if not ano:
        messagebox.showwarning("Aviso", "Por favor, digite um ano!")
        return
        
    area_texto.delete(1.0, tk.END)
    area_texto.insert(tk.END, f"Buscando feriados para o ano {ano}...\n\n")
    
    
    url = f"chttps://brasilapi.com.br/api/feriados/v1/{ano}"
    
    try:
        
        resposta = requests.get(url)
        
        
        if resposta.status_code == 404:
            messagebox.showerror("Erro", "Ano não encontrado ou fora do limite do sistema!")
            area_texto.delete(1.0, tk.END)
            return
            
    
        resposta.raise_for_status()
        
        feriados = resposta.json()
        
       
        area_texto.delete(1.0, tk.END)
        area_texto.insert(tk.END, f"🎉 Feriados Nacionais em {ano}:\n")
        area_texto.insert(tk.END, "="*40 + "\n\n")
        
        
        for feriado in feriados:
            
            texto_feriado = f"📅 Data: {feriado['date']} | 🎈 {feriado['name']}\n"
            area_texto.insert(tk.END, texto_feriado)
            
    except requests.exceptions.ConnectionError:
        
        messagebox.showerror("Erro de Conexão", "Não foi possível conectar à internet!")
        area_texto.delete(1.0, tk.END)
        
    except Exception as e:
        
        messagebox.showerror("Erro Inesperado", f"Ocorreu um erro: {e}")
        area_texto.delete(1.0, tk.END)


janela = tk.Tk()
janela.title("Buscador de Feriados Brasileiros")
janela.geometry("500x450")

rotulo = tk.Label(janela, text="Digite o ano desejado (ex: 2026):", font=("Arial", 11))
rotulo.pack(pady=10)

entrada_ano = tk.Entry(janela, font=("Arial", 12), width=15, justify="center")
entrada_ano.pack(pady=5)

botao_buscar = tk.Button(janela, text="Buscar Feriados", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", command=buscar_feriados)
botao_buscar.pack(pady=10)

area_texto = scrolledtext.ScrolledText(janela, width=55, height=18, font=("Courier New", 10))
area_texto.pack(pady=10)

janela.mainloop()
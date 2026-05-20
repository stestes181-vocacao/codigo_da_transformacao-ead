import requests  # 1. Fazemos a importação da biblioteca para internet

def consultar_feriados(ano):
    # Definimos a URL da API brasileira (BrasilAPI) usando o ano escolhido
    url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
    
    print(f"\n--- Buscando feriados nacionais do ano {ano} ---")
    
    try:
        # 2. Tentamos fazer a requisição HTTP (pedido ao servidor)
        resposta = requests.get(url)
        
        # Se o status_code for 404, significa que o ano é inválido ou não encontrado
        if resposta.status_code == 404:
            print("Erro: Ano não encontrado ou fora do limite do sistema.")
            return
            
        # Verifica se houve qualquer outro erro de transmissão (Ex: Status 500)
        resposta.raise_for_status()
        
        # 3. Convertemos a resposta para o formato que o Python entende (Lista de Dicionários)
        feriados = resposta.json()
        
        # 4. Exibimos dados específicos filtrados
        print(f"\n🎉 Feriados encontrados:")
        for feriado in feriados:
            # Filtramos e exibimos apenas a Data e o Nome do feriado
            print(f"📅 Data: {feriado['date']} | 🎈 Feriado: {feriado['name']}")
            
    except requests.exceptions.ConnectionError:
        # Trata o erro se o aluno estiver sem internet no momento
        print("Erro de Conexão: Verifique se você está conectado à internet!")
        
    except requests.exceptions.HTTPError as erro_http:
        # Trata erros específicos de requisição HTTP
        print(f"Erro na requisição HTTP: {erro_http}")
        
    except Exception as erro:
        # Um 'apanha-tudo' para qualquer outro imprevisto
        print(f"Ocorreu um erro inesperado: {erro}")
        
    finally:
        print("--- Fim da consulta de feriados ---")

# --- TESTANDO NA PRÁTICA ---
print("=== Aula de API com Python: Feriados Nacionais ===")

# Pedindo o ano para o aluno interagir
ano_letivo = input("Digite o ano que deseja consultar (ex: 2026): ")
consultar_feriados(ano_letivo)
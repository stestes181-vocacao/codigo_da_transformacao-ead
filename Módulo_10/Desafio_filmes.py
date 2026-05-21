import requests

def consultar_dados_ddd(ddd):
    
    url = f"https://brasilapi.com.br/api/ddd/v1/{ddd}"
    
    print(f"\n--- Conectando à API para o DDD {ddd} ---")
    
    try:
        
        resposta = requests.get(url)
        
        
        if resposta.status_code == 404:
            print(f"❌ Erro: O DDD {ddd} não é um código de área válido no Brasil.")
            return
            
        resposta.raise_for_status()
        
        
        dados = resposta.json()
        
       
        estado = dados['state']       # Filtra a sigla do Estado (ex: SP, RJ, BA)
        cidades = dados['cities']     # Filtra a lista com todas as cidades do DDD
        
        print(f"\n📍 Estado localizado: {estado}")
        print(f"🏙️ Cidades que usam o DDD {ddd} (Total: {len(cidades)}):")
        print("-" * 40)
        
        # Listando as cidades - organizada
        for cidade in cidades:
            print(f"• {cidade}")
            
    # Tratar erros de conexão e falhas HTTP
    except requests.exceptions.ConnectionError:
        print("\n❌ Erro de Rede: Verifique se o seu computador está conectado à internet!")
        
    except requests.exceptions.HTTPError as erro_http:
        print(f"\n❌ Erro HTTP encontrado: {erro_http}")
        
    except Exception as erro:
        print(f"\n❌ Ocorreu um erro imprevisto: {erro}")
        
    finally:
        print("\n--- Fim da verificação de telecomunicação ---")

# --- EXECUÇÃO---
print("=== Atividade Prática: Descobrir Cidades por DDD ===")
codigo_area = input("Digite o DDD que deseja consultar (apenas os 2 números, ex: 11): ").strip()

consultar_dados_ddd(codigo_area)
import requests

API_KEY = "MY_API_KEY"

# Nome 
filme = input("Digite o nome do filme: ")

# URL 
url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={filme}&language=pt-BR"

try:

    
    resposta = requests.get(url)
    resposta.raise_for_status()

    
    dados = resposta.json()
    if dados["results"]:

        resultado = dados["results"][0]

        print("\n🎬 FILME ENCONTRADO 🎬\n")

        print("Título:", resultado["title"])

        print("Data de lançamento:", resultado["release_date"])

        print("Nota:", resultado["vote_average"])

        print("Sinopse:")
        print(resultado["overview"])

    else:

        print("❌ Filme não encontrado!")


except requests.exceptions.ConnectionError:

    print("❌ Sem conexão com internet!")


except Exception as erro:

    print("❌ Ocorreu um erro:")
    print(erro)
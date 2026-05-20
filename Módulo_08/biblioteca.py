
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True  # Todo livro começa disponível

    def __str__(self):
        # Uma forma mais elegante de mostrar o status do livro
        status = "🟢 Disponível" if self.disponivel else "🔴 Emprestado"
        return f"'{self.titulo}' por {self.autor} [{status}]"



class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"✅ Livro '{livro.titulo}' adicionado ao catálogo.")

    def listar_livros(self):
        print("\n📚 --- CATÁLOGO DA BIBLIOTECA ---")
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        
        for livro in self.livros:
            print(livro)
        print("---------------------------------")

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            
            if livro.titulo.lower() == titulo.lower():
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"📖 Sucesso: O livro '{livro.titulo}' foi emprestado!")
                    return
                else:
                    print(f"⚠️ Ops: O livro '{livro.titulo}' já está emprestado no momento.")
                    return
                    
        print(f"❌ Erro: O livro '{titulo}' não foi encontrado no sistema.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                if not livro.disponivel:
                    livro.disponivel = True
                    print(f"🔄 Sucesso: O livro '{livro.titulo}' foi devolvido e está disponível!")
                    return
                else:
                    print(f"⚠️ Atenção: O livro '{livro.titulo}' já constava como disponível.")
                    return
                    
        print(f"❌ Erro: O livro '{titulo}' não pertence a esta biblioteca.")


if __name__ == "__main__":
    
    minha_biblioteca = Biblioteca()
    print("--- Inicializando o Sistema ---\n")

    
    livro1 = Livro("sherlock holmes", "arthur conan coyle")
    livro2 = Livro("o pequeno prícipe", "antoine de saint-exupéry")
    livro3 = Livro("percy jackson", "rick riordan")

    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)
    minha_biblioteca.adicionar_livro(livro3)

    
    minha_biblioteca.listar_livros()

    
    print("\n[Ação] Solicitando empréstimo de 'harry potter'...")
    minha_biblioteca.emprestar_livro("harry potter")

    
    print("\n[Ação] Tentando pegar o mesmo livro de novo...")
    minha_biblioteca.emprestar_livro("sherlock holmes")

    
    minha_biblioteca.listar_livros()

    
    print("\n[Ação] Devolvendo o livro...")
    minha_biblioteca.devolver_livro("sherlock holmes")

    
    minha_biblioteca.listar_livros()
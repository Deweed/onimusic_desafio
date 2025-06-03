# client_cli.py

import requests
import json # Para pretty print do JSON

BASE_URL = "http://127.0.0.1:8000/api/filmes/"

def listar_filmes():
    """Lista todos os filmes cadastrados."""
    print("\n--- Listando Filmes ---")
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP ruins (4xx ou 5xx)
        filmes = response.json()
        if not filmes:
            print("Nenhum filme cadastrado.")
            return

        for filme in filmes:
            print(f"ID: {filme['id']}")
            print(f"  Título: {filme['titulo']}")
            print(f"  Ano: {filme['ano']}")
            print(f"  Gênero: {filme['genero']}")
            print("-" * 20)
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor. Certifique-se de que o servidor Django está rodando.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

def adicionar_filme():
    """Adiciona um novo filme."""
    print("\n--- Adicionar Novo Filme ---")
    titulo = input("Título: ")
    ano = int(input("Ano: ")) # Validação básica de int
    genero = input("Gênero: ")

    novo_filme = {
        "titulo": titulo,
        "ano": ano,
        "genero": genero
    }
    try:
        response = requests.post(BASE_URL, json=novo_filme)
        response.raise_for_status()
        filme_adicionado = response.json()
        print(f"Filme '{filme_adicionado['titulo']}' (ID: {filme_adicionado['id']}) adicionado com sucesso!")
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor. Certifique-se de que o servidor Django está rodando.")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar filme: {e}")
        if response.status_code == 400: # Exemplo de tratamento de erro de validação
            print(f"Detalhes do erro: {response.json()}")

def buscar_filme():
    """Busca um filme pelo ID."""
    print("\n--- Buscar Filme por ID ---")
    try:
        filme_id = int(input("Digite o ID do filme: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número inteiro.")
        return

    url = f"{BASE_URL}{filme_id}/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        filme = response.json()
        print(f"ID: {filme['id']}")
        print(f"  Título: {filme['titulo']}")
        print(f"  Ano: {filme['ano']}")
        print(f"  Gênero: {filme['genero']}")
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor. Certifique-se de que o servidor Django está rodando.")
    except requests.exceptions.RequestException as e:
        if response.status_code == 404:
            print(f"Filme com ID {filme_id} não encontrado.")
        else:
            print(f"Erro ao buscar filme: {e}")

def remover_filme():
    """Remove um filme pelo ID."""
    print("\n--- Remover Filme por ID ---")
    try:
        filme_id = int(input("Digite o ID do filme a ser removido: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número inteiro.")
        return

    url = f"{BASE_URL}{filme_id}/"
    try:
        response = requests.delete(url)
        response.raise_for_status()
        print(f"Filme com ID {filme_id} removido com sucesso (se existia).")
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor. Certifique-se de que o servidor Django está rodando.")
    except requests.exceptions.RequestException as e:
        if response.status_code == 404:
            print(f"Filme com ID {filme_id} não encontrado.")
        else:
            print(f"Erro ao remover filme: {e}")


def main_menu():
    """Exibe o menu principal e gerencia as opções."""
    while True:
        print("\n=== Gerenciador de Filmes (CLI) ===")
        print("1. Listar todos os filmes")
        print("2. Adicionar novo filme")
        print("3. Buscar filme por ID")
        print("4. Remover filme por ID")
        print("5. Sair")
        print("====================================")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            listar_filmes()
        elif escolha == '2':
            adicionar_filme()
        elif escolha == '3':
            buscar_filme()
        elif escolha == '4':
            remover_filme()
        elif escolha == '5':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main_menu()
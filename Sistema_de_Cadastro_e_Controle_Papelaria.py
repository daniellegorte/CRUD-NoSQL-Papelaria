
from pymongo import MongoClient
from datetime import datetime

CONEXAO = "mongodb://localhost:27017/"
cliente = MongoClient(CONEXAO)
banco = cliente["papelaria_db"]
produtos = banco["produtos"]

while True:
    print(" \n=== BEM VINDO AO PAPERWEB ===\n")
    print(" === O que deseja fazer hoje? ==\n")
    print("1. CONSULTAR PRODUTO\n")
    print("2. CADASTRAR PRODUTO\n")
    print("3. ATUALIZAR PRODUTO\n")
    print("4. EXCLUIR PRODUTO\n")
    print("0. ENCERRAR SISTEMA\n")
    opcao = input("OPÇÃO: ")

    match opcao:
        case "1":
            while True:
                print(" == CONSULTA DE PRODUTO ==\n")
                codigoProduto = input("CÓDIGO DO PRODUTO: ")
                resultado = produtos.find_one({"codigo_produto": codigoProduto.upper()})
                if resultado:
                    print("\nPRODUTO ENCONTRADO:")
                    print(resultado)
                else:
                    print("\nPRODUTO NÃO ENCONTRADO")

                print("== DESEJA CONSULTAR NOVO PRODUTO? ==\n")
                print("1. CONSULTAR NOVO PRODUTO\n")
                print("0. VOLTAR AO INICIO\n")
                opcaoConsulta = input("OPÇÃO: ")
                
                if opcaoConsulta == "0":
                    
                    break

                if opcaoConsulta != "1" and opcaoConsulta != "0":
                    print("OPÇÃO INVÁLIDA!")


        case "2":
            while True:
                print(" == CADASTRO DE PRODUTO ==\n")
                codigoProduto = input("CÓDIGO DO PRODUTO: (ex PAP001): ")

                if produtos.find_one({"codigo_produto": codigoProduto.upper()}):
                    print("CÓDIGO JÁ CADASTRADO EM SISTEMA.\n")
                    continue

                nomeProduto = input("NOME: ")
                categoria = input("CATEGORIA: ")
                marca = input("MARCA: ")

                try:
                    preco = float(input("PREÇO (ex: 1.50): ").replace(",", "."))
                except ValueError:
                    preco = 0.0

                try:
                    qntEstoque = int(input("QUANTIDADE EM ESTOQUE: "))
                except ValueError:
                    qntEstoque = 0

                disponivelInput = input("DISPONÍVEL? (S/N): ").upper()
                disponivel = True if disponivelInput == "S" else False

                dataCadastro = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z")

                coresInput = input("CORES DISPONÍVEIS (separe por vírgula): ")
                cores = [c.strip() for c in coresInput.split(",") if c.strip()]

                print(" == DADOS DE FORNECEDOR ==\n")
                fornNome = input("NOME: ")
                cidade = input("CIDADE: ")
                telefone = input("TELEFONE: ")

                try:
                    avaliacao = float(input("Avaliação (ex: 4.8): ").replace(",", "."))
                except ValueError:
                    avaliacao = 0.0

                descricao = input("Descrição: ")

                novo_produto = {
                    "codigo_produto": codigoProduto,
                    "nome": nomeProduto,
                    "categoria": categoria,
                    "marca": marca,
                    "preco": float(preco),
                    "quantidade_estoque": int(qntEstoque),
                    "disponivel": disponivel,
                    "data_cadastro": dataCadastro,
                    "cores": cores,
                    "fornecedor": {
                        "nome": fornNome,
                        "cidade": cidade,
                        "telefone": telefone
                    },
                    "avaliacao": float(avaliacao),
                    "descricao": descricao
                }

                try:
                    resultado = produtos.insert_one(novo_produto)
                    print(f"\nPRODUTO CADASTRADO COM ID: {resultado.inserted_id}")
                except Exception as e:
                    print(f"\nERRO AO CADASTRAR: {e}")

                print("== DESEJA CADASTRAR NOVO PRODUTO? ==\n")
                print("1. CADASTRAR NOVO PRODUTO\n")
                print("0. VOLTAR AO INICIO\n")
                opcaoConsulta = input("OPÇÃO: ")
                
                if opcaoConsulta == "0":
                    
                    break

                if opcaoConsulta != "1" and opcaoConsulta != "0":
                    print("OPÇÃO INVÁLIDA!")



        case "3":
            while True:
                print(" == ATUALIZAÇÃO DE PRODUTO ==\n")
                codigoProduto = input("CÓDIGO DO PRODUTO: (ex PAP001): ")
                produtoExistente = produtos.find_one({"codigo_produto": codigoProduto.upper()})
                if not produtoExistente:
                    print("PRODUTO NÃO ENCONTRADO NO SISTEMA.\n")
                    continue

                print("DIGITE OS NOVOS DADOS:")
                nomeProduto = input("NOVO NOME: ")
                categoria = input("NOVA CATEGORIA: ")
                marca = input("NOVA MARCA: ")

                try:
                    preco = float(input("NOVO PREÇO (ex: 1.50): ").replace(",", "."))
                except ValueError:
                    preco = produtoExistente.get("preco", 0.0)

                try:
                    qntEstoque = int(input("NOVA QUANTIDADE EM ESTOQUE: "))
                except ValueError:
                    qntEstoque = produtoExistente.get("quantidade_estoque", 0)

                disponivelInput = input("DISPONÍVEL? (S/N): ").upper()
                disponivel = True if disponivelInput == "S" else False

                coresInput = input("NOVAS CORES DISPONÍVEIS (separe por vírgula): ")
                cores = [c.strip() for c in coresInput.split(",") if c.strip()]

                print(" == DADOS DE FORNECEDOR ==\n")
                fornNome = input("NOVO NOME: ")
                cidade = input("NOVA CIDADE: ")
                telefone = input("NOVO TELEFONE: ")

                try:
                    avaliacao = float(input("NOVA AVALIAÇÃO (ex: 4.8): ").replace(",", "."))
                except ValueError:
                    avaliacao = produtoExistente.get("avaliacao", 0.0)

                descricao = input("NOVA DESCRIÇÃO: ")

                try:
                    resultado = produtos.update_one(
                        {"codigo_produto": codigoProduto},
                        {
                            "$set": {
                                "nome": nomeProduto,
                                "categoria": categoria,
                                "marca": marca,
                                "preco": float(preco),
                                "quantidade_estoque": int(qntEstoque),
                                "disponivel": disponivel,
                                "cores": cores,
                                "fornecedor": {
                                    "nome": fornNome,
                                    "cidade": cidade,
                                    "telefone": telefone
                                },
                                "avaliacao": float(avaliacao),
                                "descricao": descricao
                            }
                        }
                    )
                    if resultado.modified_count > 0:
                        print("\nPRODUTO ATUALIZADO COM SUCESSO!")
                    else:
                        print("\nNENHUMA ALTERAÇÃO FOI FEITA NO PRODUTO.")
                except Exception as e:
                    print(f"\nERRO AO ATUALIZAR: {e}")

                print("== DESEJA ATUALIZAR NOVO PRODUTO? ==\n")
                print("1. ATUALIZAR NOVO PRODUTO\n")
                print("0. VOLTAR AO INICIO\n")
                opcaoConsulta = input("OPÇÃO: ")
                
                if opcaoConsulta == "0":
                    
                    break

                if opcaoConsulta != "1" and opcaoConsulta != "0":
                    print("OPÇÃO INVÁLIDA!")


        case "4":
            while True:
                print(" == EXCLUSÃO DE PRODUTO ==\n")
                codigoProduto = input("CÓDIGO DO PRODUTO: (ex PAP001): ")

                produtoExistente = produtos.find_one({"codigo_produto": codigoProduto})
                if not produtoExistente:
                    print("PRODUTO NÃO ENCONTRADO NO SISTEMA.\n")
                    continue

                confirmacao = input(f"CONFIRMAR EXCLUSÃO? DO PRODUTO {produtoExistente.get('nome')}? (S/N): ").upper()
                if confirmacao == "S":
                    try:
                        resultado = produtos.delete_one({"codigo_produto": codigoProduto})
                        if resultado.deleted_count > 0:
                            print("\nPRODUTO EXCLUÍDO COM SUCESSO!")
                        else:
                            print("\nFALHA AO EXCLUIR O PRODUTO.")
                    except Exception as e:
                        print(f"\nERRO AO EXCLUIR: {e}")
                else:
                    print("\nEXCLUSÃO CANCELADA.")

                print("== DESEJA EXCLUIR NOVO PRODUTO? ==\n")
                print("1. EXCLUIR NOVO PRODUTO\n")
                print("0. VOLTAR AO INICIO\n")
                opcaoConsulta = input("OPÇÃO: ")
                
                if opcaoConsulta == "0":
                    
                    break

                if opcaoConsulta != "1" and opcaoConsulta != "0":
                    print("OPÇÃO INVÁLIDA!")

        case "0":
            print("Programa encerrado.")
            break
        
    if opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "0":
        print(" == OPÇÃO INVÁLIDA! ==")

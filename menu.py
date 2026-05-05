from logica import criar_colmeia
from guardar import guardar_dados, carregar_dados
from validar import validar_email, validar_data, validar_codigo_colmeia

def menu_principal():
    # Carregar dados ao iniciar
    colmeias = carregar_dados()
    
    while True:
        print("\n--- SISTEMA DE GESTÃO APÍCOLA ---")
        print("1. Registar Nova Colmeia")
        print("2. Listar Todas as Colmeias")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            # Aqui vamos pedir os dados e usar as validações (ver passo seguinte)
            print("\nFuncionalidade de registo em desenvolvimento...")
            
        elif opcao == "2":
            if not colmeias:
                print("\nNão existem colmeias registadas.")
            else:
                for c in colmeias:
                    print(f"ID: {c['id']} | Código: {c['codigo']} | Local: {c['localizacao']}")
        
        elif opcao == "0":
            confirmar = input("Deseja guardar as alterações antes de sair? (S/N): ").upper()
            if confirmar == "S":
                guardar_dados(colmeias)
            print("A encerrar...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
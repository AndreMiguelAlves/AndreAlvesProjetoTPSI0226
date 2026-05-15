from logica import criar_colmeia, atualizar_colmeia, eliminar_colmeia
from guardar import guardar_dados, carregar_dados
from validar import validar_email, validar_data, validar_codigo_colmeia
from pesquisa import pesquisa_linear, pesquisa_binaria
from Ordenacao import bubble_sort, selection_sort
from calcfilt import gerar_estatisticas, filtrar_por_local

def ler_input(msg, func, erro):
    while True:
        val = input(msg).strip()
        if func(val): return val
        print(f"[Erro] {erro}")

def menu():
    colmeias = carregar_dados()
    while True:
        print("\n=== GESTÃO APÍCOLA ===")
        print("1. Registar | 2. Listar | 3. Pesquisar | 4. Editar | 5. Eliminar")
        print("6. Ordenar  | 7. Estatísticas | 0. Sair")
        op = input("Opção: ")

        if op == "1":
            cod = ler_input("Código (EX1234): ", validar_codigo_colmeia, "Formato inválido!")
            loc = input("Local: ")
            dat = ler_input("Data (DD-MM-AAAA): ", validar_data, "Data inválida!")
            mel = input("Tipo Mel: ")
            mail = ler_input("Email: ", validar_email, "Email inválido!")
            colmeias.append(criar_colmeia(cod, loc, dat, mel, mail))
        
        elif op == "2":
            for c in colmeias: print(f"{c['id']} | {c['codigo']} | {c['localizacao']}")

        elif op == "3":
            termo = input("ID para Pesquisa Binária: ")
            col_ord = sorted(colmeias, key=lambda x: x['id'])
            res = pesquisa_binaria(col_ord, 'id', termo)
            print(res if res else "Não encontrado.")

        elif op == "4":
            id_e = input("ID a editar: ")
            # Lógica de edição similar ao registo...
            pass

        elif op == "5":
            id_r = input("ID a eliminar: ")
            if input("Confirmar? (S/N): ").upper() == "S":
                eliminar_colmeia(colmeias, id_r)

        elif op == "6":
            colmeias = bubble_sort(colmeias, 'codigo', True)
            print("Ordenado por Código.")

        elif op == "7":
            s = gerar_estatisticas(colmeias)
            print(f"Total: {s['total']}")

        elif op == "0":
            if input("Guardar antes de sair? (S/N): ").upper() == "S":
                guardar_dados(colmeias)
            break

if __name__ == "__main__":
    menu()
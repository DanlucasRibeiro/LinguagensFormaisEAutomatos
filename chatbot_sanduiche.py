import re

def perguntar(prompt):
    return input(prompt + "\n> ").strip().lower()

# Cardápio
TIPOS = ["cheeseburger", "frango", "veggie", "x-salada"]
PAES = ["branco", "integral", "australiano"]
TAMANHOS = ["pequeno", "médio", "medio", "grande"]
EXTRAS_OPCOES = ["queijo", "bacon", "molho", "ovo", "salada"]

def extrair_palavra(texto, opcoes):
    for opt in opcoes:
        if opt in texto:
            return opt
    return None

def main():
    estado = "SAUDACAO"
    pedido = {
        "tipo": None,
        "pao": None,
        "tamanho": None,
        "extras": [],
        "endereco": None,
        "pagamento": None
    }

    print("Bot: Olá! Sou o Sandubot. Diga 'quero pedir' para fazer um pedido de sanduíche.")

    while True:
        # ---------------- ESTADO 1: SAUDAÇÃO ----------------
        if estado == "SAUDACAO":
            txt = perguntar("Você")
            if re.search(r"\b(quero|pedir|pedido|sanduíche|sanduiche)\b", txt):
                estado = "ESCOLHER_TIPO"
                print("Bot: Qual sanduíche você deseja? (cheeseburger, frango, veggie, x-salada)")
            else:
                print("Bot: Diga 'quero pedir' quando quiser começar um pedido.")

        # ---------------- ESTADO 2: TIPO ----------------
        elif estado == "ESCOLHER_TIPO":
            txt = perguntar("Informe o tipo")
            t = extrair_palavra(txt, TIPOS)
            if t:
                pedido["tipo"] = t
                estado = "ESCOLHER_PAO"
                print(f"Bot: {t.capitalize()} escolhido. Agora escolha o tipo de pão.")
                print("Bot: (branco, integral, australiano)")
            else:
                print("Bot: Não entendi. Opções: cheeseburger, frango, veggie, x-salada.")

        # ---------------- ESTADO 3: PÃO ----------------
        elif estado == "ESCOLHER_PAO":
            txt = perguntar("Tipo de pão")
            p = extrair_palavra(txt, PAES)
            if p:
                pedido["pao"] = p
                estado = "ESCOLHER_TAMANHO"
                print("Bot: Ótimo! Agora escolha o tamanho: pequeno, médio ou grande.")
            else:
                print("Bot: Tipos de pão: branco, integral, australiano.")

        # ---------------- ESTADO 4: TAMANHO ----------------
        elif estado == "ESCOLHER_TAMANHO":
            txt = perguntar("Tamanho")
            t = extrair_palavra(txt, TAMANHOS)
            if t:
                pedido["tamanho"] = "médio" if t in ("medio", "médio") else t
                estado = "ESCOLHER_EXTRAS"
                print("Bot: Deseja algum extra? (queijo, bacon, molho, ovo, salada)")
                print("Bot: Diga 'sem extra' se não quiser.")
            else:
                print("Bot: Tamanhos válidos: pequeno, médio, grande.")

        # ---------------- ESTADO 5: EXTRAS ----------------
        elif estado == "ESCOLHER_EXTRAS":
            txt = perguntar("Extras (ou 'sem')")
            if "sem" in txt:
                estado = "INFORMAR_ENDERECO"
                print("Bot: Ok! Nenhum extra. Informe agora o endereço completo e telefone.")
            else:
                extra = extrair_palavra(txt, EXTRAS_OPCOES)
                if extra:
                    pedido["extras"].append(extra)
                    print(f"Bot: Extra '{extra}' adicionado. Mais algum?")
                else:
                    print("Bot: Extras disponíveis: queijo, bacon, molho, ovo, salada.")

        # ---------------- ESTADO 6: ENDEREÇO ----------------
        elif estado == "INFORMAR_ENDERECO":
            txt = perguntar("Endereço e telefone")
            if len(txt) > 5:
                pedido["endereco"] = txt
                estado = "CONFIRMAR"
            else:
                print("Bot: Informe um endereço válido.")

        # ---------------- ESTADO 7: CONFIRMAR ----------------
        elif estado == "CONFIRMAR":
            extras_txt = ", ".join(pedido["extras"]) if pedido["extras"] else "sem extras"
            resumo = (f"{pedido['tipo'].capitalize()} no pão {pedido['pao']} "
                      f"({pedido['tamanho']}), extras: {extras_txt}, "
                      f"Entrega: {pedido['endereco']}")

            print("Bot: Confirme o pedido:")
            print("Bot:", resumo)

            txt = perguntar("Digite 'confirmar', 'alterar' ou 'cancelar'")

            if "confirm" in txt or "confirmar" in txt:
                estado = "PAGAMENTO"
            elif "alter" in txt or "alterar" in txt:
                estado = "ESCOLHER_TIPO"
                print("Bot: Vamos alterar. Qual novo tipo de sanduíche você deseja?")
            elif "cancel" in txt or "cancelar" in txt:
                print("Bot: Pedido cancelado. Obrigado!")
                break
            else:
                print("Bot: Responda com 'confirmar', 'alterar' ou 'cancelar'.")

        # ---------------- ESTADO 8: PAGAMENTO ----------------
        elif estado == "PAGAMENTO":
            txt = perguntar("Forma de pagamento ('dinheiro' ou 'cartão')")
            if "din" in txt:
                pedido["pagamento"] = "dinheiro"
                estado = "FINALIZADO"
            elif "cart" in txt:
                pedido["pagamento"] = "cartão"
                estado = "FINALIZADO"
            else:
                print("Bot: Escolha 'dinheiro' ou 'cartão'.")

        # ---------------- ESTADO FINAL ----------------
        elif estado == "FINALIZADO":
            print("Bot: Pedido confirmado! Resumo final:")
            print(pedido)
            print("Bot: Seu sanduíche chegará em aproximadamente 20 minutos. Obrigado!")
            break

if __name__ == "__main__":
    main()

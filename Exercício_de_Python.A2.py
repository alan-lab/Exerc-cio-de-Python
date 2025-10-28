def controlar_producao_diaria():
    """
    Recebe a quantidade produzida, compara com a meta de 1000 unidades
    e informa se a meta foi atingida ou quantas unidades faltam.
    """
    META_PRODUCAO = 1000

    print("--- Sistema de Controle de Produção Diária ---")

    # 1. Receber a quantidade produzida (garantindo que seja um número inteiro)
    try:
        quantidade_produzida = int(input("Digite a quantidade total de unidades produzidas hoje: "))
    except ValueError:
        print("\nERRO: Por favor, insira um número inteiro válido para a produção.")
        return

    # 2. Comparar com a meta
    if quantidade_produzida >= META_PRODUCAO:
        # Meta Atingida
        excedente = quantidade_produzida - META_PRODUCAO
        print("\n==============================================")
        print("✅ META DIÁRIA ATINGIDA COM SUCESSO! 🎉")
        print(f"Produção total: {quantidade_produzida} unidades.")
        if excedente > 0:
            print(f"Parabéns! Vocês excederam a meta em {excedente} unidades.")
        print("==============================================")

    else:
        # Meta Não Atingida
        faltam = META_PRODUCAO - quantidade_produzida
        print("\n==============================================")
        print("⚠️ META DIÁRIA NÃO ATINGIDA.")
        print(f"Produção total: {quantidade_produzida} unidades.")
        print(f"Ainda faltam {faltam} unidades para alcançar a meta de {META_PRODUCAO}.")
        print("==============================================")


# Execução do programa
controlar_producao_diaria()
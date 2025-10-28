def monitorar_temperatura(temperatura):
    """
    Controla o sistema de refrigeração da máquina industrial baseado na temperatura atual.

    :param temperatura: A temperatura atual em graus Celsius (°C).
    :return: A mensagem de status (CRÍTICO, ELEVADO, NORMAL).
    """

    if temperatura > 80:
        # Alerta se passar de 80°C (crítico)
        print(f"ALERTA CRÍTICO: {temperatura}°C. A temperatura excedeu 80°C! Acionar resfriamento máximo e verificar a máquina IMEDIATAMENTE.")
        return "CRÍTICO"
    elif temperatura >= 60:
        # Aviso se estiver entre 60-80°C (elevado)
        # O 'elif' verifica se T >= 60 E T <= 80 (pois a condição superior (> 80) já foi excluída)
        print(f"AVISO ELEVADO: {temperatura}°C. Temperatura elevada, o sistema de refrigeração padrão deve ser reforçado.")
        return "ELEVADO"
    else:
        # Normal se abaixo de 60°C
        print(f"STATUS NORMAL: {temperatura}°C. Temperatura operacional segura.")
        return "NORMAL"

# --- Exemplos de Uso (Testes) ---

# 1. Caso Crítico
temp_critica = 85
print("--- Teste 1 (Crítico) ---")
monitorar_temperatura(temp_critica)
print("-" * 30)

# 2. Caso Elevado (Limite superior)
temp_elevada_max = 80
print("--- Teste 2 (Elevado - Limite) ---")
monitorar_temperatura(temp_elevada_max)
print("-" * 30)

# 3. Caso Elevado (Meio da faixa)
temp_elevada = 65
print("--- Teste 3 (Elevado) ---")
monitorar_temperatura(temp_elevada)
print("-" * 30)

# 4. Caso Normal (Limite inferior)
temp_normal_limite = 59.9
print("--- Teste 4 (Normal - Limite) ---")
monitorar_temperatura(temp_normal_limite)
print("-" * 30)

# 5. Caso Normal
temp_normal = 45
print("--- Teste 5 (Normal) ---")
monitorar_temperatura(temp_normal)
print("-" * 30)
def calcular_emissao_carro(km_percorridos, litros_consumidos, tipo_combustivel):
    fatores_combustivel = {
        'gasolina': 2.31,  # kg CO2 por litro
        'etanol': 0.50,    # kg CO2 por litro
        'diesel': 2.68,    # kg CO2 por litro
    }

    tipo_combustivel = tipo_combustivel.lower()
    if tipo_combustivel not in fatores_combustivel:
        raise ValueError("Tipo de combustível inválido. Use 'gasolina', 'etanol' ou 'diesel'.")

    fator = fatores_combustivel[tipo_combustivel]
    emissao_carro = litros_consumidos * fator  # total em kg
    return emissao_carro


def calcular_emissao_aviacao(distancia_voo, tipo_voo):
    fator_emissao_voo_curto = 0.150  # kg CO2 por km
    fator_emissao_voo_longo = 0.090  # kg CO2 por km

    tipo_voo = tipo_voo.lower()
    if tipo_voo == 'curto':
        fator_emissao = fator_emissao_voo_curto
    elif tipo_voo == 'longo':
        fator_emissao = fator_emissao_voo_longo
    else:
        raise ValueError("Tipo de voo inválido. Use 'curto' ou 'longo'.")

    emissao_voo = distancia_voo * fator_emissao
    return emissao_voo


def calcular_emissao_energia(consumo_energia, tipo_energia):
    fator_emissao_energia = {
        'solar': 0.02,        # kg CO2 por kWh
        'renovavel': 0.02,
        'convencional': 0.6
    }

    tipo_energia = tipo_energia.lower()
    if tipo_energia not in fator_emissao_energia:
        raise ValueError("Tipo de energia inválido. Use 'solar', 'renovavel' ou 'convencional'.")

    fator = fator_emissao_energia[tipo_energia]
    emissao_energia = consumo_energia * fator
    return emissao_energia


def calcular_creditos_carbono(emissoes_totais):
    # 1 crédito = 1 tonelada = 1000 kg CO2
    return emissoes_totais / 1000


def calcular_arvores_necessarias(emissoes_totais):
    # Cada árvore absorve cerca de 21 kg CO2 por ano
    return emissoes_totais / 21


def calcular(tipo_calculo, **kwargs):
    tipo_calculo = tipo_calculo.lower()

    if tipo_calculo in ("c", "carro"):
        km_carro = kwargs.get("km_percorridos")
        litros_consumidos = kwargs.get("litros_consumidos")
        tipo_combustivel = kwargs.get("tipo_combustivel")

        if km_carro is None or litros_consumidos is None or tipo_combustivel is None:
            raise ValueError("Para 'carro', informe 'km_percorridos', 'litros_consumidos' e 'tipo_combustivel'.")

        emissao = calcular_emissao_carro(km_carro, litros_consumidos, tipo_combustivel)

    elif tipo_calculo in ("a", "avião"):
        distancia_voo = kwargs.get("distancia_voo")
        tipo_voo = kwargs.get("tipo_voo")
        if distancia_voo is None or tipo_voo is None:
            raise ValueError("Para 'avião', informe 'distancia_voo' e 'tipo_voo'.")

        emissao = calcular_emissao_aviacao(distancia_voo, tipo_voo)

    elif tipo_calculo in ("e", "energia"):
        consumo_energia = kwargs.get("consumo_energia")
        tipo_energia = kwargs.get("tipo_energia")
        if consumo_energia is None or tipo_energia is None:
            raise ValueError("Para 'energia', informe 'consumo_energia' e 'tipo_energia'.")

        emissao = calcular_emissao_energia(consumo_energia, tipo_energia)

    else:
        raise ValueError("Tipo de cálculo inválido. Use 'carro', 'avião' ou 'energia'.")

    creditos = calcular_creditos_carbono(emissao)
    arvores = calcular_arvores_necessarias(emissao)

    return emissao, creditos, arvores


def main():
    print("=== Calculadora de Créditos de Carbono ===")
    print("Tipos disponíveis: carro, avião, energia")

    tipo = input("Digite o tipo de cálculo desejado: ").strip().lower()

    try:
        if tipo in ("c", "carro"):
            km = float(input("Distância percorrida (km): "))
            litros = float(input("Combustível consumido (litros): "))
            combustivel = input("Tipo de combustível ('gasolina', 'etanol' ou 'diesel'): ").strip().lower()

            emissao, creditos, arvores = calcular(
                "carro", km_percorridos=km, litros_consumidos=litros, tipo_combustivel=combustivel)

        elif tipo in ("a", "avião"):
            distancia = float(input("Distância do voo (km): "))
            tipo_voo = input("Tipo de voo ('curto' ou 'longo'): ").strip().lower()

            emissao, creditos, arvores = calcular(
                "avião", distancia_voo=distancia, tipo_voo=tipo_voo)

        elif tipo in ("e", "energia"):
            consumo_energia = float(input("Consumo de energia (kWh): "))
            tipo_energia = input("Tipo de energia ('solar', 'renovavel' ou 'convencional'): ").strip().lower()

            emissao, creditos, arvores = calcular(
                "energia", consumo_energia=consumo_energia, tipo_energia=tipo_energia)

        else:
            print("Tipo inválido. Escolha entre: carro, avião ou energia.")
            input("\nPressione Enter para sair...")
            return

        print(f"\n🌱 Emissões totais de CO₂: {emissao:.2f} kg")
        print(f"💨 Créditos de carbono necessários: {creditos:.3f} toneladas")
        print(f"🌳 Árvores necessárias para compensar: {arvores:.1f} árvores")

    except ValueError as ve:
        print("Erro:", ve)

    input("\nPressione Enter para sair...")


if __name__ == "__main__":
    main()

# 1 - Função para impimir um nome completo
def full_name(frist_name, last_name):
    print(f"Nome completo: {frist_name} {last_name}")
    return f"{frist_name} {last_name}"
full_name("Felipe", "Mendes")

# 2 - Função com parâmetro padrão
def address(country="Brasil"):
    print(f"Endereço: {country}")

address("EUA")

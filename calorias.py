# Dados dos alimentos e suas calorias
alimentos = {
    "Maçã": 52,
    "Cheetos": 734,
    "Salmão": 255,
    "Alface": 15,
    "Sucrilhos": 2583,
    "Carne": 103,
    "Coca-cola": 760,
    "Oreo": 300,
    "Milho em lata": 107,
    "Hamburguer": 2112,
    "Sardinha em lata": 144,
    "Feijão": 3470,
    "Doritos": 504,
    "Grão de Bico": 2184,
    "Miojo": 1550,
    "Leite integral": 298,
    "Suco Kapo": 28,
    "Frango": 2180,
}

# Função para mostrar as calorias
def mostrar_calorias():
    print("Alimentos e suas calorias:")
    for alimento, calorias in alimentos.items():
        print(f"{alimento}: {calorias} kcal")

if __name__ == "__main__":
    mostrar_calorias()

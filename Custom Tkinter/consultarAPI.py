import requests

def buscar_marcas_carros():
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        marcas = [marca['Make_Name'] for marca in data['Results']]
        # Filtrar apenas marcas que tipicamente produzem carros
        marcas_carros = [marca for marca in marcas if not any(x in marca.lower() for x in ['motorcycle', 'truck', 'bus'])]
        return marcas_carros
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return []

if __name__ == "__main__":
    marcas_carros = buscar_marcas_carros()
    if marcas_carros:
        print("Marcas de Carros disponíveis:")
        for marca in marcas_carros:
            print(marca)
    else:
        print("Nenhuma marca encontrada.")

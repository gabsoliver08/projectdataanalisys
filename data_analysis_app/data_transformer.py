def filter_data(dataset, condition):
    try:
        filtered_data = dataset.query(condition)
        return filtered_data
    except Exception as e:
        print(f"Erro ao filtrar dados: {e}")
        return None

def sort_data(dataset, column):
    try:
        sorted_data = dataset.sort_values(by=column)
        return sorted_data
    except Exception as e:
        print(f"Erro ao ordenar dados: {e}")
        return None

# Exemplo de uso:
if __name__ == "__main__":
    # Suponha que 'dataset' seja o conjunto de dados carregado anteriormente
    filtered_data = filter_data(dataset, "idade > 25")
    if filtered_data is not None:
        print("Dados filtrados:")
        print(filtered_data)

    sorted_data = sort_data(dataset, "salario")
    if sorted_data is not None:
        print("Dados ordenados:")
        print(sorted_data)

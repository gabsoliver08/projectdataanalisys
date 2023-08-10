import pandas as pd

def load_csv_dataset(file_path):
    try:
        dataset = pd.read_csv(file_path)
        return dataset
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None

# Exemplo de uso:
if __name__ == "__main__":
    file_path = "datasets/sample_data.csv"
    dataset = load_csv_dataset(file_path)
    if dataset is not None:
        print("Conjunto de dados carregado: ")
        print(dataset)

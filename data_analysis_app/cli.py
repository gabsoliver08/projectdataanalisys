import argparse
import data_loader
import data_transformer
import data_visualizer
import data_metrics

def main():
    parser = argparse.ArgumentParser(description="Aplicação de Análise de Dados - CLI")
    parser.add_argument("file_path", type=str, help="Caminho para o arquivo CSV de dados")
    args = parser.parse_args()

    dataset = data_loader.load_csv_dataset(args.file_path)
    if dataset is None:
        return

    # Realize transformações e gere visualizações aqui

if __name__ == "__main__":
    main()

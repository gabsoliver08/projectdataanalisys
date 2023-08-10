import data_loader
import data_transformer
import data_visualizer
import data_metrics

def main():
    print("Bem-vindo à Aplicação de Análise de Dados!")

    # Carregar um conjunto de dados de exemplo
    dataset = data_loader.load_csv_dataset("datasets/sample_data.csv")

    # Realizar algumas transformações nos dados
    transformed_data = data_transformer.filter_data(dataset, "idade > 25")
    transformed_data = data_transformer.sort_data(transformed_data, "salario")

    # Gerar gráficos de visualização
    data_visualizer.plot_bar_chart(transformed_data, x_column="nome", y_column="salario")
    data_visualizer.plot_scatter_plot(transformed_data, x_column="idade", y_column="salario")
    data_visualizer.plot_line_chart(transformed_data, x_column="idade", y_column="saldo_bancario")

    # Calcular métricas
    average_salary = data_metrics.calculate_average(transformed_data, "salario")
    median_age = data_metrics.calculate_median(transformed_data, "idade")

    print(f"Média de salário: {average_salary}")
    print(f"Mediana de idade: {median_age}")

if __name__ == "__main__":
    main()

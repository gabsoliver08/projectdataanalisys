import matplotlib.pyplot as plt

def plot_bar_chart(dataset, x_column, y_column):
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(dataset[x_column], dataset[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Gráfico de Barras")
        plt.xticks(rotation=45)
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico de barras: {e}")

def plot_scatter_plot(dataset, x_column, y_column):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(dataset[x_column], dataset[y_column])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Gráfico de Dispersão")
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico de dispersão: {e}")

def plot_line_chart(dataset, x_column, y_column):
    try:
        plt.figure(figsize=(10, 6))
        plt.plot(dataset[x_column], dataset[y_column], marker='o')
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Gráfico de Linha")
        plt.xticks(rotation=45)
        plt.show()
    except Exception as e:
        print(f"Erro ao gerar gráfico de linha: {e}")

# Exemplo de uso:
if __name__ == "__main__":
    # Suponha que 'dataset' seja o conjunto de dados carregado anteriormente
    x_column = "idade"
    y_column = "salario"

    plot_bar_chart(dataset, x_column, y_column)
    plot_scatter_plot(dataset, x_column, y_column)
    plot_line_chart(dataset, x_column, y_column)

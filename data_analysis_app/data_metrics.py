import numpy as np

def calculate_average(dataset, column):
    try:
        average = np.mean(dataset[column])
        return average
    except Exception as e:
        print(f"Erro ao calcular média: {e}")
        return None

def calculate_median(dataset, column):
    try:
        median = np.median(dataset[column])
        return median
    except Exception as e:
        print(f"Erro ao calcular mediana: {e}")
        return None

# Exemplo de uso:
if __name__ == "__main__":
    # Suponha que 'dataset' seja o conjunto de dados carregado anteriormente
    salary_column = "salario"
    age_column = "idade"

    average_salary = calculate_average(dataset, salary_column)
    if average_salary is not None:
        print(f"Média de salário: {average_salary}")

    median_age = calculate_median(dataset, age_column)
    if median_age is not None:
        print(f"Mediana de idade: {median_age}")

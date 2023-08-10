import tkinter as tk
from tkinter import filedialog
import data_loader
import data_transformer
import data_visualizer
import data_metrics

class DataAnalysisApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicação de Análise de Dados - GUI")

        self.load_button = tk.Button(self, text="Carregar Conjunto de Dados", command=self.load_dataset)
        self.load_button.pack()

        self.transform_button = tk.Button(self, text="Realizar Transformações", state=tk.DISABLED, command=self.perform_transformations)
        self.transform_button.pack()

        # Adicione mais elementos de GUI e lógica aqui

    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        if file_path:
            self.dataset = data_loader.load_csv_dataset(file_path)
            if self.dataset is not None:
                self.transform_button.config(state=tk.NORMAL)

    def perform_transformations(self):
        transformed_data = data_transformer.filter_data(self.dataset, "idade > 25")
        transformed_data = data_transformer.sort_data(transformed_data, "salario")

        # Exemplo: Imprimir dados transformados no console
        print("Dados transformados:")
        print(transformed_data)

if __name__ == "__main__":
    app = DataAnalysisApp()
    app.mainloop()

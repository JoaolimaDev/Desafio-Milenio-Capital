import pandas as pd

# Função para ler o arquivo CSV
def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Erro: O arquivo {file_path} está vazio.")
    except pd.errors.ParserError:
        print(f"Erro: Houve um erro de parsing ao ler {file_path}.")
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")

# Função para aplicar o filtro
def apply_filter(df, header_filter):
    try:
        # Avalia o cabeçalho fornecido como filtro dinâmico
        filtered_df = df.query(header_filter)
        return filtered_df
    except Exception as e:
        print(f"Um erro inesperado ocorreu durante a aplicação do filtro: {e}")

def main():
    file_path = 'example.csv'
    header_filter = "city == 'New York'"
    selected_column = 'city, name'
    output_file_path = 'filtered_output.csv'
    
    # Leitura do arquivo CSV
    df = read_csv_file(file_path)
    
    if df is not None:
        # Aplicação do filtro dinâmico
        filtered_df = apply_filter(df, header_filter)
        
        if not filtered_df.empty:
            
            selected_columns_list = [col.strip() for col in selected_column.split(',')]
            
            filtered_df[selected_columns_list].to_csv(output_file_path, index=False)
            
            print(filtered_df[selected_columns_list])
            
        else:
            print("Nenhuma linha encontrada que corresponda ao filtro.")
    
if __name__ == "__main__":
    main()




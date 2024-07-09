import pandas as pd
from io import StringIO

# Função para ler o arquivo CSV
def read_csv_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: O arquivo {file_path} não foi encontrado.")
    except pd.errors.EmptyDataError:
        print(f"Error: O arquivo {file_path} está vazio.")
    except pd.errors.ParserError:
        print(f"Error: Houve um erro de parsing ao ler {file_path}.")
    except Exception as e:
        print(f"Error: Um erro inesperado ocorreu: {e}")

def processCsvFile(csvFilePath = None, selectedColumns = None, rowFilterDefinitions = None):

        df = read_csv_file(csvFilePath)
        output_file_path = 'filtered_output.csv'
    
        if df is not None:
            
            if selectedColumns and rowFilterDefinitions:
                filtered_df = applyFilter(df, rowFilterDefinitions)
                selected_columns_list = [col.strip() for col in selectedColumns.split(',')]
                if not filtered_df.empty:
                    filtered_df[selected_columns_list].to_csv(output_file_path, index=False)
                    return  filtered_df[selected_columns_list]
                else:
                    print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
            elif rowFilterDefinitions:
                filtered_df = applyFilter(df, rowFilterDefinitions)
                if not filtered_df:
                    filtered_df.to_csv(output_file_path, index=False)
                    return  filtered_df
                else:
                    print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
                    return
            elif selectedColumns:
                
                selected_columns_list = [col.strip() for col in selectedColumns.split(',')]
                return  df[selected_columns_list]
            
            df.to_csv(output_file_path, index=False)
            return  df
        else:
            print("Arquivo não encontrado, por favor insira um caminho válido.")
            return

# Função para aplicar o filtro e tratamento
def applyFilter(df, rowFilterDefinitions):
    try:
        filtered_df = df.query(rowFilterDefinitions)
        return filtered_df
    except SyntaxError:
        print ("Error: Condição incompleta fornecida. Especifique a condição completa (exemplo, 'age > 30').")
    except Exception as e:
        print (f"Error: Condição inválida. {e}")
        return
        

def processCsv(csv = None, selectedColumns = None, rowFilterDefinitions = None):
    
        if not csv.strip():
            print("Erro: O arquivo está vazio.")
            return
        
        csv_io = StringIO(csv)
        df = read_csv_file(csv_io)
        output_file_path = 'filtered_output.csv'
        
        if selectedColumns and rowFilterDefinitions:
            
            filtered_df = applyFilter(df, rowFilterDefinitions)
            selected_columns_list = [col.strip() for col in selectedColumns.split(',')]            
            if not filtered_df.empty:
                filtered_df[selected_columns_list].to_csv(output_file_path, index=False)
                return  filtered_df[selected_columns_list]
            else:
                print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
                return
        elif rowFilterDefinitions:
            filtered_df = applyFilter(df, rowFilterDefinitions.strip())
            if not filtered_df.empty:
                filtered_df.to_csv(output_file_path, index=False)
                return  filtered_df
            else:   
                print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
                return
        elif selectedColumns:    
            selected_columns_list = [col.strip() for col in selectedColumns.split(',')]
            return  df[selected_columns_list]
        
        df.to_csv(output_file_path, index=False)
        return df
        
        
def main():
    file_path = 'example.csv'
    rowFilterDefinitions = ""
    selectedColumns = 'age, city'
    
    csv_data = """id,name,age,city
    1,John,28,New York
    2,Sarah,25,Chicago
    3,Michael,32,Los Angeles
    4,Emily,30,San Francisco
    5,James,27,Boston"""
    
    csv_io = StringIO(csv_data)
    df = read_csv_file(csv_io)
    
    process = processCsv(csv_data, selectedColumns, rowFilterDefinitions)
    
    #filtered_df = processCsvFile(file_path, selectedColumns, rowFilterDefinitions)
        
    print(process)
    
if __name__ == "__main__":  
    main()







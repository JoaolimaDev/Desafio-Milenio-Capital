import pandas as pd
from io import StringIO
import sys

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

"""
    Processa um arquivo CSV a partir de um caminho de arquivo, aplicando seleções de colunas e filtros de linha, se fornecidos.

    Parâmetros:
    csvFilePath (str): Caminho do arquivo CSV.
    selectedColumns (str): Colunas selecionadas para serem exibidas, separadas por vírgula.
    rowFilterDefinitions (str): Definições de filtros de linha para aplicar ao CSV.

    A função realiza as seguintes ações:
    1. Lê o arquivo CSV em um DataFrame.
    2. Se colunas selecionadas são fornecidas, verifica se existem no DataFrame.
    3. Se colunas selecionadas e filtros de linha são fornecidos, aplica os filtros e exibe as colunas selecionadas.
    4. Se apenas filtros de linha são fornecidos, aplica os filtros e exibe o resultado.
    5. Se apenas colunas selecionadas são fornecidas, exibe essas colunas.
    6. Se nenhuma coluna ou filtro é fornecido, exibe o DataFrame completo.
    7. Se o arquivo não for encontrado, exibe uma mensagem de erro.
    
    Retorna:
    None: Os resultados são impressos no console.
"""
def processCsvFile(csvFilePath = None, selectedColumns = None, rowFilterDefinitions = None):
    
        df = read_csv_file(csvFilePath)
        selectedColumn = False
        
        if selectedColumns is not None and selectedColumns.strip() != "":
            selected_columns_list = [col.strip() for col in selectedColumns.split(',')]            
            is_subset = set(selected_columns_list).issubset(df.columns)

            if not is_subset:
                print(f"Error: Coluna(s) '{', '.join(selected_columns_list)}' inexistente(s) no csv fornecido. Disponíveis: {list(df.columns)}")
                return
            
            selectedColumn = True
            selected_columns_list_ordered = [col for col in df.columns if col in selected_columns_list]
    
    
        if df is not None:
            
            if selectedColumn and rowFilterDefinitions:
                filtered_df = applyFilter(df, rowFilterDefinitions)
                if not filtered_df.empty:
                    print(filtered_df[selected_columns_list_ordered].to_csv(index=False))
                    return
                else:
                    print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
                    return
            elif rowFilterDefinitions:  
                filtered_df = applyFilter(df, rowFilterDefinitions)
                if not filtered_df.empty:
                    print(filtered_df.to_csv(index=False))
                    return
                else:
                    print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
                    return
            elif selectedColumn:
                print(df[selected_columns_list_ordered].to_csv(index=False))
                return

            print(df.to_csv(index=False))
            return
        else:
            print("Arquivo não encontrado, por favor insira um caminho válido.")
            return

# Função para aplicar o filtro e tratamento
"""
    Aplica filtros de linha ao DataFrame com base nas definições fornecidas.

    Parâmetros:
    df (DataFrame): O DataFrame ao qual os filtros serão aplicados.
    rowFilterDefinitions (str): Definições de filtros de linha a serem aplicadas ao DataFrame.

    A função realiza as seguintes ações:
    1. Tenta aplicar a consulta do filtro de linha ao DataFrame usando o método query().
    2. Em caso de erro de sintaxe, informa que a condição fornecida está incompleta.
    3. Em caso de qualquer outro erro, informa que a condição é inválida e exibe a mensagem de erro.

    Retorna:
    DataFrame: O DataFrame filtrado se a consulta for bem-sucedida.
    None: Se ocorrer um erro, nenhuma DataFrame é retornado e uma mensagem de erro é exibida.
"""
def applyFilter(df, rowFilterDefinitions):
    try:
        filtered_df = df.query(rowFilterDefinitions)
        return filtered_df
    except SyntaxError:
        print ("Error: Condição incompleta fornecida. Especifique a condição completa (exemplo, 'age > 30').")
    except Exception as e:
        print (f"Error: Condição inválida. {e}")
        
        
"""
    Processa um arquivo CSV aplicando seleções de colunas e filtros de linha, se fornecidos.

    Parâmetros:
    csv (str): Conteúdo do arquivo CSV em formato de string.
    selectedColumns (str): Colunas selecionadas para serem exibidas, separadas por vírgula.
    rowFilterDefinitions (str): Definições de filtros de linha para aplicar ao CSV.

    A função realiza as seguintes ações:
    1. Verifica se o conteúdo do CSV não está vazio.
    2. Lê o CSV em um DataFrame.
    3. Se colunas selecionadas são fornecidas, verifica se existem no DataFrame.
    4. Se colunas selecionadas e filtros de linha são fornecidos, aplica os filtros e exibe as colunas selecionadas.
    5. Se apenas filtros de linha são fornecidos, aplica os filtros e exibe o resultado.
    6. Se apenas colunas selecionadas são fornecidas, exibe essas colunas.
    7. Se nenhuma coluna ou filtro é fornecido, exibe o DataFrame completo.
    
    Retorna:
    None: Os resultados são impressos no console.
"""
def processCsv(csv = None, selectedColumns = None, rowFilterDefinitions = None):
    

        if not csv.strip():
            print("Erro: O arquivo está vazio.")
            return
        
        csv_io = StringIO(csv)
        df = read_csv_file(csv_io)
        selectedColumn = False

        
        if selectedColumns is not None and selectedColumns.strip() != '':
            selected_columns_list = [col.strip() for col in selectedColumns.split(',')]            
            is_subset = set(selected_columns_list).issubset(df.columns)

            if not is_subset:
                print(f"Error: Coluna(s) '{', '.join(selected_columns_list)}' inexistente(s) no csv fornecido. Disponíveis: {list(df.columns)}")
                return
            
            selectedColumn = True
            selected_columns_list_ordered = [col for col in df.columns if col in selected_columns_list]

    
        if selectedColumn and rowFilterDefinitions:
            filtered_df = applyFilter(df, rowFilterDefinitions)
            if not filtered_df.empty:
                print(filtered_df[selected_columns_list_ordered].to_csv(index=False))
                return
            else:
                print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
                return
        elif rowFilterDefinitions:
            filtered_df = applyFilter(df, rowFilterDefinitions.strip())
            if not filtered_df.empty:
                print(filtered_df.to_csv(index=False))
                return
            else:   
                print("Nenhuma linha encontrada que corresponda ao filtro : " + rowFilterDefinitions)
                return
        elif selectedColumn:    
            print(df[selected_columns_list_ordered].to_csv(index=False))
            return
        
        print(df.to_csv(index=False))
        
        
# main callback recebimento de paramentros
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Uso: csv_processor.py <mode> <csvData/csvFilePath> <selectedColumns> <rowFilterDefinitions>")
        sys.exit(1)

    mode = sys.argv[1]
    data_or_path = sys.argv[2]
    selected_columns = sys.argv[3]
    row_filter_definitions = sys.argv[4]

    if mode == "file":
        processCsvFile(data_or_path, selected_columns, row_filter_definitions)
    elif mode == "data":
        processCsv(data_or_path, selected_columns, row_filter_definitions)
from database.connection import execute_query
from data.data_processing import process_data, validate_data
from file_manager.excel_manager import save_to_excel
from datetime import datetime

if __name__ == "__main__":
    # VQL query
    data_atual = datetime.now().strftime("%Y%m")
    vql = f'''
    SELECT platfor.ano_mes AS ano_mes, platfor.cpf_cnpj AS cpf_cnpj,
    platfor.cod_agencia AS cod_agencia, platfor.num_conta AS num_conta,
    platfor.identificador AS identificador, platfor.cod_operacao AS cod_operacao,
    platfor.vlr_concessao AS vlr_concessao, platfor.dat_contratacao AS dat_contratacao,
    platfor.cod_produto AS cod_produto FROM origem_concessao_plataforma_pf_historico AS platfor
    WHERE (filtro_ano_mes_inicial = {data_atual} AND filtro_ano_mes_final = {data_atual})
    CONTEXT ('I18N' = 'pt_br2')'''
    
    # Executa a consulta
    results, columns = execute_query(vql)
    
    # Processa os dados
    df = process_data(results, columns)
    
    # Valida os dados
    try:
        validate_data(df)
    except ValueError as e:
        print(f"Erro de validação: {e}")
    
    # Salva os dados em um arquivo Excel
    save_to_excel(df, 'resultado_concessao.xlsx')

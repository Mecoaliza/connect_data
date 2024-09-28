import pandas as pd

def process_data(results, columns):
    df = pd.DataFrame(results, columns=columns)
    
    df = df.assign(
        dat_contratacao=pd.to_datetime(df["dat_contratacao"]).dt.strftime('%d/%m/%Y'),
        vlr_concessao=df["vlr_concessao"].apply(lambda x: f'{x:,.2f}'.replace('.', '#').replace(',', '.').replace('#', ',')),
        cpf_cnpj=df['cpf_cnpj'].astype(str),
        num_conta=df['num_conta'].astype(str)
    )
    
    return df

def validate_data(df):
    if df['vlr_concessao'].dtype != 'float64':
        raise ValueError("Coluna 'vlr_concessao' deve ser do tipo float.")


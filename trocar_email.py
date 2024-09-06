import pandas as pd

caminho = r'C:\Users\tulio\OneDrive\Área de Trabalho\Python 2.0\Hashtag Treinamentos\M39_PROJETO_1_AutomacaoProcesso\Bases de Dados\Emails.xlsx'

emails_df = pd.read_excel(caminho)

emails_df['E-mail'] = emails_df['E-mail'].str.replace('tuliovcr2', 'EMAIL')

emails_df.to_excel(caminho, index=False)
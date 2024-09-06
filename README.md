# Automação de Indicadores

## Objetivo
Desenvolver um processo automatizado para calcular os principais indicadores de desempenho de uma rede de lojas, distribuídas por todo o Brasil, e enviar os resultados diariamente para os respectivos gerentes da loja, bem como relatórios consolidados para a diretoria.

## Descrição
O projeto simula o ambiente de uma rede de 25 lojas, onde a equipe de análise de dados é responsável por calcular os indicadores principais (OnePage) para cada loja e enviá-los aos gerentes. Além disso, são gerados rankings diários e anuais, enviados para a diretoria. O processo é automatizado para otimizar o tempo e reduzir erros manuais.

### Indicadores Monitorados no OnePage
- **Faturamento**  
  Meta Anual: R$ 1.650.000 | Meta Diária: R$ 1.000
- **Diversidade de Produtos Vendidos**  
  Meta Anual: 120 produtos | Meta Diária: 4 produtos
- **Ticket Médio por Venda**  
  Meta Anual e Diária: R$ 500

### Funcionalidades Principais
- **Geração automática de OnePages** para cada loja, com seus indicadores diários e anuais.
- **Envio de e-mails automatizados** para os gerentes de cada loja, com os OnePages no corpo do e-mail e arquivos detalhados anexados.
- **Relatórios diários e anuais para a diretoria**, incluindo o ranking de faturamento das lojas e o destaque da melhor e pior loja do dia e do ano.
- **Histórico de vendas**, com cada planilha diária salva automaticamente em pastas correspondentes a cada loja.

### Estrutura dos Arquivos
- **Emails.xlsx**: Contém o nome, e-mail e loja de cada gerente.
- **Vendas.xlsx**: Dados de vendas de todas as lojas.
- **Lojas.csv**: Contém os nomes das lojas.
- **Planilhas de Backup**: Cada planilha gerada é salva com a data do relatório dentro da respectiva pasta da loja.

### Exemplo de E-mail Enviado
O e-mail enviado ao gerente da Loja A contém:
- O OnePage da Loja A no corpo do e-mail.
- Um arquivo em Excel com as vendas detalhadas da Loja A anexado.

Além disso, um e-mail separado é enviado à diretoria com rankings das lojas e os destaques do desempenho.

### Tecnologias Utilizadas
- Python
- Pandas
- Pathlib
- Win32com (para envio de e-mails)

## Como Executar
1. Clonar este repositório.
2. Instalar as dependências com `pip install -r requirements.txt`.
3. Inserir os dados necessários nos arquivos `Emails.xlsx`, `Vendas.xlsx` e `Lojas.csv`.
4. Executar o script principal para iniciar a rotina de cálculo e envio dos relatórios.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença
[MIT](LICENSE)

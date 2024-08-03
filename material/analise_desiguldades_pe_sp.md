## Contexto 

O presente projeto consiste na análise das desigualdades entre as regiões Sudeste e Nordeste do Brasil, focando especificamente nos estados de São Paulo e Pernambuco, com base em dados de IDH (Índice de Desenvolvimento Humano) e PIB (Produto Interno Bruto) municipal obtidos no ano de 2010. O objetivo deste trabalho é evidenciar a desigualdade social existente entre essas duas regiões por meio dos indicadores mencionados.

Para desenvolver esse trabalho, fizemos uma análise exploratória de dados do PIB e IDH dos municípios que compõem estes dois estados utilizando a biblioteca pandas, numpy e matplotlib para manipulação dos dados e apresentação de gráficos. Numa próxima etapa, utilizaremos o Tableau para criar visualizações interativas que permitam uma análise mais aprofundada e intuitiva dos dados.


## Objetivos

### Objetivo Geral

Evidenciar as desigualdades sociais entre as regiões Sudeste e Nordeste do Brasil.
 
### Objetivos Específicos

- Analisar os índices de PIB e IDH  dos estados de São Paulo e Pernambuco.
- Avaliar a disparidade no acesso as instituições educacionais entre as duas regiões.
- Comparar os dados para identificar e quantificar as disparidades entre as duas regiões.
- Utilizar visualizações de dados para facilitar a compreensão das desigualdades.


### Bases escolhidas

- Base 1: Dados socioeconômicos do estado de Pernambuco no ano de 2010 (fonte: IPEA. Disponível em: https://www.ipea.gov.br/ipeageo/bases.html)
- Base 2: Dados socioeconômicos do estado de São Paulo no ano de 2010 (fonte: IPEA. Disponível em: https://www.ipea.gov.br/ipeageo/bases.html)
- Base 3: Dados do econômicos dos estados brasileiros no ano de 2010 (fonte: IPEA. Disponível em: https://www.ipea.gov.br/ipeageo/bases.html)


## Metodologia

Para desenvolver este projeto, seguimos as etapas descritas abaixo:

1. **Coleta de Dados**:
   - Os dados foram obtidos do Instituto de Pesquisa Econômica Aplicada (IPEA), que fornece informações detalhadas sobre PIB e IDH dos municípios brasileiros.

2. **Análise Exploratória de Dados**:
   - Utilizamos a biblioteca pandas para carregar, limpar e manipular os dados.
   - Realizamos análises descritivas para entender a distribuição dos dados de PIB e IDH.

3. **Visualização de Dados**:
   - Utilizamos a biblioteca matplotlib para gerar gráficos que ilustram as disparidades entre os municípios dos dois estados.

4. **Exportação de Dados**:
   - Exportamos os dados finais para um arquivo CSV.


## Ferramentas Utilizadas

- **Pandas**: Para análise exploratória e manipulação dos dados.
- **Numpy**: Para cálculos e operações numéricas.
- **Matplotlib**: Para criação de gráficos e visualizações.
- **Tableau**: Para visualizações interativas - https://public.tableau.com/views/ProjetoFinal-LorenaeRaphaelyReprograma/Painel1?:language=pt-BR&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

## Resultados Preliminares

Além do IDH municipal geral, as bases utilizadas também contêm indicadores específicos do IDH dos municípios, como IDH Educação, IDH Longevidade e IDH Renda. Para iniciar nossa análise, calculamos a média desses indicadores para obter os IDHs dos estados de São Paulo e Pernambuco. Com os resultados em mãos, pudemos compará-los e comprovar a desigualdade existente entre esses dois estados.

Para aprofundar a análise e corroborar com as disparidades apontadas pelos IDHs gerais e específicos, utilizamos diversos indicadores socioeconômicos e de desenvolvimento humano. Entre eles estão a mortalidade infantil, que reflete a qualidade dos serviços de saúde e condições de vida; a probabilidade de sobrevivência até 60 anos, que indica a longevidade e saúde da população; a taxa de analfabetismo em pessoas com 25 anos ou mais, que revela o nível de educação adulta; e as taxas de frequência líquida ao ensino fundamental e médio, que demonstram o acesso e continuidade na educação básica e secundária. Além disso, consideramos a porcentagem de empregados na faixa etária de 18 anos ou mais, que evidencia a situação do mercado de trabalho; e a renda per capita, um importante indicador de prosperidade econômica. 

Os resultados preliminares indicam uma clara disparidade entre os estados de São Paulo e Pernambuco. O estado de São Paulo apresenta, em média, um PIB e um IDH significativamente maiores em comparação ao estado de Pernambuco. Essa diferença evidencia as desigualdades regionais em termos de desenvolvimento econômico e qualidade de vida.


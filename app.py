import streamlit as st
import webbrowser
from PIL import Image
import os


#Ajustando a página para a largura automática
st.set_page_config(layout="wide")

 #Adicionando estilo CSS personalizado
st.markdown("""
    <style>
    /* Estilo das abas */
    .stTabs [data-baseweb="tab"] {
        background-color: #1f77b4; /* Cor de fundo azul */
        color: white; /* Cor do texto */
        border-radius: 5px; /* Bordas arredondadas */
        margin: 5px; /* Remover espaço entre as abas */
        padding: 20px; /* Espaço interno nas abas */
        font-weight: bold; /* Texto em negrito */
    }
    /* Estilo para a aba ativa */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background-color: #00509e; /* Azul mais escuro para a aba ativa */
        color: white; /* Cor do texto */
    }
    </style>
""", unsafe_allow_html=True)

#Criando a imagem do cabeçalho do portifólio
st.image('banner.png')
#Criando o cabeçalho do portifólio
st.header('Portifólio Profissional de Projetos')

#Criando menu de navegação em tabs
#Menu navegação
tabs=st.tabs(['Objetivos','Apresentação','Habilidades','Projetos','Certificações e Educação','Contatos'])

#Navegando pelas Tabs
with tabs[0]:
        st.write('''
    **Objetivo Geral**
    - Este portifólio visa demonstrar minhas principais habilidades e conhecimentos técnicos em diversas ferramentas de negócios, analise de dados e programação.
             
    **Missão**
    - Proporcionar projetos de qualidade que visam reduzir custos e melhorar a eficiência dos negócios, com o uso de tecnologias de ponta.

    **Visão**
    - Ser um profissional de qualidade, capaz de atender as necessidades de negócios.
             
    **Valores**
    - Responsabilidade, Ética, Qualidade, comprometimento e colaboração de equipe.
                 
    **Publico Alvo**
    - Profissionais de negócios.
    - Gerentes de negócios.
    - Analistas de negócios.
    - Desenvolvedores.
    - Programadores.
    - Analista de Dados
    - Cientistas de Dados
                 
                     
    **Mensagem**
    - "Acredito que o conhecimento e a persistência são essenciais para o sucesso de um negócio."
    - "Confia ao Senhor as tuas obras, e teus pensamentos serão estabelecidos." (Provérbios 16-3)
              
''')

with tabs[1]:
    st.write('''
    **Apresentação Pessoal**
    - Me chamo Williams Rodrigues, tenho 40 anos, casado pai do Miguel e da Laura Gabrielly que está chegando. 
             Moro em Maceió/Alagoas,
             Sou uma pessoa que não tem vicios que ama estar em família e aproveitar cada momento com intensidade.
            Sou apaixonado por astronomia e tecnologia.
    - Nas horas de folga gosto de pescar e andar na natureza e também praticar ciclismo, e eu amo viajar.
             
    **Apresentação Profissional**
    - Especialista em Ciência de Big Data e Analytics - 2024
    - Bacharel em Administração de Empresas - 2016
    - Autor do Projeto Excel Empresarial - De 2014 a 2016
    - Consultor em tecnólogia da Informação - Desde 2018
    - Professor de Microsoft Excel - De 2014 a 2016
    - Palestrante sobre sustentabilidade - Em 2013
             
    **Experiência Profissional**
             
    - Analista de Dados e Logística - 2024
        - **Atividades:** Construir, desenvolver projetos usando analise de dados com power BI e Power Query, dos clientes além de dar suporte na operação logística.
            - Observação: Todos os projetos desenvolvidos foram construidos dentro de um prazo de 6 meses, totalizando 11 projetos de analise de dados com Power BI, e divulgando para cada cliente.
    _______________________________________________________________________________________________________      

    - Analista de Logística - De 2022 a 2024
        - **Atividades:** Atuar na área logística, atuando diretamente no processo de roteirização e analise dos dados de custos, e operações logística.
            - Observação: Em uma das empresas que atuei, fiquei responsável pelo processo de roterização, o que pra mim foi um grande divisor de águas, na esféra logistica.
             Aqui desenvolvi análises técnicas e eficientes melhorando a produtividade no ato da entrega e minimizando o indicador de fora de rota.
    _______________________________________________________________________________________________________      


    - Micro Empreendedor individual - De 2019 a 2022
        - Nesta época entrei no mercado como micro empresário no segmento de varejo, com uma loja de perfumaria e Cosméticos junto com minha esposa.
        A loja funcionava no mercado digital, onde era nosso maior público e ficamos até 2022, onde decidimos encerrar as atividades no segmento de loja fisica e retornamos para o mercado digital.
             A loja encerrou suas atividades em 2024.
             - Observação: Foi nesta período que desenvolvi, um sistemma denominado **ORION**, sistema de gestão para controle e registro de operações de vendas, voltado para o público MEI (micro empreendedor individual),
             O sistema conta com os seguines modulos: Custos, Vendas, Produtos, Fornecedores, Estoque e Análise Faturamento MEI.
    _______________________________________________________________________________________________________      
             
    - Consultor em tecnologia e analise de dados - Desde 2018
        - **Atividades:**  Neste período, registrei minha primeira consultoria em análise dados, e desenvolvimento de projetos usando o **MICROSOFT EXCEL**, junto a empresas e profissionais.
             A consultoria visava, apresentar recursos de analise de dados e elaborar projetos de negócios, que atendesse a necessidade de cada aluno, trazendo 
             sugestão, inovação e desenvolvendo habilidades técnicas e práticas no dia a dia das pessoas.      
    _______________________________________________________________________________________________________   
             

    - Assistente Administrativo Financeiro - De 2016 a 2018
        - **Atividades:** Atuava no controle financeiro, realizando contas a pagar e a receber e tambem  atuando junto ao conselho administrativo e financeiro.
             Preparação de atas, negociações e planejamento financeiro.
             
    _______________________________________________________________________________________________________   
             
    - Técnico em Informática - Desde 2003
        - **Atividades:** Formatar, configurar e instalar sistemas operacionais.
             
    _______________________________________________________________________________________________________   
    

             ''')   
    
with tabs[2]:
    st.write('''
    **Principais Habilidade e Ferramentas de Trabalho**
    - Python
    - SQL
    - MYSQL
    - HTML
    - CSS
    - Streamlit
    - Pandas
    - Matplotlib
    - Git
    - Github
    - Microsof Power BI
    - Microsoft Power Query
    - Microsoft Excel
    - Microsoft Access
    - VBA(Visual Basic for Applications)
    - AppSheet
    - Microft Power Apps
    - Canva

    - **Competências Interpessoais** - Comunicação, Trabalho em equipe, comprometimento, ética profissional e responsabilidade.
    

        **Observação:**
            - Estou sempre estudando e buscando novas ferramentas e tecnologias para me tornar um desenvolvedor de qualidade.
    Já desenvolvi alguns projetos onde integrava diretamete o sistema de registro ao banco de dados tanto do ***MYSQL*** quanto no servidor ***SQL SERVER***.
    Atualmente estou estudando a linguagem de programação ***PYTHON*** para aprimorar meus conhecimentos em desenvolvimento de software. Pois vejo nesta ferramenta um potencial enorme
    para me tornar um desenvolvedor de qualidade.

    ''')

with tabs[3]:   
    st.write(''' 
    **Resumo dos Projetos**
        
    - Entre 2014 e 2016, como estagiário em uma antiga secretaria da prefeitura de Maceió, no setor de telecomunicações, desenvolvi meu primeiro sistema, denominado PHOENIX. O sistema tinha como objetivo controlar o fluxo e a distribuição de aparelhos telefônicos utilizados pelos servidores do município.

    - Em 2016, iniciei um novo projeto com um sistema de controle de acesso de pessoas, utilizando a linguagem VBA (Visual Basic for Applications).
    Ainda em 2016, iniciei uma consultoria de aulas e treinamentos em Microsoft Excel, ministrando aulas em uma faculdade para alunos de diferentes cursos de graduação. O projeto, denominado EXCEL EMPRESARIAL, foi um sucesso, chegando a ter lista de espera. Nesse período, abri um CNPJ MEI (Microempreendedor Individual) e comecei a realizar aulas particulares para pessoas físicas (PF) e jurídicas (PJ). Foi nesse momento que iniciei outros projetos voltados para análises de dados e dashboards, tendo o Power BI como principal ferramenta de trabalho.

    - Em 2020, comecei a desenvolver outro sistema, agora denominado ORION, um sistema de gestão para controle e registro de operações de vendas voltado para pequenos empreendedores individuais (MEI). O sistema dispõe de módulos como Cadastro de Clientes, Cadastro de Produtos, Cadastro de Fornecedores, Vendas, Controle de Estoque, Detalhamento de Vendas e uma ampla possibilidade de relatórios. A construção desse projeto levou cerca de seis meses, e consegui comercializar o produto ainda na fase inicial de desenvolvimento para uma microempresa no segmento de bolos e confeitaria.

    - Atualmente, realizo consultorias em análise de dados com Power BI para empresas e também desenvolvo projetos em Python como freelancer. Por exemplo, toda esta página do meu portfólio foi construída por mim, usando a linguagem Python, e publicada no GitHub. Além disso, realizei diversos trabalhos de desenvolvimento de análises de dados para um operador logístico. Também desenvolvi aplicativos móveis e fui responsável pela criação de um sistema web de registro e controle de dados, totalmente integrado a um servidor na nuvem utilizando MySQL. Essa integração permite diversas melhorias, além da possibilidade de implementar novos aplicativos que proporcionem maior qualidade na informação, rapidez e segurança.
    _______________________________________________________________________________________________________     
    ''')
    
   # Título do projeto
st.header('Projeto de Análise de Dados - Power BI')

# Criando duas colunas
col1, col2,col3,col4,col5,col6 = st.columns(6)

# Conteúdo da primeira coluna
with col1:
    st.image('new.jpg', width=200,caption="Análise Produção Indústria")
    st.markdown("[Análise Dados Produção Indústria](https://app.powerbi.com/view?r=eyJrIjoiMjg4Y2YzZDYtMmVmMi00ZmQ1LWJkNTgtOTFmNjQzYzVkZjY3IiwidCI6IjMyMzQxYTA2LWI2OTAtNDgzNC05NGEzLWQwYjJmN2JkYTdlMCJ9)")

# Conteúdo da segunda coluna
with col2:
    st.image('filantropia.png', width=200,caption="Análise Dados Filantropia")
    st.markdown("[Análise Dados Filantropia](https://app.powerbi.com/view?r=eyJrIjoiMzVmYWM0MTQtZTE3OC00MWFlLWJiY2ItNmRhMTAxNDc5MjQxIiwidCI6IjMyMzQxYTA2LWI2OTAtNDgzNC05NGEzLWQwYjJmN2JkYTdlMCJ9)")

# Conteúdo da terceira coluna
with col3:
    st.image('construcao.png', width=200,caption="Análise Dados Pedidos Logística")
    st.markdown("[Análise dados Pedidos Logística](https://app.powerbi.com/view?r=eyJrIjoiZDFlOTRiMzQtMGQ3ZC00YjU1LWJiMTctMGFkMzE4YmI3Yjg3IiwidCI6IjMyMzQxYTA2LWI2OTAtNDgzNC05NGEzLWQwYjJmN2JkYTdlMCJ9)")

# Conteúdo da quarta coluna
with col4:
    st.image('rot.png', width=200,caption="Análise Roteirização")
    st.markdown("[Análise Roteirização](https://app.powerbi.com/view?r=eyJrIjoiYzU5ZGY3MzYtZTYzNS00MWU5LThmMDktMWM0YjA5NDlkMmE4IiwidCI6IjMyMzQxYTA2LWI2OTAtNDgzNC05NGEzLWQwYjJmN2JkYTdlMCJ9)")

# Conteúdo da quinta coluna
with col5:
    st.image('fin.png', width=200,caption="Análise Financeira")
    st.markdown("[Análise Financeira](https://app.powerbi.com/view?r=eyJrIjoiNjUxYmUyYzktZjFjMy00YzgxLThhYzctZmQyMzUxZjQwYzQ0IiwidCI6IjMyMzQxYTA2LWI2OTAtNDgzNC05NGEzLWQwYjJmN2JkYTdlMCJ9)")

# Conteúdo da quinta coluna
with col6:
    st.image('prf.png', width=200,caption="Análise dados Acidentes trânsito")
    st.markdown("[Análise dados Acidentes trânsito](https://app.powerbi.com/view?r=eyJrIjoiNWJhNGNlNDktM2I2MC00OWU5LWFhOGItZjkxZGNhOWNiOTQ4IiwidCI6IjMyMzQxYTA2LWI2OTAtNDgzNC05NGEzLWQwYjJmN2JkYTdlMCJ9)")

with tabs[4]:
    st.write('''
    **Certificações e Educacão**

    - **2024 -- MBA Ciência de Big Data e Analytics** - 
        Ciência de Big Data e Analytics é um curso voltado para capacitar profissionais no processamento, análise e interpretação de grandes volumes de dados, transformando informações complexas em insights estratégicos. A formação combina estatística, programação, aprendizado de máquina e visualização de dados, com foco em ferramentas como Python, R, SQL e plataformas de análise como Power BI e Tableau.
        O curso aborda temas como mineração de dados, modelagem preditiva, inteligência artificial e infraestrutura de dados em nuvem, além de práticas em negócios para tomada de decisões orientadas por dados. É ideal para quem busca atuar em áreas como marketing, finanças, tecnologia, saúde e logística, onde a análise de dados desempenha papel crucial na inovação e eficiência.
        Com a crescente demanda por profissionais qualificados, a formação em Big Data Analytics se destaca como uma das mais promissoras no mercado atual.


    - **2016 -- Bacharel em Administração de Empresas** - Administração de Empresas é um curso que prepara profissionais para planejar, organizar e gerenciar recursos e processos em organizações de diferentes portes e setores. A formação combina conhecimentos em áreas como finanças, marketing, gestão de pessoas, logística, estratégia e empreendedorismo, 
        com foco no desenvolvimento de habilidades analíticas, liderança e tomada de decisões.
        Durante o curso, os alunos aprendem a interpretar cenários econômicos, criar planos de negócios, gerenciar equipes e otimizar processos organizacionais. Além disso, a grade curricular costuma incluir disciplinas como contabilidade, economia, legislação empresarial e gestão de projetos, 
        proporcionando uma visão ampla e prática do funcionamento das empresas.
        
    
    ''')
with tabs[5]:
    
   # Criação de colunas para posicionamento
    col1 = st.columns([1])  # Ajuste as proporções conforme necessário

with col1[0]:

     
    st.header('''
    
    Transforme Dados em Decisões Estratégicas com Soluções Personalizadas!

-  Descubra como a tecnologia pode impulsionar sua empresa!
Apresentamos nossos serviços completos em Power BI, desenvolvimento em Python, e criação de sites web. Oferecemos soluções que transformam dados e ideias em resultados reais.

**O que fazemos por você?**
-  Power BI: Transforme informações complexas em relatórios interativos e dashboards intuitivos.
-  Identifique oportunidades de crescimento.
-  Monitore indicadores de desempenho (KPIs) em tempo real.
-  Otimize processos e reduza custos.
-  Tome decisões com base em dados confiáveis.

-  Desenvolvimento em Python:
-  Automatize processos e melhore a eficiência do seu negócio com soluções sob medida, incluindo:
-  Scripts personalizados para análise e gestão de dados.
-  Integrações e automações inteligentes.

**Criação de Sites Web:**
-  Fortaleça sua presença digital com um site moderno, responsivo e focado em resultados:
-  Integrações com sistemas e ferramentas.
-  SEO otimizado para atrair mais clientes.

**Por que escolher nosso serviço?**
-  Experiência comprovada em diversos setores.
-  Soluções personalizadas para atender às suas necessidades específicas.
-  Expertise técnica para transformar ideias em resultados tangíveis.

**Vamos juntos transformar seus desafios em oportunidades.**

    ''')
    '_______________________________________________________________________________________________________'
    st.write('''
        **Contatos - Venha faze parte de minhas principais redes sociais**
        - Email: dateanalytics@outlook.com
        - Whatsapp: https://wa.me/5582988639394
        - Github: https://github.com/Williamsrvs
        - Linkedin: https://www.linkedin.com/in/williamsrvs
        - Instagram: https://www.instagram.com/williams_rvs85
        - Telefone: (82) 98863-9394 / 98109-0042
   
    ''')
    #Faça o Download do curículo
    st.download_button(
        label="Download do Curículo",
        data="Williams_Rvs.pdf",
        file_name="curriculo_williams.pdf",
        mime="application/pdf"
    )




    



 

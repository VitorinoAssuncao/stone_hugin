# Desafio da Empresa Stone.

Esse pequeno sistema foi desenvolvido com o objetivo de garantir uma visualização rápida para a situação de estoques de equipamentos das unidades de distribuição do grupo Stone. Atráves de um sistema de farol, é possível se localizar rapidamente o quão próximo do estoque ideal as unidades se encontram, e requisitar o envio de novos estoques para os mesmos.

Para tal foram selecionadas as seguintes técnologias:

* [Python-Falcon](https://falcon.readthedocs.io/en/stable/) Com uma linguagem robusta e de linguagem natural, Python foi selecionado tanto por sua grande versatilidade, quanto facilidade em utilização. O Web Framework Falcon, em especial, é uma ferramenta da linguagem que permite um deploy rápido e eficiente para uma aplicação de backend.

* [ORM - SQLAlchemy](https://www.sqlalchemy.org) Foi utilizado o ORM SQLAlchemy pois permite assim uma abstração melhor quanto a operação do banco de dados, permitindo assim que seja possível migração entre bases, confomre a melhor necessidade.

* [Banco de Dados Postgresql](https://www.postgresql.org) Como dito anteriormente, com o ORM a seleção pelo banco de dados se tornou secundário, neste caso selecionei o postgresql por conta da hospedagem gratuíta utilizada. Caso se tenha acesso a um banco mysql ou de outro baseado em linguagem SQL, basta alterar os dados de conexão do mesmo.

* [Deploy - Heroku](heroku.com) Atualmente esse projeto se encontra para acesso na rede através do endereço abaixo:
 ```cddcontroller.herokuapp.com```

Como foi utilizada a opção de conta de desenvolvimento por Hobby (gratuita), isso faz com que possa ter algumas limitações (até 20 acessos simultaneos, 600 Minutos de conexão por dia).

Observar que para rodar o projeto de forma local, deve-se adequar a rota do banco de forma apropriada (manager.py), na qual atualmente estão apontadas para 3 possíveis caminhos (sendo 2 deles comentados, local e docker). Igualmente a aplicação acompanha as instruções para composição de uma imagem docker que permite rodar o banco de dados diretamente.

## Requisitos para rodar o projeto de forma Local:

Para rodar o projeto de forma local é necessário se possuir ao menos o Python instalado, em versão 3.8 ou maior, versões inferiores mas acima do 3 podem vir a funcionar, porém pode haver dependencias e falhas nos mesmos.

Atualmente o banco utilizado é uma base PostgreSQL disponível online através do site heroku, porém caso se deseje configurar uma de forma local, basta se instalar a base apropriada e realizar as adequações em seu conector.

Para se baixar o arquivo diretamente do git pode se utilizar o comando abaixo:

 ``` git clone https://github.com/VitorinoAssuncao/stone_hugin.git ```

GitHub CLI
 
 ``` gh repo clone VitorinoAssuncao/stone_hugin ```

Ou simplesmente acessando  a pagina e selecionando a opção de preferencia para download.

### Instalando os requisitos e acessando o ambiente virtual:

Caso já tenha usado ambientes virtuais, deverá seguir o processo de criação comum ao mesmo, caso nunca tenha feito isso em python é questão de alguns comandos simples:

Em seu terminal python digitar a seguinte linha de comando:

 ``` virtualenv venv ```

Com isso será criada uma nova pasta em seu ambiente com uma estrutura base do python e o instalador pip, após isso é necessário se acionar o ambiente virtual com o seguinte comando:

``` venv\Scripts\activate```

*Note que esse comando deverá ser feito da pasta anterior ao dev_env, seja ela raiz ou não.*

Feito isso, basta rodar o seguinte comando que o instalador do python irá instalar todas as dependências deste projeto:
 ```pip install -r requirements.txt```

## Estruturas Relevantes:

Este projeto consiste em uma aplicação de backend, a qual não possui uma rota raiz (/) atualmente, possuindo apenas 2 estruturas de rotas, conforme a necessidade do usuário:

• stocks: Referente aos estoques das unidades cadastradas no sistema, é responsável por trazer os valores atuais de estoque, assim como receber as atualizações do mesmo.

• tickets: Referente aos chamados atendidos pelas unidades, é responsável por trazer o levantamento de chamados que foram realizados, assim como serve de rota para cadastro de novos em uma possivel expansão.


## EndPoints

Segue abaixo rotas principais liberadas atualmente no projeto:

``` "/stocks" : A rota principal a ser utilizada, responsável por trazer as informações referentes a todas as unidades, incluindo nisto número de atendimentos médios.```

```"/stocks/<id>": A rota que permite trazer os dados individuais de apenas uma unidade.```

```"/tickets": rota principal do sistema de chamados, trazendo todos os chamados atualmente cadastrados na base.```

```"/tickets/<base>": Rota que permite acessar os chamados de uma únidade em específico, trazendo todos os seus atendimentos, importante manter o padrão enviado pelo sistema (UF - UNIDADE)```

```"/tickets/<base>/average": Rota que permite acessar de forma resumida o número de atendimentos médios de uma determinada unidade.```

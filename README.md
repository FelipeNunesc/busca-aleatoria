<h1 align="center" style="font-weight: bold;">Análise de desempenho da busca em arquivos 📁🔍</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="python">
  <img src="https://img.shields.io/badge/psutil-ff69b4?style=for-the-badge&logo=python&logoColor=white" alt="psutil">
</p>

<p align="center">
 <a href="#sobre">Sobre o Projeto</a> • 
 <a href="#execucao">Como Executar</a> •
 <a href="#resultados">Resultados de Desempenho</a> •
 <a href="#colaboradores">Colaboradores</a>
</p>

<h2 id="sobre">📝 Sobre o Projeto</h2>

Este projeto foi desenvolvido como parte de uma atividade da disciplina **Estruturas e Complexidade de Algoritmos**. O objetivo foi trabalhar com a manipulação de grandes volumes de dados e a medição de desempenho computacional. A atividade consiste em duas partes principais:

1. **Criação de Arquivos com Números**:
   - Três arquivos foram criados, cada um contendo números inteiros em sequência, com o seguinte tamanho:
     - Um arquivo com **1 milhão** de números.
     - Um arquivo com **1 bilhão** de números.
     - Um arquivo com **1 trilhão** de números.

2. **Busca em Arquivos**:
   - Um programa foi desenvolvido para realizar a busca de números aleatórios dentro dos arquivos gerados. Além disso, o programa mede o desempenho da busca, coletando informações sobre:
     - Tempo total de execução.
     - Volume de RAM consumida.
     - Percentual de CPU utilizada.

<h2 id="execucao">🚀 Como Executar o Projeto</h2>

Para executar o projeto, siga os passos abaixo:

<h3>Pré-requisitos</h3>

- Python 3 instalado em sua máquina.
- Biblioteca `psutil` instalada. Você pode instalá-la usando o comando:

  ```bash
  pip install psutil
  ```

<h3>Estrutura de Arquivos</h3>

Este projeto está organizado em duas partes principais: a geração dos arquivos binários e a busca dentro desses arquivos.

1. **Geração dos Arquivos Binários**:
   - Existem três scripts Python na pasta `number-generator`, cada um responsável por gerar um arquivo binário contendo números inteiros aleatórios:
     - `gerar-1M.py`: Gera um arquivo `1M.bin` com 1 milhão de números.
     - `gerar-1B.py`: Gera um arquivo `1B.bin` com 1 bilhão de números.
     - `gerar-1T.py`: Gera um arquivo `1T.bin` com 1 trilhão de números.

   - Cada script utiliza o módulo `random` para gerar números inteiros aleatórios e o módulo `struct` para escrever esses números no formato binário em um arquivo.

   - **⚠️ Importante: Certifique-se de executar cada um dos scripts da pasta `number-generator` para gerar os arquivos binários antes de rodar o script de busca.**

2. **Busca nos Arquivos**:
   - O script principal, `main.py`, localizado na pasta `numbers`, realiza a busca de números aleatórios nos arquivos binários gerados. Ele também mede o desempenho da operação, incluindo tempo de execução, uso de RAM e percentual de CPU utilizada.

   - Certifique-se de que os arquivos binários estão na pasta `numbers` com os seguintes nomes:
     - `1M.bin` (arquivo com 1 milhão de números)
     - `1B.bin` (arquivo com 1 bilhão de números)
     - `1T.bin` (arquivo com 1 trilhão de números)

<h3>Executando o Programa</h3>

- Navegue até o diretório do projeto e execute o script `main.py` com o comando:
  ```bash
  python main.py
  ```
- Escolha o tamanho do arquivo no menu apresentado e o programa irá realizar a busca, e exibira os resultados de desempenho.

<h2 id="resultados">📊 Resultados de Desempenho</h2>

Abaixo estão os resultados obtidos após a execução das buscas nos três arquivos:

1. **Arquivo com 1 milhão de números**:
   - **Número buscado**: `888491`
   - **Tempo de execução**: `0.165365 segundos`
   - **Uso de CPU**: `25.98%`
   - **Uso de RAM**: `14.79 MB`

2. **Arquivo com 1 bilhão de números**:
   - **Número buscado**: `565712609`
   - **Tempo de execução**: `201.344807 segundos`
   - **Uso de CPU**: `21.71%`
   - **Uso de RAM**: `14.96 MB`

3. **Arquivo com 1 trilhão de números**:
   - **Número buscado**: `XXXXX`
   - **Tempo de execução**: `YYYYY segundos`
   - **Uso de CPU**: `ZZZZ%`
   - **Uso de RAM**: `AAAA MB`

<h2 id="colaboradores">🤝 Colaboradores</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/felipenunesc">
        <img src="https://avatars.githubusercontent.com/u/86086389?v=4" width="100px;" alt="Profile Picture"/><br>
        <sub>
          <b>Felipe Nunes</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<hr>

<p align="center">
  Este projeto demonstrou a importância da eficiência em operações de leitura e busca em arquivos de grande porte. As medições de desempenho fornecem insights sobre como o uso de recursos varia com o tamanho dos dados, ajudando a otimizar aplicações que lidam com grandes volumes de informação.
</p>

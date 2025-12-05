# Trabalho Indivídual de Algoritmos e Estrutura de Dados

## Apresentação Geral
Este trabalho tem como objetivo consolidar o conhecimento sobre estruturas em árvore
e compressão de dados por meio da implementação prática do algoritmo de Huffman.

Foi desenvolvido um programa em Python capaz de realizar a compressão de pequenos trechos
de texto utilizando o código de Huffman como método de codificação estatística.

O algoritmo de Huffman, amplamente utilizado em sistemas de compressão sem perdas
(lossless), baseia-se na frequência de ocorrência dos símbolos em uma mensagem. A partir dessas frequências, é construída uma árvore binária ponderada, que associa códigos
binários menores aos símbolos mais frequentes e códigos maiores aos menos frequentes, promovendo a redução do tamanho total da representação. 

---

### Estrutura do Projeto

Foram construídos **4 scripts em Python**:

- **huffman_structures.py**  
    Contém as estruturas necessárias para a representação da Árvore de Huffman:
    
    - `HuffmanNode`: Representa um nó da árvore e seus dois filhos. A frequência do nó foi especificada como valor principal para propósitos de comparação, e o construtor padrão inicializa com frequência '0'.
    - `CodeTable`: Um dicionário que irá associar cada palavra do texto com o Código de Huffman gerado para ela.
    - `FrequencyMap` : Um dicionário que irá associar cada palavra do texto com o número de vezes que ela apareceu.

- **huffman_core.py**  
  Possui a implementação das funções que irão gerar e manipular a Árvore de Huffman  
  - `calculate_word_frequencies`: Recebe uma string já concatenada, a formata e tokeniza em seguida gera o FrequencyMap com base na frequência de cada palavra. Cada tipo de pontuação é considerada como uma palavra diferente.
  - `build_huffman_tree` : Recebe o mapa de frequências e adiciona cada palavra a uma `heapq`, de forma que, para cada palavra adicionada compara-se a frequência e o início da heap sempre seja a palavra com menor frequência. Em seguida remove elementos do iníco da heap em pares, criando novos `HuffmanNode` contendo a frequência somada dos dois valores e estes mesmos como filhos.
  - `generate_huffman_codes` : A partir do nó raíz da Árvore de Huffman completa percorre a árvore usando DFS para gerar a `CodeTable` que será usada para comprimir o texto.
  - `compress_text`: A partir da Tabela de Códigos e de um Bloco de Texto retirado do texto original, gera a versão comprimida daquele bloco.

- **huffman_io.py**  
  Lê o arquivo `trabalho1/data/maze.txt` e cria uma matriz de adjacência que será utilizada para a execução do algoritmo.

- **main_huffman.py**  
  Contém a função `main`, além de outras funções que geram os arquivos de saída.  
  Deste arquivo, os outros métodos são chamados automaticamente.

---

### Utilização

#### 1. Pré-requisitos
- Certifique-se de ter o **Python 3.12** ou superior instalado em seu sistema.  
- O **PATH** deve estar configurado corretamente. 
- Mova o arquivo `input.dat`, contendo o texto a ser comprimido, para a localização: `/data/input.dat`

#### Dependências
OPCIONALMENTE, para gerar a IMAGEM da árvore de huffman, instale o graphviz usando seu gerenciador de pacotes, no caso do Ubuntu, o seguinte comando pode ser usado no terminal.
```bash
sudo apt-get install graphviz
```
Também é necessário instalar o wrapper para o graphviz no python usando o seguinte comando:
```bash
pip install graphviz
```

Caso não o graphviz não seja encontrado, o código AINDA será COMPLETAMENTE FUNCIONAL, porém será emitida uma mensagem de erro e o arquivo '.png' não será gerado.

---

#### 2. Execução
Abra um terminal e navegue até o diretório raiz do projeto.  
Execute o comando:

```bash
python main_huffman.py
```
#### 3. Saída

Após a execução do projeto, será gerado na pasta `/data`:

- O arquivo `input.dat` contendo o texto de exemplo, caso nenhum arquivo seja fornecido ao início da execução.

- O arquivo `output.dat` contendo, nesta ordem:
  - A estrutura da árvore de huffman serializada
  - Uma lista dos Códigos de Huffman gerados, onde cada linha contém uma palavra e seu código binário respectivo separados por ' : '
  - Cada bloco de texto e sua versão comprimida.

```bash
- Estrutura da Árvore (serializada):
(40,(16,(8,(4,(2,(1,do),(1,as)),(2,(1,informações),(1,coordenam))),(4,(2,recursos),(2,(1,coordena),(1,processador)))),(8,(4,(2,(1,e),(1,operacionais)),(2,cpu)),(4,(2,(1,processa),(1,dados)),(2,tarefas)))),(24,(10,(4,(2,sistema),(2,(1,armazena),(1,acessa))),(6,.)),(14,(6,(3,os),(3,(1,sistemas),(2,memória))),(8,(4,a),(4,(2,o),(2,controlam))))))

- Lista de códigos de Huffman gerados:
'.': 101
'a': 1110
'acessa': 10011
'armazena': 10010
'as': 00001
'controlam': 11111
'coordena': 00110
'coordenam': 00011
'cpu': 0101
'dados': 01101
'do': 00000
'e': 01000
'informações': 00010
'memória': 11011
'o': 11110
'operacionais': 01001
'os': 1100
'processa': 01100
'processador': 00111
'recursos': 0010
'sistema': 1000
'sistemas': 11010
'tarefas': 0111

-----------------------------------------------------------------


 - Bloco de Texto 1
 Texto Original: A memória armazena informações. A CPU acessa a memória. A CPU processa dados.
 Texto Comprimido: 11101101110010000101011110010110011111011011101111001010110001101101


 - Bloco de Texto 2
 Texto Original: Os recursos controlam o sistema. O sistema coordena tarefas.
 Texto Comprimido: 1100001011111111101000101111101000001100111101


 - Bloco de Texto 3
 Texto Original: Os sistemas operacionais controlam os recursos e coordenam as tarefas do processador.
 Texto Comprimido: 11001101001001111111100001001000000110000101110000000111101
```

- O arquivo `huffman_tree` contendo a representação em grafo da **Árvore de Huffman** na linguagem `DOT`

- O arquivo `huffman_tree.png` - Caso o graphviz esteja devidamente instalado - contendo uma representação gráfica da **Árvore de Huffman** gerada.

 <img src="data/huffman_tree.png">

### Especificações do Teste
Os testes foram executados utilizando as seguintes especificações de máquina:

| Componente | Modelo / Especificação |
|-------------|------------------------|
| **Processador** | AMD Ryzen 3 4350G 3.8GHz|
| **Placa-mãe** | ASRock B450M Steel Legend |
| **Placa de video** | Radeon Graphics Vega 6 (Renoir)|
| **Memória RAM** | 32 GB Crucial Ballistix 3800MHz CL16|
| **Sistema Operacional** | MacOS Ventura 13.7.8 |
| **Versão do Python** | 3.12.1 |


# Autor

<table style="margin: 0 auto; text-align: center;">
  <tr>
    <td colspan="5"><strong>Aluno</strong></td>
  </tr>
  <tr>
      <td>
      <img src="https://avatars.githubusercontent.com/u/83346676?v=4" alt="Avatar de Arthur Santana" style="border-radius:50%; border:4px solid #4ECDC4; box-shadow:0 0 10px #4ECDC4; width:100px;"><br>
      <strong>Arthur Santana</strong><br>
      <a href="https://github.com/Rutrama">
        <img src="https://img.shields.io/github/followers/Rutrama?label=Seguidores&style=social&logo=github" alt="GitHub - Arthur Santana">
      </a>
    </tr>
    <tr>
        <td colspan="5"><strong>Professor</strong></td>
    </tr>
    <tr>
    <td colspan="5" style="text-align: center;">
      <img src="https://avatars.githubusercontent.com/u/46537744?v=4" alt="Avatar de Prof. Michel Pires" style="border-radius:50%; border:4px solid #00599C; box-shadow:0 0 10px #00599C; width:100px;"><br>
      <strong>Prof. Michel Pires</strong><br>
      <a href="https://github.com/mpiress">
        <img src="https://img.shields.io/github/followers/mpiress?label=Seguidores&style=social&logo=github" alt="GitHub - Prof. Michel Pires">
      </a>
    </td>
  </tr>



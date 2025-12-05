import os
import re
from typing import List, Dict, Optional, Tuple

# Importa as estruturas de dados e tipos definidos
from huffman_structures import HuffmanNode, CodeTable
from huffman_core import compress_text

INPUT_FILE = "data/input.dat"
OUTPUT_FILE = "data/output.dat"

def read_input_texts(filename: str = INPUT_FILE) -> List[str]:
    """Lê o arquivo de entrada e separa os textos por linhas em branco."""
    if not os.path.exists('data'):
        os.makedirs('data')
        
    if not os.path.exists(filename):
        # Cria um arquivo de exemplo caso não haja nenhum na pasta 'data'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("A memória armazena informações. A CPU acessa a memória. A CPU processa dados.\n\n")
            f.write("Os recursos controlam o sistema. O sistema coordena tarefas.\n\n")
            f.write("Os sistemas operacionais controlam os recursos e coordenam as tarefas do processador.")
        print(f"ATENÇÃO: Arquivo {filename} não foi encontrado e será criado com conteúdo de exemplo.")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            # Divide por uma ou mais linhas em branco
            return [block.strip() for block in re.split(r'\n{2,}', content) if block.strip()]
    except Exception as e:
        print(f"Erro ao ler o arquivo {filename}: {e}")
        return []

def serialize_tree_structure(node: Optional[HuffmanNode]) -> str:
    """Serializa a estrutura da árvore em formato textual (Pré-ordem simplificada)."""
    if node is None:
        return ""
    
    # Formato: (Frequencia, Palavra ou 'INT', Filhos)
    if node.word is not None:
        return f"({node.frequency},{node.word})"
    else:
        left_str = serialize_tree_structure(node.left)
        right_str = serialize_tree_structure(node.right)
        return f"({node.frequency},{left_str},{right_str})"


def write_output_file(
    root_node: Optional[HuffmanNode], 
    codes: CodeTable, 
    texts_and_compressed: List[Tuple[str, str]]
):
    """
    Escreve os dados no output.dat, usando a Árvore/Códigos Universal
    e listando os resultados para cada bloco.
    """
    
    # Limpa o arquivo de saída antes de começar
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)

    tree_structure = serialize_tree_structure(root_node)
    
    # Bloco 1: Estrutura Universal e Códigos
    output_lines = [
        "\n- Estrutura da Árvore (serializada):",
        tree_structure,
        "\n- Lista de códigos de Huffman gerados:"
    ]
    
    # Tabela de Códigos Universal
    sorted_codes = sorted(codes.items())
    for word, code in sorted_codes:
        output_lines.append(f"'{word}': {code}")
        
    output_lines.append("\n-----------------------------------------------------------------\n")
    
    # Escreve a estrutura base
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        f.write('\n'.join(output_lines) + '\n')
    
    # Bloco 2: Resultados por Texto
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as f:
        for i, (original_text, compressed_data) in enumerate(texts_and_compressed):
            f.write(f"\n - Bloco de Texto {i+1}")
            f.write("\n Texto Original: ")
            f.write(original_text.strip())
            f.write("\n Texto Comprimido: ")
            f.write(compressed_data)
            f.write("\n\n")

def draw_huffman_tree(root, filename='data/huffman_tree'):
    try:
        # Tenta importar o módulo externo (Graphviz)
        from graphviz import Digraph
    except ImportError:
        # Se falhar (Graphviz não instalado), imprime um aviso e retorna.
        print("\nBiblioteca 'graphviz' ou executável 'dot' não encontrado. Pulando a visualização da árvore.")
        return
    dot = Digraph(comment='Huffman Tree', graph_attr={'rankdir': 'TB'}) # TB = Top-Bottom

    def add_nodes_edges(node):
        if node is None:
            return
        
        # 1. Cria o rótulo do nó
        label = f"{node.word or ''}\n({node.frequency})"
        dot.node(str(id(node)), label) # id(node) garante um nome único
        
        # 2. Conecta aos filhos
        if node.left:
            dot.edge(str(id(node)), str(id(node.left)), label='0')
            add_nodes_edges(node.left)
            
        if node.right:
            dot.edge(str(id(node)), str(id(node.right)), label='1')
            add_nodes_edges(node.right)

    add_nodes_edges(root)
    try:
        dot.render(filename, view=True, format='png', cleanup=True)
        print(f"Imagem da Árvore de Huffman foi salva em: {filename}.png")
    except Exception as e:
        print(f"Falha ao executar o programa Graphviz. A imagem não foi gerada. (Erro: {e})")
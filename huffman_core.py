import heapq
import re
from collections import Counter
from typing import Optional, List

# Importa as estruturas de dados e tipos definidos em huffman_structures.py
from huffman_structures import HuffmanNode, CodeTable, FrequencyMap

def calculate_word_frequencies(text_block: str) -> FrequencyMap:
    """Calcula a frequência de cada palavra em um bloco de texto."""
    if not text_block.strip():
        return {}
    
    # Normalização para minúsculas e tokenização
    normalized_block = text_block.lower()
    words = re.findall(r'\b\w+\b|[.,?!]', normalized_block)
    
    return Counter(words)

def build_huffman_tree(frequencies: FrequencyMap) -> Optional[HuffmanNode]:
    """Constrói a Árvore de Huffman a partir do mapa de frequências."""
    min_heap: List[HuffmanNode] = []
    
    for word, freq in frequencies.items():
        heapq.heappush(min_heap, HuffmanNode(word=word, frequency=freq))

    if not min_heap:
        return None
    
    # Agrupamento até restar apenas um nó (a Raiz)
    while len(min_heap) > 1:
        node1 = heapq.heappop(min_heap) # Menor frequência
        node2 = heapq.heappop(min_heap) # Próxima menor frequência
        
        merged_freq = node1.frequency + node2.frequency
        new_internal_node = HuffmanNode(
            frequency=merged_freq,
            left=node1, 
            right=node2
        )
        heapq.heappush(min_heap, new_internal_node)
        
    return min_heap[0]

def generate_huffman_codes(root: Optional[HuffmanNode]) -> CodeTable:
    """Percorre a árvore (DFS) para gerar os códigos binários."""
    codes: CodeTable = {}
    
    def traverse(node: Optional[HuffmanNode], current_code: str):
        if node is None:
            return
        
        if node.word is not None:
            # Caso especial de uma única palavra: código é '0'
            if not current_code and node.frequency > 0:
                 codes[node.word] = '0'
            else:
                codes[node.word] = current_code
            return
        
        # Esquerda -> 0 | Direita -> 1
        traverse(node.left, current_code + '0')
        traverse(node.right, current_code + '1')

    traverse(root, "")
    return codes

def compress_text(text_block: str, code_table: CodeTable) -> str:
    """Comprime o texto usando a tabela de códigos de Huffman."""
    normalized_block = text_block.lower()
    words = re.findall(r'\b\w+\b|[.,?!]', normalized_block)
    
    compressed_data = [code_table.get(word, '') for word in words]
        
    return "".join(compressed_data)
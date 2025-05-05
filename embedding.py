import ollama

# gerar os embeddings
def gerarEmbeddings():
    # solicitar a frase para gerar os embeddings
    frase = input("Digite uma frase: ")

    # Gera os embeddings
    resultado = ollama.embeddings(model='nomic-embed-text', prompt=frase)

    # Pega o vetor de embeddings do resultado
    vetor = resultado['embedding']

    # resultado
    print(f"\nQuantidade de dimensões: {len(vetor)}")
    print("Primeiros 10 valores:")
    print(vetor[:10])
    
gerarEmbeddings()

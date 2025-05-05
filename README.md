# atividade-ollama-1

# Geração de Embeddings com Ollama e Python

Este repositório demonstra como instalar e utilizar o [Ollama](https://ollama.com/) localmente para gerar vetores de embeddings a partir de textos simples, usando um script Python.

## 📌 Objetivo

- Instalar e configurar o Ollama localmente.
- Utilizar o modelo `nomic-embed-text` para gerar embeddings.
- Criar um script Python que conecta ao Ollama, recebe uma frase e retorna os vetores de embeddings.
- Exibir o vetor resultante (dimensões e valores iniciais).

---

## ✅ Pré-requisitos

- Python 3.8 ou superior
- Ollama instalado e configurado localmente

---

## ⚙️ Instalação

### 1. Instalar o Ollama

Siga as instruções oficiais de instalação em: https://ollama.com/download

Após a instalação, verifique se o Ollama está funcionando:

```bash
ollama --version
```

### 2. Instalar o modelo de embeddings

Execute o seguinte comando no terminal:

```bash
ollama pull nomic-embed-text
```

Isso fará o download local do modelo utilizado para gerar embeddings.

---

## 🚀 Execução do Script

Clone o repositório ou baixe o arquivo `embedding.py`.

Instale a biblioteca `ollama`:

```bash
pip install ollama
```

Execute o script com:

```bash
python embedding.py
```

Você será solicitado a digitar uma frase. O script irá gerar os embeddings usando o modelo `nomic-embed-text` e mostrar:

- O número de dimensões do vetor
- Os primeiros 10 valores do embedding

---

## 🧪 Exemplo de Saída

```bash
Digite uma frase: O céu está azul hoje.

Quantidade de dimensões: 768
Primeiros 10 valores:
[0.032, -0.021, 0.078, ..., 0.014]
```

---

## 🎥 Demonstração em Vídeo

O vídeo com a execução local do Ollama e do script pode ser acessado pelo link abaixo:

📺 [Link para o vídeo de demonstração](video: https://www.loom.com/share/e2ca64feaf7444cf9aa775a8fb2700d9?sid=62dbe56e-ee95-460d-ba67-63ea5788a066)


---
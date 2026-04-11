# Transformer

A Transformer is a Neural Network Architecture introduced by Google researchers in 2017 in a paper titled.
* It was designed to handle sequential data (like text, speech, or time series) more efficiently than older models such as **RNNs (Recurrent Neural Networks)** and **LSTMs (Long Short-Term Memory networks)**.
* A Transformer is a type of neural network architecture designed for processing sequential data, such as text, by learning context and tracking relationships between sequence elements using mechanisms called attention and self-attention.
* Transformers are the foundation for modern natural language processing (NLP) models like GPT (Generative Pretrained Transformer), BERT, and Gemini, and have also been adapted for computer vision, audio, and multimodal AI applications.


**Core Idea**
Instead of processing text word-by-word sequentially (like older RNNs), a transformer processes all words in parallel and learns relationships between them using a mechanism called self-attention.

**Key Components**\
**1. Tokenization**\
Input text is split into tokens (words or subwords), each converted into a numerical vector (embedding).\
**2. Self-Attention**\
The model learns how much each word should "pay attention" to every other word in the sequence. For example, in "The cat sat on the mat because it was tired", the model learns that "it" refers to "cat".\
**3. Multi-Head Attention**\
Multiple attention mechanisms run in parallel, each capturing different types of relationships (grammar, meaning, coreference, etc.).\
**4. Feed-Forward Layers**\
After attention, each token passes through a neural network layer to further process the information.\
**5. Positional Encoding**\
Since the model processes tokens in parallel, positional encodings are added to tell the model the order of words.\
**6. Encoder–Decoder Structure**
 * **Encoder**: Reads and understands the input (used in models like BERT)\
 * **Decoder**: Generates output text (used in models like GPT)\
 * **Both together**: Used in translation models


**Real-World Applications**
* Language models: ChatGPT, Claude, Gemini
* Translation: Google Translate
* Image generation: Vision Transformers (ViT), DALL·E
* Code generation: GitHub Copilot
* Speech recognition: Whisper


# Attention

In a transformer, attention is the mechanism that lets the model decide which parts of the input matter most when processing each word (or token).\
Instead of reading a sentence strictly left-to-right, attention allows every word to look at all other words and weigh their importance.\
Self-attention determines how important each word is in sentence by considering its relationship with other words

When processing a word, attention lets the model ask: "Which other words in the sequence are most relevant to understanding this word?"

**Intuition (simple idea)**

Take this sentence:\
“The cat sat on the mat because it was tired.”

To understand what “it” refers to, the model needs to focus on “cat”, not “mat”.\
Attention helps the model do exactly that:
* It assigns a **higher weight** to “cat”
* Lower weights to less relevant words

**How it works (core idea)**\
For each token, the transformer creates three vectors:
* Query (Q) → what this word is looking for
* Key (K) → what each word offers
* Value (V) → the actual information of each word

Then it computes:\
<img width="456" height="76" alt="image" src="https://github.com/user-attachments/assets/0f5a1c19-c113-4bf8-be44-c26414fbc32f" />


What this means:
* Compare the query with all keys → gives relevance scores
* Apply softmax → turn scores into weights (probabilities)
* Multiply by values → get a weighted combination of information

# Encoder and Decoder

**Encoder**
The encoder's job is to read and understand the input — it converts input tokens into rich, context-aware representations (embeddings).\
“reads the question and thinks deeply about it,” producing a rich internal representation.

**What it does:**
* Takes the input sequence (e.g., a sentence in French)
* Applies self-attention — each word looks at every other word to understand context
* Outputs a set of hidden states that capture the meaning of the whole input

**Decoder**
The decoder's job is to generate the output — it produces the output sequence one token at a time.\
“writes the answer step by step,” peeking back into the encoder’s representation at each step to decide what to output next.

**What it does:**
* Takes the encoder's output + what it has generated so far
* Uses masked self-attention (can only look at past tokens, not future ones)
* Uses cross-attention to attend to the encoder's output
* Predicts the next token


<img width="457" height="491" alt="image" src="https://github.com/user-attachments/assets/c9ea92f4-2fcc-4b04-a3ce-a74407ca0949" />



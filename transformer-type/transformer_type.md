# Transformer Type

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

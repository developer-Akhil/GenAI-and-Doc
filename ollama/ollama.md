**What is Ollama?**

Ollama is a free, open-source tool that simplifies running powerful, open-source Large Language Models (LLMs) like Llama 3 directly on your own computer (local machine) for macOS, Windows, and Linux, offering privacy, speed, and offline use by bundling models for easy setup and an API for integration. Think of it as a "Docker for LLMs," making AI accessible for development, experimentation, and private use without complex cloud setups. 
*	Customize Models
*	Use Different Ollama models
*	Build RAG system powered by Ollama models
*	Build full fledged LLM  application using Ollama models

**How to install Ollama?**\
**Step 1**: Download Installer\
Go to the official Ollama site and download the Windows installer:
* https://ollama.com \
Run the ``.exe`` installer and complete setup.

**Step 2**: Verify Installation\
Open PowerShell/cmd and run:\
``ollama --version``\
You should see a version number. If not, restart your system once and retry.

**Step 3**: Start Ollama Service \
Ollama runs as a background service automatically on Windows. \
Verify it is running:\
```ollama list```

**Step 4**: Pull a Model (Required) \
```ollama pull tinyllama```\
Test it:\
```ollama run tinyllama```

**Python Integration (Required for LangChain)**\
**Step 1**: Install Python dependencies\
```python -m pip install langchain langchain-community```

**Step 2**: Minimal Python Test

```
from langchain_community.llms import Ollama

m = Ollama(model='tinyllama')

reponse = m.generate(["When did India got its Independence? was it 26 January, 1950"])

print(reponse.generations[0][0].text)
```


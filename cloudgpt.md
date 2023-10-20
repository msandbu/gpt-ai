## LLM Features

It should be noted here that FM refers to Foundation language models. Since most providers also have support for 3.party LLMs such as LLaMA2.

* References to Bison is also just one of the codenames for PALM. 

Last Update: 31/08/2023

| Features                         | Google                    | Microsoft              | Amazon Web Services  |
|----------------------------------|---------------------------|------------------------|----------------------|
| **LLM Service/Runtime**             | Vertex AI                 | Azure OpenAI           | Bedrock              |
| **LLM Models available**            | PaLM, LLaMa2, Falcon, Claude2* | GPT, LLaMa2, Falcon, Databricks Dolly | Titan, Claude2, Cohere |
| **LLM Models Code**             | Code-Bison | Codex  |  |
| **LLM Models Security**             | Sec-PaLM | tbd |  |
| **LLM Models Catalog**               | Model Garden              | Model Catalog         |  Model Providers                    |
| **LLM Token Size FM**                   | 32k (PaLM2)               | 32k (GPT4)             | 8k (Titan)                     |
| **LLM Availability**                 |                           |                        |                      |
| **LLM Integration framework**        | Vertex AI Extensions      | Microsoft Semantic Kernel |                    |
| **LLM Safety filter**                |                           | Azure AI Content Safety |                    |
| **LLM Fine-tuning support**          | Code-bison(PaLM), text-bison(PaLM) |  GPT-3.5 supports Fine-tuning                  |                    |
| **LLM Agent**                        | Vertex AI Conversation |  Power Virtual agents                  | Bedrock Agents, Amazon Lex                   |

## Machine Learning Features

| Features                         | Google                    | Microsoft              | Amazon Web Services  |
|----------------------------------|---------------------------|------------------------|----------------------|
| **ML Service**                       | Vertex AI Workbench       | Azure Machine Learning | Amazon Sagemaker    |
| **ML Model Catalogue 3.party**               |                           | Huggingface                      |                      |
| **Vector Search**                    | Vertex AI Vector Search   | Azure Cognitive Search | Amazon OpenSearch, Amazon Kendra |

## Text and Speech Features

| Features                         | Google                    | Microsoft              | Amazon Web Services  |
|----------------------------------|---------------------------|------------------------|----------------------|
| **Text-to-image**                    | Imagen                    | DALL-E                 |                      |
| **Speech-to-text**                   | Chirp                     | Azure Speech Recognition, Whisper | Amazon Transcribe |
| **Text-to-speech**                   | Vertex AI                 | Azure Text to speech, Whisper  | Amazon Polly        |

## Additional Services

| Features                         | Google                    | Microsoft              | Amazon Web Services  |
|----------------------------------|---------------------------|------------------------|----------------------|
| **Vector database**                  | Cloud SQL (Pgvector), AlloyDB, Vertex AI Vector Search | Azure Cosmos DB | Amazon RDS (Pgvector) |
| **Embedding**                        | Text embedding API Gecko  | Ada OpenAI Embedding  | Titan Embeddings    |
| **Integration services - Langchain** | Vertex AI, Google Search  | Azure Cognitive Search |                      |
| **Code assistant based AI**          | Duet AI                   | Github Copilot        | Amazon Code Whisperer |
| **Collaboration GPT**                | Duet AI                   | Microsoft Copilot     |                      |
| **Digital Watermarking**             | Synthid (Image)           |                        |                      |
| **Security Powered LLM**           | Security Command Center AI         | Microsoft Security Copilot                        |                      |

import os
import openai

from langchain.chat_models import AzureChatOpenAI
from langchain.llms.openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

os.environ["AZURE_OPENAI_API_KEY"] = ""
os.environ["AZURE_OPENAI_ENDPOINT"] = ""
os.environ["OPENAI_API_VERSION"] = "2024-02-15-preview"








llm = AzureChatOpenAI(deployment_name="trd", temperature=0.7)
system_message = "You are an AI assistant that tells jokes."

system_message_prompt = SystemMessagePromptTemplate.from_template(system_message)
human_template="{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=llm, prompt=chat_prompt)
result = chain.run(f"Tell me a dad joke about norwegians")
print(result)



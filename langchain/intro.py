# ref = https://arxiv.org/pdf/2210.03629.pdf

import os
import pandas as pd
from langchain.agents import load_tools
from langchain import PromptTemplate
from langchain.agents import initialize_agent
from langchain_experimental.agents import create_pandas_dataframe_agent  # Updated import statement
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI


# openai 설정
OPENAI_API_KEY = "OpenAI API"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
# df
df = pd.read_csv('C:\\study\\ERP\\SAP_bike_sales(datasets)\\Addresses.csv')

# 모델
chat_model = ChatOpenAI(temperature=0)

# 에이전트
agent = create_pandas_dataframe_agent(llm=chat_model,
                                      df=df,
                                      agent=AgentType.OPENAI_FUNCTIONS,
                                      verbose=True)

# 프롬프트
prompt_template = PromptTemplate.from_template("how many women survived?")

# 질문
formatted = prompt_template.format()
agent(formatted)
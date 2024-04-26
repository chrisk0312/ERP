#ref = https://www.researchgate.net/publication/372669736_Creating_Large_Language_Model_Applications_Utilizing_LangChain_A_Primer_on_Developing_LLM_Apps_Fast

"""
As large language models (LLMs) were trained on increasing amounts of data and incorporated more parameters, their capabilities expanded significantly.
A large language model (LLM) is a type of AI model capable of generating text with human-like proficiency.
LangChain is a framework designed for building applications using large language models. 
Its aim is to allow developers to easily integrate additional data sources and interact with other applications. 
To achieve this, LangChain offers components (modular abstractions) and chains (customizable pipelines tailored to specific use cases).

The main components of LangChain include Prompts, Memory, Chains, Models, and Agent.
Prompts = These are inputs provided to a Large Language Model (LLM). 
LangChain offers various classes to construct prompts using specialized Prompt Templates.
Memory = This component stores information and state across multiple interactions. 
Each transaction to the LLM's API endpoint is independent, requiring a memory component to store previous conversations and pass them to the LLM with the next prompt.
Chains = Chains are pipelines that connect multiple components to create a complete application. 
They are fundamental building blocks in LangChain. 
Multiple chains can be concatenated using the Simple Sequential Chain class when there is one input and one output.
Models = Large Language Models (LLMs) are the primary models used in LangChain. 
They accept a text prompt and output a text response. 
Additionally, LangChain utilizes other types of models such as Chat Models and Text Embedding Models.
Agent = The Agent component manages the interaction between the user and the application. 
The Action Agent receives user input, determines the appropriate tool and its input, executes the tool, 
records its output (termed as an 'observation'), and makes decisions on subsequent steps based on the history of tool usage, inputs, and observations.
The Plan and Execute Agent receives user input, devises a comprehensive sequence of steps, and implements these steps in a sequential manner.
This involves using a language model as the planner and an action agent as the executor.



Document Loaders = These components load documents from various sources 
such as CSV, PDF, HTML, JSON, Excel, GitHub, Google Drive, One Drive, XML, Wikipedia, and more.
Document Transformers = These components split documents into smaller chunks to enable processing by Large Language Models (LLMs).
Text Embedding Models = These models convert unstructured text into a list of floating-point numbers, representing corresponding embeddings.
Vector Stores = These components assist in storing and searching over embedded data.
Retrievers = These components facilitate querying your data based on embedding similarities.


"""    

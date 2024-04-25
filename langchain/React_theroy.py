#ref = https://arxiv.org/pdf/2210.03629.pdf

"""
Reasoning = traces help the model induce, track, and update action plans as well as handle exceptions
Actions = allow it to interface with and gather additional information from external sources such as knowledge bases or environment
ReAct = reason + act, a general paradigm to combine reasoning and acting with language models for solving diverse language reasoning and decision making tasks

ReAct = diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines in addition to improved human interpretability and trustworthiness. 
a general paradigm to combine reasoning and acting with language models for solving diverse language reasoning and decision making tasks 

ReAct prompts LLMs to generate both verbal reasoning traces and actions pertaining to a task in an interleaved manner, 
Allows the model to perform dynamic reasoning to create, maintain, and adjust high-level plans for acting 
Interact with the external environments (e.g. Wikipedia) to incorporate additional information into reasoning (act to reason).

Evaluations of ReAct and state-of-the-art baselines on four diverse benchmarks: question answering, fact verification, text-based game, and webpage navigation.
The best approach overall is a combination of ReActand CoT that allows for the use of both internal knowledge and externally obtained information during reasoning. 

Wikipedia API, ReAct is able to retrieve information to support reasoning, while also use reasoning to target what to retrieve next,
demonstrating a synergy of reasoning and acting.

setup = domains, action space[search(entity), lookup(string) ,finish(answer)] 
method = react prompting, baselines, combing internal and external knowledge, finetuning

To prompt ReAct,  
(1)decompose the goal, (2) track subgoal completion, (3) determine the next subgoal, and (4) reason via commonsense 

CoT = chain of thought
"""
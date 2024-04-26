#ref = https://arxiv.org/pdf/2210.03629.pdf

"""
Reasoning = traces help the model induce, track, and update action plans as well as handle exceptions
Actions = allow it to interface with and gather additional information from external sources such as knowledge bases or environment
ReAct = reason + act, a general paradigm to combine reasoning and acting with language models for solving diverse language reasoning and decision making tasks
CoT (chain of thought) = sequence of actions or decisions made by the AI system when reacting to user input or when guiding the learning process

 ReAct combines reasoning and acting in language models, enabling them to generate action plans and interface with external sources for information.
 
 This paradigm facilitates dynamic reasoning and adaptation to user input, enhancing interpretability and trustworthiness.
 
 ReAct prompts models to generate verbal reasoning traces and actions simultaneously, allowing for dynamic reasoning and interaction with external environments like Wikipedia. 
 
 Evaluations across diverse benchmarks show that combining ReAct with a chain of thought approach yields the best results, utilizing both internal knowledge and external information effectively. 
 
 The setup involves defining domains and action spaces, while the method includes React prompting, baseline comparisons, and fine-tuning. 

To prompt ReAct,  
(1)decompose the goal, (2) track subgoal completion, (3) determine the next subgoal, and (4) reason via commonsense 

true positive  = the model correctly generates the next subgoal / helps it progress through the maze.
false positive = the model generates an incorrect subgoal / leading it in the wrong direction.
true negative  = the model correctly fails to generate a subgoal /it is already on the correct path.
false negative = the model fails to generate a subgoal /causing it to miss a turn or overlook an important step in reaching the end of the maze.


Performance Evaluation: These metrics assess the model's accuracy by distinguishing between correct decisions (true positives and true negatives) and mistakes (false positives and false negatives).

Identifying Strengths and Weaknesses: True positives and true negatives reveal the model's strengths, while false positives and false negatives highlight areas for improvement, allowing focused attention.

Improvement and Optimization: Analyzing false positives and false negatives helps identify the model's errors, facilitating adjustments to its architecture, parameters, or training data to enhance performance.

Decision Making and Confidence: Understanding these metrics builds confidence in the model's decision-making process by discerning between correct decisions and mistakes, crucial for applications with real-world consequences.

"""
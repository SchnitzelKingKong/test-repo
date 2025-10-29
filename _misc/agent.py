# import crewai
# import Crew, Task, Agent
# from crewai_tools import SerperDevTool
# from langchain_ibm import WatsonxLLM
# import os
# 
# os.environ['WATSONX_APIKEY'] = ""
# os.environ['SERPER_API_KEY'] = ""
# 
# # Parameters
# parameters = {"decoding_method":"greedy","max_new_tokens":500}
# 
# # Create the first 'LLM'
# llm = WatsonxLLM(
#     model = "",
#     url = "",
#     params = parameters,
#     project_id = ""
# )
# # Tools
# search = SerperDevTool()
# 
# # Create the first Agent
# researcher = Agent(
#     llm = llm,
#     function_calling_llm = function_calling_llm,
#     role = "",
#     goal = "",
#     backstory = "",
#     allow_deligation = ""
#     tools = [],
#     verbose = 1
# )
# 
# # Create a Task
# task1 = Task(
#     description="",
#     expected_output="",
#     output_file="",
#     agent=researcher
# )
# task2 = Task(
#     description="",
#     expected_output="",
#     output_file="",
#     agent=researcher
# )
# 
# # Put all togehter with crew
# crew = Crew(
#     agents=[researcher],
#     task=[task1],
#     erbose=1
# )
# print(crew.kichoff)
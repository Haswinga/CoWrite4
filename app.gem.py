import os
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Agent, Task, Crew, Process
from langchain.tools import DuckDuckGoSearchRun


#Set gemini pro as llm
llm = ChatGoogleGenerativeAI(model="gemini-pro",
                             verbose=True,
                             tempreture=0.5,
                             google_api_key="AIzaSyAqee4dqJ7SzSd9jsAxtDGAmDm0RHHF0UM")


#create search
tool_search = DuckDuckGoSearchRun()

#define Agents


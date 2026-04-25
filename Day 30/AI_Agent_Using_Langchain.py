import os
import requests
from langchain_openai import ChatOpenAI
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import tool

os.environ["OPENAI_API_KEY"] = "openai_api_key"
WEATHERSTACK_API_KEY = "weatherstack_api_key"


@tool
def get_weather_data(city: str):
    """
    Takes a city name and returns the current weather data of that city 
    using the weatherstack API.
    """
    url = f"http://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={city}"
    response = requests.get(url)
    return response.json()


llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
search_tool = DuckDuckGoSearchRun()
prompt = hub.pull("hwchase17/react")


tools = [search_tool, get_weather_data]


agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)


if __name__ == "__main__":
    query = "Find the capital of Punjab then find its current weather condition."
    response = agent_executor.invoke({"input": query})
    print("\nFinal Answer:", response["output"])
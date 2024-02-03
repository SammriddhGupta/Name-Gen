import random
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

def generate_team_name(company_name, theme_name, problem_name, idea_name):
    llm = ChatOpenAI(model_name = "gpt-3.5-turbo-0125")
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a creative professional specializing in brainstorming unique and catchy team names for hackathons."),
        ("user", "{input}")
    ])
    
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    
    return chain.invoke({
        "input": f"I'm taking part in the {company_name} hackathon, the theme is {theme_name}, the problem statement involves {problem_name} and our idea is {idea_name}. Now suggest 20 awesome team names for our group!"
    })

# this is for debugging only, is not considered by the webapp when you run it
if __name__ == "__main__":
    print(generate_team_name("Dolby IO", "Social Good", "using Dolby IO's APIs", "dunno yet"))
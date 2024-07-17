from crewai import agent
from dotenv import load_dotenv
load_dotenv()
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))
#news reasearcher
news_researcher=Agent(
    role='Senior Researcher',
    goal="Uncover ground breaking technologies in {topics}",
    verbose=True,
    memory=True,
    backstory=(
        "DRIVEN BY CURIOSITY, YOU'RE AT THE FRONT OF"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)
#news writeer agent
news_writer = Agent(
    role='Writer',
    goal='Narrate compelling teach stories about {topics}',
    verbose=True,
    memory=True,
    backstory=(
          "engaging narratives can educate and bringing new!!"
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True,
)

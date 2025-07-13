from autogen_agentchat.agents import AssistantAgent,UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
from dotenv import load_dotenv
import asyncio
import os


model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    api_key="Your openai apikey here"
)


job_position="Ml Engineer"

interviewer=AssistantAgent(
    name="interviewer",
    model_client=model_client,
    description=f"You are an AI Agent you should interview the candidate for {job_position}.",
    system_message=f'''you are an expert in the field of {job_position}.
                    you should ask atleast 3 well structured questions one after other after 
                    you receive answer for one question from candidate.
                    based on the role. and you should stop asking the questions after you receive "Terminated" Message '''
)

candidate=UserProxyAgent(
    name="candidate",
    description=f"you are simulating a candidate behaviour for the {job_position}.",
    input_func=input
)

career_coach=AssistantAgent(
    name="career_coach",
    model_client=model_client,
    description=f"you are an ai assistant and give the feed back to the candidate answers for the interviewer questions",
    system_message=f''' you are an expert in {job_position} and you should provide the accurate info. 
    to the answers provided by the candidate based on the questions asked by the interviewer'''

)

team=RoundRobinGroupChat(
    participants=[interviewer,candidate,career_coach],
    termination_condition=TextMentionTermination("TERMINATED"),
    max_turns=20
)
async def main():
    stream = team.run_stream(task=f"Conducting an interview for {job_position}")
    console = await Console(stream)
    await console.print_stream()

if __name__ == "__main__":
    asyncio.run(main())





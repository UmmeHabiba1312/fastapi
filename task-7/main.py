from openai import Agent, Runner

agent = Agent(
    name="HelperAgent",
    instructions="You are a helpful assistant who answers questions clearly."
)

response = Runner.run(agent, "What's the capital of France?")
print(response.final_output)

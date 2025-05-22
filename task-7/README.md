#  OpenAI Agents SDK 

**OpenAI Agents SDK**, a powerful Python framework for building tool-using, goal-driven, instruction-following AI agents. This SDK abstracts away the complexity of agentic reasoning and tool orchestration.

---

##  Installation

Install the OpenAI Agents SDK with pip:

```bash
pip install openai-agents 

```

## Core Components Explained

### Agent Class
The Agent defines the behavior of the AI system via:

* A name
* Instructions (system prompt)
* Optional tools, memory, or context handlers

1. Why is Agent a dataclass?

- Simplifies boilerplate: auto-generates __init__, __repr__, etc.
- Makes it easier to declare agent configurations
- Keeps code clean and declarative

```
from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    instructions: str
```

2a. Why is the system prompt contained in the Agent class as instructions? Why can it also be a callable?

The system prompt sets the agent's personality and behavior; it is stored as the instructions attribute.

It can be a static string or a callable function.

When callable, it allows the system prompt to be dynamically generated based on the current runtime context.

This enables the agent to adapt its behavior depending on external data or environment without redefining the agent.

```
Example:
def dynamic_instructions(context, agent):
    return f"You are assisting with the project: {context['project_name']}."

agent = Agent(
    name="DynamicAgent",
    instructions=dynamic_instructions
)
```

2b. Why is the user prompt passed as a parameter in the run method of Runner, which is a classmethod?
The user prompt is the runtime input — the actual question or command the user wants the agent to process.

It is not fixed, so it is passed as a parameter each time the agent runs.

The run method is a classmethod for convenience — you don’t need to instantiate a Runner object to execute an agent.

This makes it easy to call:

`Runner.run(agent, "Your user prompt here")`

3. What is the purpose of the Runner class?
The Runner class is the engine that runs the agent logic.

It manages:
- Taking user prompts as input,
- Feeding them along with system prompts and context into the language model,
- Handling any tools the agent uses,
- Returning the generated output.
- By separating execution (Runner) from configuration (Agent), the SDK achieves modularity and reusability.

4. What are generics in Python? Why do we use it for TContext?
Generics allow you to write classes or functions that work with any type while preserving type safety.
TContext is a generic type variable representing the type of runtime context passed to the agent.

Using generics for TContext means:
- Your agent can accept any kind of context (e.g., dict, custom classes).
- Type checkers and IDEs can understand what kind of context is used.
- It improves code flexibility and maintainability.

```
Example:
from typing import TypeVar, Generic

TContext = TypeVar("TContext")

class Agent(Generic[TContext]):
    ...
```
**Difference Between System Prompt and User Prompt**


|        System Prompt     |       User Prompt             |
|--------------------------|-------------------------------|
| In Agent.instructions    |Passed to Runner.run()         |
|Defines agent’s behavior  |Runtime input from the user    |                      
| and persona              |                               |



Made with ❤️ by UmmeHabiba Agentic AI developer 

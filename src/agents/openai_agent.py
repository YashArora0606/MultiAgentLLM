from enum import Enum
import os
from agents.agent import Agent
from openai import OpenAI


class OpenAIModel(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"


MODEL = OpenAIModel.GPT_3_5_TURBO


class OpenAIAgent(Agent):
    """Represents an agent that uses OpenAI's API to generate responses."""

    def __init__(self, id: int) -> None:
        """Initializes the OpenAI agent.

        Args:
            id (int): The unique identifier of the agent.
        """

        super().__init__(id)
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def ask(self, prompt: str) -> str:
        """Prompts the agent and returns the response.

        Args:
            prompt (str): The prompt to provide the agent.

        Returns:
            str: The response from the agent.
        """

        result = self.client.chat.completions.create(
            model=MODEL.value,
            messages=[{"role": "user", "content": prompt}],
        )
        return result.choices[0].message.content

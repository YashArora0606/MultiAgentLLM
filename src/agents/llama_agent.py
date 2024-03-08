from agents.agent import Agent
from llama_cpp import Llama

# TODO-soon yasharora0606: replace this with the path to the LLama model file
LLAMA_PATH = "./llama-2-7b-chat.ggmlv3.q8_0.bin"


class LLamaAgent(Agent):
    """Represents an agent that uses a local LLAMA model to generate responses."""

    def __init__(self, id: int) -> None:
        """Initializes the LLAMA agent.

        Args:
            id (int): The unique identifier of the agent.
        """

        super().__init__(id)
        self.client = Llama(model_path=LLAMA_PATH)

    def ask(self, prompt: str) -> str:
        """Prompts the agent and returns the response.

        Args:
            prompt (str): The prompt to provide the agent.

        Returns:
            str: The response from the agent.
        """

        output = self.client(prompt)
        return output["choices"][0]["text"]

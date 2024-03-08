from agents.agent import Agent
from agents.openai_agent import OpenAIAgent


class Caucus:
    """Represents a caucus of agents."""

    def __init__(self, num_agents: int) -> None:
        """Initializes a caucus of agents.

        Args:
            num_agents (int): The desired number of agents in the caucus.
        """
        self.agents = [OpenAIAgent(agent_id) for agent_id in range(num_agents)]

    def ask(self, prompts: list[str]) -> list[str]:
        """Provides each agent with their respective prompt and returns their responses.

        Args:
            prompts (list[str]): The prompt to provide each agent.

        Raises:
            ValueError: If the number of prompts does not match the number of agents.

        Returns:
            list[str]: The responses from each agent.
        """

        if len(prompts) != len(self.agents):
            raise ValueError("Number of prompts must match number of agents.")

        # Provide each agent its respective prompt
        return [agent.ask(prompt) for agent, prompt in zip(self.agents, prompts)]

from caucus import Caucus

MAX_AGENTS = 10
MIN_AGENTS = 2
MAX_ROUNDS = 10
MIN_ROUNDS = 1
DEFAULT_NUM_AGENTS = 3
DEFAULT_NUM_ROUNDS = 3


class Debate:
    """Represents a debate simulation among LLM agents."""

    def __init__(
        self, num_agents: int = DEFAULT_NUM_AGENTS, num_rounds: int = DEFAULT_NUM_ROUNDS
    ) -> None:
        """Initializes a debate simulation.

        Args:
            num_agents (int, optional): The desired number of agents in the debate.
            num_rounds (int, optional): The desired number of rounds in the debate.

        Raises:
            ValueError: If the number of agents or rounds is invalid.
        """
        if num_agents < MIN_AGENTS or num_agents > MAX_AGENTS:
            raise ValueError(
                f"Debate must have between {MIN_AGENTS} and {MAX_AGENTS} agents."
            )

        if num_rounds < MIN_ROUNDS or num_rounds > MAX_ROUNDS:
            raise ValueError(
                f"Debate must have between {MIN_ROUNDS} and {MAX_ROUNDS} rounds."
            )

        self.caucus: Caucus = Caucus(num_agents)
        self.num_rounds: int = num_rounds
        self.num_agents: int = num_agents

    def simulate(self, prompt: str) -> list[str]:
        """Simulates a debate among agents.

        Args:
            prompt (str): The initial prompt to be debated.

        Returns:
            list[str]: Answers from all agents at the end of the debate.
        """

        # Set up initial prompts
        prompts: list[str] = [
            self.setup_initial_prompt(agent_id, prompt)
            for agent_id in range(self.num_agents)
        ]

        # Set up initial responses
        responses: list[str] = [
            f"No response from {agent_id}." for agent_id in range(self.num_agents)
        ]

        # Simulate rounds of debate
        for round_id in range(self.num_rounds):

            print(round_id, prompts)

            # Recieve a response from each agent
            responses: list[str] = self.caucus.ask(prompts)

            print(round_id, responses)

            # Aggregate responses from all other agents for each agent
            prompts: list[str] = [
                self.aggregate_responses(agent_id, responses)
                for agent_id in range(self.num_agents)
            ]

            print()

        # TODO-someday yasharora0606: determine if the agents came to a consensus, and if so, return the consensus response.
        return responses

    def aggregate_responses(self, current_agent_id: int, responses: list[str]) -> str:
        """Aggregates responses from all other agents into a new prompt to give to the current agent on the next round.

        Args:
            agent_id (int): The id of the current agent.
            responses (list[str]): The responses of all agents, including the current agent.

        Returns:
            str: The new prompt to give to the current agent.
        """

        pre_response_setup: str = (
            "The following are the responses from all other agents."
        )

        other_agent_responses: str = "\n".join(
            [
                f"Agent {agent_id}: {response}"
                for agent_id, response in enumerate(responses)
                if agent_id != current_agent_id
            ]
        )

        # TODO-soon yasharora0606: ensure that the prompt does not cause agents to add unnecessary information
        post_response_call_to_action: str = (
            "Given these responses from the other agents, what is your answer?"
        )

        return f"{pre_response_setup} {other_agent_responses} {post_response_call_to_action}"

    def setup_initial_prompt(self, agent_id: int, prompt: str) -> str:
        """Creates an initial prompt for an agent in preparation for the debate.

        Args:
            agent_id (int): The id of the current agent.
            prompt (str): The initial prompt for the debate.

        Returns:
            str: The initial prompt for the current agent.
        """

        setup: str = (
            f"You are agent {agent_id}. Your task is to work with other agents to come to a consensus on an answer to a question. Before we begin, independently of other agents' responses, answer the following."
        )

        return f"{setup} {prompt}"


# TODO yasharora0606: Remove testing code
if __name__ == "__main__":
    debate = Debate(num_agents=2, num_rounds=2)
    prompt = "What is the sum of 12 and 23?"
    print(debate.simulate(prompt))

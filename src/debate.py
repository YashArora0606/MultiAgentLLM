from caucus import Caucus

class Debate:
    def __init__(self, num_agents: int = 3, num_rounds: int = 3) -> None:
        self.caucus = Caucus(num_agents)
        self.num_rounds = num_rounds
        self.num_agents = num_agents

    def simulate(self, prompt: str) -> list[str]:
        for round in range(self.num_rounds):
            responses = self.caucus.ask(prompt)
            next_round_prompts = [self.aggregate_responses(agent_id, responses) for agent_id in range(self.num_agents)]
        return self.caucus.ask(prompt)

    def aggregate_responses(self, agent_id: int, responses: int) -> str:
        # TODO yasharora0606: for each agent, assemble all other agents' responses into a single new response.
        return ""
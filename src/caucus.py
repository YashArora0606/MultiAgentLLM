from agent import Agent

class Caucus:
    def __init__(self, num_agents: int = 3) -> None:
        self.agents = [Agent(agent_id) for agent_id in range(num_agents)]
        
    def ask(self, prompt) -> list[str]:
        return [agent.ask(prompt) for agent in self.agents]
        
        
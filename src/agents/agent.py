# TODO-soon yasharora0606: Use abstract base class to represent an abstract agent.
class Agent:
    """Represents an an abstract agent that can generate responses."""

    def __init__(self, id: int) -> None:
        """Initializes the agent.

        Args:
            id (int): The unique identifier of the agent.
        """

        self.id = id

    def ask(self, _: str) -> str:
        """Provides each agent with their respective prompt and returns their responses.

        Args:
            _ (str): The prompt to provide the agent.

        Raises:
            ValueError: If the method is called on the base agent class.

        Returns:
            str: The response from the agent
        """

        raise ValueError("Base agent class method should not be called.")

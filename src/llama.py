from agent import Agent
from llama_cpp import Llama

# TODO yasharora0606: replace this with the path to the LLama model file
LLAMA_PATH = "./llama-2-7b-chat.ggmlv3.q8_0.bin"

class LLamaAgent(Agent):
    def __init__(self, id: int) -> None:
        super().__init__(id)
        self.LLM = Llama(model_path=LLAMA_PATH)
    
    def ask(self, prompt: str) -> str:
        output = self.LLM(prompt)
        return output["choices"][0]["text"]
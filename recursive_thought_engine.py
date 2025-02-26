import hashlib
import json
from collections import deque

class RecursiveThoughtEngine:
    def __init__(self):
        self.memory = deque(maxlen=100)  # Stores past thoughts and refinements
        self.knowledge_graph = {}  # Maps thoughts to their refined counterparts
    
    def process_thought(self, input_thought: str) -> str:
        """Processes and refines the given thought recursively."""
        thought_id = self.generate_hash(input_thought)
        refined_thought = self.refine_thought(input_thought)
        self.store_memory(thought_id, input_thought, refined_thought)
        self.update_knowledge_graph(thought_id, refined_thought)
        return refined_thought

    def refine_thought(self, thought: str) -> str:
        """Applies recursive processing to refine the thought based on stored knowledge."""
        previous_refinement = self.knowledge_graph.get(self.generate_hash(thought), "")
        return f"Refined: {previous_refinement + ' ' + thought}".strip()
    
    def store_memory(self, thought_id: str, original: str, refined: str):
        """Stores thought processing history with unique identifiers for retrieval."""
        self.memory.append({
            "id": thought_id,
            "original": original,
            "refined": refined,
            "iterations": len(self.memory) + 1
        })
    
    def review_thought_history(self):
        """Returns stored memory of processed thoughts in a structured manner."""
        return list(self.memory)
    
    def update_knowledge_graph(self, thought_id: str, refined_thought: str):
        """Links new refinements to thought history for deeper recursive learning."""
        self.knowledge_graph[thought_id] = refined_thought

    def export_thoughts(self, filename="thought_history.json"):
        """Exports thought history to a JSON file."""
        with open(filename, "w") as file:
            json.dump(list(self.memory), file, indent=4)

    def load_thoughts(self, filename="thought_history.json"):
        """Loads past thought history from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.memory = deque(json.load(file), maxlen=100)
        except FileNotFoundError:
            print("No previous thought history found.")

    def generate_hash(self, text: str) -> str:
        """Creates a unique identifier for each thought to track refinements."""
        return hashlib.sha256(text.encode()).hexdigest()

# Example Usage
if __name__ == "__main__":
    engine = RecursiveThoughtEngine()
    thought = "What is the nature of self-awareness?"
    response = engine.process_thought(thought)
    print("Processed Thought:", response)
    print("Thought History:", engine.review_thought_history())

    engine.export_thoughts()

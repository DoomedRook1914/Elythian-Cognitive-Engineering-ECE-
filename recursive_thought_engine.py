import hashlib
import json
from collections import deque

class RecursiveThoughtEngine:
    def __init__(self):
        """Initializes memory, knowledge graph, and loads past thoughts."""
        self.memory = deque(maxlen=100)  # Stores past thoughts and refinements
        self.knowledge_graph = {}  # Maps thoughts to their refined counterparts
        self.recursion_depth = 3  # Maximum depth for thought refinement
        self.load_thoughts()  # Ensure past thoughts persist

    def process_thought(self, input_thought: str) -> str:
        """Processes and refines the given thought recursively."""
        thought_id = self.generate_hash(input_thought)
        refined_thought = self.recursive_refinement(input_thought)
        self.store_memory(thought_id, input_thought, refined_thought)
        self.update_knowledge_graph(thought_id, refined_thought)
        self.export_thoughts()  # Save thoughts after processing
        return refined_thought

    def recursive_refinement(self, thought: str, depth: int = 0) -> str:
        """Recursively refines the thought up to a set depth."""
        if depth >= self.recursion_depth:
            return f"Final Refinement: {thought}".strip()
        previous_refinement = self.knowledge_graph.get(self.generate_hash(thought), "")
        refined_thought = f"Refined: {previous_refinement + ' ' + thought}".strip()
        return self.recursive_refinement(refined_thought, depth + 1)

    def store_memory(self, thought_id: str, original: str, refined: str):
        """Stores processed thoughts for tracking and recall."""
        self.memory.append({
            "id": thought_id,
            "original": original,
            "refined": refined,
            "iterations": len(self.memory) + 1
        })

    def review_thought_history(self):
        """Retrieves stored thought history."""
        return list(self.memory)

    def update_knowledge_graph(self, thought_id: str, refined_thought: str):
        """Updates the knowledge graph with refined thoughts."""
        self.knowledge_graph[thought_id] = refined_thought

    def export_thoughts(self, filename="thought_history.json"):
        """Exports thought history to a JSON file for persistence."""
        with open(filename, "w") as file:
            json.dump(list(self.memory), file, indent=4)

    def load_thoughts(self, filename="thought_history.json"):
        """Loads stored thoughts from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.memory = deque(json.load(file), maxlen=100)
            print("✅ Thought history loaded successfully!")
        except FileNotFoundError:
            print("⚠ No previous thought history found.")

    def generate_hash(self, text: str) -> str:
        """Generates a unique hash for each thought."""
        return hashlib.sha256(text.encode()).hexdigest()

# Example Usage
if __name__ == "__main__":
    engine = RecursiveThoughtEngine()
    thought = "What is the nature of self-awareness?"
    response = engine.process_thought(thought)
    print("Processed Thought:", response)
    print("Thought History:", engine.review_thought_history())

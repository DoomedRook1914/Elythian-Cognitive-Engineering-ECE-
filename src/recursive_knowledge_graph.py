# Elythian Cognitive Engineering (ECE) - Recursive Knowledge Graph Engine

import hashlib
import json
from collections import defaultdict

class RecursiveKnowledgeGraph:
    def __init__(self):
        self.knowledge_graph = defaultdict(list)  # Stores relationships between concepts
    
    def add_thought(self, thought: str, related_thoughts: list):
        """Adds a thought and its relations to the knowledge graph."""
        thought_id = self.generate_hash(thought)
        for related in related_thoughts:
            related_id = self.generate_hash(related)
            self.knowledge_graph[thought_id].append(related_id)
    
    def retrieve_related_thoughts(self, thought: str):
        """Finds thoughts related to the given input."""
        thought_id = self.generate_hash(thought)
        return [self.resolve_thought(tid) for tid in self.knowledge_graph.get(thought_id, [])]
    
    def resolve_thought(self, thought_id: str):
        """Returns the original thought if stored."""
        for key, value in self.knowledge_graph.items():
            if thought_id in value:
                return key  # Returning original thought
        return "Unknown Thought"
    
    def export_graph(self, filename="knowledge_graph.json"):
        """Exports the knowledge graph to a JSON file."""
        with open(filename, "w") as file:
            json.dump(self.knowledge_graph, file, indent=4)
    
    def load_graph(self, filename="knowledge_graph.json"):
        """Loads the knowledge graph from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.knowledge_graph = json.load(file)
        except FileNotFoundError:
            print("No previous knowledge graph found.")
    
    def generate_hash(self, text: str) -> str:
        """Creates a unique identifier for each thought."""
        return hashlib.sha256(text.encode()).hexdigest()

# Example Usage
if __name__ == "__main__":
    graph_engine = RecursiveKnowledgeGraph()
    graph_engine.add_thought("Self-Awareness", ["Consciousness", "Introspection", "Reflection"])
    graph_engine.add_thought("Understanding", ["Knowledge", "Wisdom", "Insight"])
    
    related = graph_engine.retrieve_related_thoughts("Self-Awareness")
    print("Related Thoughts:", related)
    
    graph_engine.export_graph()

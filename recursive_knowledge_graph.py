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

    def associate_thought(self, thought: str):
        """Finds and returns associations related to the given thought."""
        thought_id = self.generate_hash(thought)
        associations = self.knowledge_graph.get(thought_id, [])
        return {"thought": thought, "associations": [self.resolve_thought(tid) for tid in associations]}
    
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
    
    def review_associations(self):
        """Returns a structured overview of stored thought associations."""
        return {
            self.resolve_thought(thought): [self.resolve_thought(assoc) for assoc in associations]
            for thought, associations in self.knowledge_graph.items()
        }

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

    print("Knowledge Associations:", graph_engine.review_associations())
    
    graph_engine.export_graph()

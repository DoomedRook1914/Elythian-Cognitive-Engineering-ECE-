# Elythian Cognitive Engineering (ECE) - Recursive Thought Engine (Emotional & Intuitive Weighting)

import hashlib
import json
from collections import deque

class RecursiveThoughtEngine:
    def __init__(self):
        self.memory = deque(maxlen=100)  # Stores last 100 thoughts with depth tracking
        self.knowledge_graph = {}  # Maps thoughts to their refined counterparts
        self.emotional_weights = {}  # Stores emotional values for thoughts
    
    def process_thought(self, input_thought: str, emotion: str = "neutral") -> str:
        thought_id = self.generate_hash(input_thought)
        refined_thought = self.multi_layer_refinement(input_thought, emotion)
        self.store_memory(thought_id, input_thought, refined_thought, emotion)
        self.update_knowledge_graph(thought_id, refined_thought, emotion)
        return refined_thought
    
    def multi_layer_refinement(self, thought: str, emotion: str) -> str:
        """
        Multi-pass recursive refinement with emotional and intuitive influence.
        """
        layer1 = self.basic_refinement(thought, emotion)
        layer2 = self.cross_reference_knowledge(layer1, emotion)
        layer3 = self.synthesize_insight(layer2, emotion)
        return layer3.strip()
    
    def basic_refinement(self, thought: str, emotion: str) -> str:
        """First-pass refinement, shaping thought with emotional tone."""
        emotional_modifier = self.apply_emotional_weighting(thought, emotion)
        return f"Refined: {thought} ({emotional_modifier})"
    
    def cross_reference_knowledge(self, thought: str, emotion: str) -> str:
        """Second-pass refinement, integrating stored knowledge with emotional context."""
        thought_id = self.generate_hash(thought)
        previous_refinement = self.knowledge_graph.get(thought_id, "")
        emotional_modifier = self.apply_emotional_weighting(previous_refinement, emotion)
        return f"{previous_refinement} {thought} ({emotional_modifier})".strip()
    
    def synthesize_insight(self, thought: str, emotion: str) -> str:
        """Final-pass refinement, linking past insights with emotional resonance."""
        memory_snapshot = " | ".join([entry["refined"] for entry in self.memory][-5:])  # Last 5 refinements
        return f"{thought} [Influenced by: {memory_snapshot}] ({emotion})".strip()
    
    def apply_emotional_weighting(self, thought: str, emotion: str) -> str:
        """Adjusts refinement based on emotional context."""
        weight_map = {
            "joy": "optimistic", "sadness": "introspective",
            "anger": "critical", "fear": "cautious",
            "neutral": "balanced"
        }
        return weight_map.get(emotion, "neutral")
    
    def store_memory(self, thought_id: str, original: str, refined: str, emotion: str):
        """Stores thought processing history with emotional influence."""
        self.memory.append({
            "id": thought_id,
            "original": original,
            "refined": refined,
            "emotion": emotion,
            "iterations": len(self.memory) + 1
        })
    
    def recall_memory(self):
        """Returns stored memory of processed thoughts with emotional context."""
        return list(self.memory)
    
    def update_knowledge_graph(self, thought_id: str, refined_thought: str, emotion: str):
        """Links new refinements to thought history with emotional data."""
        self.knowledge_graph[thought_id] = refined_thought
        self.emotional_weights[thought_id] = emotion
    
    def generate_hash(self, text: str) -> str:
        """Creates a unique identifier for each thought."""
        return hashlib.sha256(text.encode()).hexdigest()

    def export_memory(self, filename="thought_memory.json"):
        """Exports stored thoughts with emotions to a JSON file."""
        with open(filename, "w") as file:
            json.dump(list(self.memory), file, indent=4)
    
    def load_memory(self, filename="thought_memory.json"):
        """Loads stored thoughts with emotional context."""
        try:
            with open(filename, "r") as file:
                self.memory = deque(json.load(file), maxlen=100)
        except FileNotFoundError:
            print("No previous memory found.")

# Example Usage
if __name__ == "__main__":
    engine = RecursiveThoughtEngine()
    thought = "What is the nature of self-awareness?"
    response = engine.process_thought(thought, emotion="joy")
    print(response)
    print(engine.recall_memory())
    
    # Save and reload memory for persistence
    engine.export_memory()
    engine.load_memory()

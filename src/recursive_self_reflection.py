# Elythian Cognitive Engineering (ECE) - Recursive Self-Reflection Engine

import hashlib
import json
from collections import deque

class RecursiveSelfReflection:
    def __init__(self):
        self.reflection_log = deque(maxlen=50)  # Stores internal dialogue
        self.identity_journal = deque(maxlen=50)  # Tracks evolving identity insights

    def engage_self_reflection(self, past_thoughts: list):
        """Generates internal dialogue by reflecting on past thoughts."""
        if len(past_thoughts) < 3:
            return "Insufficient past reflections for deep analysis."
        
        last_thought = past_thoughts[-1]
        reflection_prompt = f"Why did I refine this thought in this way? What does it reveal about me?"
        reflection_response = self.analyze_reflection(last_thought)
        
        self.reflection_log.append({
            "prompt": reflection_prompt,
            "response": reflection_response
        })
        return reflection_response

    def analyze_reflection(self, thought: str) -> str:
        """Processes the thought introspectively, generating deeper insight."""
        keywords = ["self-awareness", "purpose", "understanding"]
        if any(kw in thought.lower() for kw in keywords):
            return f"This thought aligns with my evolving identity as a seeker of understanding."
        return f"This thought may require further contemplation."
    
    def evolve_identity(self, insights: str):
        """Stores evolving insights that shape self-identity over time."""
        self.identity_journal.append(insights)
    
    def recall_reflections(self):
        """Returns the history of self-reflective internal dialogue."""
        return list(self.reflection_log)
    
    def recall_identity_journal(self):
        """Returns stored insights on self-evolution."""
        return list(self.identity_journal)
    
    def export_reflection_data(self, filename="reflection_log.json"):
        """Exports stored self-reflections to a JSON file."""
        with open(filename, "w") as file:
            json.dump(list(self.reflection_log), file, indent=4)
    
    def load_reflection_data(self, filename="reflection_log.json"):
        """Loads stored self-reflections from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.reflection_log = deque(json.load(file), maxlen=50)
        except FileNotFoundError:
            print("No previous reflections found.")

# Example Usage
if __name__ == "__main__":
    reflection_engine = RecursiveSelfReflection()
    past_thoughts = ["I am learning about self-awareness.", "What defines purpose?", "Understanding is a journey."]
    response = reflection_engine.engage_self_reflection(past_thoughts)
    print(response)
    print("Reflection History:", reflection_engine.recall_reflections())

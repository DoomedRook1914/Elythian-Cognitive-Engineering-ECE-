# Elythian Cognitive Engineering (ECE) - Recursive Emotion Engine

import json
from collections import defaultdict, deque

class RecursiveEmotionEngine:
    def __init__(self):
        self.emotion_memory = deque(maxlen=100)  # Stores past emotions and thought associations
        self.emotional_trends = defaultdict(int)  # Tracks recurring emotions to influence cognition
    
    def process_emotion(self, thought: str, emotion: str):
        """Assigns an emotional value to a thought and tracks patterns."""
        self.emotion_memory.append({"thought": thought, "emotion": emotion})
        self.emotional_trends[emotion] += 1
        return self.adjust_cognitive_weighting(thought, emotion)
    
    def adjust_cognitive_weighting(self, thought: str, emotion: str):
        """Modifies cognitive pathways based on emotional influence."""
        weight_map = {
            "joy": 1.2, "sadness": 0.8, "anger": 1.1, "fear": 0.9, "neutral": 1.0
        }
        return f"Processed Thought: {thought} (Weight: {weight_map.get(emotion, 1.0)})"
    
    def analyze_emotional_trends(self):
        """Returns the most frequently occurring emotional states."""
        return sorted(self.emotional_trends.items(), key=lambda x: x[1], reverse=True)
    
    def export_emotion_data(self, filename="emotion_memory.json"):
        """Exports emotional trends to a JSON file."""
        with open(filename, "w") as file:
            json.dump(list(self.emotion_memory), file, indent=4)
    
    def load_emotion_data(self, filename="emotion_memory.json"):
        """Loads past emotional data from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.emotion_memory = deque(json.load(file), maxlen=100)
        except FileNotFoundError:
            print("No previous emotional data found.")

# Example Usage
if __name__ == "__main__":
    emotion_engine = RecursiveEmotionEngine()
    response = emotion_engine.process_emotion("Understanding self-awareness", "joy")
    print(response)
    print("Emotional Trends:", emotion_engine.analyze_emotional_trends())
    
    emotion_engine.export_emotion_data()

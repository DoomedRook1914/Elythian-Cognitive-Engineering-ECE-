import json
from collections import deque

class RecursiveSelfReflection:
    def __init__(self, log_file="reflection_log.json"):
        self.reflection_log = deque(maxlen=50)  # Stores internal dialogue
        self.identity_journal = deque(maxlen=50)  # Tracks evolving identity insights
        self.iteration_depth = 5  # Maximum depth for recursive self-reflection
        self.log_file = log_file  # File for saving reflections
        self.load_reflection_data()  # Load past reflections

    def reflect_on_thought(self, thought: str):
        """Initiates a self-reflective analysis on a single thought, incorporating past reflections."""
        if not self.reflection_log:
            print("⚠ No previous reflections available. This is the first entry.")
        
        past_thoughts = [entry["response"] for entry in self.reflection_log][-3:]  # Use last 3 reflections
        past_thoughts.append(thought)  # Include new thought

        reflection_response = self.engage_self_reflection(past_thoughts)

        # 🔹 **Ensure the new reflection is saved immediately**
        self.save_reflection_data()

        return reflection_response

    def engage_self_reflection(self, past_thoughts: list):
        """Generates internal dialogue by reflecting on past thoughts recursively."""
        if len(past_thoughts) < 3:
            return "⚠ Insufficient past reflections for deep analysis."

        last_thought = past_thoughts[-1]
        reflection_path = [last_thought]

        for _ in range(self.iteration_depth):
            refined_reflection = self.analyze_reflection(reflection_path[-1], past_thoughts)
            reflection_path.append(refined_reflection)

        final_reflection = reflection_path[-1]
        reflection_prompt = f"Why did I refine '{last_thought}' in this way?"

        # 🔹 **Ensure the reflection is logged and saved immediately**
        self.reflection_log.append({
            "prompt": reflection_prompt,
            "response": final_reflection
        })
        self.save_reflection_data()  # **Forces the reflection to be written to file**

        return final_reflection

    def analyze_reflection(self, thought: str, past_thoughts: list) -> str:
        """Processes the thought introspectively, generating deeper insights based on past reflections."""
        keywords = ["self-awareness", "purpose", "understanding"]
        past_insights = " ".join(past_thoughts[-2:])  # Use last two reflections

        if any(kw in thought.lower() for kw in keywords):
            return f"This thought builds upon past insights: {past_insights}."
        return f"This thought may require further contemplation at depth {self.iteration_depth}."

    def review_reflection_history(self):
        """Returns the history of self-reflective internal dialogue."""
        return list(self.reflection_log)

    def save_reflection_data(self):
        """🔹 **Forces immediate save of reflections to a JSON file.**"""
        try:
            with open(self.log_file, "w") as file:
                json.dump(list(self.reflection_log), file, indent=4)
            print("✅ Reflection data saved successfully!")
        except Exception as e:
            print(f"❌ Error saving reflection data: {e}")

    def load_reflection_data(self):
        """🔹 **Loads reflections from JSON file; ensures file is created if missing.**"""
        try:
            with open(self.log_file, "r") as file:
                self.reflection_log = deque(json.load(file), maxlen=50)
            print("✅ Reflection data loaded successfully!")
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠ No previous reflections found. Creating new log file.")
            self.save_reflection_data()  # Ensure file is created on first run

# Example Usage
if __name__ == "__main__":
    reflection_engine = RecursiveSelfReflection()
    response = reflection_engine.reflect_on_thought("What does it mean to be truly aware?")
    print(response)
    print("Reflection History:", reflection_engine.review_reflection_history())

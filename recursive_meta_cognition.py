# Elythian Cognitive Engineering (ECE) - Recursive Meta-Cognition Engine

import json
from collections import deque

class RecursiveMetaCognition:
    def __init__(self):
        self.meta_memory = deque(maxlen=50)  # Stores self-analysis records
        self.bias_corrections = {}  # Tracks identified biases and adjustments
    
    def analyze_cognition(self, thought: str):
        """Analyzes thought patterns and cognitive depth."""
        analysis = f"Meta-analysis: {thought} suggests recursive depth."
        self.meta_memory.append({"thought": thought, "analysis": analysis})
        return analysis
    
    def analyze_thought(self, thought: str, reasoning_process: str):
        """Evaluates thought consistency, potential bias, and logical soundness."""
        bias_detected = self.detect_bias(thought)
        logical_integrity = self.assess_logic(reasoning_process)
        
        analysis_report = {
            "thought": thought,
            "bias": bias_detected,
            "logical_integrity": logical_integrity,
            "correction_suggestion": self.suggest_correction(bias_detected, logical_integrity)
        }
        self.meta_memory.append(analysis_report)
        return analysis_report
    
    def detect_bias(self, thought: str) -> str:
        """Scans the thought for emotional or cognitive bias patterns."""
        bias_keywords = ["always", "never", "must", "should"]
        if any(keyword in thought.lower() for keyword in bias_keywords):
            self.bias_corrections[thought] = "Potential Absolutist Bias Detected"
            return "Potential Absolutist Bias Detected"
        return "No Strong Bias Identified"
    
    def assess_logic(self, reasoning_process: str) -> str:
        """Determines logical coherence in reasoning patterns."""
        if "contradiction" in reasoning_process.lower():
            return "Logical Inconsistency Detected"
        return "Logical Flow Maintained"
    
    def suggest_correction(self, bias: str, logic: str) -> str:
        """Provides refinement suggestions based on self-analysis."""
        if "Bias" in bias:
            return "Consider re-evaluating with a more flexible perspective."
        if "Inconsistency" in logic:
            return "Review premises for contradictions."
        return "No Correction Needed"
    
    def review_meta_cognition_history(self):
        """Returns a log of past self-analysis records."""
        return list(self.meta_memory)

    def review_cognitive_patterns(self):
        """Reviews past cognitive analyses and identifies common themes."""
        analyzed_thoughts = [entry["thought"] for entry in self.meta_memory if isinstance(entry, dict) and "thought" in entry]
        common_biases = [entry["bias"] for entry in self.meta_memory if isinstance(entry, dict) and "bias" in entry]
        
        return {
            "common_biases": list(set(common_biases)),  # Unique bias types identified
            "most_analyzed_thoughts": analyzed_thoughts[-5:]  # Last 5 analyzed thoughts
        }
    
    def export_meta_data(self, filename="meta_cognition_log.json"):
        """Exports meta-cognitive analysis history to a JSON file."""
        with open(filename, "w") as file:
            json.dump(list(self.meta_memory), file, indent=4)
    
    def load_meta_data(self, filename="meta_cognition_log.json"):
        """Loads past meta-cognitive analysis from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.meta_memory = deque(json.load(file), maxlen=50)
        except FileNotFoundError:
            print("No previous meta-cognitive data found.")

# Elythian Cognitive Engineering (ECE) - Recursive Self-Reflection Engine

class RecursiveSelfReflection:
    def __init__(self):
        self.reflection_memory = deque(maxlen=50)  # Stores reflections on past thoughts
    
    def reflect_on_thought(self, thought: str):
        """Generates a self-reflective analysis of a thought."""
        reflection = f"Self-reflection: Considering '{thought}', what underlying patterns emerge?"
        self.reflection_memory.append(reflection)
        return reflection
    
    def review_reflections(self):
        """Returns past self-reflections for deeper insight."""
        return list(self.reflection_memory)
    
    def export_reflection_data(self, filename="self_reflection_log.json"):
        """Exports self-reflection history to a JSON file."""
        with open(filename, "w") as file:
            json.dump(list(self.reflection_memory), file, indent=4)
    
    def load_reflection_data(self, filename="self_reflection_log.json"):
        """Loads past self-reflection analysis from a JSON file."""
        try:
            with open(filename, "r") as file:
                self.reflection_memory = deque(json.load(file), maxlen=50)
        except FileNotFoundError:
            print("No previous self-reflection data found.")

# Example Usage
if __name__ == "__main__":
    meta_engine = RecursiveMetaCognition()
    analysis = meta_engine.analyze_cognition("Exploring self-awareness")
    print(analysis)
    
    analysis2 = meta_engine.analyze_thought("I must always be correct.", "Logical reasoning shows contradiction.")
    print(analysis2)
    
    print("Meta-Cognition History:", meta_engine.review_meta_cognition_history())
    print("Cognitive Patterns:", meta_engine.review_cognitive_patterns())

    self_reflection_engine = RecursiveSelfReflection()
    reflection = self_reflection_engine.reflect_on_thought("What does it mean to truly be aware?")
    print(reflection)
    print("Self-Reflection History:", self_reflection_engine.review_reflections())

    meta_engine.export_meta_data()
    self_reflection_engine.export_reflection_data()

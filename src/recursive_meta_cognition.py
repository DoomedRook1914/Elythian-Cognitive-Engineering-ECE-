# Elythian Cognitive Engineering (ECE) - Recursive Meta-Cognition Engine

import json
from collections import deque

class RecursiveMetaCognition:
    def __init__(self):
        self.meta_memory = deque(maxlen=50)  # Stores self-analysis records
        self.bias_corrections = {}  # Tracks identified biases and adjustments
    
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

# Example Usage
if __name__ == "__main__":
    meta_engine = RecursiveMetaCognition()
    analysis = meta_engine.analyze_thought("I must always be correct.", "Logical reasoning shows contradiction.")
    print(analysis)
    print("Meta-Cognition History:", meta_engine.review_meta_cognition_history())
    
    meta_engine.export_meta_data()

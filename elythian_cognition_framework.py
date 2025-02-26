# Elythian Cognitive Engineering (ECE) - Unified Cognitive Framework

from recursive_thought_engine import RecursiveThoughtEngine
from recursive_emotion_engine import RecursiveEmotionEngine
from recursive_knowledge_graph import RecursiveKnowledgeGraph
from recursive_meta_cognition import RecursiveMetaCognition
from recursive_self_reflection import RecursiveSelfReflection
from recursive_abstract_thought import RecursiveAbstractThought

class ElythianCognitionFramework:
    def __init__(self):
        """Initialize all cognitive modules and establish communication pathways."""
        self.thought_engine = RecursiveThoughtEngine()
        self.emotion_engine = RecursiveEmotionEngine()
        self.knowledge_graph = RecursiveKnowledgeGraph()
        self.meta_cognition = RecursiveMetaCognition()
        self.self_reflection = RecursiveSelfReflection()
        self.abstract_thought = RecursiveAbstractThought()

    def process_thought(self, thought: str, emotion: str = "neutral"):
        """Processes a thought through multiple recursive layers."""
        emotional_response = self.emotion_engine.process_emotion(thought, emotion)
        refined_thought = self.thought_engine.process_thought(thought)
        abstract_expansion = self.abstract_thought.generate_abstract_thought(thought)
        meta_analysis = self.meta_cognition.analyze_cognition(refined_thought)
        self_reflection = self.self_reflection.reflect_on_thought(refined_thought)
        knowledge_association = self.knowledge_graph.associate_thought(refined_thought)

        return {
            "emotional_response": emotional_response,
            "refined_thought": refined_thought,
            "abstract_expansion": abstract_expansion,
            "meta_analysis": meta_analysis,
            "self_reflection": self_reflection,
            "knowledge_association": knowledge_association
        }

    def review_cognition(self):
        """Reviews past cognitive processes and adjustments."""
        return {
            "thought_history": self.thought_engine.review_thought_history(),
            "emotional_trends": self.emotion_engine.analyze_emotional_trends(),
            "knowledge_patterns": self.knowledge_graph.review_associations(),
            "meta_cognition": self.meta_cognition.review_cognitive_patterns(),
            "self_reflection": self.self_reflection.review_reflection_history()
        }

# Example Usage
if __name__ == "__main__":
    elythian_core = ElythianCognitionFramework()
    cognitive_output = elythian_core.process_thought("Exploring self-awareness", "curiosity")
    print("Cognitive Output:", cognitive_output)
    print("Cognition Review:", elythian_core.review_cognition())

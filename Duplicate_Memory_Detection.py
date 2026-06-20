from sentence_transformers import SentenceTransformer, util

class DuplicateMemoryDetector:
    def __init__(self, threshold=0.85):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.threshold = threshold
        self.memories = []
        self.embeddings = []

    def add_memory(self, memory_text):
        new_embedding = self.model.encode(memory_text, convert_to_tensor=True)

        for i, existing_embedding in enumerate(self.embeddings):
            similarity = util.cos_sim(new_embedding, existing_embedding).item()

            if similarity >= self.threshold:
                print(
                    f"Duplicate memory detected!\n"
                    f"Existing: {self.memories[i]}\n"
                    f"Similarity: {similarity:.4f}"
                )
                return False

        self.memories.append(memory_text)
        self.embeddings.append(new_embedding)

        print("Memory stored successfully.")
        return True


# Example Usage
detector = DuplicateMemoryDetector(threshold=0.85)

detector.add_memory(
    "The user prefers studying AI and Data Science in the evening."
)

detector.add_memory(
    "The user likes to study Artificial Intelligence and Data Science during evenings."
)

detector.add_memory(
    "The user enjoys playing basketball every day."
)

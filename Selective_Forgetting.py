from datetime import datetime, timedelta

class Memory:
    def __init__(self, content, importance):
        self.content = content
        self.importance = importance  # 1-10
        self.created_at = datetime.now()
        self.access_count = 0

    def access(self):
        self.access_count += 1


class ForgetNetMemoryManager:
    def __init__(self, forget_threshold=3):
        self.memories = []
        self.forget_threshold = forget_threshold

    def add_memory(self, content, importance):
        memory = Memory(content, importance)
        self.memories.append(memory)

    def selective_forgetting(self):
        current_time = datetime.now()
        retained_memories = []

        for memory in self.memories:
            age_days = (current_time - memory.created_at).days

            retention_score = (
                memory.importance * 0.6 +
                memory.access_count * 0.3 -
                age_days * 0.1
            )

            if retention_score >= self.forget_threshold:
                retained_memories.append(memory)

        forgotten = len(self.memories) - len(retained_memories)
        self.memories = retained_memories

        print(f"Forgot {forgotten} low-value memories.")


# Example
manager = ForgetNetMemoryManager()

manager.add_memory("User likes Python.", importance=8)
manager.add_memory("User visited website once.", importance=2)

manager.memories[0].access()
manager.memories[0].access()

manager.selective_forgetting()

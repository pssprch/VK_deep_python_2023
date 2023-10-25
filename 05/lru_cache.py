class LRUCache:
    def __init__(self, limit=42):
        if not (isinstance(limit, int) and 0 < limit < 10_000):
            raise ValueError("Limit must be from 1 to 9999")
        self.limit = limit
        self.cache = []
        self.box = {}

    def get(self, key):
        if key in self.box:
            self.cache.remove(key)
            self.cache.append(key)
            return self.box[key]
        return None

    def set(self, key, value):
        if key in self.cache:
            self.cache.remove(key)
        elif len(self.cache) >= self.limit:
            old_key = self.cache.pop(0)
            del self.box[old_key]
        self.cache.append(key)
        self.box[key] = value

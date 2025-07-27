class FeatureStore:
    def __init__(self):
        self.store = {}

    def ingest(self, entity_id, features):
        self.store[entity_id] = features

    def get_features(self, entity_id):
        return self.store.get(entity_id, {})

    def summary(self):
        return {k: len(v) for k, v in self.store.items()}

if __name__ == "__main__":
    fs = FeatureStore()
    fs.ingest("user_1", {"age": 25, "interests": ["tech", "sports"]})
    fs.ingest("user_2", {"age": 30, "interests": ["music", "movies"]})
    print("Stored Features:", fs.store)
    print("Feature Summary:", fs.summary())

import unittest
from src.main import FeatureStore

class TestFeatureStore(unittest.TestCase):
    def test_ingest_and_retrieve(self):
        fs = FeatureStore()
        fs.ingest("user_1", {"feature1": 1.0, "feature2": 2.0})
        result = fs.get_features("user_1")
        self.assertEqual(result["feature1"], 1.0)
        self.assertEqual(result["feature2"], 2.0)

    def test_empty_result(self):
        fs = FeatureStore()
        self.assertEqual(fs.get_features("nonexistent"), {})

if __name__ == '__main__':
    unittest.main()

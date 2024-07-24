import unittest
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


class TestETL(unittest.TestCase):

    def test_extract_data(self):
        data = extract_data("path/to/data_source")
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_transform_data(self):
        raw_data = [{"field1": "value1", "field2": "value2"}]
        transformed_data = transform_data(raw_data)
        self.assertIsNotNone(transformed_data)
        self.assertIn("transformed_field", transformed_data[0])

    def test_load_data(self):
        data = [{"transformed_field": "transformed_value"}]
        result = load_data(data, "path/to/destination")
        self.assertTrue(result)
        self.assertEqual(result, "Data loaded successfully!")


if __name__ == "__main__":
    unittest.main()

import unittest
import pandas as pd
import os

class TestDataPipeline(unittest.TestCase):
    
    def setUp(self):
        self.processed_file = 'data/processed/structured_bank_reviews.csv'

    def test_dataset_existence_and_volume(self):
        # 1. Verify the pipeline file exists
        self.assertTrue(os.path.exists(self.processed_file), "Processed data file is completely missing!")
        
        # 2. Enforce the 1,200+ total record volume criteria constraint
        df = pd.read_csv(self.processed_file)
        self.assertGreaterEqual(len(df), 1200, f"Data volume tracking lower than minimum threshold. Found: {len(df)}")

    def test_required_columns_exist(self):
        # 3. Ensure all mandatory analytical feature fields exist
        df = pd.read_csv(self.processed_file)
        required_columns = ['review_text', 'rating', 'date', 'bank_name', 'source', 'cleaned_text']
        for col in required_columns:
            self.assertIn(col, df.columns, f"Mandatory reporting feature column '{col}' is missing.")

    def test_no_null_keys(self):
        # 4. Critical relational integrity check: Review IDs cannot be null
        df = pd.read_csv(self.processed_file)
        self.assertEqual(df['reviewId'].isnull().sum(), 0, "Critical structural failure: Primary review ID values cannot contain nulls.")

if __name__ == '__main__':
    unittest.main()

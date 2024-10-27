import unittest
import pandas as pd
from src.utils.data_transformation import transform_test_csv, transform_test_json

class TestETL(unittest.TestCase):
    def test_transform_csv(self):
        data = {
            "id": [6311],
            "name": ["Jennifer Green"],
            "created_at": ["2013-06-30"],
            "last_login": ["2013-06-30"],
            "is_claimed": ["True"],
            "paid_amount": ["5004.67"]
        }
        df = pd.DataFrame(data)
        transformed = transform_test_csv(df)
        self.assertEqual(transformed['is_claimed'].iloc[0], True)
        self.assertEqual(transformed['paid_amount'].iloc[0], 5004.67)

    def test_transform_json(self):
        json_data = [{
            "user_id": "e9703a66-6556-4b48-8a0b-0ace129d7a11",
            "user_details": {
                "name": "Joshua Webster",
                "dob": "1983-05-15",
                "telephone_numbers": ["001-640-924-3637"]
            }
        }]
        users, _, _ = transform_test_json(json_data)
        self.assertEqual(users[0]['name'], "J*****")

if __name__ == '__main__':
    unittest.main()

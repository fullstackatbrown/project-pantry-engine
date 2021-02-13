import unittest
from src.scraper.ingredient_parser.parse_ingredients import parse_ingredient

class ParseIngredients(unittest.TestCase):
    def test_parse_ingredients(self):
        self.assertEqual("grated parmesan cheese", parse_ingredient(".5 oz grated parmesan cheese").name)


if __name__ == '__main__':
    unittest.main()

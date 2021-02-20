import unittest
from src.scraper.ingredient_parser.parse_ingredients import parse_ingredient


class ParseIngredients(unittest.TestCase):
    def test_parse_ingredients(self):
        self.assertEqual("parmesan cheese", parse_ingredient(".5 oz grated parmesan cheese").name)
        self.assertEqual("sesame seeds", parse_ingredient("¹¹⁄₂ teaspoon toasted sesame seeds").name)
        self.assertEqual("tomato", parse_ingredient("1 can whole tomatoes").name)
        self.assertEqual("potato", parse_ingredient("12 lb yukon gold potato").name)
        self.assertEqual("flour", parse_ingredient("12 cups all-purpose flour").name)
        self.assertEqual("chocolate syrup", parse_ingredient("1 ¼ cups chocolate syrup, optional, for garnish").name)
        self.assertEqual("potato", parse_ingredient(".5 lb baby potatoes").name)

if __name__ == '__main__':
    unittest.main()

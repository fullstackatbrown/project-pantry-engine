# taken from the package parse_ingredients

from nltk.stem import WordNetLemmatizer
import unicodedata
import re
from dataclasses import dataclass
import nltk
nltk.download("wordnet")


@dataclass
class Ingredient:
    name: str
    quantity: int
    unit: str
    comment: str
    original_string: str


# a predefined list of unit's
units = {
    "l": ["l", "litre", "litres", "liter", "liters"],
    "ml": ["ml", "millilitre", "milli litre", "millilitres", "milli litres", "milliliter", "milli liter", "milliliters", "milli liters"],
    "g": ["g", "gram", "grams"],
    "mg": ["mg", "milligram", "milli gram", "milligrams", "milli grams"],
    "kg": ["kg", "kilogram", "kilo gram", "kilograms", "kilo grams"],
    "oz": ["oz", "ounce", "ounces"],
    "fl": ["fl"],
    "tsp": ["tsp", "tsps", "teaspoon", "teaspoons"],
    "tbsp": ["tbsp", "tbsps", "tablespoon", "tablespoons"],
    "cup": ["cup", "cups"],
    "pint": ["pint", "pints"],
    "pinch": ["pinch"],
    "strip": ["strip", "strips"],
    "envelope": ["envelope", "envelopes", "sheet", "sheets"],
    "gal": ["gal", "gallon", "gallons"],
    "qt": ["qt", "quarter", "quarters"],
    "lb": ["lb", "lbs", "pound", "pounds"],
    "bunch": ["bunch", "bunches"],
    "sprig": ["sprig", "sprigs"],
    "spear": ["spear", "spears"],
    "slice": ["slice", "slices"],
    "stick": ["stick", "sticks"],
    "stalk": ["stalk", "stalks"],
    "loaf": ["loaf", "loaves"],
    "leaf": ["leaf", "leaves"],
    "clove": ["clove", "cloves"],
    "jar": ["jar", "jars"],
    "head": ["head", "heads"],
    "handful": ["handful", "handfuls"],
    "fillet": ["fillet", "fillets"],
    "drop": ["drop", "drops"],
    "can": ["can", "cans"],
    "box": ["box", "boxes"],
    "block": ["block", "blocks"],
    "piece": ["piece", "pieces"],
    "package": ["package", "packages"],
}

descriptors = [
    "sliced",
    "plain",
    "yukon gold",
    "toasted",
    "yellow",
    "whole wheat",
    "whole",
    "white",
    "warm",
    "virgin",
    "unsweetened",
    "unsalted",
    "toasted",
    "taco-size",
    "superfine",
    "strong",
    "store-bought",
    "unsalted",
    "softened",
    "soft",
    "small",
    "slightly browned",
    "skinless boneless",
    "shredded",
    "shaved",
    "seasoned",
    "roasted",
    "ripe",
    "refried",
    "refined",
    "reduced",
    "raw",
    "premade",
    "of",
    "nutritional",
    "non-dairy",
    "neutral",
    "natural",
    "mixed",
    "minced",
    "melted",
    "medium",
    "mccormick®",
    "madagascar bourbon",
    "low sodium",
    "lean",
    "whole",
    "large",
    "homemade",
    "green",
    "grated",
    "gold",
    "full-fat",
    "frozen",
    "freshly",
    "fresh",
    "freeze-dried",
    "dry",
    "dried",
    "distilled",
    "diced",
    "dairy-free",
    "cubed",
    "crushed",
    "crumbled",
    "cooked",
    "cooked and shredded",
    "coarse",
    "chopped",
    "canned",
    "pacific foods®",
    "batch tasty's",
    "85%",
    "all purpose",
    "all-purpose",
    "additive-free",
    "yukon",
    "russet",
    "baby",
]

excluded = [
    "spice grinder",
    "sauce of choice",
    "ramekins",
    "peanut or vegetable oil",
    "hearts of palm",
]

# numbers with a simple slash fraction (1 1/3, 2 4/5, etc.)
numberAndSlashFraction = re.compile(r'(\d{1,3}?\s\d\/\d{1,3})')
# Vulgar fractions (½, ⅓, etc.)
fractionMatch = re.compile(r'[\u00BC-\u00BE\u2150-\u215E]')
# numbers (0, 1, 2, 3, ..., etc.)
numberMatch = re.compile(r'(\d*\.?\d+)')
# numbers and fractions (1 ⅓, 1 ⅓, etc.)¹¹⁄₂
numberAndFractionMatch = re.compile(
    r'(\d{1,3}\s?[\u00BC-\u00BE\u2150-\u215E])')
# simple slash fractions (1/2, 1/3, 5/4, etc.)
slashFractionMatch = re.compile(r'(\d{1,3}\/\d{1,3})')
# vulgar slash which is it's own character in unicode.
# for example: 1⁄2, 4⁄3
vulgarSlashFractionMatch = re.compile(r'(\d{1,3}\u2044\d{1,3})')
# number with a vulgar slash in a fraction (1 1⁄2)
numberAndVulgarSlashFraction = re.compile(r'(\d{1,3}?\s\d\u2044\d{1,3})')
# any of the above
# string between parantheses, for example: "this is not a match (but this is, including the parantheses)"
quantityMatch = re.compile(
    r'(?<!\w)((\d{1,3}?\s\d\/\d{1,3})|(\d{1,3}?\s?\d\u2044\d{1,3})|(\d{1,3}\u2044\d{1,3})|(\d{1,3}\s?[\u00BC-\u00BE\u2150-\u215E])|([\u00BC-\u00BE\u2150-\u215E])|(\d{1,3}\/?\d?)|(\d*\.?\d+)%?)')
betweenParanthesesMatch = re.compile(r'\(([^\)]+)\)')

wnl = WordNetLemmatizer()


def isFullTypedFraction(text: str) -> bool:
    if text.find('/') >= 0 or text.find('\u2044') >= 0:
        return True
    else:
        return False


def toFloat(quantity: str) -> float:
    """ Parse a valid quantity string to a float """
    # We're using 'match', which searches only in the front of the string.
    # That way we know that if it's just a fraction (½) it can never be 1 ½, for example.
    # Then just logically look if it's anything else.
    if fractionMatch.match(quantity) is not None:
        return unicodedata.numeric(quantity)
    if slashFractionMatch.match(quantity) is not None:
        splitted = quantity.split('/')
        return int(splitted[0]) / int(splitted[1])
    if vulgarSlashFractionMatch.match(quantity) is not None:
        splitted = quantity.split('\u2044')
        return int(splitted[0]) / int(splitted[1])
    if numberAndFractionMatch.match(quantity) is not None:
        first = numberMatch.match(quantity).group()
        fraction = fractionMatch.search(quantity).group()
        return int(first) + toFloat(fraction)
    if numberAndSlashFraction.match(quantity) is not None:
        first = numberMatch.match(quantity).group()
        fraction = slashFractionMatch.search(quantity).group()
        return int(first) + toFloat(fraction)
    if numberAndVulgarSlashFraction.match(quantity) is not None:
        first = numberMatch.match(quantity).group()
        fraction = vulgarSlashFractionMatch.search(quantity).group()
        return int(first) + toFloat(fraction)
    if numberMatch.match(quantity) is not None:
        return float(quantity)


def parse_ingredient(ingredient: str) -> Ingredient:
    """ Tries to extract the quantity, the unit and the ingredient itself from a string """
    # We're doing a VERY simple parse. This could probably be better with some NLP
    # but we have nowhere near time enough for that during this assignment.
    ingredient = unicodedata.normalize(
        "NFKD", ingredient).replace("\u2044", "/").lower()
    rest = ingredient

    quantity = 0
    unit = ''
    name = ''
    comment = ''

    quantity_string = None

    # First, let's see if we can find any quantity in the forms of:
    # type                              -   example
    # a vulgar fraction                 -   ½ or \u00BC
    # a vulgar slash between numbers    -   1⁄2
    # a normal slash between numbers    -   1/2
    # a number                          -   1 or 2 etc.
    # a number and a vulgar fraction    -   1 ½ or 1½
    match = quantityMatch.match(ingredient)
    if match is not None:
        quantity_string = match.group().strip(' ')
        quantity = toFloat(quantity_string)

    if quantity_string is not None:
        length = len(quantity_string)
        if ingredient[length] == ' ':
            length = length + 1
        rest = ingredient[length:]

    # Recipe websites tend to put a comment between parantheses.
    # for example: 1 (fresh) egg. Let's see if we can find any and extract it
    betweenMatch = betweenParanthesesMatch.search(rest)
    if betweenMatch is not None:
        betweenParentheses = betweenMatch.group()
        comment = betweenParentheses[1:-1]
        rest = rest.replace(betweenParentheses, '')
        if rest[0] == ' ':
            rest = rest[1:]

    # Other recipe websites tend to put a comment in the end of the line
    # seperated by a comma. Let's see if we can find any and extract it
    commaSplitted = rest.split(',')
    if len(commaSplitted) > 1:
        comment = comment + ' ' + ', '.join(commaSplitted[1:])
        comment = comment.strip(' ')
        rest = commaSplitted[0]

    # Now split the rest of the string.
    splitted = rest.split(' ')

    # If the string is just one more word, it's probably safe to assume
    # that there is no unit string available, but we're dealing with,
    # for example: 1 egg, where egg is both the ingredient and unit.
    if len(splitted) == 1:
        return Ingredient(rest, quantity, '', comment, ingredient)

    # let's see if we can find something in the string that matches any
    # of my defined units. The list isn't finished and will probably miss
    # lot's of them. But by using a predefined list we avoid a situation where
    # "1 fresh egg" gives us a unit "fresh". Here the unit will be undefined
    # and 'fresh egg' will be the ingredient. This should probably later be
    # filtered again.
    wouldBeUnit = splitted[0]
    for key in units:
        value = units[key]
        if wouldBeUnit in value:
            unit = key

    # If we did have a unit, join the rest of the string
    # if we didn't, join the entire string
    if unit != '':
        name = ' '.join(splitted[1:])
    else:
        name = ' '.join(splitted)

    # remove descriptors
    for descriptor in descriptors:
        if name.startswith(descriptor):
            name = name[len(descriptor)+1:]

    # singularize
    name = wnl.lemmatize(name).strip()

    # and voila! The most basic ingredient parser ever.
    # as I said, I'm not too happy with it and NLP would probably
    # be a better fit, but this brings more complexity
    return Ingredient(name, quantity, unit, comment, ingredient)

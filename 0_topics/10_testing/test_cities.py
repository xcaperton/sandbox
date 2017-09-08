import unittest
from city_funcs import city_country


class CityTestCase(unittest.TestCase):
    """testing some city funcs"""

    def test_city_country(self):
        cityc = city_country('richmond', 'virginia')
        self.assertEqual(cityc, 'Richmond, Virginia')


if __name__ == '__main__':
    unittest.main()


#test = city_country('richmond','virginia')

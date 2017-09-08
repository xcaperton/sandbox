# Testing Suryeys

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Testin ghte sruvey"""

    def setUp(self):
        """Setting some stuff up to be used below"""
        question = "What is your first language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Mandarin', 'Spanish']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """test 3 responses"""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()

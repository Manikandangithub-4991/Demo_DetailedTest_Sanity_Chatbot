# -*- coding: utf-8 -*-
import unittest
from RestClient import RestClient
from Response_from_API import Response_from_API
from ConfigManager import ConfigManager

class DetailedTest_01_SOP_MediClaim_Spellcheck(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_hrpolicy_mediclaim_spellcheck1 = ["hi", "hw can i claim for mecal reimbursement?", "bye"]
    inputstring_hrpolicy_mediclaim_spellcheck2 = ["hi", "how can i clam for mdical reimbursement?", "bye"]
    inputstring_hrpolicy_mediclaim_spellcheck3 = ["hi", "ow can i claim for medical reimrsement?", "bye"]
    inputstring_hrpolicy_mediclaim_spellcheck4 = ["hi", "how can i caim for medical rebursement?", "bye"]

    resposne_instance = Response_from_API()

    def test_SOP_HRPolicy_MediClaim_SpellCheck1(self):
        """To test the SOP_MASClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck1[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck1[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.4 Allowed under MAS')) and (
            convertunicode_to_string.endswith('diagnosis and treatment of specified illness.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck1[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])
    def test_SOP_HRPolicy_MediClaim_SpellCheck2(self):
        """To test the SOP_MediClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck2[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck2[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.4 Allowed under MAS')) and (
            convertunicode_to_string.endswith('diagnosis and treatment of specified illness.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck2[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPolicy_MediClaim_SpellCheck3(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck3[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck3[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.4 Allowed under MAS')) and (
            convertunicode_to_string.endswith('diagnosis and treatment of specified illness.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck3[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPolicy_MediClaim_SpellCheck4(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck4[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck4[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.4 Allowed under MAS')) and (
            convertunicode_to_string.endswith('diagnosis and treatment of specified illness.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_mediclaim_spellcheck4[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_MediClaim_Spellcheck)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_MediClaim_Spellcheck)
    unittest.TextTestRunner(verbosity=2).run(suite)




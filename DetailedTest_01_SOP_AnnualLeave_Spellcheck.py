# -*- coding: utf-8 -*-
import unittest
from RestClient import RestClient
from Response_from_API import Response_from_API
from ConfigManager import ConfigManager

class DetailedTest_01_SOP_AnnualLeave_Spellcheck(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_hrpolicy_annualleave_spellcheck1 = ["hi", "hw Annual leave encashment calculated ?", "bye"]
    inputstring_hrpolicy_annualleave_spellcheck2 = ["hi", "How Annual leve encahment calcultd ?", "bye"]
    inputstring_hrpolicy_annualleave_spellcheck3 = ["hi", "How Anual leave encashment calculated ?", "bye"]
    inputstring_hrpolicy_annualleave_spellcheck4 = ["hi", "hw Annual leave encament clculated ?", "bye"]


    resposne_instance = Response_from_API()

    def test_SOP_HRPlicy_AnnualLeave_SpellCheck1(self):
        """To test the SOP_MASClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck1[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck1[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.2 Annual leave encashment calculated')) and (
            convertunicode_to_string.endswith('(WBP + *Special Allowance + Provision for car for 1 month)) / 30')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck1[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])
    def test_SOP_HRPlicy_AnnualLeave_SpellCheck2(self):
        """To test the SOP_MediClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck2[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck2[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.2 Annual leave encashment calculated')) and (
            convertunicode_to_string.endswith('(WBP + *Special Allowance + Provision for car for 1 month)) / 30')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck2[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPlicy_AnnualLeave_SpellCheck3(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck3[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck3[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.2 Annual leave encashment calculated')) and (
            convertunicode_to_string.endswith('(WBP + *Special Allowance + Provision for car for 1 month)) / 30')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck3[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPlicy_AnnualLeave_SpellCheck4(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck4[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck4[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.2 Annual leave encashment calculated')) and (
            convertunicode_to_string.endswith('(WBP + *Special Allowance + Provision for car for 1 month)) / 30')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_annualleave_spellcheck4[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_AnnualLeave_Spellcheck)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_AnnualLeave_Spellcheck)
    unittest.TextTestRunner(verbosity=2).run(suite)




# -*- coding: utf-8 -*-
import unittest
from RestClient import RestClient
from Response_from_API import Response_from_API
from ConfigManager import ConfigManager

class DetailedTest_01_SOP_WBSClaims_Spellcheck(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_wbsclaim_spellcheck1 = ["hi", "what is the ducation allowance as part of WBS?","bye"]
    inputstring_wbsclaim_spellcheck2 = ["hi", "what is the education allwnce as pat of WBS?", "bye"]
    inputstring_wbsclaim_spellcheck3 = ["hi", "wt is the educton lowance as part of WBS?", "bye"]
    inputstring_wbsclaim_spellcheck4 = ["hi", "wt is the eduction allownce as part of WBS?", "bye"]


    resposne_instance = Response_from_API()

    def test_SOP_HRPolicy_WBSClaims_SpellCheck1(self):
        """To test the SOP_MASClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck1[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck1[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.3 Education Allowance as part of WBS')) and (
            convertunicode_to_string.endswith('hostel fee could be produced once in a quarter.')))


        response = self.resposne_instance.input_value_json(self,self.inputstring_wbsclaim_spellcheck1[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_SOP_HRPolicy_WBSClaims_SpellCheck2(self):
        """To test the SOP_MediClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck2[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck1[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.3 Education Allowance as part of WBS')) and (
            convertunicode_to_string.endswith('hostel fee could be produced once in a quarter.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck1[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPolicy_WBSClaims_SpellCheck3(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck3[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck1[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.3 Education Allowance as part of WBS')) and (
            convertunicode_to_string.endswith('hostel fee could be produced once in a quarter.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck1[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    def test_SOP_HRPolicy_WBSClaims_SpellCheck4(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck4[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck4[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.3 Education Allowance as part of WBS')) and (
            convertunicode_to_string.endswith('hostel fee could be produced once in a quarter.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_wbsclaim_spellcheck4[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_WBSClaims_Spellcheck)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_WBSClaims_Spellcheck)
    unittest.TextTestRunner(verbosity=2).run(suite)




# -*- coding: utf-8 -*-
import unittest
from RestClient import RestClient
from Response_from_API import Response_from_API
from ConfigManager import ConfigManager

class DetailedTest_01_SOP_Leave_Spellcheck(unittest.TestCase):
    url = ConfigManager.chatbot_url
    restClient = RestClient()
    inputstring_hrpolicy_leave_spellcheck1 = ["hi", "hw many leves do i have while in probation", "bye"]
    inputstring_hrpolicy_leave_spellcheck2 = ["hi", "how may leaves do i hve while in prbation", "bye"]
    inputstring_hrpolicy_leave_spellcheck3 = ["hi", "ho many leves do i have whle in probtion", "bye"]
    inputstring_hrpolicy_leave_spellcheck4 = ["hi", "how mny leavs do i have while in probaton", "bye"]

    resposne_instance = Response_from_API()

    def test_SOP_HRPolicy_MediClaim_SpellCheck1(self):
        """To test the SOP_MASClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck1[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck1[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.6 Leaves during probation')) and (
            convertunicode_to_string.endswith('start earning 1.75 days of leave every month.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck1[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])
    def test_SOP_HRPolicy_MediClaim_SpellCheck2(self):
        """To test the SOP_MediClaim Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck2[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck2[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.6 Leaves during probation')) and (
            convertunicode_to_string.endswith('start earning 1.75 days of leave every month.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck2[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPolicy_MediClaim_SpellCheck3(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck3[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck3[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.6 Leaves during probation')) and (
            convertunicode_to_string.endswith('start earning 1.75 days of leave every month.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck3[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])


    def test_SOP_HRPolicy_MediClaim_SpellCheck4(self):
        """To test the SOP_LEave during probation Query """
        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck4[0])
        self.assertEquals("Hi , I am your IT Bot. I can help you with your IT issues and policy queries.",
                          response['text'])

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck4[1])
        convertunicode_to_string = response['text'].encode('ascii', 'ignore')
        self.assertTrue((convertunicode_to_string.startswith('1.6 Leaves during probation')) and (
            convertunicode_to_string.endswith('start earning 1.75 days of leave every month.')))

        response = self.resposne_instance.input_value_json(self, self.inputstring_hrpolicy_leave_spellcheck4[2])
        self.assertEquals("Thank you, have a Great Day.",
                          response['text'])

    @staticmethod
    def suite():
        """TestProject for this class"""
        suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_Leave_Spellcheck)
        unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DetailedTest_01_SOP_Leave_Spellcheck)
    unittest.TextTestRunner(verbosity=2).run(suite)




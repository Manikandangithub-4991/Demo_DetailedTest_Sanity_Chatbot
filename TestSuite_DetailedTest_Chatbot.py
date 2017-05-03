# coding=utf-8

import unittest

from TestProject import DetailedTest_01_SOP_AnnualLeave_Spellcheck
from TestProject import DetailedTest_01_SOP_Leave_Spellcheck
from TestProject import DetailedTest_01_SOP_MediClaim_Spellcheck
from TestProject import DetailedTest_01_SOP_WBSClaims_Spellcheck


class TestSuite_DetailedTest_Chatbot(unittest.TestCase):

        if __name__ == '__main__':
                loader = unittest.TestLoader()
                module1 = DetailedTest_01_SOP_AnnualLeave_Spellcheck.suite()
                module2 = DetailedTest_01_SOP_Leave_Spellcheck.suite()
                module3 = DetailedTest_01_SOP_MediClaim_Spellcheck.suite()
                module4 = DetailedTest_01_SOP_WBSClaims_Spellcheck.suite()
                suite = unittest.TestSuite([module1,module2,module3,module4])
                unittest.TextTestRunner(verbosity=2).run(suite)

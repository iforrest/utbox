import sys
import os
import unittest

path_to_add = os.path.abspath(os.path.join(__file__, '..','..','utbox', 'bin'))
sys.path.append(path_to_add)

import ut_parse_lib


class TestParseMethods(unittest.TestCase):

    def test_parse_extended(self):
        domain = "http://www.example.com/123/123.php"
        lists = ["mozilla", "iana", "custom"]

        for l in lists:
            with self.subTest(l=l):
                TLDList = ut_parse_lib.loadTLDFile(l)
                parse_result = ut_parse_lib.parse_extended(domain, TLDList)
                self.assertEqual(parse_result["ut_domain"], "example.com")


if __name__ == "__main__":
    unittest.main()

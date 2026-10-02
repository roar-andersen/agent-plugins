from pathlib import Path
import re
import unittest

SKILL = Path(__file__).resolve().parents[1] / 'plugins/fest-251-ekspert/skills/instructions'
CLIENT = (SKILL / 'examples/dotnet/HttpClient/FestM30Client.cs').read_text(encoding='utf-8')
WCF = (SKILL / 'examples/dotnet/Wcf/FestWcfClient.cs').read_text(encoding='utf-8')
REFERENCE = (SKILL / 'references/10-webservice-integrasjon-dotnet.md').read_text(encoding='utf-8')
ACTION = 'http://www.slv.no/201410325/FestService251/GetM30'


class ExampleContractTests(unittest.TestCase):
    def test_endpoints_match_reference(self):
        endpoints = set(re.findall(r'new\("(https://[^"]+)"\)', CLIENT))
        documented = set(re.findall(r'`(https://[^`]+FestService251\.svc)`', REFERENCE))
        self.assertEqual(len(endpoints), 5)
        self.assertEqual(endpoints, documented)

    def test_action_and_parameter_names_match_reference(self):
        for text in (CLIENT, WCF, REFERENCE):
            self.assertIn(ACTION, text)
        for name in ('"filter"', '"incrementalDate"'):
            self.assertIn(name, CLIENT)
            self.assertIn(name, WCF)
        self.assertIn('Soap12WSAddressing10', WCF)
        self.assertIn('http://www.w3.org/2003/05/soap-envelope', CLIENT)


if __name__ == '__main__':
    unittest.main()

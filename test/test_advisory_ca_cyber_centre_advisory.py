# coding: utf-8

"""
    VulnCheck API

    Version 3 of the VulnCheck API

    The version of the OpenAPI document: 3.0
    Contact: support@vulncheck.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from vulncheck_sdk.models.advisory_ca_cyber_centre_advisory import AdvisoryCACyberCentreAdvisory

class TestAdvisoryCACyberCentreAdvisory(unittest.TestCase):
    """AdvisoryCACyberCentreAdvisory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryCACyberCentreAdvisory:
        """Test AdvisoryCACyberCentreAdvisory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryCACyberCentreAdvisory`
        """
        model = AdvisoryCACyberCentreAdvisory()
        if include_optional:
            return AdvisoryCACyberCentreAdvisory(
                control_systems = True,
                cve = [
                    ''
                    ],
                date_added = '',
                html_url = '',
                serial_number = '',
                title = ''
            )
        else:
            return AdvisoryCACyberCentreAdvisory(
        )
        """

    def testAdvisoryCACyberCentreAdvisory(self):
        """Test AdvisoryCACyberCentreAdvisory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

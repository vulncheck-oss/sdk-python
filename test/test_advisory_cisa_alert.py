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

from vulncheck_sdk.models.advisory_cisa_alert import AdvisoryCISAAlert

class TestAdvisoryCISAAlert(unittest.TestCase):
    """AdvisoryCISAAlert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryCISAAlert:
        """Test AdvisoryCISAAlert
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryCISAAlert`
        """
        model = AdvisoryCISAAlert()
        if include_optional:
            return AdvisoryCISAAlert(
                affected_products = '',
                alert_id = '',
                archived = True,
                cve = [
                    ''
                    ],
                cveexploited_itw = True,
                cvss = '',
                date_added = '',
                icsa = True,
                icsma = True,
                mitigations = '',
                release_date = '',
                title = '',
                updated_at = '',
                url = '',
                vendor = ''
            )
        else:
            return AdvisoryCISAAlert(
        )
        """

    def testAdvisoryCISAAlert(self):
        """Test AdvisoryCISAAlert"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

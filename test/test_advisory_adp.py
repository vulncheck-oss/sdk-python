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

from vulncheck_sdk.models.advisory_adp import AdvisoryADP

class TestAdvisoryADP(unittest.TestCase):
    """AdvisoryADP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryADP:
        """Test AdvisoryADP
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryADP`
        """
        model = AdvisoryADP()
        if include_optional:
            return AdvisoryADP(
                affected = [
                    vulncheck_sdk.models.advisory/m_affected.advisory.MAffected(
                        collection_url = '', 
                        cpes = [
                            ''
                            ], 
                        default_status = '', 
                        package_name = '', 
                        platforms = [
                            ''
                            ], 
                        product = '', 
                        repos = '', 
                        vendor = '', 
                        versions = [
                            vulncheck_sdk.models.advisory/m_version.advisory.MVersion(
                                less_than = '', 
                                less_than_or_equal = '', 
                                status = '', 
                                version = '', 
                                version_type = '', )
                            ], )
                    ],
                metrics = [
                    vulncheck_sdk.models.advisory/vulnrichment_metric.advisory.VulnrichmentMetric(
                        other = vulncheck_sdk.models.advisory/vulnrichment_other.advisory.VulnrichmentOther(
                            content = vulncheck_sdk.models.advisory/vulnrichment_content.advisory.VulnrichmentContent(
                                id = '', 
                                options = [
                                    vulncheck_sdk.models.advisory/vulnrichment_option.advisory.VulnrichmentOption(
                                        automatable = '', 
                                        exploitation = '', 
                                        technical_impact = '', )
                                    ], 
                                role = '', 
                                timestamp = '', 
                                version = '', ), 
                            type = '', ), )
                    ],
                provider_metadata = vulncheck_sdk.models.advisory/m_provider_metadata.advisory.MProviderMetadata(
                    date_updated = '', 
                    org_id = '', 
                    short_name = '', )
            )
        else:
            return AdvisoryADP(
        )
        """

    def testAdvisoryADP(self):
        """Test AdvisoryADP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from vulncheck_sdk.models.api_configurations import ApiConfigurations

class TestApiConfigurations(unittest.TestCase):
    """ApiConfigurations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiConfigurations:
        """Test ApiConfigurations
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiConfigurations`
        """
        model = ApiConfigurations()
        if include_optional:
            return ApiConfigurations(
                cve_data_version = '',
                nodes = [
                    vulncheck_sdk.models.api/nodes.api.Nodes(
                        children = [
                            vulncheck_sdk.models.api/nodes.api.Nodes(
                                cpe_match = [
                                    vulncheck_sdk.models.api/cpe_match.api.CPEMatch(
                                        cpe22_uri = '', 
                                        cpe23_uri = '', 
                                        cpe_name = [
                                            vulncheck_sdk.models.api/cpe_name.api.CPEName(
                                                cpe22_uri = '', 
                                                cpe23_uri = '', 
                                                last_modified_date = '', )
                                            ], 
                                        version_end_excluding = '', 
                                        version_end_including = '', 
                                        version_start_excluding = '', 
                                        version_start_including = '', 
                                        vulnerable = True, )
                                    ], 
                                operator = '', )
                            ], 
                        cpe_match = [
                            vulncheck_sdk.models.api/cpe_match.api.CPEMatch(
                                cpe22_uri = '', 
                                cpe23_uri = '', 
                                version_end_excluding = '', 
                                version_end_including = '', 
                                version_start_excluding = '', 
                                version_start_including = '', 
                                vulnerable = True, )
                            ], 
                        operator = '', )
                    ]
            )
        else:
            return ApiConfigurations(
        )
        """

    def testApiConfigurations(self):
        """Test ApiConfigurations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

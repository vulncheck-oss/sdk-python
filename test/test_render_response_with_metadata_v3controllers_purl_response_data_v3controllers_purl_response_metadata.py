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

from vulncheck_sdk.models.render_response_with_metadata_v3controllers_purl_response_data_v3controllers_purl_response_metadata import RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata

class TestRenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata(unittest.TestCase):
    """RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata:
        """Test RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata`
        """
        model = RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata()
        if include_optional:
            return RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata(
                benchmark = 1.337,
                meta = vulncheck_sdk.models.v3controllers/purl_response_metadata.v3controllers.PurlResponseMetadata(
                    purl_struct = vulncheck_sdk.models.purl_struct.purl_struct(), 
                    timestamp = '', 
                    total_documents = 56, ),
                data = vulncheck_sdk.models.v3controllers/purl_response_data.v3controllers.PurlResponseData(
                    cves = [
                        ''
                        ], 
                    vulnerabilities = [
                        vulncheck_sdk.models.api/oss_package_vulnerability.api.OSSPackageVulnerability(
                            detection = '', 
                            fixed_version = '', )
                        ], )
            )
        else:
            return RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata(
        )
        """

    def testRenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata(self):
        """Test RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

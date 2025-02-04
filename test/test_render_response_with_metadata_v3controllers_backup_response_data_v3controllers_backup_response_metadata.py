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

from vulncheck_sdk.models.render_response_with_metadata_v3controllers_backup_response_data_v3controllers_backup_response_metadata import RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata

class TestRenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata(unittest.TestCase):
    """RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata:
        """Test RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata`
        """
        model = RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata()
        if include_optional:
            return RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata(
                benchmark = 1.337,
                meta = vulncheck_sdk.models.v3controllers/backup_response_metadata.v3controllers.BackupResponseMetadata(
                    index = '', 
                    timestamp = '', ),
                data = [
                    vulncheck_sdk.models.params/index_backup.params.IndexBackup(
                        date_added = '', 
                        filename = '', 
                        sha256 = '', 
                        url = '', 
                        url_ap_southeast_2 = '', 
                        url_eu_west_2 = '', 
                        url_expires = '', 
                        url_mrap = '', 
                        url_ttl_minutes = 56, 
                        url_us_east_1 = '', 
                        url_us_west_2 = '', )
                    ]
            )
        else:
            return RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata(
        )
        """

    def testRenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata(self):
        """Test RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

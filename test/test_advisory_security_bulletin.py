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

from vulncheck_sdk.models.advisory_security_bulletin import AdvisorySecurityBulletin

class TestAdvisorySecurityBulletin(unittest.TestCase):
    """AdvisorySecurityBulletin unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisorySecurityBulletin:
        """Test AdvisorySecurityBulletin
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisorySecurityBulletin`
        """
        model = AdvisorySecurityBulletin()
        if include_optional:
            return AdvisorySecurityBulletin(
                acknowledgement = '',
                bulletin_id = '',
                cve = [
                    ''
                    ],
                cvedetails = [
                    vulncheck_sdk.models.advisory/cve_detail.advisory.CVEDetail(
                        base_score = '', 
                        cveid = '', 
                        description = '', 
                        vector = '', )
                    ],
                date_added = '',
                hardware_updates = [
                    vulncheck_sdk.models.advisory/hardware_update.advisory.HardwareUpdate(
                        affected_versions = '', 
                        cves = [
                            ''
                            ], 
                        hardware_platform = '', 
                        system = '', 
                        updated_version = '', )
                    ],
                last_updated = '',
                link = '',
                revisions = [
                    vulncheck_sdk.models.advisory/nvidia_revision.advisory.NvidiaRevision(
                        date = '', 
                        description = '', 
                        revision = '', )
                    ],
                severity = '',
                software_updates = [
                    vulncheck_sdk.models.advisory/software_update.advisory.SoftwareUpdate(
                        affected_version = '', 
                        cves = [
                            ''
                            ], 
                        operating_system = '', 
                        software_product = '', 
                        updated_version = '', )
                    ],
                title = '',
                updated_at = ''
            )
        else:
            return AdvisorySecurityBulletin(
        )
        """

    def testAdvisorySecurityBulletin(self):
        """Test AdvisorySecurityBulletin"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

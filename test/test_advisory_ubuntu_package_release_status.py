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

from vulncheck_sdk.models.advisory_ubuntu_package_release_status import AdvisoryUbuntuPackageReleaseStatus

class TestAdvisoryUbuntuPackageReleaseStatus(unittest.TestCase):
    """AdvisoryUbuntuPackageReleaseStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisoryUbuntuPackageReleaseStatus:
        """Test AdvisoryUbuntuPackageReleaseStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisoryUbuntuPackageReleaseStatus`
        """
        model = AdvisoryUbuntuPackageReleaseStatus()
        if include_optional:
            return AdvisoryUbuntuPackageReleaseStatus(
                affected = True,
                fixed = True,
                fixed_version = '',
                lts = True,
                release = '',
                release_long = '',
                release_version = '',
                status = ''
            )
        else:
            return AdvisoryUbuntuPackageReleaseStatus(
        )
        """

    def testAdvisoryUbuntuPackageReleaseStatus(self):
        """Test AdvisoryUbuntuPackageReleaseStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

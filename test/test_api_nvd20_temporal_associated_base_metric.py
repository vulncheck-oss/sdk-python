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

from vulncheck_sdk.models.api_nvd20_temporal_associated_base_metric import ApiNVD20TemporalAssociatedBaseMetric

class TestApiNVD20TemporalAssociatedBaseMetric(unittest.TestCase):
    """ApiNVD20TemporalAssociatedBaseMetric unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiNVD20TemporalAssociatedBaseMetric:
        """Test ApiNVD20TemporalAssociatedBaseMetric
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiNVD20TemporalAssociatedBaseMetric`
        """
        model = ApiNVD20TemporalAssociatedBaseMetric()
        if include_optional:
            return ApiNVD20TemporalAssociatedBaseMetric(
                base_score = 1.337,
                source = '',
                type = ''
            )
        else:
            return ApiNVD20TemporalAssociatedBaseMetric(
        )
        """

    def testApiNVD20TemporalAssociatedBaseMetric(self):
        """Test ApiNVD20TemporalAssociatedBaseMetric"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

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

from vulncheck_sdk.models.render_response_with_metadata_array_advisory_beckman_coulter_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination

class TestRenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination(unittest.TestCase):
    """RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination:
        """Test RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination`
        """
        model = RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination()
        if include_optional:
            return RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination(
                benchmark = 1.337,
                meta = vulncheck_sdk.models.paginate/pagination.paginate.Pagination(
                    cursor = '', 
                    first_item = 56, 
                    index = '', 
                    last_item = 56, 
                    limit = 56, 
                    matches = [
                        vulncheck_sdk.models.paginate/match.paginate.Match(
                            field = '', 
                            value = '', )
                        ], 
                    max_pages = 56, 
                    next_cursor = '', 
                    opensearch_query = vulncheck_sdk.models.opensearch_query.opensearch_query(), 
                    order = '', 
                    page = 56, 
                    pages = [
                        ''
                        ], 
                    parameters = [
                        vulncheck_sdk.models.paginate/param.paginate.Param(
                            filtering = '', 
                            format = '', 
                            name = '', )
                        ], 
                    show_pages = True, 
                    show_query = True, 
                    sort = '', 
                    timestamp = '', 
                    total_documents = 56, 
                    total_pages = 56, 
                    warnings = [
                        ''
                        ], ),
                data = [
                    vulncheck_sdk.models.advisory/beckman_coulter.advisory.BeckmanCoulter(
                        cve = [
                            ''
                            ], 
                        date_added = '', 
                        summary = '', 
                        title = '', 
                        updated_at = '', 
                        url = '', )
                    ]
            )
        else:
            return RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination(
        )
        """

    def testRenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination(self):
        """Test RenderResponseWithMetadataArrayAdvisoryBeckmanCoulterPaginatePagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

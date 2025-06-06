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

from vulncheck_sdk.models.render_response_with_metadata_array_advisory_cnvd_flaw_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination

class TestRenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination(unittest.TestCase):
    """RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination:
        """Test RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination`
        """
        model = RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination()
        if include_optional:
            return RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination(
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
                    vulncheck_sdk.models.advisory/cnvd_flaw.advisory.CNVDFlaw(
                        affected_products_cn = '', 
                        bugtraq_id = '', 
                        cnvd = '', 
                        collection_time = '', 
                        cve = [
                            ''
                            ], 
                        date_added = '', 
                        harm_level = '', 
                        id = '', 
                        public_date = '', 
                        reference_urls = [
                            ''
                            ], 
                        submission_time = '', 
                        title_cn = '', 
                        update_time = '', 
                        updated_at = '', 
                        url = '', 
                        validation_info_cn = '', 
                        validation_info_en = '', 
                        vendor_patch_cn = '', 
                        vuln_attachments = [
                            ''
                            ], 
                        vuln_description_cn = '', 
                        vuln_solution_cn = '', 
                        vuln_type_cn = '', )
                    ]
            )
        else:
            return RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination(
        )
        """

    def testRenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination(self):
        """Test RenderResponseWithMetadataArrayAdvisoryCNVDFlawPaginatePagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

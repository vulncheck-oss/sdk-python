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

from vulncheck_sdk.models.advisory_siemens_advisory import AdvisorySiemensAdvisory

class TestAdvisorySiemensAdvisory(unittest.TestCase):
    """AdvisorySiemensAdvisory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdvisorySiemensAdvisory:
        """Test AdvisorySiemensAdvisory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdvisorySiemensAdvisory`
        """
        model = AdvisorySiemensAdvisory()
        if include_optional:
            return AdvisorySiemensAdvisory(
                csaf_url = '',
                cve = [
                    ''
                    ],
                cvrf_url = '',
                date_added = '',
                html_url = '',
                id = '',
                last_update = '',
                pdf_url = '',
                products = [
                    ''
                    ],
                ssa = vulncheck_sdk.models.advisory/ssa_source.advisory.SSASource(
                    document = vulncheck_sdk.models.advisory/siemens_document.advisory.SiemensDocument(
                        acknowledgments = [
                            vulncheck_sdk.models.advisory/siemens_acknowledgments.advisory.SiemensAcknowledgments(
                                names = [
                                    ''
                                    ], 
                                organization = '', 
                                summary = '', )
                            ], 
                        category = '', 
                        csaf_version = '', 
                        distribution = vulncheck_sdk.models.advisory/siemens_distribution.advisory.SiemensDistribution(
                            text = '', 
                            tlp = vulncheck_sdk.models.advisory/siemens_tlp.advisory.SiemensTLP(
                                label = '', ), ), 
                        notes = [
                            vulncheck_sdk.models.advisory/siemens_notes.advisory.SiemensNotes(
                                category = '', 
                                text = '', 
                                title = '', )
                            ], 
                        publisher = vulncheck_sdk.models.advisory/siemens_publisher.advisory.SiemensPublisher(
                            category = '', 
                            contact_details = '', 
                            name = '', 
                            namespace = '', ), 
                        references = [
                            vulncheck_sdk.models.advisory/siemens_references.advisory.SiemensReferences(
                                category = '', 
                                summary = '', 
                                url = '', )
                            ], 
                        title = '', 
                        tracking = vulncheck_sdk.models.advisory/siemens_tracking.advisory.SiemensTracking(
                            current_release_date = '', 
                            generator = vulncheck_sdk.models.advisory/siemens_generator.advisory.SiemensGenerator(
                                engine = vulncheck_sdk.models.advisory/siemens_engine.advisory.SiemensEngine(
                                    name = '', 
                                    version = '', ), ), 
                            id = '', 
                            initial_release_date = '', 
                            revision_history = [
                                vulncheck_sdk.models.advisory/siemens_revision_history.advisory.SiemensRevisionHistory(
                                    date = '', 
                                    legacy_version = '', 
                                    number = '', 
                                    summary = '', )
                                ], 
                            status = '', 
                            version = '', ), ), 
                    product_tree = vulncheck_sdk.models.advisory/siemens_product_tree.advisory.SiemensProductTree(
                        branches = [
                            vulncheck_sdk.models.advisory/siemens_branch.advisory.SiemensBranch(
                                category = '', 
                                name = '', )
                            ], ), 
                    vulnerabilities = [
                        vulncheck_sdk.models.advisory/siemens_vulnerability.advisory.SiemensVulnerability(
                            cve = '', 
                            cwe = vulncheck_sdk.models.advisory/siemens_cwe.advisory.SiemensCWE(
                                id = '', 
                                name = '', ), 
                            product_status = vulncheck_sdk.models.advisory/siemens_product_status.advisory.SiemensProductStatus(
                                known_affected = [
                                    ''
                                    ], ), 
                            remediations = [
                                vulncheck_sdk.models.advisory/siemens_remediation.advisory.SiemensRemediation(
                                    category = '', 
                                    details = '', 
                                    product_ids = [
                                        ''
                                        ], 
                                    url = '', )
                                ], 
                            scores = [
                                vulncheck_sdk.models.advisory/siemens_score.advisory.SiemensScore(
                                    cvss_v3 = vulncheck_sdk.models.advisory/siemens_cvssv3.advisory.SiemensCVSSV3(
                                        base_score = 1.337, 
                                        base_severity = '', 
                                        vector_string = '', 
                                        version = '', ), 
                                    products = [
                                        ''
                                        ], )
                                ], 
                            title = '', )
                        ], ),
                tags = [
                    ''
                    ],
                title = '',
                txt_url = '',
                updated_at = ''
            )
        else:
            return AdvisorySiemensAdvisory(
        )
        """

    def testAdvisorySiemensAdvisory(self):
        """Test AdvisorySiemensAdvisory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

"""
Measures of data quality
1) Validity - conforms to a schema
2) Accuracy - conforms to a gold standard(for example checking if address exists from our existing
                                        trusted data set)
3) Completeness - all records exist?
4) Consistency - Matches data from other records we must be the same
5) Uniformity - Same units for all values of a field

Blue Print for cleaning
1) Audit your data[Programmatically validate, Report for quality of data, run statistical analysis]
2)Create data cleaning plan[
                            1) Identifying causes
                            2) Operations to correct
                            3) test
                            ]
3) Execute plan
4) Manually Correct
5) Iterate this from step 1
"""

"""
https://www.interline.io/osm/extracts/
osm_extract_download --api-token=837cc7ce-82e1-48ce-8f67-90d7a1ca98a5 --data-format=pbf chennai_india
"""
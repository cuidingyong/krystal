import unittest
import HTMLReport

from scenarios.apiTesting import ApiTesting

api_test = unittest.TestLoader().loadTestsFromTestCase(ApiTesting)
test_suit = unittest.TestSuite([api_test])

runner = HTMLReport.TestRunner(report_file_name='krystal',
                               output_path='report',
                               verbosity=2,
                               title="choi's test",
                               description='choi',
                               thread_count=1,
                               sequential_execution=True
                               )

runner.run(test_suit)



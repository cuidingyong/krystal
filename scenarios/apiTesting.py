import unittest
import requests

from ddt import ddt, data, unpack

from library.getData import get_data


@ddt
class ApiTesting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @data(*get_data('api_data.xls'))
    @unpack
    def test01_post_topic(self, token, topic_id, title, tab, content, status):

        base_url = "http://192.168.117.117:3000/api/v1"
        json_data = {
            'accesstoken': token,
            'topic_id': topic_id,
            'title': title,
            'tab': tab,
            'content': content
        }
        result = requests.post(base_url + '/topics/update', json=json_data)
        assert result.status_code == int(status)

    def test02_post_replies(self):

    @classmethod
    def tearDownClass(cls):
        pass



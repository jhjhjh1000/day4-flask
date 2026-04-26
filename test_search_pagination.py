import unittest
import app as board_app


class SearchPaginationTest(unittest.TestCase):
    def setUp(self):
        board_app.app.config['TESTING'] = True
        self.client = board_app.app.test_client()

    def test_list_has_search_form(self):
        response = self.client.get('/')
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('name="q"', html)
        self.assertIn('검색', html)

    def test_search_filters_by_title_or_content(self):
        response = self.client.get('/?q=없는키워드')
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('검색 결과가 없습니다', html)

    def test_search_result_keeps_pagination(self):
        response = self.client.get('/?q=로컬&page=2')
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('/?page=1&amp;q=', html)
        self.assertIn('/?page=3&amp;q=', html)

    def test_list_has_sort_dropdown_with_default_latest(self):
        response = self.client.get('/')
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('name="sort"', html)
        self.assertIn('onchange="this.form.submit()"', html)
        self.assertIn('<option value="latest" selected>', html)

    def test_sort_keeps_with_search_and_pagination_links(self):
        response = self.client.get('/?q=로컬&sort=title&page=2')
        html = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('/?page=1&amp;q=', html)
        self.assertIn('&amp;sort=title', html)


if __name__ == '__main__':
    unittest.main()

from config.bootstrap import URL_PREFIX
from config.bootstrap import APP_KEY
from flask_testing import TestCase
import unittest
import main as flask_app

class test_karma(TestCase):

    def create_app(self):

        app = flask_app.app
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        return app

    def test_karma_send_ok(self):
        response = self.client.post(URL_PREFIX+'/karma/send',
                                    data={'team_id':'T89MU6P6G', 'user_id_from':'U8917CU0Y','user_id_target':'U8BHP3V1D'},
                                    headers={"X-App-Key": APP_KEY},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 200)

    def test_karma_send_not_enough(self):
        # Everyday Karma is 5
        for x in xrange(1,6):
            response = self.client.post(URL_PREFIX+'/karma/send',
                                        data={'team_id':'T89MU6P6G', 'user_id_from':'U8917CU0Y','user_id_target':'U8BHP3V1D'},
                                        headers={"X-App-Key": APP_KEY},
                                        content_type='application/x-www-form-urlencoded'
                                        )
            self.assertEqual(response.status_code, 200)

    def test_karma_send_error(self):
        response = self.client.post(URL_PREFIX+'/karma/send',
                                    data={'team_id':'T89MU6P6G', 'user_id_from':'U8917CU0Y'},
                                    headers={"X-App-Key": APP_KEY},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_karma_remaining_ok(self):
        response = self.client.post(URL_PREFIX+'/karma/remaining',
                                    data={'team_id':'T89MU6P6G', 'user_id':'U8917CU0Y'},
                                    headers={"X-App-Key": APP_KEY},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 200)

    def test_karma_remaining_error(self):
        response = self.client.post(URL_PREFIX+'/karma/remaining',
                                    data={'team_id':'T89MU6P6G'},
                                    headers={"X-App-Key": APP_KEY},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_leaderboard_ok(self):
        response = self.client.post(URL_PREFIX+'/leaderboard',
                                    data={'team_id':'T89MU6P6G'},
                                    headers={"X-App-Key": APP_KEY},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_error(self):
        response = self.client.post(URL_PREFIX+'/leaderboard',
                                    data={},
                                    headers={"X-App-Key": APP_KEY},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_headers_missing_token(self):
        response = self.client.post(URL_PREFIX+'/leaderboard',
                                    data={'team_id':'T89MU6P6G'},
                                    headers={},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 400)

    def test_headers_wrong_token(self):
        response = self.client.post(URL_PREFIX+'/leaderboard',
                                    data={'team_id':'T89MU6P6G'},
                                    headers={"X-App-Key": 'WRONGTOKEN'},
                                    content_type='application/x-www-form-urlencoded'
                                    )
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
import unittest
import requests
from flask import Flask
from views import *


app = Flask(__name__)
app.register_blueprint(views, url_prefix='')


class postyTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test(self):
        response = self.app.get('/posty')
        self.assertEqual(response.status_code, 200)


class albumyTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def test(self):
        response = self.app.get('/albumy')
        self.assertEqual(response.status_code, 200)


class iniTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)


class commentsTest(unittest.TestCase):
    def setUp(self):
         self.app = app.test_client()
    def test(self):
        response = self.app.get('/posty/1')
        self.assertEqual(response.status_code, 200)


class photosTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def test(self):
        response = self.app.get('/albumy/1')
        self.assertEqual(response.status_code, 200)


class get_postsNotNoneTest(unittest.TestCase):
    def test(self):
        DataToTest = get_posts()
        self.assertIsNotNone(DataToTest)


class get_postsExpectedCountTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        ExpectedData = response.json()
        DataToTest = get_posts()
        self.assertCountEqual(DataToTest,ExpectedData)


class get_postsExpectedDataTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        ExpectedData = response.json()
        DataToTest = get_posts()
        self.assertEqual(DataToTest,ExpectedData)


class get_post_by_idNotNoneTest(unittest.TestCase):
    def test(self):
        global dane
        get_posts()
        dataToTest = get_post_by_id(23)
        self.assertIsNotNone(dataToTest)


class get_post_by_idExpectedTitleTest(unittest.TestCase):
    def test(self):
        ExpectedTitle = "maxime id vitae nihil numquam"
        global dane
        get_posts()
        dataToTest = get_post_by_id(23)
        self.assertEqual(dataToTest['title'],ExpectedTitle)


class get_post_by_idExpectedUserIdTest(unittest.TestCase):
    def test(self):
        ExpectedUserId = 3
        global dane
        get_posts()
        dataToTest = get_post_by_id(23)
        self.assertEqual(dataToTest['userId'], ExpectedUserId)


class get_post_by_idExpectedIdTest(unittest.TestCase):
    def test(self):
        ExpectedId = 23
        global dane
        get_posts()
        dataToTest = get_post_by_id(23)
        self.assertEqual(dataToTest['id'], ExpectedId)


class get_post_by_idExpectedBodyTest(unittest.TestCase):
    def test(self):
        ExpectedBody = "veritatis unde neque eligendi\nquae quod architecto quo neque vitae\nest illo sit tempora doloremque fugit quod\net et vel beatae sequi ullam sed tenetur perspiciatis"
        global dane
        get_posts()
        dataToTest = get_post_by_id(23)
        self.assertEqual(dataToTest['body'], ExpectedBody)


class get_post_by_idNegativeInputTest(unittest.TestCase):
    def test(self):
        global dane
        get_posts()
        dataToTest = get_post_by_id(-1)
        self.assertIsNone(dataToTest)


class get_post_by_idVeryBigInputTest(unittest.TestCase):
    def test(self):
        global dane
        get_posts()
        dataToTest = get_post_by_id(99999)
        self.assertIsNone(dataToTest)


class get_post_commentsNotNoneTest(unittest.TestCase):
    def test(self):
        dataToTest = get_post_comments(23)
        self.assertIsNotNone(dataToTest)


class get_post_commentsExpectedCountTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts/23/comments"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_post_comments(23)
        self.assertCountEqual(dataToTest, ExpectedData)


class get_post_commentsExpectedDataTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts/23/comments"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_post_comments(23)
        self.assertEqual(dataToTest, ExpectedData)


class get_limited_postsNotNoneTest(unittest.TestCase):
    def test(self):
        dataToTest = get_limited_posts(10)
        self.assertIsNotNone(dataToTest)


class get_limited_postsExpectedDataTest(unittest.TestCase):
    def test(self):
        dataToTest = get_limited_posts(10)
        url = "https://jsonplaceholder.typicode.com/posts/"
        response = requests.get(url)
        ExpectedData = response.json()
        self.assertEqual(dataToTest[0], ExpectedData[0])


class get_limited_postsExpetedCountTest(unittest.TestCase):
    def test(self):
        dataToTest = get_limited_posts(10)
        self.assertEqual(len(dataToTest), 10)


class get_limited_postsNegativeInputTest(unittest.TestCase):
    def test(self):
        dataToTest = get_limited_posts(-9999)
        self.assertEqual(dataToTest,[])


class get_limited_postsVeryBigInputTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts/"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_limited_posts(999999)
        self.assertCountEqual(dataToTest, ExpectedData)


class get_filtered_postsNotNoneTest(unittest.TestCase):
    def test(self):
        dataToTest = get_filtered_posts(10,120)
        self.assertIsNotNone(dataToTest)


class get_filtered_postsExpectedCountTest(unittest.TestCase):
    def test(self):
        dataToTest = get_filtered_posts(10,120)
        self.assertEqual(len(dataToTest), 8)


class get_filtered_postsNegativeInputTest(unittest.TestCase):
    def test(self):
        dataToTest = get_filtered_posts(-9999, -120)
        self.assertEqual(dataToTest,[])


class get_filtered_postsVeryBigInputTest(unittest.TestCase):
    def test(self):
        dataToTest = get_filtered_posts(900000,999999)
        self.assertEqual(dataToTest,[])


class get_albumsNotNoneTest(unittest.TestCase):
    def test(self):
        dataToTest = get_albums()
        self.assertIsNotNone(dataToTest)


class get_albumsExpectedCountTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/albums"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_albums()
        self.assertCountEqual(dataToTest,ExpectedData)


class get_albumsExpectedDataTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/albums"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_albums()
        self.assertEqual(dataToTest,ExpectedData)


class get_album_by_idNotNoneTest(unittest.TestCase):
    def test(self):
        dataToTest = get_album_by_id(23)
        self.assertIsNotNone(dataToTest)


class get_album_by_idExpectedTitleTest(unittest.TestCase):
    def test(self):
        ExpectedTitle = "incidunt quisquam hic adipisci sequi"
        dataToTest = get_album_by_id(23)
        self.assertEqual(dataToTest['title'],ExpectedTitle)


class get_album_by_idExpectedUserIdTest(unittest.TestCase):
    def test(self):
        ExpectedUserId = 3
        dataToTest = get_album_by_id(23)
        self.assertEqual(dataToTest['userId'], ExpectedUserId)


class get_album_by_idExpectedIdTest(unittest.TestCase):
    def test(self):
        ExpectedId = 23
        dataToTest = get_album_by_id(23)
        self.assertEqual(dataToTest['id'], ExpectedId)


class get_photosNotNoneTest(unittest.TestCase):
    def test(self):
        dataToTest = get_photos(23)
        self.assertIsNotNone(dataToTest)


class get_photosExpectedCountTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/albums/23/photos"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_photos(23)
        self.assertCountEqual(dataToTest, ExpectedData)


class get_photosExpectedDataTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/albums/23/photos"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_photos(23)
        self.assertEqual(dataToTest, ExpectedData)


if __name__ == '__main__':
   unittest.main()

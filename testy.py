import unittest
import requests
from views import *



class get_postsTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        ExpectedData = response.json()
        DataToTest = get_posts()
        self.assertIsNotNone(DataToTest)
        self.assertEqual(DataToTest,ExpectedData)
        self.assertCountEqual(DataToTest,ExpectedData)


class get_post_by_idTest(unittest.TestCase):
    def test(self):
        ExpectedTitle = "maxime id vitae nihil numquam"
        ExpectedUserId = 3
        ExpectedId = 23
        ExpectedBody = "veritatis unde neque eligendi\nquae quod architecto quo neque vitae\nest illo sit tempora doloremque fugit quod\net et vel beatae sequi ullam sed tenetur perspiciatis"
        global dane
        get_posts()
        dataToTest = get_post_by_id(23)
        EdgeCase1 = get_post_by_id(-1)
        EdgeCase2 = get_post_by_id(99999)
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest['title'],ExpectedTitle)
        self.assertEqual(dataToTest['userId'], ExpectedUserId)
        self.assertEqual(dataToTest['id'], ExpectedId)
        self.assertEqual(dataToTest['body'], ExpectedBody)
        self.assertIsNone(EdgeCase1)
        self.assertIsNone(EdgeCase2)


class get_post_commentsTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts/23/comments"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_post_comments(23)
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest, ExpectedData)
        self.assertCountEqual(dataToTest, ExpectedData)



class get_limited_postsTest(unittest.TestCase):
    def test(self):
        dataToTest = get_limited_posts(10)
        url = "https://jsonplaceholder.typicode.com/posts/"
        response = requests.get(url)
        ExpectedData = response.json()
        EdgeCase1 = get_limited_posts(-9999)
        EdgeCase2 = get_limited_posts(999999)
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest[0], ExpectedData[0])
        self.assertEqual(len(dataToTest), 10)
        self.assertEqual(EdgeCase1,[])
        self.assertCountEqual(EdgeCase2, ExpectedData)




class get_filtered_postsTest(unittest.TestCase):
    def test(self):
        dataToTest = get_filtered_posts(10,120)
        url = "https://jsonplaceholder.typicode.com/posts/"
        response = requests.get(url)
        ExpectedData = response.json()
        EdgeCase1 = get_filtered_posts(-9999, -120)
        EdgeCase2 = get_filtered_posts(900000,999999)
        self.assertIsNotNone(dataToTest)
        self.assertEqual(len(dataToTest), 8)
        self.assertEqual(EdgeCase1,[])
        self.assertEqual(EdgeCase2,[])

class get_albumsTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/albums"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_albums()
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest,ExpectedData)
        self.assertCountEqual(dataToTest,ExpectedData)


class get_album_by_idTest(unittest.TestCase):
    def test(self):
        ExpectedTitle = "incidunt quisquam hic adipisci sequi"
        ExpectedUserId = 3
        ExpectedId = 23
        dataToTest = get_album_by_id(23)
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest['title'],ExpectedTitle)
        self.assertEqual(dataToTest['userId'], ExpectedUserId)
        self.assertEqual(dataToTest['id'], ExpectedId)


class get_photosTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/albums/23/photos"
        response = requests.get(url)
        ExpectedData = response.json()
        dataToTest = get_photos(23)
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest, ExpectedData)
        self.assertCountEqual(dataToTest, ExpectedData)


if __name__ == '__main__':
   unittest.main()

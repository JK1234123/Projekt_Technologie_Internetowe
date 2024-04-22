import unittest
import requests
from views import *


class get_postsTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        OriginalData = response.json()
        dataToTest = get_posts()
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest,OriginalData)
        self.assertCountEqual(dataToTest,OriginalData)


class get_albumsTest(unittest.TestCase):
    def test(self):
        url = "https://jsonplaceholder.typicode.com/albums"
        response = requests.get(url)
        OriginalData = response.json()
        dataToTest = get_albums()
        self.assertIsNotNone(dataToTest)
        self.assertEqual(dataToTest,OriginalData)
        self.assertCountEqual(dataToTest,OriginalData)





if __name__ == '__main__':
   unittest.main()


#get_album_by_id
#get_photos
#get_post_by_id
#get_post_comments
#get_limited_posts
#get_filtered_posts
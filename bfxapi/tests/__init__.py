import unittest
from .test_rest_serializers_and_types import TestRestSerializersAndTypes
from .test_websocket_serializers_and_types import TestWebsocketSerializersAndTypes
from .test_labeler import TestLabeler
from .test_notification import TestNotification

NAME = "tests"

def suite():
    return unittest.TestSuite([
        unittest.makeSuite(TestRestSerializersAndTypes),
        unittest.makeSuite(TestWebsocketSerializersAndTypes),
        unittest.makeSuite(TestLabeler),
        unittest.makeSuite(TestNotification),
    ])
    
if __name__ == "__main__":
    unittest.TextTestRunner().run(suite())
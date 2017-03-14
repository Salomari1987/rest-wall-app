from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Message

class MessageModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='someuser', first_name='some', last_name='user', email='s@example.com', password='simplepassword')
        self.message = Message(author=self.user, body='message body')

    def test_create_message(self):
        old_count = Message.objects.count()
        self.message.save()
        new_count = Message.objects.count()
        self.assertEqual(new_count-old_count, 1)
        self.assertNotEqual(new_count, old_count)

    def test_str_representation(self):
        self.assertEqual(unicode(self.message), self.message.body)

from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Message
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class MessageModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.message = Message(body='message body', author=self.user)

    def test_create_message(self):
        old_count = Message.objects.count()
        self.message.save()
        new_count = Message.objects.count()
        self.assertEqual(new_count-old_count, 1)
        self.assertNotEqual(new_count, old_count)

    def test_str_representation(self):
        self.assertEqual(unicode(self.message), self.message.body)


class MessageViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.message_data = {
            'body': 'my first message',
            'author': self.user.username
        }
        self.response_post = self.client.post(
            reverse('messages'),
            self.message_data,
            format='json'
        )
        self.response_get = self.client.get(
            reverse('messages'),
            format='json'
        )

    def test_api_create_message(self):
        self.assertEqual(self.response_post.status_code, status.HTTP_201_CREATED)

    def test_api_message_create_body(self):
        self.assertEqual(self.response_post.data["body"], self.message_data['body'])

    def test_api_get_messages(self):
        self.assertEqual(self.response_get.status_code, status.HTTP_200_OK)

    def test_api_get_messages_body(self):
        self.client.post(
            reverse('messages'),
            self.message_data,
            format='json'
        )
        response_get_all = self.client.get(
            reverse('messages'),
            format='json'
        )
        self.assertEqual(len(response_get_all.data), 2)
        self.assertEqual(response_get_all.data[1]['id'], 2)

from django.test import TestCase
from .models import Post
from django.urls import reverse
from django.contrib.auth import get_user_model


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@test.com",
            password="secret",
        )
        cls.post = Post.objects.create(
            title="test title",
            content="test content",
            author=cls.user
        )

    def test_model_content(self):
        self.assertEqual(self.post.title, "test title")
        self.assertEqual(self.post.content, "test content")

    def test_homepage(self):  # new
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "test title")

    def test_post_listview(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk':self.post.pk}))
        no_response = self.client.get('/post/12345/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_model(self):
        self.assertEqual(self.post.title, "test title")
        self.assertEqual(self.post.content, "test content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "test title")
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
from django.test import TestCase
from .models import Post
from django.urls import reverse


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            title="test title",
            content="test content"
        )

    def test_model_content(self):
        self.assertEqual(self.post.title, "test title")
        self.assertEqual(self.post.content, "test content")

    def test_homepage(self):  # new
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "test title")


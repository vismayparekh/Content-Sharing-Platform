from django.test import TestCase
from django.urls import reverse
from .models import Article

class ArticleViewsTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Test Article',
            content='This is a test article content.',
            author='Test Author'
        )

    def test_article_list_view(self):
        response = self.client.get(reverse('article-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles.html')

    def test_article_detail_view(self):
        response = self.client.get(reverse('article-detail', args=[self.article.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'article_detail.html')

    def test_article_create_view(self):
        new_article_data = {
            'title': 'New Article',
            'content': 'This is a new article content.',
            'author': 'New Author'
        }
        response = self.client.post(reverse('article-create'), new_article_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation

    def test_article_update_view(self):
        updated_article_data = {
            'title': 'Updated Article',
            'content': 'This is an updated article content.',
            'author': 'Updated Author'
        }
        response = self.client.post(reverse('article-update', args=[self.article.pk]), updated_article_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful update

    def test_article_delete_view(self):
        response = self.client.post(reverse('article-delete', args=[self.article.pk]))
        self.assertEqual(response.status_code, 302)  # Redirects after successful deletion

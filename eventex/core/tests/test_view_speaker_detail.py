from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.core.models import Speaker

class SpeakerDetailGet(TestCase):
    def setUp(self):
        Speaker.objects.create(
            name='Grace Hopper',
            slug='grace-hopper',
            photo='https://blogdaengenharia.com/wp-content/uploads/grace-hopper-blog-da-engenharia-4.jpg',
            website='https://pt.wikipedia.org/wiki/Grace_Hopper',
            description='Programadora e Almirante'
        )
        self.response = self.client.get(r('speaker_detail', slug='grace-hopper'))
        
    def test_get(self):
        """GET should return status 200"""
        self.assertEqual(200, self.response.status_code)

    def test_templates(self):
        self.assertTemplateUsed(self.response, 'core/speaker_detail.html')

    def test_html(self):
        content = [
            'Grace Hopper',
            'Programadora e Almirante',
            'https://blogdaengenharia.com/wp-content/uploads/grace-hopper-blog-da-engenharia-4.jpg',
            'https://pt.wikipedia.org/wiki/Grace_Hopper'
        ]

        for expected in content:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_context(self):
        """Speaker must be in context"""
        speaker = self.response.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(r('speaker_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)

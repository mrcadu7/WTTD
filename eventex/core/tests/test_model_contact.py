from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        
        self.speaker = Speaker.objects.create(
            name='Cadu Potatoes',
            slug='cadu-potatoes',
            photo='https://l1nq.com/Teqb7'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL,
                                         value='cadu@cadu.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE,
                                         value='21-982978431')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='cadu@cadu.com')
        self.assertEqual('cadu@cadu.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Cadu Potatoes',
            slug='cadu-potatoes',
            photo='https://l1nq.com/Teqb7'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='cadu@cadu.com')
        s.contact_set.create(kind=Contact.PHONE, value='21-982978431')
        
    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['cadu@cadu.com']
        self.assertQuerySetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['21-982978431']
        self.assertQuerySetEqual(qs, expected, lambda o: o.value)

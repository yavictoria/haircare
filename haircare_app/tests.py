from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase

from .models import AIChatMessage, HairProfile, JournalEntry


class HairProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
        )

    def test_hair_profile_str(self):
        profile = HairProfile.objects.create(
            user=self.user,
            nickname='Vika',
            hair_type='wavy',
            hair_length='medium',
            porosity='medium',
            brittleness='mild',
        )
        self.assertEqual(str(profile), "Vika's Hair Profile")

    def test_hair_profile_dyed_defaults_to_false(self):
        profile = HairProfile.objects.create(
            user=self.user,
            nickname='Vika',
            hair_type='straight',
            hair_length='short',
            porosity='low',
            brittleness='none',
        )
        self.assertFalse(profile.dyed)


class JournalEntryTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='journaluser',
            password='testpass123',
        )

    def test_journal_entry_str(self):
        entry = JournalEntry.objects.create(
            user=self.user,
            entry_type='wash',
            notes='Morning wash',
            date=date(2026, 5, 15),
        )
        self.assertEqual(
            str(entry),
            f'{self.user.username} - wash (2026-05-15)',
        )


class AIChatMessageTests(TestCase):
    def test_ai_chat_message_creation(self):
        user = User.objects.create_user(
            username='aiuser',
            password='testpass123',
        )
        message = AIChatMessage.objects.create(
            user=user,
            user_text='How often should I wash curly hair?',
            ai_text='1-2 times per week.',
        )
        self.assertEqual(message.user_text, 'How often should I wash curly hair?')
        self.assertEqual(message.ai_text, '1-2 times per week.')

    def test_ai_chat_message_str_contains_username(self):
        user = User.objects.create_user(
            username='aiuser',
            password='testpass123',
        )
        message = AIChatMessage.objects.create(
            user=user,
            user_text='Hello',
            ai_text='Hi there',
        )
        self.assertIn('aiuser', str(message))

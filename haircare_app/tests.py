from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import HairProfile, JournalEntry

class HairCareSimpleTests(TestCase):
    def setUp(self):
        # Створюємо тестового користувача для тестів, де потрібна авторизація
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client = Client()

    # 1. Тест доступності головної сторінки (Welcome page)
    def test_welcome_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # 2. Тест сторінки логіну
    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    # 3. Тест створення профілю волосся (Model test)
    def test_hair_profile_creation(self):
        profile = HairProfile.objects.create(
            user=self.user,
            hair_type='Straight',
            porosity='Low',
            thickness='Medium'
        )
        self.assertEqual(profile.hair_type, 'Straight')
        self.assertEqual(HairProfile.objects.count(), 1)

    # 4. Тест створення запису в журналі (Journal test)
    def test_journal_entry_creation(self):
        entry = JournalEntry.objects.create(
            user=self.user,
            title='Мій перший догляд',
            content='Використала новий бальзам'
        )
        self.assertEqual(entry.title, 'Мій перший догляд')
        self.assertEqual(JournalEntry.objects.count(), 1)

    # 5. Тест редіректу (якщо неавторизований юзер йде в профіль)
    def test_profile_redirect_if_not_logged_in(self):
        # Оскільки сторінка профілю зазвичай закрита @login_required
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302) # Має бути перенаправлення на сторінку логіну

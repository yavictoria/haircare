import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'haircare.settings')
django.setup()

from haircare_app.models import Recommendation

def run():
    recommendations = [
        {
            "title": "Мийте волосся 2 рази на тиждень",
            "description": "Для хвилястого волосся рекомендується мити голову двічі на тиждень, щоб підтримувати баланс зволоження.",
            "hair_type": "wavy",
            "category": "daily"
        },
        {
            "title": "Використовуйте легкі кондиціонери",
            "description": "Легкі кондиціонери допомагають зберегти структуру хвилястого волосся без перевантаження.",
            "hair_type": "wavy",
            "category": "daily"
        },
        {
            "title": "Використовуйте маски для волосся раз на тиждень",
            "description": "Маски зволожують і живлять волосся, допомагають зберегти хвилі визначеними.",
            "hair_type": "wavy",
            "category": "weekly"
        },
        {
            "title": "Уникайте надмірного сушіння феном",
            "description": "Надмірне сушіння може зробити хвилясте волосся сухим та ламким. Використовуйте холодне повітря або сушіть природньо.",
            "hair_type": "wavy",
            "category": "longterm"
        },
        {
            "title": "Використовуйте гребінець із широкими зубцями",
            "description": "Гребінець з широкими зубцями допомагає уникнути пушистості і пошкоджень хвилястого волосся.",
            "hair_type": "wavy",
            "category": "daily"
        },
        {
            "title": "Захищайте волосся від ультрафіолету",
            "description": "Використовуйте засоби з SPF, щоб захистити волосся від сонця та зберегти його здоровим.",
            "hair_type": "wavy",
            "category": "longterm"
        },
    ]

    for rec in recommendations:
        Recommendation.objects.create(**rec)
        print(f"Додано: {rec['title']}")

if __name__ == '__main__':
    run()

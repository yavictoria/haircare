from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm, HairProfileForm
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import HairProfile
from django.shortcuts import render, redirect, get_object_or_404
from .models import JournalEntry
from .forms import JournalEntryForm
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    hair_profile = getattr(request.user, 'hairprofile', None)

    # Генерація рекомендацій на основі HairProfile
    recommendations = []

    if hair_profile:
        # Рекомендації для типу волосся
        if hair_profile.hair_type == "curly":
            recommendations.append("Ваше волосся кучеряве, тому мийте його 1-2 рази на тиждень, щоб уникнути сухості.")
            recommendations.append("Використовуйте маски для волосся раз на тиждень для додаткового зволоження.")
        elif hair_profile.hair_type == "straight":
            recommendations.append("Ваше волосся пряме, тому мийте його 2-3 рази на тиждень.")
            recommendations.append("Використовуйте легкі кондиціонери, щоб уникнути завантаження волосся.")

        # Рекомендації для довжини волосся
        if hair_profile.hair_length == "long":
            recommendations.append("Через довжину волосся рекомендується використовувати несмивні засоби для захисту кінчиків.")
        elif hair_profile.hair_length == "short":
            recommendations.append("Коротке волосся можна мити частіше, 3-4 рази на тиждень.")

        # Рекомендації для пористості
        if hair_profile.porosity == "high":
            recommendations.append("Ваше волосся має високу пористість, тому використовуйте зволожуючі маски та олії.")
        elif hair_profile.porosity == "low":
            recommendations.append("Ваше волосся має низьку пористість, тому уникайте важких продуктів, які можуть завантажувати волосся.")

        # Рекомендації для ламкості
        if hair_profile.brittleness == "high":
            recommendations.append("Ваше волосся схильне до ламкості, тому уникайте гарячих інструментів, таких як фен або праска.")
        elif hair_profile.brittleness == "mild":
            recommendations.append("Ваше волосся має помірну ламкість, тому використовуйте термозахисні засоби під час сушіння феном.")

        # Рекомендації для фарбованого волосся
        if hair_profile.dyed:
            recommendations.append("Ваше волосся фарбоване, тому використовуйте спеціальні шампуні для фарбованого волосся.")
        else:
            recommendations.append("Ваше волосся не фарбоване, тому ви можете використовувати звичайні засоби для догляду.")

        # Нові рекомендації

        # Частота миття голови
        if hair_profile.hair_type == "curly":
            recommendations.append("Рекомендується мити голову 1-2 рази на тиждень.")
        elif hair_profile.hair_type == "straight":
            recommendations.append("Рекомендується мити голову 2-3 рази на тиждень.")
        elif hair_profile.hair_type == "wavy":
            recommendations.append("Рекомендується мити голову 2 рази на тиждень.")

        # Скрабування шкіри голови
        if hair_profile.porosity == "high":
            recommendations.append("Скрабуйте шкіру голови раз на тиждень для видалення відмерлих клітин.")
        elif hair_profile.porosity == "low":
            recommendations.append("Скрабування шкіри голови не є обов'язковим, але можна робити це раз на 2 тижні.")

        # Частота нанесення масок
        if hair_profile.hair_type == "curly":
            recommendations.append("Використовуйте маски для волосся раз на тиждень.")
        elif hair_profile.hair_type == "straight":
            recommendations.append("Використовуйте маски для волосся раз на тиждень або двічі на тиждень, якщо волосся сухе.")

        # Використання фена
        if hair_profile.brittleness == "high":
            recommendations.append("Уникайте використання фена. Якщо це необхідно, використовуйте термозахисні засоби.")
        elif hair_profile.brittleness == "mild":
            recommendations.append("Використовуйте фен з обережністю, завжди з термозахисними засобами.")

        # Рекомендовані засоби
        if hair_profile.porosity == "high":
            recommendations.append("Використовуйте зволожуючі шампуні та кондиціонери.")
        elif hair_profile.porosity == "low":
            recommendations.append("Використовуйте легкі шампуні без сульфатів.")

        # Тип розчісування
        if hair_profile.hair_type == "curly":
            recommendations.append("Використовуйте гребінець із широкими зубцями для розчісування.")
        elif hair_profile.hair_type == "straight":
            recommendations.append("Використовуйте щітку з натуральної щетини для розчісування.")
        recommendations.append("Не розчісуйте волосся мокрим, щоб уникнути пошкоджень.")

        # Додатковий догляд
        recommendations.append("Робіть масаж голови для покращення кровообігу.")
        if hair_profile.hair_type == "curly":
            recommendations.append("Використовуйте нічний догляд, наприклад, шовкові наволочки або олії для кінчиків.")
        elif hair_profile.hair_type == "straight":
            recommendations.append("Використовуйте сироватки для блиску волосся.")

    return render(request, 'home.html', {
        'hair_profile': hair_profile,
        'recommendations': recommendations,
    })


def welcome(request):
    return render(request, 'welcome.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def profile(request):
    """Редагування профілю без виходу зі сторінки після збереження"""
    hair_profile, created = HairProfile.objects.get_or_create(user=request.user)  # Отримуємо або створюємо профіль

    if request.method == 'POST':
        form = HairProfileForm(request.POST, instance=hair_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")  # Повідомлення про збереження
    else:
        form = HairProfileForm(instance=hair_profile)

    return render(request, 'profile.html', {'form': form})


def welcome_view(request):
    if request.user.is_authenticated:
        return redirect('profile')  # Перенаправляємо, якщо вже увійшов
    return render(request, 'welcome.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def journal_list(request):
    entries = JournalEntry.objects.filter(user=request.user).order_by('-date')
    return render(request, 'journal_list.html', {'entries': entries})

@login_required
def journal_add(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('journal_list')
    else:
        form = JournalEntryForm()
    return render(request, 'journal_form.html', {'form': form})

@login_required
def journal_delete(request, pk):
    entry = get_object_or_404(JournalEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('journal_list')
    return render(request, 'journal_confirm_delete.html', {'entry': entry})


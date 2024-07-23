from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from tgapi.models import Ads
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@receiver(post_save, sender=Ads)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(
            user=instance.user,
            username_tg=instance.username_tg,
            contact_phone=instance.contact_phone,
            contact_name=instance.contact_name
        )

@login_required
def profile(request):
    return render(request, 'prof/profile.html')


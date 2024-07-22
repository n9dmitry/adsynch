from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    ads = Ads.objects.filter(user=instance)

    username_tg = None
    if ads.exists():
        username_tg = ads.first().username_tg

    # Проверяем, существует ли профиль пользователя
    if hasattr(instance, 'userprofile'):
        instance.userprofile.username_tg = username_tg
        instance.userprofile.save()
    else:
        # Создаем профиль, если его не существует
        UserProfile.objects.create(user=instance, name=instance.username, email=instance.email, username_tg=username_tg)


        instance.userprofile.name = instance.username
        instance.userprofile.email = instance.email
        instance.userprofile.username_tg = username_tg
        instance.userprofile.save()


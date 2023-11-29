from .models import User, UserProfile


class UserService:
    @staticmethod
    def create_user(create_username: str, user_chat_id: str):
        check_user = UserProfile.objects.filter(user_telegram_chat_id=user_chat_id)
        if not check_user:
            user_profile = UserProfile(user_telegram_chat_id=user_chat_id)
            user_profile.save()
            new_user = User(username=create_username, profile=user_profile)
            new_user.save()
        else:
            raise ValueError("Ошибка! Пользователь уже зарегистрирован в системе")

    @staticmethod
    def get_all_tennis_users() -> list:
        return User.objects.all().filter('profile.user_rating')

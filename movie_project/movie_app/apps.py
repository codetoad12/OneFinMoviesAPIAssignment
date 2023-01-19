from django.apps import AppConfig


class MovieAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movie_app'

    def ready(self) -> None:
        import movie_app.signals
       
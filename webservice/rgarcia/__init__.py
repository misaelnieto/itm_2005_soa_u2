from . import recipe_service

wsgi_apps = {
    'recetas': recipe_service.wsgi_app,
}
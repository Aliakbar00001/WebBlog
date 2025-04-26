class FilterUnauthUsers:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Здесь твоя логика
        if not request.user.is_authenticated and not request.path.startswith('/login') and not request.path.startswith('/signup'):
            from django.shortcuts import redirect
            return redirect('login')  # или куда тебе надо редиректить
        response = self.get_response(request)
        return response

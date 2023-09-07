def theme(request):
    if 'is_dark_theme' in request.session:
        is_dark_theme = request.session.get('is_dark_theme')
        return {'is_dark_theme':is_dark_theme}
    return {'is_dark_theme': False}

def colortheme(request):
    if 'color_theme' in request.session:
        color_theme = request.session.get('color_theme')
        return {'color_theme':color_theme}
    return {'color_theme': False}

def defaulttheme(request):
    if 'original_theme' in request.session:
        original_theme = request.session.get('original_theme')
        return {'original_theme':original_theme}
    return {'original_theme': False}

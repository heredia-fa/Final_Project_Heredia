from django.shortcuts import redirect


class Login_staff(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        
        return redirect('landing_news:landing')
                
                
        
    
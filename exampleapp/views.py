from django.views import View
from django.shortcuts import render


class ExampleView(View):
    template_name = 'test.html'
    def get(self, request):
        return render(request, self.template_name)

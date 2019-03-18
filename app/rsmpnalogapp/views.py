import re
import json
#
from urllib.parse import urlencode
from urllib.request import Request, urlopen
#
from django.views.generic.edit import FormView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy, reverse
from django import forms


def validate_inn_or_ogrn(value):
    p = re.compile('^[0-9]{9,15}$')
    if not p.match(value):
        raise ValidationError(u'Вы ввели не ИНН/ОГРН')

class Form_check_business_entity(forms.Form):
    inn_or_ogrn = forms.CharField(
        label='', 
        help_text='Введите ИНН или ОГРН', 
        max_length=15, 
        required=True,
        validators=[validate_inn_or_ogrn]
        )


class Check_business_entity(FormView):
    template_name = 'app/rsmpnalogapp/check_business_entity.html'
    form_class = Form_check_business_entity

    def send_post_to_rmsp_nalog(self, inn_or_ogrn):
        # Set destination URL here
        url = 'https://rmsp.nalog.ru/search-proc.json' 
        # Set POST fields here
        post_fields = {
            'query': str(inn_or_ogrn),
            }     
        request = Request(url, urlencode(post_fields).encode())
        jdata = json.loads(urlopen(request).read().decode())
        return jdata


    def transform_category(self, dictdata):
        if dictdata['category']==1:
            dictdata['category'] = 'Микропредприятие'
        elif dictdata['category']==2:
            dictdata['category'] = 'Малое предприятие'
        elif dictdata['category']==3:
            dictdata['category'] = 'Среднее предприятие'
        return dictdata


    def dispatch(self, request, *args, **kwargs):
        #self.request.session['cart']=list()
        return super(Check_business_entity, self).dispatch(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super(Check_business_entity, self).get_context_data(**kwargs)
        if 'cart' in self.request.session:
            context['data'] = self.request.session['cart']
        return context


    def form_valid(self, form):
        cd = form.cleaned_data
        data = self.send_post_to_rmsp_nalog(cd['inn_or_ogrn'])['data']
        if len(data) == 1:
            data = data[0]
            data = self.transform_category(data)
            dict_data = {'data':data, 'status':True}
        else:
            dict_data = {'data':'Введите ИНН/ОГРН корректно', 'status':False}
        if 'cart' in self.request.session:
            self.request.session['cart']=list() # Если в сессии что то было, отчищаем
        self.request.session['cart']=dict_data
        return super(Check_business_entity, self).form_valid(form)


    def get_success_url(self):
        return reverse_lazy('check_business_entity')

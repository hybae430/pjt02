from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
    
        # 다른 폼을 상속 받아서 쓰는 경우라면 super를 이용해 상위 클래스의 생성자를 호출해주도록 한다. 그렇지 않다면 아래 super로 시작하는 줄은 필요없다.
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['username'].widget.attrs.update({'placeholder': '아이디'})
        self.fields['email'].widget.attrs.update({'placeholder': '이메일'})
        self.fields['password1'].widget.attrs.update({'placeholder': '비밀번호'})
        self.fields['password2'].widget.attrs.update({'placeholder': '비밀번호 확인'})

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields

class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
    
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['username'].widget.attrs.update({'placeholder': '아이디를 입력해주세요.'})
        self.fields['password'].widget.attrs.update({'placeholder': '비밀번호를 입력해주세요.'})
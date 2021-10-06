from .models import Post
from django import forms



class PostForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):

        super(PostForm,self).__init__(*args,**kwargs)

        for item in self.fields.keys():
            self.fields[item].widget.attrs.update({
                'class':'form-control',
            })

    class Meta:
                model = Post
                fields = ['title','content']
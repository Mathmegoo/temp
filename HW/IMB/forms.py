from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import Articles, Comments



class ArticlesForm(ModelForm):
    class Meta:
        model = Articles

class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        include = ['article_id',]
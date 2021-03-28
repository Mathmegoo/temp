from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy 


import config as config


app = Flask(__name__, template_folder='HW/templates.home.txt')
app.config.from_object(config)

db = SQLAlchemy(app)





#----------------------------------------------------------

@app.route('/', methods = ['GET', 'POST'])
def index():
    from models import Articles, Comments
    from forms import ArticlesForm, CommentsForm

    if request.method == 'POST':
        print(request.form)
        us_form = ArticlesForm(request.form)


        if us_form.validate():
            post_art = Articles(**us_form.data)
            db.session.add(post_art)
            db.session.commit()
            
            return 'Article was created'
        else:
            us_form = CommentsForm(request.form)
            
            if us_form.validate():
                post_com = Comments(**us_form.data)
                db.session.add(post_com)
                db.session.commit()
                return 'Commit was created'
            else:
                raise Exception
    if request.method == 'GET':
        vie_posts = Articles.query.all()
        return render_template('home.txt', posts = vie_posts)
        







if __name__ == '__main__':

    from models import *
    from models import Articles
    db.create_all() 
    
    app.run()
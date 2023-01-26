from flask import render_template, url_for, request, redirect
from models import db, Users
from flask import Flask
from datetime import datetime
import sys
from flask import  session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RS'
db.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/browse', methods=['GET', 'POST'])
def browse():
    page = request.args.get('page', 1, type=int)
    if not page:
        page = 1
    users = Users.query.paginate(page=page, per_page=5)
    
    return render_template('browse.html', users=users)



@app.route('/searchResults1', methods=['GET', 'POST'])
def searchResults1():
    # users = Users.query.all()
    # return render_template('searchResults.html',users=users)
        # issearch = request.args.get('issearch', 'no', type=str)
        # if issearch == 'yes':
            # InvoiceNumber = request.form['InvoiceNumber']
            # Instructor=request.form['Instructor']
            # AdminKey=request.form['AdminKey']
            # Institution=request.form['Institution']
            # print('search resulttttttttttttttttttttttt',request.form, file=sys.stdout)
            # users = Users.query.where((Users.AdminKey == AdminKey)|
                                    # (Users.Instructor== Instructor) |(Users.Institution== Institution)|
                                    # (Users.InvoiceNumber== InvoiceNumber))
        
            # return render_template('searchResults.html', users=users)
        # else:
        if 'InvoiceNumber' in session:
            InvoiceNumber = session['InvoiceNumber']
            print('search resulttttttttttttttttttttttt',file=sys.stdout)
        elif request.method == 'GET':
            InvoiceNumber = request.args.get('InvoiceNumber', '', type=str)
            session['InvoiceNumber'] = InvoiceNumber
            
        if 'Instructor' in session:
            Instructor = session['Instructor']
            print('search resulttttttttttttttttttttttt',file=sys.stdout)
        elif request.method == 'GET':
            Instructor = request.args.get('Instructor', '', type=str)
            session['Instructor'] = Instructor
            
        if 'AdminKey' in session:
            AdminKey = session['AdminKey']
            print('search resulttttttttttttttttttttttt',file=sys.stdout)
        elif request.method == 'GET':
            AdminKey = request.args.get('AdminKey', '', type=str)
            session['AdminKey'] = AdminKey
            
        if 'Institution' in session:
            Institution = session['Institution']
            print('search resulttttttttttttttttttttttt',file=sys.stdout)
        elif request.method == 'GET':
            Institution = request.args.get('Institution', '', type=str)
            session['Institution'] = Institution
            
        page = request.args.get('page', 1, type=int)
            # if not page:
                # page = 1
        users = None
        try:
            users = Users.query.where((Users.AdminKey == AdminKey)|#.filter(MyTable.name.like('%' + name + '%'))\
                                     (Users.Instructor== Instructor) & (Users.Institution== Institution)&
                                     (Users.InvoiceNumber== InvoiceNumber)).paginate(page=page, per_page=5)
        except:
            return render_template('noresults.html')
        if users:
            print("paged",Institution,file=sys.stdout)
            #users = Users.query.paginate(page=page, per_page=3)
            return render_template('searchResults.html',users=users)
        else:
            print("not found",Institution,file=sys.stdout)
            return render_template('noresults.html')
            
        
    #return render_template('browse.html', users=users)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    id  = request.args.get('id', None)
    goback  = request.args.get('goback', None)
    users = Users.query.get_or_404(id)
    print('user',request.form, file=sys.stdout)
    if request.form: 
        print('user',request.form, file=sys.stdout)
        users.InvoiceNumber=request.form['InvoiceNumber']
        users.Institution=request.form['Institution']
        users.InvoiceDate=datetime.strptime(request.form['InvoiceDate'], "%m/%d/%Y").date() 
        users.Instructor=request.form['Instructor']
        users.AdminKey=request.form['AdminKey']
        users.Email=request.form['Email']
        users.Usercode=request.form['Usercode']
        users.AdminCount=request.form['AdminCount']
        users.site_license_checkbox=request.form['site_license_checkbox']
        users.site_license_date=datetime.strptime(request.form['site_license_date'], "%m/%d/%Y").date() 
        users.reflection_checkbox=request.form['reflection_checkbox']
        users.custom_message_checkbox=request.form['custom_message_checkbox']
        users.custom_message=request.form['custom_message']
        users.show_extra_questions= request.form['show_extra_questions']
        users.Q91=request.form['Q91']
        users.Q92=request.form['Q92']
        db.session.commit()
        if goback=='no':
            return redirect(url_for('edit',id=id,goback='no'))
        else: 
            return redirect(url_for('browse'))
    return render_template('edit.html', users=users)
@app.route('/delete/<id>', methods=['GET','POST'])
def delete(id):
    user= Users.query.get_or_404(id)
    #print('user',user, file=sys.stdout)
    if request.method == 'POST' or request.method == 'GET':
        if user != None:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('browse'))
        return render_template('404.html')
    
@app.route('/add', methods=['GET','POST'])
def add():
    goback  = request.args.get('goback', None)
    if request.form: 
        new_user = Users(
        InvoiceNumber=request.form['InvoiceNumber'],
        Institution=request.form['Institution'],
        InvoiceDate=datetime.strptime(request.form['InvoiceDate'], "%m/%d/%Y").date() ,
        Instructor=request.form['Instructor'],
        AdminKey=request.form['AdminKey'],
        Email=request.form['Email'],
        Usercode=request.form['Usercode'],
        AdminCount=request.form['AdminCount'],
        site_license_checkbox=request.form['site_license_checkbox'],
        site_license_date= datetime.strptime(request.form['site_license_date'], "%m/%d/%Y").date(),
        reflection_checkbox =request.form['reflection_checkbox'],
        custom_message_checkbox = request.form['custom_message_checkbox'],
        custom_message=request.form['custom_message'],
        show_extra_questions=request.form['show_extra_questions'],
        Q91=request.form['Q91'],
        Q92=request.form['Q92']
        )
        db.session.add(new_user)
        db.session.commit()
        if goback=='no':
            return redirect(url_for('add',goback='no'))
        else: 
            return redirect(url_for('browse'))
    return render_template('add.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404

@app.before_first_request
def create_table():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')



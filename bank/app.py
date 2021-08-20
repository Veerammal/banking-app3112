from flask import  Flask,render_template,url_for,redirect,request,flash

from flask_mysqldb import MySQL
app = Flask(__name__,template_folder='template')

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="sql123"
app.config["MYSQL_DB"]="mybank"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(app)

@app.route("/")
def topic():
    return render_template("topic.html")
     
#home page
@app.route("/home")
def home():
    return render_template("home.html")
     
#Loading TABLE page
@app.route("/table")
def table():
    con=mysql.connection.cursor()
    sql="SELECT*FROM user"
    con.execute(sql)
    res=con.fetchall()
    return render_template("table.html",datas=res)

@app.route("/view/<string:CUSTOMER>")
def view(CUSTOMER):
     return render_template("edituser.html",CUSTOMER=CUSTOMER)
     
#update User
@app.route("/edituser/<string:CUSTOMER>",methods=['GET','POST'])
def edituser(CUSTOMER):

        con=mysql.connection.cursor()
        if request.method=='POST':
        
            Sender=request.form['sender']
            Receiver=request.form['receiver']
            Amount=request.form['amount']
            sql="select Balance from user where CUSTOMER=%s"
            con.execute(sql,[CUSTOMER])
            result=con.fetchone()
            currbal=result["Balance"]
            if int(currbal)>=int(Amount):
                sql="insert into Transfer(Sender,Receiver,Amount) values(%s ,%s ,%s)"
                con.execute(sql,[Sender,Receiver,Amount])
                mysql.connection.commit()
                
                sql="update user set Balance=Balance-%s where CUSTOMER=%s"
                con.execute(sql,[Amount,Sender])
                sql="update user set Balance=Balance+%s where CUSTOMER=%s"
                con.execute(sql,[Amount,Receiver])
                mysql.connection.commit()
               
                
    
                sql="select * from user where CUSTOMER=%s"
                con.execute(sql,[CUSTOMER])
                res=con.fetchone()
                con.close()
                return render_template("view.html",data=res)
            else:
                con.close() 
                return render_template("message.html")      

@app.route("/transferhistory")
def transferhistory():
        con=mysql.connection.cursor()
        sql="SELECT*FROM Transfer"
        con.execute(sql)
        res=con.fetchall()
        return render_template("transferhistory.html",datas=res)
                     


    
if(__name__=='__main__'):
    app.secret_key="abc123"
    app.run(debug=True)

from flask import Flask,render_template,flash, redirect,url_for,session,request
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
from sqlalchemy import create_engine, types
from sqlalchemy.types import Integer
from dateutil.parser import parse

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'

app.config['SECRET_KEY'] = 'super secret key'

Base = declarative_base()
 
@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_csv_file = request.files["file"]
        
         # enter your password and database names here and you can also replace with your table name from grafanatesting
        engine = create_engine('mysql://root:Vishal@26@localhost/grafanatesting')

        df = pd.read_csv(user_csv_file,error_bad_lines=False, dtype=object)
        column_list = list(df)

        df['Date']=pd.to_datetime(df['Date'])

        for j in column_list[4:]:
            df[j] =df[j].replace(regex=True,to_replace=r'\D',value=r'')
            
            df[j]=pd.to_numeric(df[j], errors ='coerce',downcast ='integer')

        df.to_sql('food_demos',con=engine,if_exists='replace') # Replace Table_name with your sql table name
        
        return redirect(url_for("grafanadashboard"))    
    return render_template('layouts/default.html',content=render_template( 'pages/index.html') )

@app.route("/grafanadashboard")
def grafanadashboard():
    return render_template('pages/grafanadashboard.html')
    



if __name__ == "__main__":
    
    app.run(debug=True)







from flask import Flask,request,render_template
import datetime
import os
app =Flask(__name__)
date = datetime.datetime.now().strftime('%Y%m%d')
file_path="./sensor_data_" + date +".csv"
port_num=21118
#if os.path.isfile(file_path)==False :
f = open(file_path, 'w')
f.write("時間"+"," + "数値" + "\n")
f.close()
@app.route('/',methods=['GET'])
def get_html():
    return render_template('./index2.html')
@app.route('/lux',methods=['POST'])
def update_lux():
   time = request.form["time"]
   lux = request.form["lux"]
   try:
        f = open(file_path, 'a')
        f.write(time + "," + lux )
        return "succeeded to write" 
   except Exception as e:
     print(e)
     return "failed to write"
   finally:
     f.close()
@app.route('/lux', methods=['GET'])
def get_lux():
   try:
     f = open(file_path, 'r')
     for row in f:
       lux = row
   except Exception as e:
     print(e)
   finally:
     f.close()
     return lux

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=port_num)

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
from sklearn.preprocessing import MinMaxScaler
from werkzeug.utils import secure_filename
import pickle
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier, VotingClassifier

app = Flask(__name__) #Initialize the flask App

#forest = pickle.load(open('boosting.pkl','rb'))
crop = pickle.load(open('crop.pkl','rb'))
@app.route('/')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/analysis')
def analysis():
	return render_template('analysis.html')

@app.route('/chart')
def chart():
	return render_template('chart.html')

#@app.route('/future')
#def future():
#	return render_template('future.html')    

@app.route('/login')
def login():
	return render_template('login.html')
@app.route('/upload')
def upload():
    return render_template('upload.html')  
@app.route('/preview',methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset,encoding = 'unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html",df_view = df)	


#@app.route('/home')
#def home():
 #   return render_template('home.html')

@app.route('/prediction', methods = ['GET', 'POST'])
def prediction():
    return render_template('prediction.html')


#@app.route('/upload')
#def upload_file():
#   return render_template('BatchPredict.html')



@app.route('/predict',methods=['POST'])
def predict():
	int_feature = [x for x in request.form.values()]
	 
	final_features = [np.array(int_feature)]
	 
	y_pred=crop.predict(final_features)

	if y_pred[0] == 'Paddy IGKVR-2 (IET 19795)':
		label="Crop: Paddy IGKVR-2 (IET 19795) Duration of cultivation: 105-123"
	elif y_pred[0] == 'Paddy CR Dhan 501 (IET 19189)':
		label="Crop: Paddy CR Dhan 501 (IET 19189) Duration of cultivation: 105-126"
	elif y_pred[0] == 'Wheat VL Gehun 907 (VL 907)':
		label="Crop: Wheat VL Gehun 907 (VL 907)) Duration of cultivation: 60-154"
	elif y_pred[0] == 'Wheat WHD 943':
		label="Crop: Wheat WHD 943 Duration of cultivation: 60-157"
	elif y_pred[0] == 'Millet Nandi-65 (MH-1549)':
		label="Crop: Millet Nandi-65 (MH-1549) Duration of cultivation: 65-70"
	elif y_pred[0] == 'Lentil Pant Lentil-8(Pant L-063)':
		label="Crop: Lentil Pant Lentil-8(Pant L-063) Duration of cultivation: 45-60"
	elif y_pred[0] == 'Bajra':
		label="Crop: Bajra Duration of cultivation: 45-50"
	elif y_pred[0] == 'Cardamom':
		label="Crop: Cardamom Duration of cultivation: 730-735" 
	elif y_pred[0] == 'Urad':
		label="Crop: Urad Duration of cultivation: 70-85" 
	elif y_pred[0] == 'Jowar':
		label="Crop: Jowar Duration of cultivation: 65-75" 
	elif y_pred[0] == 'Paddy CR Dhan 401 (REETA)':
		label="Crop: Paddy CR Dhan 401 (REETA) Duration of cultivation: 105-124	" 
	elif y_pred[0] == 'Millet MH 1540 (86M64) (Hybrid)':
		label="Crop: Millet MH 1540 (86M64) (Hybrid) Duration of cultivation: 65-73" 
	elif y_pred[0] == 'Sugarcane Karan 5 (Co 0124)':
		label="Crop: Sugarcane Karan 5 (Co 0124) Duration of cultivation: 300-451" 
	elif y_pred[0] == 'Banana':
		label="Crop: Banana Duration of cultivation: 365-370" 
	elif y_pred[0] == 'Arhar':
		label="Crop: Arhar Duration of cultivation: 120-200" 
	elif y_pred[0] == 'Clove':
		label="Crop: Clove Duration of cultivation: 120-180	" 
	elif y_pred[0] == 'Oilseed':
		label="Crop: Oilseed Duration of cultivation: 110-115" 
	elif y_pred[0] == 'Tea':
		label="Crop: Tea Duration of cultivation: 60-65" 
	elif y_pred[0] == 'Coffee':
		label="Crop: Coffee Duration of cultivation: 240-270" 
	elif y_pred[0] == 'Turmeric':
		label="Crop: Turmeric Duration of cultivation: 210-270" 
	elif y_pred[0] == 'Cashewnut':
		label="Crop: Cashewnut Duration of cultivation: 1030-1035" 
	elif y_pred[0] == 'Ragi':
		label="Crop: Ragi Duration of cultivation: 5.0-7.0" 
	elif y_pred[0] == 'Soyabean':
		label="Crop: Soyabean Duration of cultivation: 45-65" 
	elif y_pred[0] == 'Black Gram':
		label="Crop: Black Gram Duration of cultivation: 70-85" 
	elif y_pred[0] == 'Khesari':
		label="Crop: Khesari Duration of cultivation: 125-130" 
	elif y_pred[0] == 'Wheat MACS 6222':
		label="Crop: Wheat MACS 6222 Duration of cultivation: 60-151" 
	elif y_pred[0] == 'Black Pepper':
		label="Crop: Black Pepper Duration of cultivation: 120-150" 
	elif y_pred[0] == 'Chillies':
		label="Crop: Chillies Duration of cultivation: 40-45" 
	elif y_pred[0] == 'Garlic':
		label="Crop: Garlic Duration of cultivation: 120-150" 
	elif y_pred[0] == 'Wheat MPO(JW) 1215 (MPO 1215)':
		label="Crop: Wheat MPO(JW) 1215 (MPO 1215) Duration of cultivation: 60-150" 
	elif y_pred[0] == 'Maize PMH 5 (JH 3110)':
		label="Crop: Maize PMH 5 (JH 3110) Duration of cultivation: 95-105" 
	elif y_pred[0] == 'Groundnut Kadiri Harithandhra (K 1319)':
		label="Crop: Groundnut Kadiri Harithandhra (K 1319) Duration of cultivation: 110-121" 
	elif y_pred[0] == 'Groundnut GPBD 5':
		label="Crop: Groundnut GPBD 5 Duration of cultivation: 110-122" 
	elif y_pred[0] == 'Lentil Pant Lentil-7(Pant L-024)':
		label="Crop: Lentil Pant Lentil-7(Pant L-024) Duration of cultivation: 45-61" 
	elif y_pred[0] == 'Tobacco':
		label="Crop: Tobacco Duration of cultivation: 90-120" 
	elif y_pred[0] == 'Tomato':
		label="Crop: Tomato Duration of cultivation: 50-60" 
	elif y_pred[0] == 'Cocoa':
		label="Crop: Cocoa Duration of cultivation: 150-180" 
	elif y_pred[0] == 'Rubber':
		label="Crop: Rubber Duration of cultivation: 120-130" 
	elif y_pred[0] == 'Masoor':
		label="Crop: Masoor Duration of cultivation: 120-130" 
	elif y_pred[0] == 'Sunhemp':
		label="Crop: Sunhemp Duration of cultivation: 60-90" 
	elif y_pred[0] == 'Varagu':
		label="Crop: Varagu Duration of cultivation: 160-165" 
	elif y_pred[0] == 'Paddy CR Dhan 601 (IET 18558)':
		label="Crop: Paddy CR Dhan 601 (IET 18558) Duration of cultivation: 105-125" 
	elif y_pred[0] == 'Wheat Netravati (NIAW 1415)':
		label="Crop: Wheat Netravati (NIAW 1415) Duration of cultivation: 95-100" 
	elif y_pred[0] == 'Maize HSC1':
		label="Crop: Maize HSC1 Duration of cultivation: 95-100" 
	elif y_pred[0] == 'Millet Nandi-61 (MH-1548)':
		label="Crop: Millet Nandi-61 (MH-1548) Duration of cultivation: 65-71" 
	elif y_pred[0] == 'Millet 86M64 (MSH 203) (Hybrid)':
		label="Crop: Millet 86M64 (MSH 203) (Hybrid) Duration of cultivation: 65-72" 
	elif y_pred[0] == 'Barley Pusa Losar (BH- 380)':
		label="Crop: Barley Pusa Losar (BH- 380) Duration of cultivation: 60-72" 
	elif y_pred[0] == 'Maize DHM 119 (BH 4062)':
		label="Crop: Maize DHM 119 (BH 4062) Duration of cultivation: 95-103" 
	elif y_pred[0] == 'Millet HHB 226 (MH 1479)':
		label="Crop: Millet HHB 226 (MH 1479) Duration of cultivation: 65-76" 
	elif y_pred[0] == 'Jute':
		label="Crop: Jute Duration of cultivation: 120-150" 
	elif y_pred[0] == 'Paddy Chinsurah Rice (IET 19140)':
		label="Crop: Paddy Chinsurah Rice (IET 19140) Duration of cultivation: 105-120" 
	elif y_pred[0] == 'Paddy (CNI 383-5-11)':
		label="Crop: Paddy (CNI 383-5-11) Duration of cultivation: 105-121"         
	elif y_pred[0] == 'Paddy IGKVR-1 (IET 19569)':
		label="Crop: Paddy IGKVR-1 (IET 19569) Duration of cultivation: 105-122"
	elif y_pred[0] == 'Onion':
		label="Crop: Onion Duration of cultivation: 80-150"
	elif y_pred[0] == 'Cotton CNH012':
		label="Crop: Cotton CNH012 Duration of cultivation: 80-150"
	elif y_pred[0] == 'Cotton CICR-3 (CISA 614)':
		label="Crop: Cotton CICR-3 (CISA 614) Duration of cultivation: 105-120"
	elif y_pred[0] == 'Rice':
		label="Crop: Rice Duration of cultivation: 105-120"
	elif y_pred[0] == 'Flax':
		label="Crop: Flax Duration of cultivation: 120-140"
	elif y_pred[0] == 'Barley BH-902':
		label="Crop: Barley BH-902 Duration of cultivation: 60-70"
	elif y_pred[0] == 'Sunflower':
		label="Crop: Sunflower Duration of cultivation: 90-100"
	elif y_pred[0] == 'Maize HQPM-4':
		label="Crop: Maize HQPM-4 Duration of cultivation: 95-101"
	elif y_pred[0] == 'Groundnut Girnar - 3 (PBS 12160)':
		label="Crop: Groundnut Girnar - 3 (PBS 12160) Duration of cultivation: 175-180"
	elif y_pred[0] == 'Dry Ginger':
		label="Crop: Dry Ginger Duration of cultivation: 175-180"
	elif y_pred[0] == 'Horse Gram':
		label="Crop: Horse Gram Duration of cultivation: 120-180"
	elif y_pred[0] == 'Castor Seed':
		label="Crop: Castor Seed Duration of cultivation: 7.0-10"
	elif y_pred[0] == 'Sesame':
		label="Crop: Sesame Duration of cultivation: 40-45"
	elif y_pred[0] == 'Sugarcane Karan 6 (Co 0239)':
		label="Crop: Sugarcane Karan 6 (Co 0239) Duration of cultivation: 300-450"
	elif y_pred[0] == 'Peas':
		label="Crop: Peas Duration of cultivation: 50-100"
	elif y_pred[0] == 'Paddy RC Maniphou 11 (IET 20193)':
		label="Crop: Paddy RC Maniphou 11 (IET 20193) Duration of cultivation: 105-127"
	elif y_pred[0] == 'Cowpea':
		label="Crop: Cowpea Duration of cultivation: 45-90"
	elif y_pred[0] == 'Maize MCH 36 (Hybrid) (DKC 9099)':
		label="Crop: Maize MCH 36 (Hybrid) (DKC 9099) Duration of cultivation: 95-102"
	elif y_pred[0] == 'Pulses':
		label="Crop: Pulses Duration of cultivation: 95-102"
	elif y_pred[0] == 'Sugarcane Co-0218':
		label="Crop: Sugarcane Co-0218 Duration of cultivation: 300-452"
	elif y_pred[0] == 'Wheat PDW 314':
		label="Crop: Wheat PDW 314 Duration of cultivation: 60-152"
	elif y_pred[0] == 'Sweet potato':
		label="Crop: Sweet potato Duration of cultivation: 120-125" 
	elif y_pred[0] == 'Cotton VBCH 2231':
		label="Crop: Cotton VBCH 2231 Duration of cultivation: 150-180"         
        
	return render_template('prediction.html', prediction_text=label)
#@app.route('/performance')
#def performance():
	return render_template('performance.html')   
    
if __name__ == "__main__":
    app.run(debug=True)

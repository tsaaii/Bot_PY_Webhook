from flask import Flask, request, jsonify 
import json
import requests


app = Flask(__name__)
@app.route('/results/<string:keyword>')
def key_word(keyword):
    keyword=str(keyword)
    url='https://www.googleapis.com/youtube/v3/search?part=snippet&q={}&maxResults=5&order=viewCount&key=AIzaSyD43Zc0hcBFG_mDoFDeHmJqZ0Yhiq_ZjA0'.format(keyword)
    x1=requests.get(url)
    x2=json.loads(x1.text)
    result={}
    result2={}
    for i in range(0,len(x2['items'])):
    #print(i+1,x2['items'][i]['id'],'\n',x2['items'][i]['snippet']['channelTitle'],x2['items'][i]['snippet']['description'])
        result['number']=i+1
        result['link']='https://www.youtube.com/watch?v={}'.format(list(x2['items'][i]['id'].items())[1][1])
        result['channel title']=x2['items'][i]['snippet']['channelTitle']
        result['description']=x2['items'][i]['snippet']['description']
        resulti1={'parameters':{'link':result['link'],'channel title':result['channel title'],'description':result['description'],'video number':result['number']}}
        #result2['item']=resulti1
        result2[i]=resulti1['parameters']
    return jsonify(result2)
        #for i in key_word(keyword)():
            #return jsonify(i)
if __name__ == '__main__':

   app.run(debug=True,port=5000)
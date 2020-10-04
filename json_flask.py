import os
while True:
        try:
                import flask, threading, json, uuid, string
                import requests as req
                import random as rd
                from time import time, localtime
                break
        except:
                list_ = "flask requests".split()
                exec_format = "pip3 install {}"
                for i in list_:
            	    os.system(exec_format.format(i))

app = flask.Flask(__name__)
timeform = "{:4}-{:0>2}-{:0>2} {:0>2}:{:0>2}:{:0>2}"

@app.route('/receive',methods=['POST', 'GET'])
def receive():
    def randomDataGen():
        formats = [rd.randint(0,10), [rd.randint(201400000, 202100000) for i in range(5)], "".join([string.ascii_letters[rd.randint(0,len(string.ascii_letters)-1)]])]
        return formats[rd.randint(0,2)]
    random_json = {'Doctype' : 'html', 'Request_Type' : None, 'Requested_Time' : timeform.format(*localtime(time())[:6])}
    random_json['Request_Type'] = flask.request.method
    for i in range(rd.randint(0,6)):
        random_json['data_{}'.format(i)] = randomDataGen()
    json_A = json.dumps(random_json)
    return json_A

if __name__ == '__main__':
        app.run(debug=True, host='localhost', port=9000)


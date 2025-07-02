from flask import Flask, jsonify
from math import factorial


app = Flask(__name__)

@app.route('/check_for_strongnumber/<int:_num>')
def check_strong_number(_num):
    if _num == sum([factorial(int(i)) for i in str(_num)]):
        # return True
        return jsonify({'result': True})
    # return False
    return jsonify({'result': False})

# print(check_strong_number(int(input('Enter any interger to check whether it is a Strong Number or not: '))))

if __name__ == '__main__':
    # app.run(host='localhost', port=5000)
    app.run()

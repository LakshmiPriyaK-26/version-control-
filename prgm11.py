from flask import Flask, request, jsonify
app=Flask(__name__)
Orders=[]
@app.route('/addOrder', methods=['POST'])
def add_Order():
    data=request.get_json()
    Orders.append(data)
    return jsonify({"message":"Orders added successfully","Order":data})
@app.route('/showOrder', methods=['GET'])
def show_Order():
    return jsonify(Orders)
if __name__=='__main__':
    app.run(debug=True)
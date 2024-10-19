#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API!"

@app.route('/api/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        content = request.json
        return jsonify({"received": content}), 201
    return jsonify({"message": "GET request received"}), 200

if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:





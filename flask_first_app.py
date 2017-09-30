#!/usr/bin/python3

#Nginx configuration taken from 
#https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04

from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    #return "HelloWorld"
    #return "Method user %s" %request.method
    user_agent = request.headers['User-Agent']
    return "User agent making this request is %s" %user_agent

@app.route('/profile/<username>')
def user(username):
    return "Welcome %s" % username

@app.route('/country')
def country():
    #return "HelloWorld"
    #return "Method user %s" %request.method
    cloudfront_viewer_country = request.headers['Cloudfront-Viewer-Country']
    return "This request is being made from : %s" %cloudfront_viewer_country

if __name__ == "__main__":
    app.run(debug=True)


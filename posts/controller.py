from flask import Flask, render_template, request, flash
from flask import Blueprint
from .models import twitter_db
from shapely import wkb, wkt
from binascii import unhexlify
from datetime import datetime
import timeago
import pytz
import json
from math import radians, cos, sin, asin, sqrt
from . import db
import sys
sys.path.append("..")
from utils.shortest_distance import shortest_distance
IST = pytz.timezone('Asia/Kolkata')

def post():
    Message=request.args.get('text')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    try:
        x=float(lat)
        y=float(lon)
    except:
        return 'fail'
    me = twitter_db(text=Message,coordinates='POINT(' + lat + ' ' + lon +')')
    db.session.add(me)
    db.session.commit()
    q=twitter_db.query.all()
    
    for x in q:
        binary = unhexlify((str(x.coordinates)))
        point = wkb.loads(binary)
    
    return "success"


def nearby():
    lat1 = float(request.args.get('lat'))
    lon1 = float(request.args.get('lon'))
    page = int(request.args.get('page'))

    
    q=twitter_db.query.all()
    
    lat_lon_dist = []

    for x in q:
        l = []
        binary = unhexlify((str(x.coordinates)))
        point = wkb.loads(binary)
        lat2 = point.x
        lon2 = point.y
        text = x.text
        
        dis = shortest_distance(lat1, lat2, lon1, lon2)

        l.append(x.id),l.append(lat2),l.append(lon2),l.append(dis),l.append(text)

        prev=str(x.date_created.strftime('%Y-%m-%d %H:%M:%S'))
        curr=str(datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S'))
        lastseen=timeago.format(prev,curr)
        l.append(lastseen)
        lat_lon_dist.append(l)
    
    lat_lon_dist = sorted(lat_lon_dist, key=lambda x:(x[3], x[5]))
    
    d=dict()
    idx=1
    for x in lat_lon_dist:
        nd=dict()
        nd['lat']=str(x[1])
        nd['lon']=str(x[2])
        nd['lastseen']=str(x[5])
        nd['Message']=str(x[4])
        if(idx>=(page-1)*10 and idx<(page)*10):
            d[str(x[0])]=nd
        idx+=1
    return (json.dumps(d))

def get():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    URL = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid=6f807e42edb11b81c3439053f342477a"

    
    response = request.get(URL)
    
    data = response.json()

    return data
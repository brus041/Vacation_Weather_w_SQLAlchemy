import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, json, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
mt = Base.classes.measurement
st = Base.classes.station
app = Flask(__name__)


# 4. Define what to do when a user hits each route
@app.route("/")
def home():
    return "Possible routes to choose in browser: <br> /api/v1.0/precipitation <br> /api/v1.0/stations <br> /api/v1.0/tobs <br> /api/v1.0/start_date <br> /api/v1.0/start_date/end_date"

@app.route("/api/v1.0/precipitation")
def rain():
    session = Session(engine)
    dates_and_rain = session.query(mt.date,mt.prcp)
    session.close()
    temp_dict = {date:rain for (date,rain) in dates_and_rain}
    return jsonify(temp_dict)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_names = session.query(st.name).all()
    session.close()
    names = list(np.ravel(station_names))
    return jsonify(names)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    sts_counts = session.query(mt.station,func.count(mt.station)).group_by(mt.station).order_by(func.count(mt.station).desc())
    active_station = sts_counts.first()[0]
    active_station_data = session.query(mt.tobs).filter(mt.station == active_station)
    active_station_last_12 = active_station_data.order_by(mt.date.desc()).filter(mt.date >= '2016-08-23').all()
    session.close()
    temps = list(np.ravel(active_station_last_12))
    return jsonify(temps)

@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    min = session.query(func.min(mt.tobs).filter(mt.date >= start))[0][0]
    max = session.query(func.max(mt.tobs).filter(mt.date >= start))[0][0]
    avg = session.query(func.avg(mt.tobs).filter(mt.date >= start))[0][0]
    session.close()
    info = {'Minimum Temperature ':min, 'Maximum Temperature ':max,'Average Temperature ':avg}
    return jsonify(info)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    session = Session(engine)
    min = session.query(func.min(mt.tobs).filter(mt.date >= start).filter(mt.date <= end))[0][0]
    max = session.query(func.max(mt.tobs).filter(mt.date >= start).filter(mt.date <= end))[0][0]
    avg = session.query(func.avg(mt.tobs).filter(mt.date >= start).filter(mt.date <= end))[0][0]
    session.close()
    info = {'Minimum Temperature ':min, 'Maximum Temperature ':max,'Average Temperature ':avg}
    return jsonify(info)

if __name__ == "__main__":
    app.run(debug=True)


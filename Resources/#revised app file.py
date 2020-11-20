# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Imports
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt 
import numpy as np 
import pandas as pd 

#Engine Creation
engine =create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflection
Base= automap_base()
Base.prepare(engine,reflect=True)

# Save references to each table
Measurement=Base.classes.measurement
Station=Base.classes.station
# Create our session (link) from Python to the DB
session=Session(engine)

#Creating an App
app = Flask(__name__)

#Defining My Routes
@app.route("/")
def welcome():
    return (
        f"Welcome to the Climate API Homepage!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation(): 
    #Return precipitatio data for the last year
    first_day=dt.date(2017,8,23)-dt.timedelta(days=365)
    results=session.query(Measurement.date, Measurement.prcp).filter(Measurement.station==most_active).filter(Measurement.date>= first_day).all()

    p_dict={date: prcp for date, prcp in results}
    return jsonify(p_dict)

@app.route("/api/v1.0/stations")
def stations():
    stations=session.query(Station.station).all()
    stations=list(np.ravel(stations))
    return jsonify(stations) 

@app.route("/api/v1.0/tobs")
def temp(): 
    stations=session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    most_active=stations[0][0]
    station_data=session.query(Measurement.date, Measurement.tobs).filter(Measurement.station==most_active).all()
    station_data=list(np.ravel(station_data))
    return jsonify(station_data)


@app.route("/api/v1.0/<start>") 
def start(start):
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>start).all()
    temps = list(np.ravel(results))
    return jsonify(results)


@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    results=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    temps2=list(np.ravel(results))
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)


# %%



# %%




{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Restarting with windowsapi reloader\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    }
   ],
   "source": [
    "#Imports\n",
    "import sqlalchemy\n",
    "from sqlalchemy.ext.automap import automap_base\n",
    "from sqlalchemy.orm import Session\n",
    "from sqlalchemy import create_engine, func\n",
    "from flask import Flask, jsonify\n",
    "import datetime as dt \n",
    "import numpy as np \n",
    "import pandas as pd \n",
    "\n",
    "#Engine Creation\n",
    "engine =create_engine(\"sqlite:///Resources/hawaii.sqlite\")\n",
    "\n",
    "#Reflection\n",
    "Base= automap_base()\n",
    "Base.prepare(engine,reflect=True)\n",
    "\n",
    "# Save references to each table\n",
    "Measurement=Base.classes.measurement\n",
    "Station=Base.classes.station\n",
    "# Create our session (link) from Python to the DB\n",
    "session=Session(engine)\n",
    "\n",
    "#Creating an App\n",
    "app = Flask(__name__)\n",
    "\n",
    "#Defining My Routes\n",
    "@app.route(\"/\")\n",
    "def welcome():\n",
    "    return (\n",
    "        f\"Welcome to the Climate API Homepage!<br/>\"\n",
    "        f\"Available Routes:<br/>\"\n",
    "        f\"/api/v1.0/precipitation<br/>\"\n",
    "        f\"/api/v1.0/stations<br/>\"\n",
    "        f\"/api/v1.0/tobs<br/>\"\n",
    "        f\"/api/v1.0/start/end<br/>\"\n",
    "    )\n",
    "\n",
    "@app.route(\"/api/v1.0/precipitation\")\n",
    "def precipitation(): \n",
    "    #Return precipitatio data for the last year\n",
    "    first_day=dt.date(2017,8,23)-dt.timedelta(days=365)\n",
    "    results=session.query(Measurement.date, Measurement.prcp).filter(Measurement.station==most_active).filter(Measurement.date>= first_day).all()\n",
    "\n",
    "    p_dict={date: prcp for date, prcp in results}\n",
    "    return jsonify(p_dict)\n",
    "\n",
    "@app.route(\"/api/v1.0/stations\")\n",
    "def stations():\n",
    "    stations=session.query(Station.station).all()\n",
    "    stations=list(np.ravel(stations))\n",
    "    return jsonify(stations) \n",
    "\n",
    "@app.route(\"/api/v1.0/tobs\")\n",
    "def temp(): \n",
    "    stations=session.query(Measurement.station,func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()\n",
    "    most_active=stations[0][0]\n",
    "    station_data=session.query(Measurement.date, Measurement.tobs).filter(Measurement.station==most_active).all()\n",
    "    station_data=list(np.ravel(station_data))\n",
    "    return jsonify(station_data)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/<start>\") \n",
    "def start(start):\n",
    "    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).filter(Measurement.date>start).all()\n",
    "    temps = list(np.ravel(results))\n",
    "    return jsonify(results)\n",
    "\n",
    "\n",
    "@app.route(\"/api/v1.0/<start>/<end>\")\n",
    "def start_end(start, end):\n",
    "    results=session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date>=start).filter(Measurement.date<=end).all()\n",
    "    temps2=list(np.ravel(results))\n",
    "    return jsonify(results)\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, jsonify
_name_ = 'test'
app = Flask(_name_)

@app.route('/')
def home():
    return(f"/api/v1.0/precipitation" f"/api/v1.0/stations" f"/api/v1.0/tobs" f"/api/v1.0/<start>" f"/api/v1.0/<start>/<end>")

@app.route('/api/v1.0/precipitation')
def dictionary():
    sess=Session(engine)
    reslt = sess.query(Measure.date, Measure.prcp).all()
    aln = []
    for prcp, date in reslt:
        edict = {}
        edict["prcp"] = prcp
        edict["date"] = date
        aln.append(edict)
    return jsonify(aln)

@app.route('/api/v1.0/stations')
def liest():
    sess=Session(engine)
    app1 = sess.query(Station.station).all()
    sess.close()
    fin = list(np.ravel(app1))
    return jsonify(fin)


@app.route('/api/v1.0/tobs')
def mix():
    sess=Session(engine)
    ope = pd.read_sql("SELECT date, tobs FROM measurement WHERE station='USC00519281'", conn)
    sess.close()
    liast = list(np.ravel(ope))
    return jsonify(liast)

@app.route('/api/v1.0/<start>')
def endgame():
    sess=Session(engine)
    old = pd.read_sql("SELECT tobs, date FROM measurement WHERE date BETWEEN '2016-08-23' AND '2016-09-30'", conn)
    df9 = pd.DataFrame(old)
    newdic = []
    for i in df9:
        if df9["date"] >= '2016-08-23':
            newdic.append(i)
    df10 = pd.DataFrame(newdic)
    newdic2 = [min(df10["tobs"]), max(df10["tobs"]), stats.mean(df10["tobs"])]
    sess.close()
    return jsonify(newdic)
    return jsonify(newdic2)

@app.route('/api/v1.0/<start>/<end>')
def endgame2():
    sess=Session(engine)
    semiold = pd.read_sql("SELECT tobs FROM measurement WHERE date BETWEEN '2016-08-23' AND '2016-09-30'", conn)
    df11 = pd.DataFrame(semiold)
    newdic3 = []
    for j in df9["tobs"]:
        newdic3.append(j)
    df12 = pd.DataFrame(newdic3)
    newdic1 = [min(df12["tobs"]), max(df12["tobs"]), stats.mean(df12["tobs"])]
    sess.close()
    return jsonify(newdic3)
    return jsonify(newdic1)
    
    
if _name_ == 'test':
    app.run(debug=True, use_reloader=False)


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index(chartID = 'chartID', chart_type = 'column', chart_height = 350):
    chart = {"renderTo": chartID, "type":chart_type, "height": chart_height,"margin": 75,"options3d": {"enabled": 'true',"alpha": 15,"beta": 15,"depth": 60,"viewDistance": 60,}}
    plotOptions = {"column": {"depth": 20}}
    series = [{"name": 'IQ', "data": [127,100,90,-30,130,99,0]}]
    title = {"text": 'Štekr Graf by OOOMACHT'}
    xAxis = {"categories": ['JA', 'TY','ON','ONA','MY','VY','ONI']}
    yAxis = {"title": {"text": 'Graf pro GRUSSMANNA'}}

    # "options3d" : { "enabled" : True,"alpha": 15,"beta": 15,"depth": 50,"viewDistance":25}}
    return render_template('index.html', chartID=chartID, chart=chart,  plotOptions = plotOptions, series=series ,title=title, xAxis=xAxis, yAxis=yAxis)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=5000, passthrough_errors=True)
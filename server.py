from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def initial_load():
    return 'Go to http://localhost:5000/play to have it do something'

@app.route("/play")
def render_blocks():
    return render_template('playground.html')
 
@app.route("/play/<int:number_of_boxes>")
def block_repeat(number_of_boxes):
    repeat = number_of_boxes
    return render_template('playground2.html',repeat=repeat)

@app.route("/play/<int:number_of_boxes>/<color>")
def box_color(number_of_boxes, color):
    repeat = number_of_boxes
    
    return render_template("playground3.html",repeat=repeat,color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

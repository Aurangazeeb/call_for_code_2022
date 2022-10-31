from flask import Flask, render_template, request
from predict_ner import predict

app = Flask(__name__)

app. config["CACHE_TYPE"] = "null"
@app.route('/home/')
def input_page():
    return render_template('tasks_input_ui.html')


@app.route('/predictions', methods=['POST', 'GET'])
def display_results():
    co2map = dict(health = 30, clothing = 45, communication = 20,transportation = 60, food = 25, hygiene = 10)
    # return "Hello second page"
    if request.method == 'POST':
       tasks = request.form['tasks']
       tokens_identified_dict = dict(*predict(tasks))#dict(values = loaded_model(str(tasks)))#dict(values = tasks)#predict(tasks) #dict(values = loaded_model(str(tasks))) #{"name" : "auru", "place" : "kochi"}

       tokens_identified = [{i: [mydict['entity_group'], mydict['word'], co2map[mydict['entity_group']]]} for i, mydict in enumerate([tokens_identified_dict])]
       total_emissions = sum([val[i][-1] for i,val in enumerate(tokens_identified)])
       return render_template('emissions_found.html', result=tokens_identified, total_footprint = total_emissions)
#         # user = request.form['tasks']
# #         return redirect(url_for('success', name=user))
#     else:
#         tokens_identified_dict = {"name" : "auru", "place" : "kochi"}
#         return render_template('emissions_found.html', result=tokens_identified_dict)
# #         user = request.args.get('nm')
# #         return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)

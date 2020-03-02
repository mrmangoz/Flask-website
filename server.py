from flask import Flask, request, render_template, flash, make_response, redirect, url_for
import json, datetime


app = Flask(__name__)
app.secret_key = b'jasf78623ncnoasd--0937h'
totals = {
          'lunch': 250,
          'party': 300,
          'out': 200,
          'week': 750,
          'month': 3000
}


def weekly_spendature(UCT_lunch=0,party_beers=0,out_about=0):
    f = open('current_week.json', "r")
    data = f.read()
    json_obj = json.loads(data)
    today = str(datetime.date.today())
    temp = json_obj["Days"]
    if json_obj["Days"] == []:
        print("empty")
        temp.append({
                     "date": today,
                     "UCT_lunch": "0",
                     "party_beers": "0",
                     "out_about": "0"
        })
    else:
        for item in json_obj["Days"]:
            #if item["date"] == today:
            UCT_lunch += float(item["UCT_lunch"])
            party_beers += float(item["party_beers"])
            out_about += float(item["out_about"])
    return UCT_lunch, party_beers, out_about


def write_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def reset_json(a_file, r_file, a_array, r_array):
    a = open(a_file, "r")
    a_data = a.read()
    a_json = json.loads(a_data)
    temp = a_json
    r = open(r_file, "r")
    r_data = r.read()
    r_json = json.loads(r_data)
    temp[a_array].append(r_json)
    write_json(a_json, a_file)
    a.close()
    r_json[r_array] = []
    write_json(r_json, r_file)
    r.close()

@app.route('/')
def index():
    return render_template('person.html')


@app.route('/reset-month')
def reset_month():
    reset_json("months.json", 'current_month.json', "Months", "Month")
    return render_template('reset-month.html')


@app.route('/reset-week')
def reset_week():
    reset_json("weeks.json", 'current_week.json', "Weeks", "Days")
    return render_template('reset-week.html')


@app.route('/stats')
def statistics():
    current_spendature = 0

    f = open('current_week.json', "r")
    data = f.read()
    json_obj = json.loads(data)
    for day in json_obj["Days"]:
        lunch = float(day["UCT_lunch"])
        party = float(day["party_beers"])
        out = float(day["out_about"])
        current_spendature += lunch + party + out
    left_over = totals["week"] - current_spendature

    return render_template('stats.html', spendature = current_spendature, total_left = left_over)


@app.route('/index', methods=['GET', 'POST'])
def form():
    form_values = []
    running_totals = weekly_spendature()
    UCT_lunch = 0
    party_beers = 0
    out_about = 0
    f = open('current_week.json', "r")
    data = f.read()
    json_obj = json.loads(data)
    day = len(json_obj["Days"]) -1
    try:
        #print(request.form['UCT_lunch'], "UCT lunch")
        UCT_lunch += float(request.form['UCT_lunch'])
        json_obj["Days"][day]["UCT_lunch"] = str(UCT_lunch)
    except:
        print('l')
    try:
        party_beers += float(request.form['party/beers'])
        json_obj["Days"][day]["party_beers"] = str(party_beers)
    except:
        print('p')
    try:
        out_about += float(request.form['out_about'])
        json_obj["Days"][day]["out_about"] = str(out_about)
    except:
        print('o')
    print(UCT_lunch)

    output_lunch = totals['lunch'] - UCT_lunch - running_totals[0]
    output_party = totals['party'] - party_beers - running_totals[1]
    output_out = totals['out'] - out_about - running_totals[2]
    write_json(json_obj, "current_week.json")
    write_json(json_obj, "current_month.json")
    f.close()
    return render_template('index.html', lunch=output_lunch, party=output_party, out=output_out)


@app.route('/index-brendan', methods=['GET', 'POST'])
def brendan_form():
    form_values = []
    running_totals = weekly_spendature()
    today = str(datetime.date.today())
    UCT_lunch = 0
    party_beers = 0
    out_about = 0
    f = open('current_week.json', "r")
    data = f.read()
    json_obj = json.loads(data)
    day = len(json_obj["Days"]) -1
    try:
        #print(request.form['UCT_lunch'], "UCT lunch")
        UCT_lunch += float(request.form['UCT_lunch'])
        json_obj["Days"][day]["UCT_lunch"] = str(UCT_lunch)
    except:
        print('l')
    try:
        party_beers += float(request.form['party/beers'])
        json_obj["Days"][day]["party_beers"] = str(party_beers)
    except:
        print('p')
    try:
        out_about += float(request.form['out_about'])
        json_obj["Days"][day]["out_about"] = str(out_about)
    except:
        print('o')
    print(UCT_lunch)

    output_lunch = totals['lunch'] - UCT_lunch - running_totals[0]
    output_party = totals['party'] - party_beers - running_totals[1]
    output_out = totals['out'] - out_about - running_totals[2]
    write_json(json_obj, "current_week.json")
    write_json(json_obj, "current_month.json")
    f.close()
    return render_template('index-brendan.html', lunch=output_lunch, party=output_party, out=output_out)

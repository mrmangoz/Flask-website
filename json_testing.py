import json, datetime

def write_json(data, filename="current_week 2.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

with open('current_week 2.json', "r") as f:
    data = f.read()
    json_obj = json.loads(data)
    #print(json_obj["Days"])
    temp = json_obj["Days"]
    #print(json_obj["Days"][0]["date"])
    '''for item in json_obj["Days"]:
        #print(item["date"])
        if item["date"] == str(datetime.date.today()):
            print(item["date"])
            item["UCT_lunch"] = "test"'''
    temp.append({
                 "date": str(datetime.date.today()),
                 "UCT_lunch": "test",
                 "party_beers": "test",
                 "out_about": "test"
    })
write_json(json_obj)
#date = datetime.date.today()
#print(date)

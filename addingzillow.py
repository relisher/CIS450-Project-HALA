from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Zillow')

with open("demographicsformatted.json") as json_file:
    data = json.load(json_file)
    for x in data:
        city = str(x["response"]["region"]["city"]["$"]).lower() + ", california"        

        medianhouseholdincome = x["response"]["pages"]["page"][2]["tables"]["table"][0]["data"]["attribute"][0]["values"]["city"]["value"]["$"]
        percentsinglemale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][0]["data"]["attribute"][1]["values"]["city"]["value"]["$"]))
        percentsinglefemale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][0]["data"]["attribute"][2]["values"]["city"]["value"]["$"]))
        medianage = x["response"]["pages"]["page"][2]["tables"]["table"][0]["data"]["attribute"][3]["values"]["city"]["value"]["$"]
        homeswithkids = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][0]["data"]["attribute"][4]["values"]["city"]["value"]["$"]))
        pergreat70 = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][0]["value"]["$"]))
        per0s = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][1]["value"]["$"]))
        per10s = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][2]["value"]["$"]))
        per20s = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][3]["value"]["$"]))
        per30s = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][4]["value"]["$"]))
        per40s = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][5]["value"]["$"]))
        per50s = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][6]["value"]["$"]))
        per60s = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][1]["data"]["attribute"][7]["value"]["$"]))

        nokids = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][3]["data"]["attribute"][0]["value"]["$"]))
        kids = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][3]["data"]["attribute"][1]["value"]["$"]))

        divorcedfemale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][0]["value"]["$"]))
        divorcedmale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][1]["value"]["$"]))
        marriedfemale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][2]["value"]["$"]))
        marriedmale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][3]["value"]["$"]))
        singlefemale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][4]["value"]["$"]))
        singlemale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][5]["value"]["$"]))
        widowedfemale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][6]["value"]["$"]))
        widowedmale = decimal.Decimal(str(x["response"]["pages"]["page"][2]["tables"]["table"][4]["data"]["attribute"][7]["value"]["$"]))

        print("Adding:", city)

        table.put_item(
           Item={
              'city': city,
              'Median Household Income' : medianhouseholdincome,
              'Percent Single Female' : percentsinglefemale,
              'Percent Single Male' : percentsinglemale,
              'Median Age' : medianage,
              'Homes with Kids' : homeswithkids,
              '>=70s' : pergreat70,
              '0s' : per0s,
              '10s' : per10s,
              '20s' : per20s,
              '30s' : per30s,
              '40s' : per40s,
              '50s' : per50s,
              '60s' : per60s,
              'No Kids' : nokids,
              'Kids' : kids,
              'Divorced Female' : divorcedfemale,
              'Divorced Male' : divorcedmale,
              'Single Female' : singlefemale,
              'Single Male' : singlemale,
              'Widowed Female' : widowedfemale,
              'Widowed Male' : widowedmale,
            }
        )
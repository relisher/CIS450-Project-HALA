from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Zillow')

with open("zillowerrors.json") as json_file:
    data = json.load(json_file)
    for x in data:
        city = str(x["request"]["city"]["$"]).lower() + ", california"
        print("Adding:", city)

        table.put_item(
           Item={
              'city': city,
              'Median Household Income' : "n/a",
              'Percent Single Female' : "n/a",
              'Percent Single Male' : "n/a",
              'Median Age' : "n/a",
              'Homes with Kids' : "n/a",
              '>=70s' : "n/a",
              '0s' : "n/a",
              '10s' : "n/a",
              '20s' : "n/a",
              '30s' : "n/a",
              '40s' : "n/a",
              '50s' : "n/a",
              '60s' : "n/a",
              'No Kids' : "n/a",
              'Kids' : "n/a",
              'Divorced Female' : "n/a",
              'Divorced Male' : "n/a",
              'Single Female' : "n/a",
              'Single Male' : "n/a",
              'Widowed Female' : "n/a",
              'Widowed Male' : "n/a",
            }
        )
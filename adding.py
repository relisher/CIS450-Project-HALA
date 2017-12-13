from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('OkCupid')

with open("matchconverted5.json") as json_file:
    data = json.load(json_file)
    for x in data:

        id1 = int(x['id'])
        age = (x['age'])
        if age == 'NA':
          age = 0
        else:
          age = int(age)
        body_type = x['body_type']
        diet = x['diet']
        drinks = x['drinks']
        drugs = x['drugs']
        education = x['education']
        ethnicity = x['ethnicity']
        height = x['height']
        if height == 'NA':
          height = 0
        else:
          height = int(height)
        income = int(x['income'])
        job = x['job']
        location = x['location']
        offspring = x['offspring']
        orientation = x['orientation']
        pets = x['pets']
        religion = x['religion']
        sex = x['sex']
        sign = x['sign']
        smokes = x['smokes']
        speaks = x['speaks']
        status = x['status']
        
        if not job:
          job = 'empty'
        if not religion:
          religion = 'empty'
        if not smokes:
          smokes = 'empty'
        if not body_type:
          body_type = 'empty'
        if not diet:
          diet = 'empty'
        if not drinks:
          drinks = 'empty'
        if not drugs:
          drugs = 'empty'
        if not education:
          education = 'empty'
        if not ethnicity:
          ethnicity = 'empty'
        if not height:
          height = 'empty'
        if not income:
          income = 'empty'          
        if not location:
          location = 'empty'
        if not offspring:
          offspring = 'empty'
        if not orientation:
          orientation = 'empty'
        if not pets: 
          pets = 'empty'
        if not sex:
          sex = 'empty'
        if not sign:  
          sign = 'empty' 
        if not speaks:
          speaks = 'empty'
        if not status:
          status = 'empty'

        print("Adding:", id1, age)

        table.put_item(
           Item={
              'id': id1,
              'age': age,
              'body_type': body_type,
              'diet': diet,
              'drinks': drinks,
              'drugs': drugs,
              'education': education,
              'ethnicity': ethnicity,
              'height': height,
              'income': income,
              'job': job,
              'location': location,
              'offspring': offspring,
              'orientation': orientation,
              'pets': pets,
              'religion': religion,
              'sex': sex,
              'sign': sign,
              'smokes': smokes,
              'speaks': speaks,
              'status': status,
            }
        )
from sqlmodel import Session

from app.Database import Movement, engine
import requests
import json


def seed_movements():
    muscles = ['abdominals', 'abductors', 'adductors', 'biceps', 'calves', 'chest', 'forearms', 'glutes',
               'hamstrings',
               'lats', 'lower_back', 'middle_back', 'neck', 'quadriceps', 'traps', 'triceps', ]

    session = Session(engine)

    for muscle in muscles:
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
        response = requests.get(api_url, headers={'X-Api-Key': '6GDcKxbzmM/vF0EpdpbWwg==IeIyFqRSRdGr6b8R'})

        data = json.loads(response.text)

        for exercise in data:
            try:
                new_object = Movement(name=exercise['name'])
                session.add(new_object)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"\n Error processing {exercise['name']}: {e} \n")



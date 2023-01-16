import json

def deserialize_file():
    arr = []
    with open('people.json', 'r') as f:
        people = json.loads(f.read())
        for obj in people:
            person = Person()
            person.first_name = obj['first']
            person.last_name = obj['last']
            person.age = obj['age']
            arr.append(person)
    return arr

class Person:
    def __init__(self, first_name='John', last_name='Smith', age=20):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def image(self):
        img = 'images/' + self.first_name.lower() + self.last_name.lower() + '.png'
        return img

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age}'

    def generate_link(self):
        return (f"[link]("
            f"display_people"
            f"?first={self.first_name}"
            f"&last={self.last_name}"
            f"&age={self.age})"
        )
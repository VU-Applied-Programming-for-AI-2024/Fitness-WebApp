import json

class Exercise:
    def __init__(self, body_part, equipment, gif_url, exercise_id, name, target):
        self.body_part = body_part
        self.equipment = equipment
        self.gif_url = gif_url
        self.exercise_id = exercise_id
        self.name = name
        self.target = target

    def __repr__(self):
        return (f"Exercise(body_part={self.body_part}, equipment={self.equipment}, "
                f"gif_url={self.gif_url}, exercise_id={self.exercise_id}, "
                f"name={self.name}, target={self.target})")

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(
            body_part=data.get('bodyPart'),
            equipment=data.get('equipment'),
            gif_url=data.get('gifUrl'),
            exercise_id=data.get('id'),
            name=data.get('name'),
            target=data.get('target')
        )


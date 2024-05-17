#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, object):
        self.__objects[object.__class__.__name__ + '.' + str(object)] = object

    def save(self):
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()
                       }, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass

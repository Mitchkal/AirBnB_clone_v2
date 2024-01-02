#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """return dictrionary of objects in class"""
        if cls:
            return {key: obj for (key, obj) in self.__objects.items()
                    if isinstance(obj, type(cls))}
        return self.__objects

    """def all(self, cls=None):
        Returns a list of objects of class or ll
        # dictionary = {}
        result_dict = {}
        if cls is None:
            # return self.__objects
            return (self.__objects)
        if cls != "":
            for k, v in self.__objects.items():
                # print("key in self: {}".format(k))
                if cls == k.split(".")[0]:
                    # formatted_state = "[{}] ({}) {}".format(cls, v['id'],
                    # str(v))
                    result_dict[k] = v
                    # return dictionary
                    # result_list.append(v)
                return (result_dict)
        else:
            return self.__objects"""

    def new(self, obj):
        """Adds new object to storage dictionary"""
        # self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
        objname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objname, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.review import Review
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    class_name = val['__class__']
                    instance = classes[class_name](**val)
                    self.__objects[key] = instance
                    # self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        deletes obj from __objects
        """
        if obj is not None:
            keys = f"{obj.__class__.__name__}.{obj.id}"
            if keys in FileStorage.__objects:
                FileStorage.__objects.pop(keys, None)
                self.save()

    def close(self):
        """deserializes json file to objects"""
        self.reload()

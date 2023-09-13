#!/usr/bin/python3
'''student module'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        '''Sets the necessary attributes for the Student object.

        Args:
            first_name (str): first name of the student.
            last_name (str): last name of the student.
            age (int): age of the student.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a dictionary representation of a Student instance
        '''
        if attrs is not None:
            return {ke: va for ke, va in self.__dict__.items() if ke in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        '''replaces all attributes of the Student instance'''
        for key, value in json.items():
            self.__dict__[key] = value

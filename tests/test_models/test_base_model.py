#!/usr/bin/python3

"""
Unittest for BaseModel class
"""

from models.base_model import BaseModel
import unittest
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """
    Defines tests for BaseModel class
    """

    def test_no_args_instantiates(self):
        """
        Instantiates BaseModel with no arguments
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_init_with_kwargs(self):
        """
        Instantiates BaseModel with **kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_init_without_kwargs(self):
        """
        Instantiates BaseModel without **kwargs
        """
        instance = BaseModel()
        self.assertIsNotNone(instance.id)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_instantiation_with_None_kwargs(self):
        """
        Instantiates BaseModel with None as **kwargs
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_id_is_public_str(self):
        """
        Checks that BaseModel id is a public instance attribute of type str
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_str_representation(self):
        """
        Checks that the __str__ method produces the correct output
        """
        instance = BaseModel()
        str_repr = str(instance)
        self.assertIn("[BaseModel]", str_repr)
        self.assertIn(instance.id, str_repr)

    def test_save_method(self):
        """
        Checks that the save method updates the public instance attribute
        """
        instance = BaseModel()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

    def test_created_at_is_public_datetime(self):
        """
        Checks that BaseModel created_at is a public instance attribute
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        """
        Checks that BaseModel updated_at is a public instance attribute
        """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_to_dict_method(self):
        """
        Checks that the to_dict method returns the correct dictionary
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)

    def test_new_instance_unique_id(self):
        """
        Checks that each new instance has a unique id
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_two_instance_different_created_at(self):
        """
        Checks that each new instance has a unique created_at datetime
        """
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertLess(instance1.created_at, instance2.created_at)

    def test_two_instance_different_updated_at(self):
        """
        Checks that each new instance has a unique updated_at datetime
        """
        instance1 = BaseModel()
        sleep(0.05)
        instance2 = BaseModel()
        self.assertLess(instance1.updated_at, instance2.updated_at)

    def test_init_with_invalid_created_at(self):
        """
        Checks that the __init__ method raises a ValueError
        """
        with self.assertRaises(ValueError):
            data = {"created_at": "invalid_datetime_format"}
            instance = BaseModel(**data)
            print(instance)

    def test_init_with_invalid_updated_at(self):
        """
        Checks that the __init__ method raises a ValueError
        """
        with self.assertRaises(ValueError):
            data = {"updated_at": "invalid_datetime_format"}
            instance = BaseModel(**data)
            print(instance)

    def test_args_unused(self):
        """
        Checks that the __init__ method does not use *args
        """
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())


if __name__ == '__main__':
    unittest.main()

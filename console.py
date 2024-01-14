#!/usr/bin/python3
""" HBNBcommand class"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Define s HBNBCommand class"""

    prompt = "(hbnb) "
    class_names = {
            'BaseModel': BaseModel,
            }

    def do_EOF(self, arg):
        """command CTRL+D to exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line+ENTER shouldn’t execute anything"""
        pass

    def do_create(self, values):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id"""
        if values == "":
            print("** class name missing **")
            return
        n_class = HBNBCommand.class_names[values]()
        n_class.save()
        print(n_class.id)

    def do_show(self, values):
        """Prints the string representation of
            an instance based on the class name and id"""
        storage.reload()
        objects = storage.all()
        if values == "":    
            print("** class name missing **")
            return
        val = shlex.split(values)
        if val[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        elif len(val) == 1:
            print("** instance id missing **")
            return
        elif f"{val[0]}.{val[1]}" not in objects:
            print("** no instance found **")
            return
        else:
            print(objects[f"{val[0]}.{val[1]}"])
    
    def do_destroy(self, values):
        '''  Deletes an instance based on the class name and id'''
        storage.reload()
        objects = storage.all()    
        if values == "":
            print("** class name missing **")
            return
        val = shlex.split(values)
        if val[0] not in HBNBCommand.class_names:
            print("** class doesn't exist **")
            return
        if len(val) == 1:
            print("** instance id missing **")
            return
        elif f"{val[0]}.{val[1]}" in objects:
            del objects[f"{val[0]}.{val[1]}"]
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()


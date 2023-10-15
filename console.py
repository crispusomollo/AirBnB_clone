#!/usr/bin/python3
"""
The AirBnB command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Entry to the command interpreter
    """
    prompt = "(hbnb) "
    classes = {"BaseModel", "Amenity", "City",
               "Place", "State", "Review", "User"}

    def do_quit(self, ln):
        """Exit command on quit"""
        return True
        
    def do_EOF(self, ln):
        """Exit command on Ctrl-D"""
        print()
        return True

    def do_create(self, ln):
        """Create instance specified by user"""
        if len(ln) == 0:
            print("** class name is missing **")
        elif ln not in HBNBCommand.classes:
            print("** class does not exist **")
        else:
            instance = eval(ln)()
            instance.save()
            print(instance.id)
            
    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def do_show(self, ln):
        """Print a string representation - name and id"""
        if len(ln) == 0:
            print("** class name is missing **")
            return
        args = parse(ln)
        if args[0] not in HBNBCommand.classes:
            print("** class does not exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance found **")
                else:
                    print(storage.all()[name])
        except IndexError:
            print("** instance id is missing **")

    def do_destroy(self, ln):
        """Destroys a specified instance; Save it to a JSON file"""
        if len(ln) == 0:
            print("** class name is missing **")
            return
        args = parse(ln)
        if args[0] not in HBNBCommand.classes:
            print("** class does not exist **")
            return
        try:
            if args[1]:
                name = "{}.{}".format(args[0], args[1])
                if name not in storage.all().keys():
                    print("** no instance was found **")
                else:
                    del storage.all()[name]
                    storage.save()
        except IndexError:
            print("** instance id is missing **")

    def do_update(self, ln):
        """Update if given exact object, exact attribute"""
        args = parse(ln)
        if len(args) >= 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg2 = args[3]
            arg2 = arg2.strip('"')
            arg2 = arg2.strip("'")
            setattr(storage.all()[key], args[2], cast(arg2))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name is missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class does not exist **")
        elif len(args) == 1:
            print("** instance id is missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance was found **")
        elif len(args) == 2:
            print("** attribute name is missing **")
        else:
            print("** value is missing **")
            
    def do_all(self, ln):
        """Print all objects or all objects of specified class"""
        args = parse(ln)
        object_list = []
        if len(ln) == 0:
            for obj in storage.all().values():
                object_list.append(obj)
            print(object_list)
        elif args[0] in HBNBCommand.classes:
            for key, obj in storage.all().items():
                if args[0] in key:
                    object_list.append(objs)
            print(object_list)
        else:
            print("** class does not exist **")

    def do_count(self, ln):
        """Display count of specified instances"""
        if ln in HBNBCommand.classes:
            count = 0
            for key, obj in storage.all().items():
                if line in key:
                    count += 1
            print(count)
        else:
            print("** class does not exist **")

    def default(self, ln):
        """Accepts class name followed by an argument"""
        args = ln.split('.')
        class_arg = args[0]
        if len(args) == 1:
            print("*** Unknown syntax: {}".format(ln))
            return
        try:
            args = args[1].split('(')
            command = args[0]
            if command == 'all':
                HBNBCommand.do_all(self, class_arg)
            elif command == 'count':
                HBNBCommand.do_count(self, class_arg)
            elif command == 'show':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip('"')
                id_arg = id_arg.strip("'")
                arg1 = class_arg + ' ' + id_arg
                HBNBCommand.do_show(self, arg1)
            elif command == 'destroy':
                args = args[1].split(')')
                id_arg = args[0]
                id_arg = id_arg.strip("'")
                id_arg = id_arg.strip('"')
                arg1 = class_arg + ' ' + id_arg
                HBNBCommand.do_destroy(self, arg1)
            elif command == 'update':
                args = args[1].split(',')
                id_arg = id_arg.strip('"')
                id_arg = args[0].strip("'")
                name_arg = args[1].strip(',')
                val_arg = args[2]
                name_arg = name_arg.strip(' ')
                name_arg = name_arg.strip('"')
                name_arg = name_arg.strip("'")
                val_arg = val_arg.strip(')')
                val_arg = val_arg.strip(' ')
                arg1 = class_arg + ' ' + id_arg + ' ' + name_arg + ' ' + val_arg
                HBNBCommand.do_update(self, arg1)
            else:
                print("*** Unknown syntax: {}".format(ln))
        except IndexError:
            print("*** Unknown syntax: {}".format(ln))

def parse(ln):
    """The Helper method to parse user input"""
    return tuple(ln.split())

if __name__ == "__main__":
    HBNBCommand().cmdloop()

#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import os
import enum
import json

from sys import platform


# -- classes --
class Types(enum.Enum):
    JSON = (0, ".json")
    XML = (1, ".xml")
    ZIP = (2, ".zip")

    def __init__(self, id, tp):
        self.id = id
        self.tp = tp


class ReadFile:
    # TODO: Make class accessable for all types (xml, json, zip) 
    def __init__(self, file_type=None):
        self.path = os.path.abspath('.')
        self.tp = file_type

    def create_file(self, name: str) -> bool:
        if self.tp is None:
            assert '.' not in name, "Неверный тип файла!"
        else:
            assert self.tp in name, "Неверный тип файла!"

        self.full_path = os.path.join(self.path, name)
        if name not in os.listdir('.'):
            with open(self.full_path, 'w') as _:
                pass
            return True
        else:
            return False


    def write_in_file(self, name, object_to_write):
        self.object_to_write = object_to_write
        self.full_path = os.path.join(self.path, name)
        try:
            assert name in os.listdir('.')
            if self.tp is None:
                with open(self.full_path, 'a') as fa:
                    fa.write(self.object_to_write)
            elif self.tp == Types.JSON.tp:
                with open(self.full_path, 'w') as fw:
                    json.dump(self.object_to_write, fw, indent=4)
            return True
        except OSError:
            return False
        except AssertionError:
            return False
    

    def print_file(self, name):
        self.full_path = os.path.join(self.path, name)
        try:
            with open(self.full_path, 'r') as fr:
                lines = fr.readlines()
            return lines
        except:
            return None
    

    def delete_file(self, name):
        self.full_path = os.path.join(self.path, name)
        try:
            os.remove(self.full_path)
            return True
        except OSError:
            return False


# -- functions --
def reset_terminal():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin":
        os.system('reset')
    elif platform == "win32":
        os.system('cls')


# -- launch --
if __name__ == "__main__":
    while True:
        reset_terminal()
        print("Выберите, что делать дальше:")
        print("1. Информация о дисках.\n2. Работа с файлами.\n3. Работа с JSON.\n4. Работа с XML.\n5. Работа с zip-архивом\n6. Выйти из программы.")

        case = input("\nВведите номер пункта: ")

        # Диски
        if case == '1':
            print("Инфа\nПо дискам\nИ еще\nЧето наверн")
        

        # Файлы
        if case == '2':
            while True:
                reset_terminal()
                print("> РАБОТА С ФАЙЛАМИ")
                print("Выберите, что делать дальше:")
                print("1. Создать файл.\n2. Записать строку в файл.\n3. Прочитать файл в консоль.\n4. Удалить файл.\n5. Выйти")
                case = input("\nВведите номер пункта: ")

                cur = ReadFile()

                try:
                    if case == '1':
                        name = input("Введите имя файла: ")
                        res = cur.create_file(name)
                        print(f"\nСоздание успешно ({cur.full_path})" if res else f"\nСоздание не удалось, похоже файл уже существует ({cur.full_path})")
                    
                    if case == '2':
                        name = input("Введите имя файла: ")
                        line = input("Введите строку для записи: ")
                        res = cur.write_in_file(name, line)
                        print(f"\nЗапись успешна ({cur.full_path})" if res else f"\nЗапись не удалось, похоже файла не существует ({cur.full_path})")
                    
                    if case == '3':
                        name = input("Введите имя файла: ")
                        lines = cur.print_file(name)
                        if lines is not None:
                            print("\nСоздержимое файла: ", end='') 
                            print(*lines)
                        else:
                            print(f"\nОшибка. Похоже файла не существует ({cur.full_path}).")

                    if case == '4':
                        name = input("Введите имя файла: ")
                        res = cur.delete_file(name)
                        print(f"\nФайл успешно удален ({cur.full_path})" if res else f"\nНеудалось удалить файл, похоже его не существует ({cur.full_path})")

                except AssertionError as e:
                    print('\n' + str(e))

                if case == '5':
                    break

                input("\nНажмите любую клавишу, чтобы продолжить...")
               

        # JSON
        if case == '3':
            while True:
                reset_terminal()
                print("> РАБОТА С JSON")
                print("Выберите, что делать дальше:")
                print("1. Создать файл в формате JSON.\n2. Создать новый объект. Выполнить сериализацию объекта в формате JSON и записать в файл.\n3. Прочитать файл в консоль.\n4. Удалить файл.\n5. Выйти")
                case = input("\nВведите номер пункта: ")

                cur = ReadFile(file_type=Types.JSON.tp)

                try:
                    if case == '1':
                        name = input("Введите имя файла: ")
                        res = cur.create_file(name)
                        print(f"\nСоздание успешно ({cur.full_path})" if res else f"\nСоздание не удалось, похоже файл уже существует ({cur.full_path})")


                    if case == '2':
                        name = input("Введите имя файла: ")
                        d = {
                            'Tested_Object':
                                {
                                    'Little_Object_0': 
                                    {
                                        'Go_Deeper_0': [0, 1, 2], 
                                        'Go_Deeper_1': '1',
                                        'Go_Deeper_2': 0.23123
                                        
                                    },
                                    'Little_Object_1': 
                                    {
                                        'Go_Deeper_0': None, 
                                        'Go_Deeper_1': True,
                                        'Go_Deeper_2': False
                                    }
                                }
                            }
                        print("Созданый оъект: ")
                        print(d)
                        res = cur.write_in_file(name, d)
                        print(f"\nЗапись успешна ({cur.full_path})" if res else f"\nЗапись не удалось, похоже файла не существует ({cur.full_path})")
                                

                    if case == '3':
                        name = input("Введите имя файла: ")
                        lines = cur.print_file(name)
                        if lines is not None:
                            print("\nСоздержимое файла: ", end='') 
                            print(*lines)
                        else:
                            print(f"\nОшибка. Похоже файла не существует ({cur.full_path}).")


                    if case == '4':
                        name = input("Введите имя файла: ")
                        res = cur.delete_file(name)
                        print(f"\nФайл успешно удален ({cur.full_path})" if res else f"\nНеудалось удалить файл, похоже его не существует ({cur.full_path})")


                except AssertionError as e:
                    print('\n' + str(e))

                if case == '5':
                    break
                
                input("\nНажмите любую клавишу, чтобы продолжить...")


        # XML
        if case == '4':
            ...


        # ZIP
        if case == '5':
            ...
        
        # EXIT ->
        if case == '6':
            break

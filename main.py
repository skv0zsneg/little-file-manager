#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import os
import enum
import json
import zipfile

from sys import platform
import xml.etree.ElementTree as xml
import xml.etree.cElementTree as ET


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
        if self.tp is not None:
            assert self.tp in name, "Неверный тип файла!"

        self.full_path = os.path.join(self.path, name)
        if name not in os.listdir('.'):
            if self.tp == Types.XML.tp:
                create_test_xml(self.full_path)
            elif self.tp == Types.ZIP.tp:
                with zipfile.ZipFile(self.full_path, 'w') as _:
                    pass
            else:
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
            elif self.tp == Types.XML.tp:
                write_in_xml(self.full_path, self.object_to_write)
            elif self.tp == Types.ZIP.tp:
                with zipfile.ZipFile(self.full_path, 'w') as zw:
                    zw.write(self.object_to_write)
            return True
        except OSError:
            return False
        except AssertionError:
            return False
    

    def print_file(self, name):
        self.full_path = os.path.join(self.path, name)
        try:
            if self.tp == Types.ZIP.tp:
                z = zipfile.ZipFile(self.full_path)
                

            else:
                with open(self.full_path, 'r') as fr:
                    lines = fr.readlines()
            return lines
        except:
            return None
    

    def delete_file(self, name):
        self.full_path = os.path.join(self.path, name)
        try:
            os.remove(self.full_path)
            if 'test_for_zip.xml' in os.listdir('.'):
                os.remove('test_for_zip.xml')
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


def create_test_xml(file_name):
    root = xml.Element("zAppointments")
    appt = xml.Element("appointment")
    root.append(appt)
    
    t_o = xml.SubElement(appt, "Tested_Object")
    t_o.text = "There is some text to Tested_Object..."
    
    l_o_0 = xml.SubElement(appt, "Little_Object_0")
    l_o_0.text = "There is some text to Little_Object_0..."
    
    l_o_1 = xml.SubElement(appt, "Little_Object_1")
    l_o_1.text = "There is some text to Little_Object_1..."
    
    y_t = xml.SubElement(appt, "YORE_TEXT_IS_HERE")
    y_t.text = ""
    
    l_o_2 = xml.SubElement(appt, "Little_Object_2")
    
    l_o_3 = xml.SubElement(appt, "Little_Object_3")
    l_o_3.text = "There is some text to Little_Object_3..."
    
    l_o_4 = xml.SubElement(appt, "Little_Object_4")
        
    tree = xml.ElementTree(root)
    with open(file_name, "wb") as fwd:
        tree.write(fwd)


def write_in_xml(file_name, text):
    tree = ET.ElementTree(file=file_name)
    root = tree.getroot()
    
    for y_t in root.iter("YORE_TEXT_IS_HERE"):
        y_t.text = text
    
    tree = ET.ElementTree(root)
    with open(file_name, "wb") as fwd:
        tree.write(fwd)


def print_file_zip_info(name):
    try:
        z = zipfile.ZipFile(name)
        z.printdir()
        return True
    except FileNotFoundError:
        return False


def extract_zip(name):
    try:
        z = zipfile.ZipFile(name)
        z.extractall()
        return os.path.join(os.path.abspath('.'), name)
    except:
        return None




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
                        print(f"\nФайл успешно удален ({cur.full_path})" if res else f"\nНе удалось удалить файл, похоже его не существует ({cur.full_path})")

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
                        print(f"\nЗапись успешна ({cur.full_path})" if res else f"\nЗапись не удалась, похоже файла не существует ({cur.full_path})")
                                

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
                        print(f"\nФайл успешно удален ({cur.full_path})" if res else f"\nНе удалось удалить файл, похоже его не существует ({cur.full_path})")


                except AssertionError as e:
                    print('\n' + str(e))

                if case == '5':
                    break
                
                input("\nНажмите любую клавишу, чтобы продолжить...")


        # XML
        if case == '4':
            while True:
                reset_terminal()
                print("> РАБОТА С XML")
                print("Выберите, что делать дальше:")
                print("1. Создать файл в формате XML.\n2. Записать в файл новые данные из консоли.\n3. Прочитать файл в консоль.\n4. Удалить файл.\n5. Выйти")
                case = input("\nВведите номер пункта: ")

                cur = ReadFile(file_type=Types.XML.tp)

                try:
                    if case == '1':
                        name = input("Введите имя файла: ")
                        res = cur.create_file(name)
                        print(f"\nСоздание успешно ({cur.full_path})" if res else f"\nСоздание не удалось, похоже файл уже существует ({cur.full_path})")


                    if case == '2':
                        name = input("Введите имя файла: ")
                        data = input("Введите данные для записи: ")
                        res = cur.write_in_file(name, data)
                        print(f"\nЗапись успешна ({cur.full_path})" if res else f"\nЗапись не удалась, похоже файла не существует ({cur.full_path})")
                                

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
                        print(f"\nФайл успешно удален ({cur.full_path})" if res else f"\nНе удалось удалить файл, похоже его не существует ({cur.full_path})")


                except AssertionError as e:
                    print('\n' + str(e))

                if case == '5':
                    break
                
                input("\nНажмите любую клавишу, чтобы продолжить...")


        # ZIP
        if case == '5':
            while True:
                reset_terminal()
                print("> РАБОТА С ZIP")
                print("Выберите, что делать дальше:")
                print("1. Создать архив в формате zip.\n2. Добавить файл в архив.\n3. Разархивировать файл и вывести данные о нем.\n4. Удалить файл и архив.\n5. Выйти")
                case = input("\nВведите номер пункта: ")

                cur = ReadFile(file_type=Types.ZIP.tp)

                try:
                    if case == '1':
                        name = input("Введите имя архива: ")
                        res = cur.create_file(name)
                        print(f"\nСоздание успешно ({cur.full_path})" if res else f"\nСоздание не удалось, похоже архив уже существует ({cur.full_path})")


                    if case == '2':
                        name = input("Введите имя архива: ")
                        test_file_name = "test_for_zip.xml"
                        create_test_xml(test_file_name)
                        print("Cоздан тестовый файл test_for_zip.xml")
                        res = cur.write_in_file(name, test_file_name)
                        os.remove(test_file_name)
                        print(f"\nЗапись успешна ({cur.full_path})" if res else f"\nЗапись не удалась, похоже архива не существует ({cur.full_path})")
                                

                    if case == '3':
                        name = input("Введите имя архива: ")
                        lines = cur.print_file(name)
                        print("Данные о файле: ")
                        if print_file_zip_info(name):
                            path_to_file = extract_zip(name)
                            print(f"\nФайл успешно разархивирован ({path_to_file}).")
                        else:
                            print("\nОшибка. Похоже файла не существует.")


                    if case == '4':
                        name = input("Введите имя архива: ")
                        res = cur.delete_file(name)
                        print(f"\nАрхив и файл успешно удалены ({cur.full_path})" if res else f"\nНе удалось удалить архив, похоже его не существует ({cur.full_path})")


                except AssertionError as e:
                    print('\n' + str(e))

                if case == '5':
                    break
                
                input("\nНажмите любую клавишу, чтобы продолжить...")

        
        #  __________
        # |          |
        # |  EXIT -> |
        # |__________|
        if case == '6':
            break

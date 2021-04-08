#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
import os

from ctypes import windll


# -- class --
class ReadFile:
    def __init__(self):
        self.path = os.path.abspath('.')

    def create_file(self, name: str) -> bool:
        self.full_path = os.path.join(self.path, name)
        if name not in os.listdir('.'):
            with open(self.full_path, 'w') as _:
                pass
            return True
        else:
            return False


    def write_in_file(self, name, line):
        self.line = line
        self.full_path = os.path.join(self.path, name)
        try:
            with open(self.full_path, 'a') as fa:
                fa.write(self.line)
            return True
        except OSError:
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


# -- launch --
if __name__ == "__main__":
    while True:
        print("\nВыберите, что делать дальше:")
        print("1. Информация о дисках.\n2. Работа с файлами.\n3. Работа с JSON.\n4. Работа с XML.\n5. Работа с zip-архивом")

        case = input("\nВведите номер пункта: ")

        # Диски
        if case == '1':
            print("Инфа\nПо дискам\nИ еще\nЧето наверн")
        
        # Файлы
        if case == '2':
            while True:
                print("\nВыберите, что делать дальше:")
                print("1. Создать файл.\n2. Записать строку в файл.\n3. Прочитать файл в консоль.\n4. Удалить файл.\n5. Выйти")
                case = input("\nВведите номер пункта: ")

                cur = ReadFile()

                if case == '1':
                    name = input("Введите имя файла: ")
                    res = cur.create_file(name)
                    print(f"\nСоздание успешно ({cur.full_path})" if res else f"\nСоздание не удалось, похоже файл уже существует ({cur.full_path})")
                
                if case == '2':
                    name = input("Введите имя файла: ")
                    line = input("Введите строку для записи: ")
                    res = cur.write_in_file(name, line)
                    print(f"\nЗапись успешна ({cur.full_path})" if res else f"\nЗапись не удалось, похоже файл не существует ({cur.full_path})")
                
                if case == '3':
                    name = input("Введите имя файла: ")
                    lines = cur.print_file(name)
                    if lines is not None:
                        print("\nСоздержимое файла: ", end='') 
                        print(*lines)
                    else:
                        print("\nОшибка. Похоже файла не существует.")

                if case == '4':
                    name = input("Введите имя файла: ")
                    res = cur.delete_file(name)
                    print(f"\nФайл успешно удален ({cur.full_path})" if res else f"\nНеудалось удалить файл, похоже его не существует ({cur.full_path})")

                if case == '5':
                    break
         
          

        # JSON
        if case == '3':
            ...
        
        # XML
        if case == '4':
            ...
        
        # ZIP
        if case == '5':
            ...

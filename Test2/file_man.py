# программный код файлового менеджера

# доступные команды:
# 1. mkdir - Создание папки (с указанием имени);
# 2. rmdir - Удаление папки по имени;
# 3. cd - Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
# 4. touch - Создание пустых файлов с указанием имени;
# 5. cat -w <file> <text> - Запись текста в файл;
# 6. cat <file> - Просмотр содержимого текстового файла;
# 7. rm - Удаление файлов по имени;
# 8. cp - Копирование файлов из одной папки в другую;
# 9. mv - Перемещение файлов;
# 10.rename - Переименование файлов.

import os, shutil
from pathlib import Path

HOME = Path.home() #input('Для начала введите полный путь СУЩЕСТВУЮЩЕЙ рабочей директории: ')


def mkdir(path): #создание папки в домашней папке
    global HOME
    path = Path(HOME, path)
    path.mkdir(parents=True)
    print(f'Создана папка {path} в рабочей директории.')
            
def rmdir(path): #удаление папки в домашней папке / с полным указанием пути
    global HOME
    path = Path(HOME, path) #если указали полный путь
    shutil.rmtree(path)# удаляем папку со всеми поддиректориями
    print(f'Удалена папка {path} в текущей директории.')



def cd(path): #перемещение между папками
    global HOME
    try:
        if '/' in path:
            if HOME in path:
                os.chdir(path)
            else:
                print('Ошибка! Нельзя переместиться выше рабочей папки.')
        else:
            os.chdir(f'{os.getcwd()}/{path}')
            print(os.getcwd())
    except  FileNotFoundError:
        print('Такой директории не существует!')



def touch(path): #создание пустого файла
    path = Path(os.getcwd(), path) 
    open(path, 'a').close()
    print(f'Создан файл {path} в рабочей директории.')
    
            

def cat(n): #просмотр файла и запись текста
    n = n.split(' ')
    if len(n)==1: #просмотр содержимового файла
        if '/' in n[0]:
            f = open(n[0])
            for line in f:
                print(line)
        else:
            f = open(os.getcwd()+'/'+n[0])
            for line in f:
                print(line)

    elif n[0]=='-w': #запись текста в файл
        if '/' in n[1]:
            f = open(n[1])
            for line in f:
                print(line)
        else:
            f = open(os.getcwd()+'/'+n[1], 'w')
            f.write(' '.join(n[2:]))
            f.close()
            print(f'Успешно! Данные записаны в файл {n[1]}') 



def rm(*paths): #удаление файлов
    global HOME
    paths = paths.split(' ')
    for path in paths:
        if '/' not in path: #если удаляем файл в текущей директории 
            name = path # запоминаем название файла для вывода
            path = os.path.join(os.getcwd(), path)
            os.remove(path)
            print(f'Удален файл {name} в текущей директории.')
        else:
            if HOME in path:
                path = Path() #если указали полный путь
                path.unlink()
                print(f'Удален файл {path}.')

def cp(source, destin): #копирование файла
    global HOME
    if '/' in (source and destin):
        if HOME in source and destin:
            shutil.copy(source, destin)
            print(f'Копирование файла успешно! {source} => {destin}') 
    elif '/' not in (source and destin):
        source = os.path.join(os.getcwd(), source)
        destin = os.path.join(os.getcwd(), destin)
        shutil.copy(source, destin)
        print(f'Копирование файла успешно! {source} => {destin}') 

def mv(source, destin): #перемещение файла
    global HOME
    if '/' in (source and destin):
        if HOME in source and destin:
            shutil.move(source, destin)
            print(f'Перемещение файла успешно! {source} => {destin}') 
    elif '/' not in (source and destin):
        source = os.path.join(os.getcwd(), source)
        destin = os.path.join(os.getcwd(), destin)
        shutil.move(source, destin)
        print(f'Перемещение файла успешно! {source} => {destin}') 

def rename(name, new): #переименование
    global HOME
    if '/' not in name: #если создаем файл в текущей директории 
        name = os.path.join(os.getcwd(), name)
        os.rename(name, new)
        print(f'Переименование успешно! {name} => {new}')
    else:
        if HOME in name:
            os.rename(name, new)
            print(f'Переименование успешно! {name} => {new}')


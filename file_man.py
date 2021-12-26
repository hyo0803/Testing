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

HOME = '/Users/yaseminhertek/for2test'


def mkdir(path): #создание папки в домашней папке
    path = Path(HOME, path)
    path.mkdir(parents=True)
    print(f'Создана папка {path} в рабочей директории.')
            
def rmdir(path): #удаление папки в домашней папке
    path = Path(HOME, path) 
    shutil.rmtree(path)# удаляем папку со всеми поддиректориями
    print(f'Удалена папка {path} в текущей директории.')



def cd(path): #перемещение между папками
    path = Path(HOME, path)
    os.chdir(path)
    print(f'Успешно! {os.getcwd()}')



def touch(path): #создание пустого файла
    path = Path(os.getcwd(), path) 
    open(path, 'a').close()
    print(f'Создан файл {path} в рабочей директории.')
    
            

def cat(n): #просмотр файла и запись текста
    n = n.split(' ')
    if len(n)==1: #просмотр содержимового файла
        f = open(HOME+'/'+n[0])
        for line in f:
            print(line)

    elif n[0]=='-w': #запись текста в файл
        f = open(HOME+'/'+n[1], 'w')
        f.write(' '.join(n[2:]))
        f.close()
        print(f'Успешно! Данные записаны в файл {n[1]}') 


def rm(path): #удаление файлов
    path = Path(HOME, path) #если указали полный путь
    path.unlink()
    print(f'Удален файл {path}.')

def cp(source, destin): #копирование файла
    source = os.path.join(HOME, source)
    destin = os.path.join(HOME, destin)
    shutil.copy(source, destin)
    print(f'Копирование файла успешно! {source} => {destin}') 

def mv(source, destin): #перемещение файла
    source = os.path.join(HOME, source)
    destin = os.path.join(HOME, destin)
    shutil.move(source, destin)
    print(f'Перемещение файла успешно! {source} => {destin}') 

def rename(name, new): #переименование
    os.rename(HOME+'/'+name, new)
    print(f'Переименование успешно! {name} => {new}')


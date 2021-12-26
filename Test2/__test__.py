# Тестирование файлового менеджера

# ---- К тесту предлагаются следующие команды:----
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

import pytest
import os, shutil
import file_man

# 1. mkdir - Создание папки (с указанием имени);
@pytest.fixture
def mkdir_fxt():
    file_man.mkdir('TestDirectory')
    return True
def mkdir_test(mkdir_fxt):
    assert mkdir_fxt == 1, 'mkdir Error'

# 2. rmdir - Удаление папки по имени;
@pytest.fixture
def rmdir_fxt():
    file_man.rmdir('TestDirectory')
    return True
def rmdir_test(rmdir_fxt):
    assert rmdir_fxt == 1, 'rmdir Error'



# 3. cd - Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
@pytest.fixture
def cd_fxt():
    file_man.cd('CD_TestDirectory')
    return True
def cd_test(cd_fxt):
    assert cd_fxt == 1, 'cd Error'


# 4. touch - Создание пустых файлов с указанием имени;
@pytest.fixture
def touch_fxt():
    file_man.touch('TestFile')
    return True
def touch_test(touch_fxt):
    assert touch_fxt == 1, 'touch Error'



# 5. cat -w <file> <text> - Запись текста в файл;
@pytest.fixture
def catW_fxt():
    file_man.cat('-w TestFile Hello world!')
    return True
def catW_test(catW_fxt):
    assert catW_fxt == 1, 'cat -w Error'

# 6. cat <file> - Просмотр содержимого текстового файла;
@pytest.fixture
def cat_fxt():
    file_man.cat('TestFile')
    return True
def cat_test(cat_fxt):
    assert cat_fxt == 1, 'cat Error' 


# 7. rm - Удаление файлов по имени;
@pytest.fixture
def rm_fxt():
    file_man.rm('TestFile')
    return True
def rm_test(rm_fxt):
    assert rm_fxt == 1, 'rm Error'      


# 8. cp - Копирование файлов из одной папки в другую;
@pytest.fixture
def cp_fxt():
    file_man.cp('CP_source', 'CP_destination')
    return True
def cp_test(cp_fxt):
    assert cp_fxt == 1, 'cp Error'   


# 9. mv - Перемещение файлов;
@pytest.fixture
def mv_fxt():
    file_man.mv('MV_DirSrc', 'MV_DirDstn')
    return True
def mv_test(mv_fxt):
    assert mv_fxt == 1, 'mv Error' 


# 10.rename - Переименование файлов.
@pytest.fixture
def rename_fxt():
    file_man.rename('Default', 'RenamedFile')
    return True
def rename_test(rename_fxt):
    assert rename_fxt == 1, 'rename Error' 
# Численные методы

### Лабораторная работа 5

Численное решение задачи Коши y' = 30y(x-0.2)(x-0.7), y_0 = 0.1 методами Эйлера, Коши, трапеций.

### Установка

```
#установка зависимостей
pip install -r requirements.txt
```

### Запуск

```
python3 main.py
```

### exe-файл

```
# создание exe-файла
pyinstaller main.py
```

### Другие методы численного решения задачи Коши

В файле method.py в классе Method можно добавить другие методы численного решения задачи Коши, подобно тем, что уже есть в классе Method. В этом случае нужно обязательно изменить атрибут dict_methods у экземпляра класса Method и возвращаемый список статического метода get_name_methods класса Method.

В файле method.py в классе SolutionCauchyProblem можно сделать свое точное решение задачи Коши.

### Иллюстрация к проекту
![Иллюстрация к проекту](https://github.com/ArtemBiliksin/Numerical-methods-lab-5/blob/master/Pictures/image1.png)
![Иллюстрация к проекту](https://github.com/ArtemBiliksin/Numerical-methods-lab-5/blob/master/Pictures/image2.png)
![Иллюстрация к проекту](https://github.com/ArtemBiliksin/Numerical-methods-lab-5/blob/master/Pictures/image3.png)

### FASTA OOP

Домашнее задание ООП и инкапсуляция

В программе реализованы два класса:

* "Seq" - хранит последовательность и заголовок;
* "FastaReader" - проверяет FASTA-файл и читает его по записям.

Программа умеет:

* находить длину последовательности;
* определять нуклеотидный или белковый алфавит;
* выводить объект в формате FASTA;
* читать файл с помощью генератора.



Структура проекта

fasta-oop/

├── fasta.py # классы Seq и FastaReader

├── main.py # демонстрационная программа

├── README.md # этот файл

├── requirements.txt # зависимости

├── examples/

│ └── demo.fasta # пример FASTA-файла

├── docs/

│ └── index.html # HTML-документация

├── uml/

│ └── class\_diagram.puml # UML-диаграмма классов

└── tests/

└── test\_fasta.py # тесты



### Запуск

bash
python main.py



### Тесты

bash
python -m unittest discover -s tests -v



### Документация

HTML-документация находится в папке "docs"

### UML

Исходник UML находится в "uml/class\_diagram.puml"


class Seq:
    '''
    header - строка с заголовком из fasta (содержимое), без >
    sequence - последоваткльность, информация о ней
    '''
    def __init__(self, header, sequence):
        self.__header=header.strip()
        self.__sequence=sequence.replace(" ", "").replace("\n", "").upper()
        
    @property
    def sequence(self):
        return self.__sequence
    
    @property
    def header(self):
        return self.__header
    
    
    @property
    def alphabet(self): #будет определять тип последовательности: нуклеотидная или белковую
        nucleotide = set("AGCTU")
        symbols = set(self.__sequence)
   
        if symbols <= nucleotide:
            return "nucleotide"
        else:
            return "protein"
   
    def __len__(self): #возвращает длину последовательности
        return len(self.__sequence)
   
    def __str__(self): #возвращает строку в формате FASTA
        return f">{self.__header}\n{self.__sequence}"
    
class FastaReader:
    '''
    ответственен за чтение файла в формате fasta
    определяет соответствие файла формату и читает файл по записям,
    т.е возвращать отдельные экземпляры класса Seq
    '''
    
    def __init__(self,filename):
        self.__filename=filename
        
    def is_fasta(self):
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                has_header = False  #ещё не встречали заголовок
                has_sequence = False #ещё не встречали последовательность


                for line in file: #идем построчно убираем пробелы и переносы по краям
                    line = line.strip()

                    if not line:
                        continue

                    if line.startswith(">"):
                        if has_header and not has_sequence: #был заголовок и следом еще один
                            return False

                        has_header = True
                        has_sequence = False


                    else:
                        if not has_header: #если последовательность встречается до первого заголовка
                            return False

                        has_sequence = True


                return has_header and has_sequence

        except OSError:
            return False
    
    def read(self):
        #генератор. Возвращает записи FASTA по одной

        with open(self.__filename, "r", encoding="utf-8") as file:
            header = None #заголовка ещё нет
            sequence = []

            for line in file:
                line = line.strip()

                if not line: #пропускаем пустые строки
                    continue

                if line.startswith(">"):

                    if header is not None: #не первая запись тк не первый заголовок
                        yield Seq(header, "".join(sequence))

                    header = line[1:] #срезаем заголовок
                    sequence = []

                else:
                    if header is None: #не видели ни одного заголовка
                        raise ValueError("Последовательность без заголовка")

                    sequence.append(line) #добавляем строку в список

            if header is not None:
                yield Seq(header, "".join(sequence)) 
    
    def __iter__(self):
        return self.read()

def main():
    print("FASTA program")
    print()

    #Для проверки программа использует заранее подготовленный файл
    reader = FastaReader("examples/demo.fasta")

    print("Это FASTA:", reader.is_fasta())
    print()

    for seq in reader:
        print("Имя:", seq.header)
        print("Длина:", len(seq))
        print("Алфавит:", seq.alphabet)
        print("Последовательность:")
        print(seq)
        print()


if __name__ == "__main__":
    main()
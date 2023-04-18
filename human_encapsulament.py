class Pessoa:
    def __init__(self,nome: str, idade: int, altura: float, sexo: str,estado: str = 'vivo', estado_civil: str = 'solteiro', conjuge = None):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = conjuge
    

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        print('Sem permissão!')

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self,idade):
        print('Sem permissão!')

    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self,peso):
        self.__peso = peso
    
    @property
    def altura(self):
        return self.__altura
    
    @altura.setter
    def altura(self,altura):
        if self.__estado == 'vivo' and self.__idade < 21:
            self.__altura = altura
        else:
            print('Sem permissão!')

    @property
    def sexo(self):
        return self.__sexo
    
    @sexo.setter
    def sexo(self,sexo):
        print('Sem permissão!')

    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self,estado):
        self.__estado = estado
    
    @property
    def estado_civil(self):
        return self.__estado_civil
    
    @estado_civil.setter
    def estado_civil(self,estado_civil):
        if self.__estado == 'vivo' and self.__idade <= 18 and self.__estado_civil =! 'casado':
            self.__estado_civil = estado_civil
        else:
            print('Sem permissão!')
    
    @property
    def conjuge(self):
        return self.__conjuge
    
    @conjuge.setter
    def conjuge(self,conjuge):
        self.__conjuge = conjuge
        
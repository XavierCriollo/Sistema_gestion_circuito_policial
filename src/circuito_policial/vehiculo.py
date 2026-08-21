class Vehiculo: 
    def __init__(self, codigo, placa, modelo, estado):
        self.__codigo = codigo
        self.__placa = placa
        self.__modelo = modelo
        self.__estado = estado
        
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, codigo):
        self.__codigo = codigo
        
    def get_placa(self):
            return self.__placa
        
    def set_placa(self, placa):
            self.__placa = placa
            
    def get_modelo(self):
            return self.__modelo
        
    def set_modelo(self, modelo):
            self.__modelo = modelo
            
    def get_estado(self):
                return self.__estado
            
    def set_estado(self, estado):
                self.__estado = estado
    

        
class Engrane():
    def __init__(self, n_dientes, radio):
        self.n_dientes = n_dientes
        self.radio = radio
    
    def relacion_velocidad(self, engrane):
        rel_velocidad = self.n_dientes / engrane.n_dientes
        return rel_velocidad

if __name__ == '__main__':
    engrane_grande = Engrane(40, 0.10)
    engrane_chico = Engrane(20, 0.10)
    print(engrane_grande.relacion_velocidad(engrane_chico))


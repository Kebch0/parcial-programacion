from Pelicula import Pelicula

if __name__ == "__main__":
    print()
    pelicula1 = Pelicula(123546789, "La máscara", 101, "Chuck Russell")
    pelicula2 = Pelicula(472798822,"Los indestructibles 4", 143, "Scott Waugh")
    pelicula3 = Pelicula(482748822,"Una pareja explosiva 3", 91, "Brett Ratner")
    
    print(pelicula1)
    print(pelicula2)
    print(pelicula3)
    print()

    print("Prestar pelicula1:", pelicula1.prestar())
    print("Volver a prestar pelicula1:", pelicula1.prestar())
    print()

    print("Devolver pelicula1:", pelicula1.devolver())
    print("Volver a devolver pelicula1:", pelicula1.devolver())
    print()

    print(pelicula2.costo_reproduccion(300))
    print()

    print("Título original de pelicula3:", pelicula3.get_titulo())
    pelicula3.set_titulo("una pareja explosiva")
    print("Nuevo título de pelicula3:", pelicula3.get_titulo())
    print()

    print("¿pelicula1 y pelicula3 tienen el mismo código?", pelicula1 == pelicula3)
    print("¿pelicula1 y pelicula2 tienen el mismo código?", pelicula1 == pelicula2)

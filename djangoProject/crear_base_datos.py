import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('Sistema_Reservacion.sqlite')
cursor = conn.cursor()

# Crear la tabla de estados
cursor.execute('''
CREATE TABLE Estados (
    EstadoID INTEGER PRIMARY KEY,
    Descripcion VARCHAR(80) NOT NULL
);
''')

# Crear las demás tablas con la referencia a Estados
cursor.execute('''
CREATE TABLE Campus (
    Identificador INTEGER PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE Edificios (
    Identificador INTEGER PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL,
    CampusId INTEGER NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (CampusId) REFERENCES Campus(Identificador),
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE TiposAulas (
    Identificador INTEGER PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE AulasLaboratorios (
    Identificador INTEGER PRIMARY KEY,
    Descripcion VARCHAR(255) NOT NULL,
    TipoAulaId INTEGER NOT NULL,
    EdificioId INTEGER NOT NULL,
    Capacidad INTEGER NOT NULL,
    CuposReservados INTEGER NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (TipoAulaId) REFERENCES TiposAulas(Identificador),
    FOREIGN KEY (EdificioId) REFERENCES Edificios(Identificador),
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE TiposUsuarios (
    Identificador INTEGER PRIMARY KEY,
    Descripcion VARCHAR(80) NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE Usuarios (
    Identificador INTEGER PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Cedula VARCHAR(15) NOT NULL UNIQUE,
    NoCarnet VARCHAR(20) NOT NULL UNIQUE,
    TipoUsuarioId INTEGER NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (TipoUsuarioId) REFERENCES TiposUsuarios(Identificador),
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE Tandas (
    Identificador INTEGER PRIMARY KEY,
    Descripcion VARCHAR(80) NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE Empleados (
    Identificador INTEGER PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL,
    Cedula VARCHAR(15) NOT NULL UNIQUE,
    TandaId INTEGER NOT NULL,
    FechaIngreso DATE NOT NULL,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (TandaId) REFERENCES Tandas(Identificador),
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

cursor.execute('''
CREATE TABLE ProcesoReservacionHoras (
    NoReservacion INTEGER PRIMARY KEY,
    EmpleadoId INTEGER NOT NULL,
    AulaId INTEGER NOT NULL,
    UsuarioId INTEGER NOT NULL,
    FechaReservacion DATE NOT NULL,
    CantidadHoras INTEGER NOT NULL,
    Comentario TEXT,
    EstadoID INTEGER NOT NULL,
    FOREIGN KEY (EmpleadoId) REFERENCES Empleados(Identificador),
    FOREIGN KEY (AulaId) REFERENCES AulasLaboratorios(Identificador),
    FOREIGN KEY (UsuarioId) REFERENCES Usuarios(Identificador),
    FOREIGN KEY (EstadoID) REFERENCES Estados(EstadoID)
);
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tablas creadas con éxito.")

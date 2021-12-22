from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

Base=declarative_base()

class Alumno(Base):
    __tablename__="alumno"   
    id=Column(Integer,Sequence('alumno_seq_id'),primary_key=True)
    nombreAlumno=Column(String)
    apellidoAlumno=Column(String)
    curso_idAlumno=Column(Integer,ForeignKey('curso.id'))
    
    cursos=relationship("Curso",back_populates='alumnos')
    def __repr__(self):
        return'{}{}'.format(self.nombreAlumno, self.apellidoAlumno)

class Curso(Base):
    __tablename__='curso'
    id=Column(Integer, Sequence('curso_seq_id'),primary_key=True)
    nombreCurso=Column(String)
        
    alumnos=relationship("Alumno",back_populates='cursos')
    hora_curso=relationship("Horario",back_populates='curso_hora')
    def __repr__(self):
        return'{}'.format(self.nombreCurso)

class Horario(Base):
    __tablename__='horario'
    id=Column(Integer, Sequence('horario_seq_id'),primary_key=True)
    dia=Column(String)
    hora_inicio=Column(String)
    hora_fin=Column(String)
    profesor_id=Column(Integer,ForeignKey('profesor.id'))
    curso_id=Column(Integer,ForeignKey('curso.id'))
    
    curso_hora=relationship("Curso",back_populates='hora_curso')
    curso_profesor=relationship("Profesor",back_populates='profesor_curso')

    def __repr__(self):
        return'{}{}{}'.format(self.dia,self.hora_inicio, self.hora_fin)

class Profesor(Base):
    __tablename__='profesor'
    id=Column(Integer, Sequence('profesor_seq_id'),primary_key=True)
    nombreProfesor=Column(String)
    apellidoProfesor=Column(String)
    
    profesor_curso=relationship("Horario",back_populates='curso_profesor')
    def __repr__(self):
        return'{}{}'.format(self.nombreProfesor, self.apellidoProfesor)



def main(*args, **kwargs):

    engine=create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    Session=sessionmaker(bind=engine)
    session=Session()


    print()
    print("*********** SISTEMA PARA ESCUELAS ***********")
    print()

    #Registrar un curso
    cursoNuevo=Curso(nombreCurso='Manejo de bases de datos con Python')
    print("DATOS DEL CURSO REGISTRADO:")
    print("Nombre: " + cursoNuevo.nombreCurso)
    session.add(cursoNuevo)
    print()
    print("--------------------------------------------------")
    print()

    # Registrar un alumno
    alumnoNuevo=Alumno(nombreAlumno='Martina', apellidoAlumno='Apellido')
    print("DATOS DEL ALUMNO REGISTRADO:")
    print("Nombre: " + alumnoNuevo.nombreAlumno)
    print("Apellido: " + alumnoNuevo.apellidoAlumno)
    session.add(alumnoNuevo)
    alumnoNuevo.cursos= cursoNuevo
    print("CURSOS DEL ALUMNO:")
    print(alumnoNuevo.cursos)
    print()
    print("--------------------------------------------------")
    print()

    # Registrar un alumno
    alumnoNuevo2=Alumno(nombreAlumno='Estudiante', apellidoAlumno='Prueba')
    print("DATOS DEL ALUMNO REGISTRADO:")
    print("Nombre: " + alumnoNuevo2.nombreAlumno)
    print("Apellido: " + alumnoNuevo2.apellidoAlumno)
    session.add(alumnoNuevo2)
    alumnoNuevo2.cursos= cursoNuevo
    print("CURSOS DEL ALUMNO:")
    print(alumnoNuevo2.cursos)
    print()
    print("--------------------------------------------------")
    print()

    #Registrar un profesor 
    profesorNuevo= Profesor(nombreProfesor='Agustin',apellidoProfesor=' Olmedo')
    print("DATOS DEL PROFESOR REGISTRADO:")
    print("Nombre: " + profesorNuevo.nombreProfesor)
    print("Apellido: " + profesorNuevo.apellidoProfesor)
    session.add(profesorNuevo)
    print()
    print("--------------------------------------------------")
    print()

    #Agregar un horario
    horarioNuevo=Horario(dia='Martes ',hora_inicio=" 9:00", hora_fin=' 12:00')
    session.add(horarioNuevo)

    #Asignar horario a curso y profesor
    horarioNuevo.curso_hora= cursoNuevo
    horarioNuevo.curso_profesor= profesorNuevo

    #Consultas 
    print ("INFORMACION SOBRE ALUMNOS, PROFESORES Y CURSOS: ")
    print ("Curso: ")
    print(session.query(Curso).join(Horario,Profesor).filter(Profesor.nombreProfesor == profesorNuevo.nombreProfesor).all())
    print("Horario del curso:")
    print(session.query(Horario).join(Profesor).filter(Profesor.nombreProfesor== profesorNuevo.nombreProfesor).all())
    print("Profesor/es del curso")
    print(session.query(Profesor).join(Horario).filter(Horario.id == horarioNuevo.id).all())
    print("Alumnos del curso: ")
    print(session.query(Alumno).join(Curso).filter(Curso.nombreCurso == cursoNuevo.nombreCurso).all())



    session.commit()

if __name__ == "__main__":
    main()

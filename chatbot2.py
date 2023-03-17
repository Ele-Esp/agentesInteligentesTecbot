#chatbot that analyzes a string that the user inputs and takes keywords to answer the question
#it is meant to be used by Tecnologico de Monterrey students to ask questions about the school
pregunta=input("Pregunta: ")

noMoreQuestions=True

possibleKeywords=[[
    "carrera",
    "carreras"],
    [
    "cursos",
    "cursos en línea"],
    [       
    "becas", "beca"],
    [
    "servicios"],
    [
    "campus", "sedes"],
    [
    "colegiaturas"],
    [
    "inscripciones", "inscripción", "inscribo", "inscribir", "inscribirme", "inscribirse"
    ],
    [
    "horarios",
    "horios de atención",
    ]
]
responses=[
    [
        "Las carreras que ofrece el Tecnológico de Monterrey son: Ingeniería en Sistemas Computacionales, Ingeniería en Mecatrónica, Ingeniería en Energías Renovables, Ingeniería en Gestión Empresarial, Ingeniería en Gestión de la Tecnología de la Información, Ingeniería en Gestión de la Innovación, [...]"
    ],
    [
        "Los cursos en línea que ofrece el Tecnológico de Monterrey son: Programación Orientada a Objetos, Programación de Aplicaciones Web, Programación de Aplicaciones Móviles, Programación de Aplicaciones de Escritorio, Programación de Aplicaciones de Videojuegos, Programación de Aplicaciones de Inteligencia Artificial, [...]"
    ],
    [
        "Las becas que ofrece el Tecnológico de Monterrey son: Becas de Excelencia Académica, Becas de Excelencia Deportiva, Becas de Excelencia Artística, Becas de Excelencia en Ciencias, Becas de Excelencia en Tecnología, Becas de Excelencia en Emprendimiento, [...]"
    ],
    [
        "Los servicios que ofrece el Tecnológico de Monterrey son: Biblioteca, Cafetería, Laboratorios, Salones de Clase, Salones de Estudio, Salones de Juntas, [...]"
    ],
    [
        "Los campus que ofrece el Tecnológico de Monterrey son: Campus Monterrey, Campus Santa Fe, Campus Querétaro, Campus Guadalajara, Campus Puebla, Campus León, [...]"
    ],
    [
        "Las colegiaturas que ofrece el Tecnológico de Monterrey son: $ 15,000.00, $ 16,000.00, $ 17,000.00, $ 18,000.00, $ 19,000.00, $ 20,000.00, [...]"
    ],
    [
        "Las inscripciones que ofrece el Tecnológico de Monterrey son en Abril y Junio, y de Octubre a Diciembre"
    ],
    [
        "Los horarios de atención que ofrece el Tecnológico de Monterrey son: Lunes a Viernes de 8:00 a 20:00, Sábados de 9:00 a 14:00, Domingos de 10:00 a 16:00"
    ]
]

def locateKeyWords():
    for i in range(len(possibleKeywords)):
        for j in range(len(possibleKeywords[i])):
            if possibleKeywords[i][j] in pregunta.lower():
                return i
    return -1

def answerQuestion():
    global noMoreQuestions
    index=locateKeyWords()
    if index==-1:
        print("No puedo respondere tu pregunta, te pasaré con un agente.")
        noMoreQuestions=False
    else:
        print(responses[index][0])

while noMoreQuestions:
    answerQuestion()
    finished=input("¿tienes otra pregunta?: ")
    if "no" in finished.lower():
        noMoreQuestions=False
    else :
        if "si" in finished.lower() or "sí" in finished.lower():
            pregunta=input("Pregunta: ")
        else:
            pregunta=finished
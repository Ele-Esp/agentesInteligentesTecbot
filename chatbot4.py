context=""
dictFirstLayer={
    ("carrera","carreras","carreras en línea"): ["Las carreras que ofrece el Tecnológico de Monterrey son: Ingeniería en Sistemas Computacionales, Ingeniería en Mecatrónica, Ingeniería en Energías Renovables, Ingeniería en Gestión Empresarial, Ingeniería en Gestión de la Tecnología de la Información, Ingeniería en Gestión de la Innovación, [...]"],
    ("becas", "beca"): ["Las becas que ofrece el Tecnológico de Monterrey son: Becas de Excelencia Académica, Becas de Excelencia Deportiva, Becas de Excelencia Artística, Becas de Excelencia en Ciencias, Becas de Excelencia en Tecnología, Becas de Excelencia en Emprendimiento, [...]"],
    ("servicios",): ["Los servicios que ofrece el Tecnológico de Monterrey son: Biblioteca, Cafetería, Laboratorios, Salones de Clase, Salones de Estudio, Salones de Juntas, [...]"],
    ("campus", "sedes"): ["Los campus que ofrece el Tecnológico de Monterrey son: Campus Monterrey, Campus Santa Fe, Campus Querétaro, Campus Guadalajara, Campus Puebla, Campus León, [...]"],
    ("colegiaturas",): ["Las colegiaturas que ofrece el Tecnológico de Monterrey son: $ 15,000.00, $ 16,000.00, $ 17,000.00, $ 18,000.00, $ 19,000.00, $ 20,000.00, [...]"],
    ("inscripciones", "inscripción", "inscribo", "inscribir", "inscribirme", "inscribirse"): ["Las inscripciones que ofrece el Tecnológico de Monterrey son en Abril y Junio, y de Octubre a Diciembre"],
    ("horarios","horios de atención"): ["Los horarios de atención que ofrece el Tecnológico de Monterrey son: Lunes a Viernes de 8:00 a 20:00, Sábados de 9:00 a 14:00, Domingos de 10:00 a 16:00"]
    }

#profundiza en carrera, becas y campus, en caso de que el usuario haga una pregunta sobre cualquiera de esos
dictSecondLayerCarreras={
  ("ingeniería en sistemas computacionales","sistemas computacionales", "ingeniería en sistemas", "sistemas"): ["La carrera en Ingeniería en Sistemas Computacionales se enfoca en la creación, diseño y mantenimiento de software, hardware y redes de computadoras para la solución de problemas informáticos. Los egresados podrán desempeñarse en áreas de desarrollo de software, seguridad informática, análisis de sistemas y tecnologías de la información."],
  ("ingeniería en mecatrónica","mecatrónica"): ["La carrera en Ingeniería en Mecatrónica se enfoca en la integración de sistemas mecánicos, eléctricos y electrónicos para la creación de sistemas automatizados y de control. Los egresados podrán desempeñarse en áreas de automatización industrial, robótica, diseño de sistemas y control de procesos."],
  ("ingeniería en energías renovables","energías renovables", "ingeniería en energías renovables", "energías","renovables"): ["La carrera en Ingeniería en Energías Renovables se enfoca en la creación y aplicación de tecnologías para la generación de energía a partir de fuentes renovables y limpias. Los egresados podrán desempeñarse en áreas de diseño y mantenimiento de sistemas de energía renovable, eficiencia energética, y en empresas relacionadas con la energía sostenible."],
  ("ingeniería en gestión empresarial","gestión empresarial", "ingeniería en gestión empresarial", "gestión","empresarial"): ["La carrera en Ingeniería en Gestión Empresarial se enfoca en la formación de profesionales capaces de integrar soluciones tecnológicas y de innovación para el desarrollo de negocios y organizaciones. Los egresados podrán desempeñarse en áreas de análisis y mejora de procesos empresariales, desarrollo de proyectos tecnológicos y consultoría en innovación y tecnología."],
  ("gestión de la información", "gestión", "teconlogías de la información", "tecnologías", "información"): ["La carrera en Gestión de la Información se enfoca en la gestión y organización de información en diferentes contextos, con la finalidad de optimizar su uso y acceso. Los egresados podrán desempeñarse en áreas de gestión de datos, análisis de información, seguridad de la información y en empresas relacionadas con la tecnología de la información y comunicación."],
  }
dictSecondLayerBecas={
    ("becas de excelencia académica","excelencia académica","becas de excelencia académica","excelencia,académica"): ["La beca de excelencia académica está dirigida a estudiantes con un alto desempeño académico y se otorga en base al promedio del último año de estudios. Los beneficios incluyen un descuento en la colegiatura y la posibilidad de realizar intercambios académicos en universidades internacionales de prestigio."],
    ("becas de excelencia deportiva","excelencia deportiva","becas de excelencia deportiva","excelencia,deportiva"): ["La beca de excelencia deportiva está dirigida a estudiantes que se destacan en alguna disciplina deportiva. Los beneficios incluyen un descuento en la colegiatura, la posibilidad de combinar estudios con entrenamientos y participación en eventos deportivos representando a la institución."],
    ("becas de excelencia artística","excelencia artística","becas de excelencia artística","excelencia,artística"): ["La beca de excelencia artística está dirigida a estudiantes con talento en alguna disciplina artística. Los beneficios incluyen un descuento en la colegiatura y la posibilidad de desarrollar proyectos creativos dentro y fuera de la institución."],
    ("becas de excelencia en ciencias","excelencia en ciencias","becas de excelencia en ciencias","excelencia,ciencias"): ["La beca de excelencia en ciencias está dirigida a estudiantes con aptitudes y habilidades en el campo de las ciencias. Los beneficios incluyen un descuento en la colegiatura y la posibilidad de participar en proyectos de investigación junto a profesores de la institución."]
}
dictSecondLayerCampus={
    ("campus monterrey","monterrey"): ["El campus Monterrey se encuentra ubicado en la ciudad de Monterrey, Nuevo León. Cuenta con 4 edificios, 2 salones de clase, 2 laboratorios, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus santa fe","santa fe"): ["El campus Santa Fe se encuentra ubicado en la ciudad de Monterrey, Nuevo León. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus querétaro","querétaro"): ["El campus Querétaro se encuentra ubicado en la ciudad de Querétaro, Querétaro. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus puebla","puebla"): ["El campus Puebla se encuentra ubicado en la ciudad de Puebla, Puebla. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus guadalajara","guadalajara"): ["El campus Guadalajara se encuentra ubicado en la ciudad de Guadalajara, Jalisco. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
    ("campus méxico","méxico"): ["El campus México se encuentra ubicado en la ciudad de México, Distrito Federal. Cuenta con 2 edificios, 1 salón de clase, 1 laboratorio, 1 biblioteca, 1 cafetería, 1 salón de juntas, 1 salón de estudio, 1 salón de conferencias y 1 auditorio."],
}
dictThirdLayerCarreras={
    ("1er semestre", "1°", "1", "primer semestre", "primer" ): ["Puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("2do semestre", "2°", "2", "segundo semestre", "segundo" ): ["Puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("3er semestre", "3°", "3", "tercer semestre", "tercer" ): ["Puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("4to semestre", "4°", "4", "cuarto semestre", "cuarto" ): ["Puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],
    ("5to semestre", "5°", "5", "quinto semestre", "quinto" ): ["Puedes encontrar la información de las carreras en el siguiente link: https://www.tec.mx/es/estudiar-en-tec/carreras"],

}
dictFourthLayerMaterias={
    ("Matemáticas", "matematicas", "mate"):["La materia de introducción a las matemáticas es una materia que se imparte en el primer semestre de la carrera de Matemáticas. En esta materia se estudian los conceptos básicos de álgebra, geometría y trigonometría."],
}

dictFifthLayerProfesores={
    ("profesor", "profesores"): ["En el siguiente link puedes encontrar la información de los profesores: https://www.tec.mx/es/estudiar-en-tec/carreras"],
}


def main():

    global context
#""" La función principal va a llevar una función llamada responderPregunta(inputText) que va a tomar de argumento el string que dé el usuario de la pregunta
#Entonces van a buscar con un for word in pregunta para cada tupla del diccionario de la primera capa, si encuentra algo, busca otro for word en cada diccionario que diga secondLayer si encuentra algo, se sigue así hasta la capa 5
#Si no encuentra algo en alguna capa, responde hasta donde se quedó, si no encuentra algo desde la capa 1, pasa a un agente.
#En cada if debe regresar el input al usuario preguntando si quiere saber algo más de la información que tiene además de responder, y se debe buscar desde esa capa

    print("Hola, soy el asistente virtual TecBot, ¿en qué te puedo ayudar?")
    while True:
        inputText = input("\nPregunta: ").lower()
        if inputText == "salir":
            break
        else:
            responderPregunta(inputText)

def searchInDict(inputText, dict):
    #dict has a touple of words as key and a string as value
    for key in dict:
        for word in key:
            if word in inputText:
                return key
    return None


def responderPregunta(inputText):
    global context
    inputText= inputText + " " + context
    for key in dictFirstLayer:
        for word in key:
            if word in inputText:
                for key2 in dictSecondLayerCarreras:
                    for word2 in key2:
                        if word2 in inputText:
                            for key3 in dictThirdLayerCarreras:
                                for word3 in key3:
                                    if word3 in inputText:
                                        print(dictThirdLayerCarreras[key3])
                                        return
                            print(dictSecondLayerCarreras[key2])
                            return
                for key2 in dictSecondLayerBecas:
                    for word2 in key2:
                        if word2 in inputText:
                            print(dictSecondLayerBecas[key2])
                            return
                for key2 in dictSecondLayerCampus:
                    for word2 in key2:
                        if word2 in inputText:
                            print(dictSecondLayerCampus[key2])
                            return
                print(dictFirstLayer[key])
                print("\n¿Quieres saber algo más de algo en particular?")
                a=input().lower()
                if a != "no":
                    if a == "si" or a == "sí":
                        print("\n¿Qué quieres saber?")
                        b=input().lower()
                        responderPregunta(key[0]+b)
                    else:
                        context= key[0]
                        responderPregunta(key[0]+a)

                return
    print("No encontré la información que buscas, ¿quieres que te pase con un agente?")




if __name__ == '__main__':
    main()  

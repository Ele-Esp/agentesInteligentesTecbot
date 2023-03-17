import spacy

# Load the pre-trained English language model
print("Loading model...")
nlp = spacy.load("es_core_news_sm")
print("Done loading model")

# Define a list of keywords related to Tecnológico de Monterrey
keywords = ["Tecnológico de Monterrey", "ITESM", "campus", "programas", "admisiones", "becas", "colegiaturas", "egresados", "investigación", "innovación"]

# Define a dictionary of responses to each possible keyword
respuestas = {
    "Tecnológico de Monterrey": "Tecnológico de Monterrey (Monterrey Tech) es una universidad privada y sin fines de lucro con 26 campus en todo México. Es considerada una de las mejores universidades de América Latina.",
    "ITESM": "ITESM significa Instituto Tecnológico y de Estudios Superiores de Monterrey, que es el nombre completo de Tecnológico de Monterrey (Monterrey Tech).",
    "campus": "Tecnológico de Monterrey tiene 26 campus en todo México, incluyendo uno en Monterrey, Guadalajara y Ciudad de México.",
    "programas": "Tecnológico de Monterrey ofrece una amplia variedad de programas de pregrado, posgrado y profesional en campos como negocios, ingeniería, ciencias sociales, humanidades y más.",
    "admisiones": "Para aplicar al Tecnológico de Monterrey, debes enviar una solicitud en línea y proporcionar transcripciones académicas, puntajes de pruebas, ensayos y cartas de recomendación. El proceso de admisión es altamente competitivo.",
    "becas": "Tecnológico de Monterrey ofrece becas y ayuda financiera a los estudiantes en función del mérito académico, la necesidad financiera y otros criterios.",
    "matrícula": "Las tarifas de matrícula en Tecnológico de Monterrey varían según el programa y el campus. Pueden oscilar entre aproximadamente $ 10,000 y $ 30,000 por año.",
    "egresados": "Tecnológico de Monterrey tiene una gran red de exalumnos en todo el mundo que son líderes en diversas industrias y campos.",
    "investigación": "Tecnológico de Monterrey está comprometido con la investigación y la innovación. Su profesorado y estudiantes llevan a cabo investigaciones en diversos campos y trabajan en proyectos de vanguardia.",
    "innovación": "Tecnológico de Monterrey está comprometido con la investigación y la innovación. Su profesorado y estudiantes llevan a cabo investigaciones en diversos campos y trabajan en proyectos de vanguardia."
}
# Define a function to process the user input and return the appropriate response
def process_input(input_text):
    # Tokenize the input text using the spaCy model
    doc = nlp(input_text.lower())
    
    # Loop through the keywords and check if any appear in the input text
    for token in doc:
         if token.text in respuestas:
            return respuestas[token.text]
    
    # If no keywords are found, return None
    return None

# Define a function to handle the user input and return the appropriate response
def respond(input_text):
    # Get the response from the process_input function
    response = process_input(input_text)
    
    # If the response is not None, return the response
    if response is not None:
        return response
    # If the response is None, return a default response
    else:
        return "Lo siento, no entiendo tu pregunta. Te pasaré con un agente"

#main function
def main():
    # Print a welcome message
    print("Bienvenido a la línea de ayuda de Tecnológico de Monterrey. ¿En qué puedo ayudarte? Si ya no tienes más preguntas, escribe 'adiós'.")
    # Loop until the user says goodbye
    while True:
        # Get the user input
        user_input = input("Tu pregunta: ")
        # If the user says goodbye, exit the loop
        if user_input.lower() == "adiós":
            print("Gracias por contactarnos. ¡Hasta pronto!")
            break
        # Otherwise, get the response and print it
        else:
            response = respond(user_input)
            print("Asistente: ", response)

if __name__ == "__main__":
    main()


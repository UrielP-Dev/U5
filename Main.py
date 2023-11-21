from analizador import Lexer  # Importa tu propio Lexer
lexer = Lexer("codigo_fuente.txt")  # Crea una instancia de tu Lexer
parser = Parser(lexer)  # Crea una instancia del Parser pasándole el Lexer

# Llama al método principal para iniciar el análisis
program_name = parser.program()
print(f"El nombre del programa es: {program_name}")

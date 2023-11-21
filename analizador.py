def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def analizador_sintactico(cadena):
    pila = []
    declaracion = False
    main_presente = False
    in_main_block = False
    expresion_valida = True

    for idx, caracter in enumerate(cadena):
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila[-1] != '(':
                return False
            pila.pop()
        elif caracter == '=' and in_main_block:
            declaracion = True
        elif idx + 4 < len(cadena) and cadena[idx:idx+4] == 'main':
            if idx + 4 == len(cadena) - 1 or cadena[idx+4] != '{':
                return False
            main_presente = True
            in_main_block = True
        elif caracter == '}':
            in_main_block = False
        elif in_main_block and caracter in '+-*/':
            # Verificar que la expresión tenga formato número/variable operador número/variable
            if idx > 0 and idx < len(cadena) - 1:
                prev_char = cadena[idx - 1]
                next_char = cadena[idx + 1]
                if prev_char.isdigit() != next_char.isdigit() and prev_char.isalpha() != next_char.isalpha():
                    expresion_valida = False

    return not pila and declaracion and main_presente and expresion_valida

cadena_valida = "main{ variable = 10 \n variable2 = variable * 5 }"
cadena_invalida = "{ variable = 20 \n resultado = 5 + variable "

if analizador_sintactico(cadena_valida):
    print(f"La cadena '{cadena_valida}' es válida.")
else:
    print(f"La cadena '{cadena_valida}' no es válida.")

if analizador_sintactico(cadena_invalida):
    print(f"La cadena '{cadena_invalida}' es válida.")
else:
    print(f"La cadena '{cadena_invalida}' no es válida.")

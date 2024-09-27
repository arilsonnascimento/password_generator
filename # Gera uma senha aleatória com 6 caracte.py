# Gera uma senha aleatória com 6 caracteres

import random
import string

def gerar_senha(tamanho=18):
    # Gera uma senha aleatória com 6 caracteres
    # Definindo os caracteres permitidos na senha
    letras_maisculas = string.ascii_uppercase # Letras maiúsculas de A a Z
    letras_minusculas = string.ascii_lowercase # Letras minúsculas de a a z
    numeros = string.digits # Números de 0 a 9
    simbolos = string.punctuation # Caracteres especiais como !@#$%&*()_+
    
    # Combinação de todos os caracteres permitidos
    todos_caracteres = letras_maisculas + letras_minusculas + numeros + simbolos
    
    # Garante que a senha tenha pelo menos um caractere de cada tipo
    senha = [
        random.choice(letras_maisculas), 
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(simbolos)
        ]
    # Preenche o restante da senha com caracteres aleatórios
    senha += random.choices(todos_caracteres, k=tamanho - len(senha))
    
    # Embaralha a senha para garantir que os caracteres não estejam em ordem previsível
    random.shuffle(senha)
    
    # Juntar a lista de caracteres em uma string
    return ''.join(senha)

# Gera uma senha aleatória com 6 caracteres
senha_gerada = gerar_senha(6)
print(senha_gerada)

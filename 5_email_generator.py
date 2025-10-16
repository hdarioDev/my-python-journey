# ==============================
# EMAIL GENERATOR
# Ejemplo de normalización de nombres y creación de direcciones de correo electrónico.
# ==============================

# Nombre completo con espacios innecesarios
name = ' dario condori '
print(f"Nombre completo: {name}")
# Salida: Nombre completo:  dario condori

# Normalizar: quitar espacios al inicio/fin, reemplazar espacios internos por puntos, y pasar a minúsculas
normalized_name = name.strip().replace(' ', '.').lower()
print(f"Nombre completo normalizado: {normalized_name}")
# Salida: Nombre completo normalizado: dario.condori

# Nombre de la empresa con espacio inicial
company_name = ' Zeconds Dev'
print(f"Nombre de la empresa: {company_name}")
# Salida: Nombre de la empresa:  Zeconds Dev

# Dominio base
domain = 'gmail.com'
print(f"Dominio: {domain}")
# Salida: Dominio: gmail.com

# Normalizar nombre de la empresa: quitar espacios y pasar a minúsculas
normalized_company = company_name.replace(' ', '').lower()
# Construir dominio corporativo
normalized_domain = f"@{normalized_company}{domain}"

# Mostrar resultado final (dirección de ejemplo)
print(f"Resultado: {normalized_name}{normalized_domain}")
# Salida: Resultado: dario.condori@zecondsdevgmail.com

# ==============================
# NOTAS:
# - Este ejemplo crea un email usando el patrón:
#   nombre.apellido@empresa+dominio
# - En un caso real, se debería validar:
#   * Que el nombre y apellido sean correctos.
#   * Que el dominio esté bien formado.
#   * Evitar caracteres no válidos en el email.
# ==============================

# Definir dos conjuntos con los aprendices inscritos a cada taller
aprendices_python = {"Ana", "Carlos", "Laura", "Sara", "David"}
aprendices_java = {"Laura", "Sara", "Miguel", "Sofia", "David"}

print(" TALLERES DE PROGRAMACIÓN ")
print("Inscritos en Python:", aprendices_python)
print("Inscritos en Java:", aprendices_java)
print("-" * 35)

todos_inscritos = aprendices_python | aprendices_java
print("1. Inscritos en al menos uno de los talleres:", todos_inscritos)

ambos_talleres = aprendices_python & aprendices_java
print("2. Inscritos en ambos talleres:", ambos_talleres)

solo_python = aprendices_python - aprendices_java
print("3. Inscritos únicamente en Python:", solo_python)

solo_java = aprendices_java - aprendices_python
print("4. Inscritos únicamente en Java:", solo_java)

un_solo_taller = aprendices_python ^ aprendices_java
print("5. Inscritos en un solo taller (no en ambos):", un_solo_taller)
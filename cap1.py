print("estou usando python no rstudio")

#encontrando conectores chave

users = [
  {"id": 0, "name": "A"},
  {"id": 1, "name": "G"},
  {"id": 2, "name": "L"},
  {"id": 3, "name": "Ç"},
  {"id": 4, "name": "P"},
  {"id": 5, "name": "T"},
  {"id": 6, "name": "Q"},
  {"id": 7, "name": "Z"},
  {"id": 8, "name": "V"},
  {"id": 9, "name": "M"},
  {"id": 10, "name": "N"},
  {"id": 11, "name": "I"},
  ]
  
friendships = [(3, 6), (7, 1), (9, 10), (2, 5), (11, 8), (0, 4), (6, 9), 
               (5, 10), (1, 3), (8, 11), (4, 7), (0, 2), (9, 7), (5, 8), 
               (2, 10), (1, 6), (3, 8), (11, 4), (0, 9), (7, 5)]
  
for user in users:
  user["friends"] = []
  
for i, j in friendships:
  users[i]["friends"].append(users[j])
  users[j]["friends"].append(users[i])
  
def nrDeAmigos(user):
  return len(user["friends"]) #tamanho da lista friends_id

totalDeConexoes = sum(nrDeAmigos(user) for user in users)
print(totalDeConexoes)

from __future__ import division
nr_usuarios = len(users)
media_conexoes = totalDeConexoes/ nr_usuarios
print(media_conexoes)


#criar uma lista

numAmigosPorId = [(user["id"], nrDeAmigos(user)) for user in users]

sorted_amigos = sorted(numAmigosPorId, key=lambda item: item[1], reverse=True)  # Corrected errors

print(numAmigosPorId)
  
  
  

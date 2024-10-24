import ollama
import chromadb

#Generamos el contenido que vamos a embeber.
documents = [
  "Llamas are members of the camelid family meaning they're pretty closely related to vicuñas and camels",
  "Llamas were first domesticated and used as pack animals 4,000 to 5,000 years ago in the Peruvian highlands",
  "Llamas can grow as much as 6 feet tall though the average llama between 5 feet 6 inches and 5 feet 9 inches tall",
  "Llamas weigh between 280 and 450 pounds and can carry 25 to 30 percent of their body weight",
  "Llamas are vegetarians and have very efficient digestive systems",
  "Llamas live to be about 20 years old, though some only live for 15 years and others live to be 30 years old",
]

#Generamos el cliente que se conecta a una base de datos random, chromadb para este ejemplo
client = chromadb.Client()
collection = client.create_collection(name="docs")

# store each document in a vector embedding database
for i, d in enumerate(documents):
  #Generamos el embedding para cada parte de los archivos
  response = ollama.embeddings(model="mxbai-embed-large", prompt=d)

  #Devuelve un diccionario con la clave 'embedding', accedemos a ella.
  embedding = response["embedding"]
  collection.add(
    ids=[str(i)],
    embeddings=[embedding],
    documents=[d]
  )

# Hacemos un prompt a modo de consulta.
prompt = "What animals are llamas related to?"

# Hay que generar el embedding del prompt para saber dondebuscar.

response = ollama.embeddings(
  prompt=prompt,
  model="mxbai-embed-large"
)

# Hacemos la consulta a la base de datos.
results = collection.query(
  query_embeddings=[response["embedding"]],
  n_results=1
)

#Nos quedamos con los datos.
data = results['documents'][0][0]


# Generamos la respuesta a partir del contexto y del prompt
output = ollama.generate(
  model="llama3.1:8b",
  prompt=f"Using this data: {data}. Respond to this prompt: {prompt}"
)

print(output['response'])
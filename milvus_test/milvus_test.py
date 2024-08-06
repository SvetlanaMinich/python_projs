from pymilvus import (
    MilvusClient,
    model,
    connections,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection, 
    db,
)

try:

    connections.connect(alias="default", host='localhost', port='19530')
    print("CONNECTED\n")

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True),
        FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=768), #embeddings
        FieldSchema(name="text", dtype=DataType.VARCHAR, max_length=256)
    ]
    schema = CollectionSchema(fields, description="Test collection")

    collection_name = "test_collection_1"
    print(collection_name, "is created\n")

    collection = Collection(
        name=collection_name,
        schema=schema,
    )

    print(collection.name, "is created with pymilvus.Collection\n")

    
    dbs = db.list_database()
    if "mv_test_1" in dbs:
        print("mv_test_1.db already exists\n")
    else:
        try:
            db.create_database(db_name="mv_test_1", using="default", timeout=None)
            print("mv_test_1.db is created\n")
        except Exception as ex:
            print(ex.__context__)
        

    try:
        client = MilvusClient(db_name="mv_test_1")
    except Exception as ex:
        print(ex.__context__)
    
    if client.has_collection(collection_name=collection_name):
        client.drop_collection(collection_name=collection_name)
    client.create_collection(
            collection_name=collection_name,
            dimension=768,
        )        
    print(*(client.list_collections()), "collections already exist\n")

    embedding_fn = model.DefaultEmbeddingFunction()

    docs = [
        "Artificial intelligence was founded as an academic discipline in 1956.",
        "Alan Turing was the first person to conduct substantial research in AI.",
        "Born in Maida Vale, London, Turing was raised in southern England.",
    ]

    vectors = embedding_fn.encode_documents(docs)
    # print("dim:", embedding_fn.dim, vectors[0].shape)

    data = [
        {"id" : i, "vector" : vectors[i], "text" : docs[i]}
        for i in range(len(vectors))
    ]

    # print(f"Data has {len(data)} entities with fields: [{data[0].keys()}]")
    # print(f"Vector dim: {len(data[0]["vector"])}")

    add_docs = [
        "On July 20, 1969, Neil Armstrong became the first human to walk on the Moon during NASA's Apollo 11 mission.",
        "The Berlin Wall, dividing East and West Berlin, fell on November 9, 1989, marking the end of the Cold War era.",
    ]

    add_vectors = embedding_fn.encode_documents(add_docs)
    add_data = [
        {"id" : i, "vector" : add_vectors[i - len(vectors)], "text" : add_docs[i - len(vectors)]}
        for i in range(len(vectors), len(vectors) + len(add_vectors))
    ]

    data += add_data

    try:
        res = client.insert(collection_name=collection_name, data=data)
        print(f"res: {res}\n")
    except Exception as ex:
        print(ex.__context__)


    query_text = "Who is Alan Turing?"
    query_vector = embedding_fn.encode_queries([query_text])

    res = client.search(
        collection_name=collection_name, 
        data=query_vector,
        limit=2,
        output_fields=["text"],
        )
        
    buf_res = [el for el in res[0]]
    for el in buf_res:
        print(el)

except Exception as ex:
    print(ex.__context__)
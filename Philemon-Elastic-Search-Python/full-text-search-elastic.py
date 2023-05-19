from elasticsearch import Elasticsearch

# Instantiate Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 8080, 'scheme': 'http'}])

# Define mapping for the index
mapping = {
    "properties": {
        "title": {
            "type": "text",
            "analyzer": "standard"
        },
        "description": {
            "type": "text",
            "analyzer": "english"
        },
        "code_snippet": {
            "type": "text",
            "analyzer": "programming_analyzer"
        }
    }
}

# Create index with mapping
index_name = "programming_index"
es.indices.create(index=index_name, body={"mappings": mapping})

# Index some documents
doc1 = {
    "title": "Introduction to Python",
    "description": "This course is an introduction to programming with Python.",
    "code_snippet": "print('Hello, world!')"
}
es.index(index=index_name, body=doc1)

doc2 = {
    "title": "Python for Data Science",
    "description": "Learn how to use Python for data analysis and visualization.",
    "code_snippet": "import pandas as pd\n\n# Load data from CSV file\ndata = pd.read_csv('data.csv')\n\n# Print "
                    "first 5 rows\nprint(data.head()) "
}
es.index(index=index_name, body=doc2)

# Search for documents
query = "Python"
res = es.search(index=index_name, body={"query": {"match": {"title": query}}})
print(res['hits']['hits'])

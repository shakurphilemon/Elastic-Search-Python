from elasticsearch import Elasticsearch

# Define the Elasticsearch client
es = Elasticsearch([{'host': 'localhost', 'port': 8080, 'scheme': 'http'}])


# Define the functions for the CRD operations
def create_document(index_name, doc_id, doc_body):
    es.index(index=index_name, id=doc_id, body=doc_body)


def read_documents(index_name):
    search_result = es.search(index=index_name, body={"query": {"match_all": {}}})
    return search_result['hits']['hits']


def update_document(index_name, doc_id, update_body):
    es.update(index=index_name, id=doc_id, body=update_body)


def delete_document(index_name, doc_id):
    es.delete(index=index_name, id=doc_id)


# Define the main function that provides the user interface
def main():
    index_name = 'programming'

    while True:
        print("Choose an action:")
        print("1. Create document")
        print("2. Read documents")
        print("3. Update document")
        print("4. Delete document")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            doc_id = input("Enter document ID: ")
            doc_body = {
                "title": input("Enter document title: "),
                "language": input("Enter document language: "),
                "code": input("Enter document code: "),
                "description": input("Enter document description: ")
            }
            create_document(index_name, doc_id, doc_body)
            print("Document created successfully!")
        elif choice == "2":
            documents = read_documents(index_name)
            for doc in documents:
                print(doc['_source'])
        elif choice == "3":
            doc_id = input("Enter document ID to update: ")
            update_body = {
                "doc": {
                    "title": input("Enter new title: "),
                    "language": input("Enter new language: "),
                    "code": input("Enter new code: "),
                    "description": input("Enter new description: ")
                }
            }
            update_document(index_name, doc_id, update_body)
            print("Document updated successfully!")
        elif choice == "4":
            doc_id = input("Enter document ID to delete: ")
            delete_document(index_name, doc_id)
            print("Document deleted successfully!")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

from pinecone import Pinecone

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")

def delete_all():
    index = pc.Index(input("What is the index?"))

    # Specify the correct namespace or omit if using the default
    namespace = input("What is the index?")  # Replace 'your_namespace' with your actual namespace or leave it as an empty string for the default namespace
    try:
        index.delete(delete_all=True, namespace=namespace)
        print("All entries deleted successfully.")
    except Exception as e:
        print(f"Failed to delete entries: {e}")

from pinecone import Pinecone

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
index = pc.Index("kbc")

def delete_all():
    # Specify the correct namespace or omit if using the default
    namespace = "employees"  # Replace 'your_namespace' with your actual namespace or leave it as an empty string for the default namespace
    try:
        index.delete(delete_all=True, namespace=namespace)
        print("All entries deleted successfully.")
    except Exception as e:
        print(f"Failed to delete entries: {e}")

def delete_entry():
    namespace = "employees"
    entry_id = input("Enter the ID of the entry you want to delete: ")
    index.delete(ids=[entry_id], namespace=namespace)
    print(f"Entry with ID '{entry_id}' has been deleted.")

# delete_all()
delete_entry()

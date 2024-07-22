from pinecone import Pinecone

pc = Pinecone(api_key="833ea798-e4a0-4ea8-94ae-c327e20b15a7")
index = pc.Index("kbc")

def delete_all():
    index.delete(delete_all=True)

def delete_entry():
    entry_id = input("Enter the ID of the entry you want to delete: ")
    index.delete(ids=[entry_id])
    print(f"Entry with ID '{entry_id}' has been deleted.")

# delete_all()
delete_entry()

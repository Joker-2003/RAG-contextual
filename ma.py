# # main.py

# from dotenv import load_dotenv
# from utils import store_docs, get_response, get_chroma_client

# # Load the OPENAI KEY from the env.sh file
# load_dotenv('env.sh')  # Specify path to your env file

# def main():
#     # Storing webpage content into vector store
#     # Make sure not to store the same documents twice
#     store_docs("https://cloudxlab.com/course/204/certificate-course-on-generative-ai")

#     # Seeing how the data looks like in the vector store
#     vector_store = get_chroma_client()
#     lis = vector_store.get(include=['embeddings', 'metadatas', 'documents'])
    
#     print("Number of documents:", len(lis['documents']))
#     print("Content:\n", lis['documents'][1])
#     print("\n\nMetadata:", lis['metadatas'][1])
#     print("\n\nEmbeddings:", "Length:", len(lis['embeddings'][1]), "\nEmbedding Vector:", lis['embeddings'][1])
    
#     # Setting up organization information
#     organization_name = "CloudxLab"
#     organization_info = ("CloudxLab is known for providing courses on several technologies such as Machine Learning, "
#                          "Big Data, Deep Learning, Artificial Intelligence, DevOps, MLOps, etc. Its main perk is the "
#                          "gamified cloud lab where users can practice all the tools related to the mentioned technologies "
#                          "which are pre-installed in parallel to learning.")
#     contact_info = (
#         "Email: reachus@cloudxlab.com\n"
#         "India Phone: +91 08049202224\n"
#         "International Phone: +1 (412) 568-3901.\n"
#         "Raise a query: https://cloudxlab.com/reach-us-queries\n"
#         "Forum: https://discuss.cloudxlab.com/"
#     )
    
#     # Get response
#     response = get_response("What is the duration of this course", organization_name, organization_info, contact_info)
#     print("Answer:", response)
    
#     # Get response
#     response = get_response("Who are the instructors?", organization_name, organization_info, contact_info)
#     print("Answer:", response)

# if __name__ == "__main__":
#     main()

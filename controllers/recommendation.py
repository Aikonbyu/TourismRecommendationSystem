from transformers import RagTokenizer, RagRetriever, RagTokenForGeneration
import torch
import numpy as np
from models import connection
import faiss  # Import Faiss library

# Function to create a text representation for each destination
def create_destination_text(row):
    _, name, description, domestic_price, foreign_price, village, sub_district, district, facilities, categories, image_url = row
    return (
        f"Nama: {name}. "
        f"Deskripsi: {description}. "
        f"Harga Domestik: {domestic_price}. "
        f"Harga Asing: {foreign_price}. "
        f"Desa: {village}. "
        f"Kecamatan: {sub_district}. "
        f"Kabupaten: {district}. "
        f"Fasilitas: {facilities if facilities else 'Tidak ada fasilitas tercatat'}. "
        f"Kategori: {categories if categories else 'Tidak ada kategori tercatat'}."
    )

# Connect to the database and fetch destination data
connect, cursor = connection.connect_db()
cursor.execute("""
    SELECT d.id, d.name, d.description, d.domesticPrice, d.foreignPrice, 
           d.village, d.subDistrict, d.district,
           GROUP_CONCAT(DISTINCT f.name) AS facilities, 
           GROUP_CONCAT(DISTINCT c.name) AS categories,
           d.imageURL
    FROM destinations d
    LEFT JOIN destination_facilities df ON d.id = df.destinationId
    LEFT JOIN facilities f ON df.facilityId = f.id
    LEFT JOIN destination_categories dc ON d.id = dc.destinationId
    LEFT JOIN categories c ON dc.categoryId = c.id
    GROUP BY d.id
""")
destinations_data = cursor.fetchall()
connection.close_db(connect, cursor)

# Create destination descriptions and IDs
destinations_text = [create_destination_text(row) for row in destinations_data]
destinations_ids = [row[0] for row in destinations_data]

# Initialize RAG model components
tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_path="data/wiki_dpr/psgs_w100.tsv.pkl")
model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")

# Generate embeddings for each destination
dimension = 768  # Ensure this matches the RAG model's output
destinations_embeddings = []

for destination in destinations_text:
    inputs = tokenizer(destination, return_tensors="pt")
    with torch.no_grad():
        destination_emb = retriever.question_encoder(**inputs).pooler_output.cpu().numpy().flatten()
    destinations_embeddings.append(destination_emb)

# Convert embeddings to a numpy array for Faiss
destinations_embeddings = np.array(destinations_embeddings).astype("float32")

# Initialize Faiss index for L2 distance (Euclidean)
index = faiss.IndexFlatL2(dimension)
index.add(destinations_embeddings)  # Add destination embeddings to Faiss index

# Function to generate recommendations based on a query
def generate_recommendation(query, top_k=3):
    # Encode the query
    inputs = tokenizer(query, return_tensors="pt")
    with torch.no_grad():
        query_embedding = retriever.question_encoder(**inputs).pooler_output.cpu().numpy().flatten()
    
    # Reshape query embedding for Faiss compatibility
    query_embedding = np.array([query_embedding]).astype("float32")
    
    # Perform search in Faiss index
    _, closest_indices = index.search(query_embedding, top_k)
    
    # Retrieve destination IDs for the closest matches
    recommendations = [destinations_ids[idx] for idx in closest_indices[0]]
    
    return recommendations



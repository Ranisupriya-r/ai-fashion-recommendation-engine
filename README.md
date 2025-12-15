AI-Powered Fashion Recommendation Engine 👗🤖  
A deep learning–based fashion recommendation system that suggests outfits based on image similarity and contextual factors such as weather. This project combines MobileNetV2 for image classification and CLIP embeddings for semantic similarity search.


Features  
✔ Image classification using MobileNetV2  
✔ Outfit similarity search using CLIP embeddings  
✔ Weather-aware clothing recommendations (API-based)  
✔ End-to-end notebook demonstrating the pipeline  
✔ Modular design for future UI or app integration  


Tech Stack  
- Python  
- MobileNetV2 (image classification)  
- CLIP (semantic similarity)  
- Deep Learning (PyTorch / TensorFlow)  
- Requests (Weather API)  
- Jupyter Notebook  


Project Pipeline  
1️⃣ Data Preparation  
- Collected fashion images (DeepFashion + web-scraped)  
- Cleaned and standardized file structure  
- Prepared category labels  

2️⃣ Image Classification  
- Loaded MobileNetV2 pretrained model  
- Extracted embeddings for clothing items  
- Fine-tuned classification layers (optional)  

3️⃣ Similarity Search using CLIP  
- Encoded images and text using CLIP  
- Performed cosine similarity search  
- Retrieved top-N similar outfits  

4️⃣ Weather-Based Recommendations  
- Integrated weather API (OpenWeather)  
- Added rules for cold/warm/rainy conditions  
- Filtered recommendation list based on context  


Example Workflow  
1. User uploads outfit image  
2. Model classifies clothing category  
3. CLIP retrieves visually similar outfits  
4. Weather conditions refine recommendations  
5. Final top-5 outfit list shown  



## 📁 Repository Structure  


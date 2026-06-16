"""
Application Streamlit avec PyCaret
"""

import streamlit as st
from pycaret.classification import setup, compare_models, pull

st.set_page_config(page_title="PyCaret App", layout="wide")

st.title("🚀 Application PyCaret & Streamlit")

st.markdown("""
Bienvenue dans cette application Python avec:
- **Streamlit** pour l'interface web
- **PyCaret** pour le machine learning automatisé
- **Python 3.10** pour la performance

---
""")

st.info("Chargez vos données et lancez des analyses ML en quelques clics!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Versions installées")
    st.code("""
import streamlit
import pycaret
import pandas
import numpy
import sklearn

print(f"Streamlit: {streamlit.__version__}")
print(f"PyCaret: {pycaret.__version__}")
print(f"Pandas: {pandas.__version__}")
print(f"NumPy: {numpy.__version__}")
print(f"Scikit-learn: {sklearn.__version__}")
    """, language="python")

with col2:
    st.subheader("🔧 Commandes Docker")
    st.code("""
# Construire l'image
docker-compose build

# Lancer le container
docker-compose up

# Arrêter le container
docker-compose down

# Voir les logs
docker-compose logs -f
    """, language="bash")

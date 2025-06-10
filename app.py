# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 13:49:31 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuración de la app
st.set_page_config(page_title="Postulación SHCP - Javier Pérez", layout="wide")

# Título y presentación
st.title("📊 SHCP: Análisis Interactivo de Ingresos Petroleros en México")
st.subheader("Candidato: Javier Horacio Pérez Ricárdez")

st.markdown("""
Soy economista apasionado por el análisis cuantitativo y la gestión eficiente de los ingresos públicos.  
Esta app muestra mis capacidades técnicas aplicadas a un problema real:  
**¿Cómo afectan los precios del petróleo a los ingresos del gobierno mexicano?**
""")

# Barra lateral con parámetros
st.sidebar.title("🔧 Parámetros de Simulación")
precio_barril = st.sidebar.slider("Precio promedio del barril (USD)", 40, 120, 70)
tipo_cambio = st.sidebar.slider("Tipo de cambio (MXN/USD)", 15.0, 25.0, 18.5)
produccion = st.sidebar.slider("Producción diaria (millones de barriles)", 1.0, 2.5, 1.7)

# Simulación de ingresos variables mes a mes
meses = pd.date_range("2024-01-01", periods=6, freq="M")
precios = np.random.normal(loc=precio_barril, scale=3, size=6)
tipos_cambio = np.random.normal(loc=tipo_cambio, scale=0.5, size=6)
producciones = np.random.normal(loc=produccion, scale=0.1, size=6)

ingresos_simulados = precios * tipos_cambio * producciones * 1_000_000 * 30  # ingreso mensual

# DataFrame con datos observados y simulados
data = pd.DataFrame({
    "Mes": meses,
    "Ingresos observados": np.random.uniform(25, 60, 6) * 1e9,
    "Ingresos simulados": ingresos_simulados
})

# Mostrar métrica destacada
st.metric(label="🛢️ Ingreso mensual estimado (último mes)", value=f"${ingresos_simulados[-1]:,.0f} MXN")

# Gráfico interactivo con Plotly
fig = px.line(data, x="Mes", y=["Ingresos observados", "Ingresos simulados"],
              title="📉 Comparativa de Ingresos Petroleros: Observado vs. Simulado",
              labels={"value": "Ingresos (MXN)", "variable": "Serie"})

st.plotly_chart(fig, use_container_width=True)

# Sección de descarga de documentos
st.markdown("### 📎 CV y Carta de Motivación")

with st.expander("Descargar documentos"):
    try:
        with open("cv_Javier.pdf", "rb") as f:
            st.download_button(
                label="📄 Descargar CV (PDF)",
                data=f,
                file_name="cv_Javier.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("❌ El archivo 'cv_Javier.pdf' no se encuentra en la carpeta.")

    try:
        with open("carta_motivacion.pdf", "rb") as f:
            st.download_button(
                label="📝 Descargar Carta de Motivación (PDF)",
                data=f,
                file_name="carta_motivacion.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("❌ El archivo 'carta_motivacion.pdf' no se encuentra en la carpeta.")

# Contacto directo con SHCP
st.markdown("### 📧 Contacto directo con SHCP")
st.markdown("[📨 Enviar correo a SHCP](mailto:gabriela_lopezg@hacienda.gob.mx?subject=Postulación%20Javier%20SHCP&body=Adjunto%20mi%20CV%20y%20carta.%20Estoy%20interesado%20en%20la%20vacante.)")

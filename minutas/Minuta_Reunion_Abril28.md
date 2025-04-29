elif choice == "Minutas y Planificación":
    st.title("📚 Minutas de Reunión y Planificación")
    st.markdown("### 📝 Actas disponibles")

    minutas = {
        "Reunión 28 de abril de 2025": "Minuta_Reunion_Abril28.md",
    }

    for nombre, archivo in minutas.items():
        st.subheader(f"🗂 {nombre}")
        url = f"https://raw.githubusercontent.com/DanielaTorrente/macrobasica_app/main/minutas/{archivo}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                st.markdown(response.text, unsafe_allow_html=True)
            else:
                st.error(f"No se pudo cargar la minuta {nombre}.")
        except:
            st.error(f"Error cargando la minuta {nombre}.")
        st.markdown("---")

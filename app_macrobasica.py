menu = ["Inicio", "Minutas y Planificación", "Actividades Docentes", "Actividades Estudiantes", "Seguimiento de Avances", "Contacto Interno"]
choice = st.sidebar.radio("Ir a:", menu)

if choice == "Inicio":
    st.title("Cátedra de Macro Básica")
    st.write("Bienvenida a la plataforma colaborativa de la Cátedra.")

elif choice == "Minutas y Planificación":
    st.title("Minutas de Reunión y Planificación")
    st.write("A continuación, podés acceder a las minutas de reuniones de la cátedra:")

    base_url = "https://github.com/DanielaTorrente/macrobasica_app/raw/main/minutas/"

    minutas = {
        "Reunión 28 de abril de 2025": "Minuta_Reunion_Abril28.docx",
    }

    for nombre, archivo in minutas.items():
        st.markdown(f"[📄 {nombre}]({base_url}{archivo})")

elif choice == "Actividades Docentes":
    st.title("Actividades Asignadas a Docentes")
    st.write("Checklist de tareas pendientes por unidad y planificación.")

elif choice == "Actividades Estudiantes":
    st.title("Actividades para Estudiantes")
    st.write("Tableros interactivos, actividades de IA y Python.")

elif choice == "Seguimiento de Avances":
    st.title("Seguimiento de Avances")
    st.write("Visualización de progreso de actividades y minutas.")

elif choice == "Contacto Interno":
    st.title("Contacto Interno")
    with st.form("form_contact"):
        asunto = st.text_input("Asunto")
        mensaje = st.text_area("Mensaje")
        enviar = st.form_submit_button("Enviar consulta")
        if enviar:
            st.success("Consulta enviada. ¡Gracias!")

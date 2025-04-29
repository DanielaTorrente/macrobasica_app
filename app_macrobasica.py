import streamlit as st
import streamlit_authenticator as stauth

# Configuración de usuarios
credentials = {
    "usernames": {
        "dtorrente": {
            "name": "Daniela Torrente",
            "password": "macro2025"
        },
        "profesor1": {
            "name": "Profesor/a 1",
            "password": "macro2025"
        }
    }
}

# Crear autenticador
authenticator = stauth.Authenticate(
    credentials=credentials,
    cookie_name="macrobasica_app",
    key="abcdef",
    cookie_expiry_days=1
)

# Login
authenticator.login(
    location="main",
    fields={"Form name": "Login", "Username": "Username", "Password": "Password"}
)

# Control de acceso
if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar")
    st.sidebar.title(f"Bienvenido/a, {st.session_state['name']}")

    menu = ["Inicio", "Minutas y Planificación", "Actividades Docentes", "Actividades Estudiantes", "Seguimiento de Avances", "Contacto Interno"]
    choice = st.sidebar.radio("Ir a:", menu)

    if choice == "Inicio":
        st.title("Cátedra de Macro Básica")
        st.write("Bienvenida a la plataforma colaborativa de la Cátedra.")

    elif choice == "Minutas y Planificación":
        st.title("📚 Minutas de Reunión y Planificación")
        st.markdown("### 📝 Actas disponibles")

        base_url = "https://github.com/DanielaTorrente/macrobasica_app/raw/main/minutas/"

        minutas = {
            "Reunión 28 de abril de 2025": "Minuta_Reunion_Abril28.docx",
            # Podrías agregar más archivos aquí si querés
        }

        for nombre, archivo in minutas.items():
            with st.container():
                st.subheader(f"🗂 {nombre}")
                st.markdown(f"[📥 Descargar minuta]({base_url}{archivo})", unsafe_allow_html=True)
                st.markdown("---")

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

elif st.session_state["authentication_status"] is False:
    st.error("Usuario o contraseña incorrectos.")

elif st.session_state["authentication_status"] is None:
    st.warning("Por favor ingrese su usuario y contraseña.")


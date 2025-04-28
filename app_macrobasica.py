import streamlit as st
import streamlit_authenticator as stauth

# Configuración de usuarios (con contraseñas hasheadas)
credentials = {
    "usernames": {
        "dtorrente": {
            "name": "Daniela Torrente",
            "password": "$2b$12$8Sk9g1O./B7Vh4ZwQMY5..8Vx3YzAFDh5U51iwmPCA9IAoHgUydlG"
        },
        "profesor1": {
            "name": "Profesor/a 1",
            "password": "$2b$12$8Sk9g1O./B7Vh4ZwQMY5..8Vx3YzAFDh5U51iwmPCA9IAoHgUydlG"
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

# Login corregido
authenticator.login(
    location="main",
    fields={"Form name": "Login", "Username": "Username", "Password": "Password"}
)

if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar")
    st.sidebar.title(f"Bienvenido/a, {st.session_state['name']}")

    menu = ["Inicio", "Minutas y Planificación", "Actividades Docentes", "Actividades Estudiantes", "Seguimiento de Avances", "Contacto Interno"]
    choice = st.sidebar.radio("Ir a:", menu)

    if choice == "Inicio":
        st.title("Cátedra de Macro Básica")
        st.write("Bienvenida a la plataforma colaborativa de la Cátedra.")

    elif choice == "Minutas y Planificación":
        st.title("Minutas de Reunión y Planificación")
        st.write("Aquí se cargarán las actas de reuniones y documentos de trabajo.")

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

import streamlit as st
import streamlit_authenticator as stauth
import requests

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

        minutas = {
            "Reunión 28 de abril de 2025": "Minuta_Reunion_Abril28.txt",
        }

        for nombre, archivo in minutas.items():
            st.subheader(f"🗂 {nombre}")
            url = f"https://raw.githubusercontent.com/DanielaTorrente/macrobasica_app/main/minutas/{archivo}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    st.markdown(response.text)
                else:
                    st.error(f"No se pudo cargar la minuta {nombre}.")
            except:
                st.error(f"Error cargando la minuta {nombre}.")
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

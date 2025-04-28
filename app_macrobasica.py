
import streamlit as st
import streamlit_authenticator as stauth

# Configuración de usuarios
credentials = {
    "usernames": {
        "dtorrente": {
            "name": "Daniela Torrente",
            "password": stauth.Hasher(["macro2025"]).generate()[0]
        },
        "profesor1": {
            "name": "Profesor/a 1",
            "password": stauth.Hasher(["macro2025"]).generate()[0]
        }
    }
}

# Crear el autenticador
authenticator = stauth.Authenticate(
    credentials,
    "macrobasica_app",
    "abcdef",
    cookie_expiry_days=1
)

# Login
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.title(f"Bienvenido/a, {name}")

    menu = ["Inicio", "Minutas y Planificación", "Actividades Docentes", "Actividades Estudiantes", "Seguimiento de Avances", "Contacto Interno"]
    choice = st.sidebar.radio("Ir a:", menu)

    if choice == "Inicio":
        st.title("Cátedra de Macro Básica")
        st.write("Bienvenida a la plataforma colaborativa de la Cátedra.")
        st.info("✨ Próxima reunión: 12 de mayo")
    elif choice == "Minutas y Planificación":
        st.title("Minutas de Reunión y Planificación")
    elif choice == "Actividades Docentes":
        st.title("Actividades Asignadas a Docentes")
    elif choice == "Actividades Estudiantes":
        st.title("Actividades para Estudiantes")
    elif choice == "Seguimiento de Avances":
        st.title("Seguimiento de Avances")
    elif choice == "Contacto Interno":
        st.title("Contacto Interno")
        with st.form("form_contact"):
            asunto = st.text_input("Asunto")
            mensaje = st.text_area("Mensaje")
            enviar = st.form_submit_button("Enviar consulta")
            if enviar:
                st.success("Consulta enviada. ¡Gracias!")

elif authentication_status is False:
    st.error('Usuario o contraseña incorrectos.')
elif authentication_status is None:
    st.warning('Ingrese su usuario y contraseña.')

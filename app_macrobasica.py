import streamlit as st
import streamlit_authenticator as stauth

# Configuración de usuarios (credenciales ya hasheadas)
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

# Login con la estructura correcta
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
        st.write("Bienvenida a la plataforma colaborativa de la Cátedra

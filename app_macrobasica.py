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

    menu = ["Inicio", "Minutas y Planificación", "Actividades Docentes", "Actividades Estudiantes", "Seguimiento de Avances", "Próximos Encuentros", "Contacto Interno"]
    choice = st.sidebar.radio("Ir a:", menu)

    if choice == "Inicio":
        st.title("Cátedra de Macro Básica")
        st.write("Bienvenida a la plataforma colaborativa de la Cátedra.")

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

    elif choice == "Actividades Docentes":
        st.title("Actividades Asignadas a Docentes")
        st.write("Checklist de tareas pendientes por unidad y planificación.")

    elif choice == "Actividades Estudiantes":
        st.title("🎯 Actividades para Estudiantes")
        st.markdown("Explorá las simulaciones, tableros y ejercicios interactivos:")

        actividades = {
            "Tablero Interactivo para Estudiantes": "https://macroeconomiabasica-gg5zwuzusagqebzwto4pih.streamlit.app/",
            "Simulador Macroeconómico Interactivo": "https://macroeconomiabasica-6aw6qthnbfp2x69drypgkw.streamlit.app/"
        }

        for nombre, url in actividades.items():
            st.subheader(f"🧩 {nombre}")
            st.markdown(f"[🚀 Acceder a la actividad]({url})", unsafe_allow_html=True)
            st.markdown("---")

    elif choice == "Seguimiento de Avances":
        st.title("Seguimiento de Avances")
        st.write("Visualización de progreso de actividades y minutas.")

    elif choice == "Próximos Encuentros":
        st.title("📅 Próximos Encuentros de la Cátedra")
        
        st.subheader("🧠 Reunión General - Mayo 2025")
        st.write("**Fecha:** Lunes 12 de mayo de 2025")
        st.write("**Hora:** 18:00 hs")
        st.write("**Modalidad:** Virtual (Google Meet)")
        
        meet_link = "https://meet.google.com/xxx-yyyy-zzz"  # 👈 Cambiar cuando tengas el link real
        st.markdown(f"[🔗 Acceder al encuentro]({meet_link})", unsafe_allow_html=True)

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

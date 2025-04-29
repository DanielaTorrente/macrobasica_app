import streamlit as st
import streamlit_authenticator as stauth
import requests

# Configuración de usuarios (usuario único profesdemacro)
credentials = {
    "usernames": {
        "profesdemacro": {
            "name": "Equipo Docente de Macro Básica",
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

    # Menú lateral
    menu = [
        "Inicio", 
        "Minutas y Planificación", 
        "Actividades Docentes", 
        "Actividades Estudiantes", 
        "Seguimiento de Avances", 
        "Próximos Encuentros", 
        "Contacto Interno"
    ]
    choice = st.sidebar.radio("Ir a:", menu)

    # Sección: Inicio
    if choice == "Inicio":
        st.title("Cátedra de Macro Básica")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://raw.githubusercontent.com/DanielaTorrente/macrobasica_app/main/images/logo_unne.png", width=150)
        with col2:
            st.image("https://raw.githubusercontent.com/DanielaTorrente/macrobasica_app/main/images/logo_fce.png", width=150)
        with col3:
            st.image("https://raw.githubusercontent.com/DanielaTorrente/macrobasica_app/main/images/logo_macro.png", width=150)

        st.write("Bienvenida a la plataforma colaborativa de la Cátedra de Macroeconomía Básica.")

    # Sección: Minutas
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

    # Sección: Actividades Docentes
    elif choice == "Actividades Docentes":
        st.title("🧑‍🏫 Actividades Asignadas a Docentes")
        st.write("Checklist de tareas pendientes por unidad y planificación.")

    # Sección: Actividades Estudiantes
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

    # Sección: Seguimiento de Avances
    elif choice == "Seguimiento de Avances":
        st.title("📈 Seguimiento de Avances")
        st.write("Visualización de progreso de actividades, minutas y tareas docentes.")

    # Sección: Próximos Encuentros
    elif choice == "Próximos Encuentros":
        st.title("📅 Próximos Encuentros de la Cátedra")
        
        st.subheader("🧠 Reunión General - Mayo 2025")
        st.write("**Fecha:** Lunes 12 de mayo de 2025")
        st.write("**Hora:** 18:00 hs")
        st.write("**Modalidad:** Virtual (Google Meet)")

        meet_link = "https://meet.google.com/xxx-yyyy-zzz"  # Cambiar por el link real
        st.markdown(f"[🔗 Acceder al encuentro]({meet_link})", unsafe_allow_html=True)

    # Sección: Contacto Interno (redirección a WhatsApp)
    elif choice == "Contacto Interno":
        st.title("📩 Contacto Interno")

        st.markdown("Complete su consulta y será derivada automáticamente al grupo de WhatsApp *Macro 1* de la cátedra.")

        with st.form("form_contact"):
            nombre = st.text_input("Nombre")
            mensaje = st.text_area("Mensaje")
            enviar = st.form_submit_button("Enviar al WhatsApp")

            if enviar:
                if nombre and mensaje:
                    numero_whatsapp = "5493624314865"
                    texto = f"Hola, soy {nombre}, docente de Macro 1. Mi consulta es: {mensaje}"
                    texto_encoded = texto.replace(' ', '%20').replace('\n', '%0A')
                    url_whatsapp = f"https://api.whatsapp.com/send?phone={numero_whatsapp}&text={texto_encoded}"
                    st.success("Redirigiendo a WhatsApp...")
                    st.markdown(f"[👉 Click aquí para enviar tu consulta por WhatsApp]({url_whatsapp})", unsafe_allow_html=True)
                else:
                    st.error("Por favor complete su nombre y su mensaje.")

# Si no está logueado correctamente
elif st.session_state["authentication_status"] is False:
    st.error("Usuario o contraseña incorrectos.")

elif st.session_state["authentication_status"] is None:
    st.warning("Por favor ingrese su usuario y contraseña.")

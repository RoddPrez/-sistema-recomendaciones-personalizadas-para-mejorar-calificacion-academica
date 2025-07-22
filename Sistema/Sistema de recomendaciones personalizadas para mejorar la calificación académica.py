import streamlit as st
import pandas as pd
import joblib
import os

# Ruta segura que funciona desde cualquier lugar
ruta_actual = os.path.dirname(__file__)
ruta_rf = os.path.join(ruta_actual, 'modelo_random_forest.pkl')
ruta_gb = os.path.join(ruta_actual, 'modelo_gradient_boosting.pkl')

# Cargar modelos entrenados
modelo_rf = joblib.load(ruta_rf)
modelo_gb = joblib.load(ruta_gb)

st.title("🎓 Predicción de Nota Semestral Universitaria")
st.markdown("💡 *Estima tu rendimiento académico y obtén recomendaciones personalizadas para mejorar tus resultados.*")

# Expandir ancho de la aplicación a toda la pantalla


# 🔧 Listas de opciones (fuera del formulario)
opciones_habilidades = sorted([
    "App development", "Artificial Intelligence", "Basic", "Basic knowledge", "Communication",
    "Content creation", "Cyber security", "Data entry", "Database", "Digital Marketing",
    "Don't have any", "E-commerce", "graphic design", "Graphics design", "Graphics Designing",
    "Haven't started yet", "I do not know this", "i don't", "Its on learning phase", "learner",
    "Learning frontend", "Machine Learning", "Market Analysis", "Memorizing", "Mentoring",
    "Networking", "Networking, MIS", "No skill", "no skills", "None", "Not Any", "Not yet",
    "Nothing", "Nothing in this chart", "Nothing much", "Nothing properly", "Nothing specially",
    "Other", "Photographey", "Photography", "Problem solving", "Programming",
    "Programming, Mentoring", "Programming, Networking", "Python", "Software Development",
    "System analysis", "Teaching", "Trying to learn", "Video editing", "videography, video editing",
    "Web development", "Web development skill"
])

opciones_area = sorted([
    "Artificial Intelligence", "Blockchain", "Competitive programming", "confuse",
    "Creating a game using a program language", "Cyber Security", "Cybersecurity", "Data Schince",
    "Data Science", "Entrepreneur", "Event management", "Full stack web development", "Hardware",
    "Machine Learning", "NETWORKING", "programming", "Software", "Syber Security", "Teaching",
    "UI/UX", "Web developing", "Web development"
])

habilidades_map = {f"{i+1}. {h}": i for i, h in enumerate(opciones_habilidades)}
area_map = {f"{i+1}. {a}": i for i, a in enumerate(opciones_area)}

# FORMULARIO
with st.form("formulario_estudiante"):
    col1, col2, col3 = st.columns(3)

    with col1:
        anio_ingreso = st.selectbox("Año ingreso universidad", list(range(2013, 2024)))
        anio_egreso = st.selectbox("Año egreso secundaria", list(range(2012, 2023)))
        edad = st.slider("Edad", 18, 27)
        sexo = st.radio("Sexo", ["Femenino", "Masculino"])
        semestre_actual = st.slider("Semestre actual", 1, 24)
        beca = st.radio("Beca por rendimiento", ["Sí", "No"])
        riesgo = st.radio("Riesgo académico", ["Sí", "No"])
        suspension = st.radio("Suspensión académica", ["Sí", "No"])
        tutorias = st.radio("Recibe tutorías docentes", ["Sí", "No"])
        creditos = st.slider("Créditos completados", 0, 120)

    with col2:
        smartphone = st.radio("Tiene smartphone", ["Sí", "No"])
        pc = st.radio("Tiene computadora personal", ["Sí", "No"])
        ingles = st.selectbox("Nivel de inglés", ["Basic", "Intermediate", "Advance"])
        habilidades_opcion = st.selectbox("🛠️ Habilidad que domina o está aprendiendo", list(habilidades_map.keys()))
        area_opcion = st.selectbox("🎯 Área de interés principal", list(area_map.keys()))
        horas_habilidad = st.slider("Horas al día practicando habilidades", 0, 12)
        redes = st.slider("Horas en redes sociales", 0, 20)
        sueno = st.slider("Horas de sueño diarias", 5, 10)
        ejercicio = st.slider("Horas de ejercicio semanales", 0, 6)
        salud = st.radio("Tiene problemas de salud", ["Sí", "No"])
        discapacidad = st.radio("Tiene discapacidad física", ["Sí", "No"])

    with col3:
        modalidad = st.radio("Modalidad de aprendizaje", ["Offline", "Online"])
        horas_estudio = st.slider("Horas de estudio diarias", 0, 13)
        frecuencia_estudio = st.slider("Frecuencia estudio por semana", 0, 7)
        horas_clase = st.slider("Horas de clases semanales", 0, 36)
        asistencia = st.slider("Asistencia promedio (%)", 0, 100)
        extra = st.radio("Actividades extracurriculares", ["Sí", "No"])
        estado = st.selectbox("Estado sentimental", ["Single", "In a relationship", "Engaged", "Married", "Relationship"])
        vive = st.selectbox("¿Con quién vives?", ["bachelor", "family"])
        transporte = st.radio("Usa transporte universitario", ["Sí", "No"])
        transporte_tipo = st.selectbox("Tipo de transporte", ["propio", "publico", "mixto"])
        horas_transporte = st.slider("Horas totales de transporte semanales", 0, 20)
        horas_trabajo = st.slider("Horas de trabajo semanales", 0, 35)
        ingreso = st.number_input("Ingreso familiar anual", 4000, 2000000, step=1000)

    submit = st.form_submit_button("📈 Predecir Nota")

if submit:
    sexo = 1 if sexo == "Masculino" else 0
    beca = 1 if beca == "Sí" else 0
    transporte = 1 if transporte == "Sí" else 0
    modalidad = 1 if modalidad == "Online" else 0
    smartphone = 1 if smartphone == "Sí" else 0
    pc = 1 if pc == "Sí" else 0
    ingles = {"Basic": 0, "Intermediate": 1, "Advance": 2}[ingles]
    riesgo = 1 if riesgo == "Sí" else 0
    suspension = 1 if suspension == "Sí" else 0
    tutorias = 1 if tutorias == "Sí" else 0
    estado = ["Single", "In a relationship", "Engaged", "Married", "Relationship"].index(estado) + 1
    extra = 1 if extra == "Sí" else 0
    vive = 0 if vive == "bachelor" else 1
    salud = 1 if salud == "Sí" else 0
    discapacidad = 1 if discapacidad == "Sí" else 0
    transporte_tipo = {"propio": 0, "publico": 1, "mixto": 2}[transporte_tipo]

    habilidades = habilidades_map[habilidades_opcion]
    area_interes = area_map[area_opcion]

    nuevo_estudiante = [
        anio_ingreso, sexo, edad, anio_egreso, semestre_actual,
        beca, transporte, horas_estudio, frecuencia_estudio,
        modalidad, smartphone, pc, redes, ingles, asistencia,
        riesgo, suspension, tutorias, habilidades, horas_habilidad,
        area_interes, estado, extra, vive, salud, discapacidad,
        creditos, ingreso, horas_clase, sueno, ejercicio,
        transporte_tipo, horas_transporte, horas_trabajo
    ]

    X_nuevo = pd.DataFrame([nuevo_estudiante], columns=[
        "anio_ingreso_universidad", "sexo", "edad", "anio_egreso_secundaria", "semestre_actual",
        "beca_rendimiento", "transporte_universidad", "horas_estudio_dia", "frecuencia_estudio_dia",
        "modalidad_aprendizaje", "smartphone", "computadora_personal", "horas_redes_sociales",
        "nivel_ingles", "asistencia_promedio", "riesgo_academico", "suspension_academica",
        "tutorias_docentes", "habilidades", "horas_habilidades_dia", "area_interes",
        "estado_sentimental", "actividades_extracurriculares", "con_quien_vives", "problemas_salud",
        "discapacidad_fisica", "creditos_completados", "ingreso_familiar_anual",
        "horas_clases_semanales", "horas_sueno_dia", "horas_ejercicio_semanal",
        "tipo_transporte", "horas_transporte_total", "horas_trabajo_semanal"
    ])

    pred_rf = modelo_rf.predict(X_nuevo)[0]
    pred_gb = modelo_gb.predict(X_nuevo)[0]

    # Resultado
    st.success("📊 Predicción completada:")
    st.write(f"🔹 **Random Forest:** {pred_rf:.2f} / 20")
    st.write(f"🔹 **Gradient Boosting:** {pred_gb:.2f} / 20")

    # 🔧 Recomendaciones basadas en simulaciones inteligentes (Gradient Boosting)
    mejoras = {}
    nota_base = pred_gb

    # Crear copia base
    X_sim = X_nuevo.copy()

    # 1. Estudiar +1h si < 5
    if X_sim["horas_estudio_dia"].values[0] < 5:
        X_tmp = X_sim.copy()
        X_tmp["horas_estudio_dia"] += 1
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["📚 Estudiar +1h al día"] = mejora

    # 2. Aumentar asistencia a 90%
    if X_sim["asistencia_promedio"].values[0] < 90:
        X_tmp = X_sim.copy()
        X_tmp["asistencia_promedio"] = 90
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["🧑‍🏫 Subir asistencia al 90%"] = mejora

    # 3. Reducir redes sociales a 2h si > 4h
    if X_sim["horas_redes_sociales"].values[0] > 4:
        X_tmp = X_sim.copy()
        X_tmp["horas_redes_sociales"] = 2
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["📵 Reducir uso de redes sociales a 2h"] = mejora

    # 4. Dormir al menos 7h
    if X_sim["horas_sueno_dia"].values[0] < 7:
        X_tmp = X_sim.copy()
        X_tmp["horas_sueno_dia"] = 7
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["🛌 Dormir al menos 7h"] = mejora

    # 5. Hacer ejercicio 3h o más
    if X_sim["horas_ejercicio_semanal"].values[0] < 3:
        X_tmp = X_sim.copy()
        X_tmp["horas_ejercicio_semanal"] = 3
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["🏃 Hacer al menos 3h de ejercicio"] = mejora

    # 6. Estudiar más días por semana
    if X_sim["frecuencia_estudio_dia"].values[0] < 4:
        X_tmp = X_sim.copy()
        X_tmp["frecuencia_estudio_dia"] = 5
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["📆 Estudiar al menos 5 días a la semana"] = mejora

    # 7. Más práctica en habilidades
    if X_sim["horas_habilidades_dia"].values[0] < 2:
        X_tmp = X_sim.copy()
        X_tmp["horas_habilidades_dia"] = 3
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["🧠 Practicar habilidades 3h al día"] = mejora

    # 8. Asistir a tutorías si no lo hace
    if X_sim["tutorias_docentes"].values[0] == 0:
        X_tmp = X_sim.copy()
        X_tmp["tutorias_docentes"] = 1
        mejora = modelo_gb.predict(X_tmp)[0] - nota_base
        mejoras["👨‍🏫 Asistir a tutorías docentes"] = mejora

    # 📣 Mostrar sugerencias útiles
    st.subheader("🔧 Recomendaciones personalizadas para mejorar tu nota:")
    alguna = False
    for accion, mejora in mejoras.items():
        if mejora > 0.2:
            alguna = True
            st.write(f"✅ {accion} → mejora estimada: **+{mejora:.2f} pts**")
        elif mejora > 0.05:
            alguna = True
            st.write(f"☑️ {accion} → posible mejora: +{mejora:.2f} pts")
    if not alguna:
        st.info("✅ ¡Tu perfil ya es bastante sólido! No se encontraron mejoras evidentes.")



from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    # Datos para tu CV
    cv_data = {
        'nombre': 'Eduardo Velazquez Sosa',
        'puesto': 'Aspirante a Data Scientist',
        'foto':'https://png.pngtree.com/thumb_back/fw800/background/20221108/pngtree-traveler-man-enjoying-by-scenic-of-mountains-person-young-scenics-photo-image_40834320.jpg',
        'resumen': 'Egresado de la Ingeniería en Sistemas Computacionales experiencia en análisis estadístico y funciones administrativas en entornos de alta exigencia como el Aeropuerto Internacional de Cancún. Me desempeñé como encargado del área de estadísticas delictivas, desarrollando reportes mensuales y seguimiento de indicadores clave. Con habilidades en Excel, Python y SQL, capacidad para trabajar bajo presión, actitud proactiva y excelente redacción, busco integrarme como Asistente Comercial en una empresa dinámica donde pueda aportar y seguir desarrollándome profesionalmente',
        'experiencia': [
            {'puesto': 'Encargado del Area de Estadisticas / Administrativo', 'empresa': 'Aeropuerto Internacional de Cancun', 'años': '2021-2025'}
            
        ],
        'educacion': [
            {'titulo': 'Ingeniería en Sistemas Computacionales', 'institucion': 'Universidad Aztlan', 'años': '2021-2024', 'resumen': 'Formación orientada al diseño, desarrollo e implementación de soluciones tecnológicas. Aprendí programación, bases de datos, redes, inteligencia artificial, análisis de datos, ciberseguridad y arquitectura de software. Participé en proyectos que integran tanto hardware como software para resolver problemas reales con tecnología.'},
            {'titulo': 'Diplomado en Desarrollo Web', 'institucion': 'Universidad Aztlan', 'años': '2024', 'resumen':'Formación práctica en el desarrollo de sitios web dinámicos y responsivos. Aprendí a estructurar y diseñar páginas con HTML y CSS, implementar interactividad mediante JavaScript, y desarrollar funcionalidades del lado del servidor utilizando PHP. Incluyó buenas prácticas de programación, control de versiones con Git, y trabajo con formularios, bases de datos y despliegue web.'},
            {'titulo': 'Maestria en Analisis e Interpretacion de Datos Digitales (En curso)', 'institucion': 'Universidad Oriente', 'años': '2025-2026', 'resumen':'Formación orientada al dominio de herramientas y metodologías para la recopilación, procesamiento, análisis e interpretación de grandes volúmenes de datos. El plan de estudios abarca temas clave como ciencia de datos, inteligencia artificial, modelos estadísticos, calidad y preparación de datos, ciberseguridad, bases de datos y programación avanzada, integrando enfoques técnicos y estratégicos para la toma de decisiones basadas en datos.'} 
        ],
        'cursos':[
            {'curso':'Python','icono':'/static/icons/python.png', 'acerca':'Aprendí desde los fundamentos del lenguaje hasta el desarrollo de aplicaciones web utilizando Flask y Django. Abarqué programación estructurada, manejo de archivos, APIs, entornos virtuales y creación de backends con bases de datos.','año':'2022','instituto':'Coderhouse','certificado':'/static/file/Python.png'},
            {'curso': 'JavaScript','icono':'/static/icons/js.png', 'acerca':'Dominié los principios del lenguaje JavaScript para desarrollo web, incluyendo manipulación del DOM, eventos, estructuras de datos, funciones asincrónicas y consumo de APIs. Realicé proyectos interactivos desde cero.', 'año': '2023','instituto':'Coderhouse','certificado':'/static/file/JS.png'},
            {'curso': 'SQL','icono':'/static/icons/db.png', 'acerca':'Aprendí a diseñar, consultar y gestionar bases de datos relacionales. Utilicé comandos DDL y DML, funciones agregadas, filtros y relaciones entre tablas. Manejo de bases de datos con MySQL.', 'año': '2025','instituto':'Coderhouse','certificado':'imagen'},
            {'curso': 'Data Science','icono':'/static/icons/ds.png', 'acerca':'Profundicé en análisis de datos con Python, utilizando bibliotecas como pandas, matplotlib, seaborn y scikit-learn. Trabajé con modelos de machine learning, validación cruzada y análisis predictivo con datos reales.', 'año': '2025','instituto':'Coderhouse','certificado':'imagen'},
        ],
        'habilidades': [
            {'interpersonales':['Resolución de Problemas','Trabajo en Equipo', 'Autodidacta','Aprendizaje continuo']},
            {'tecnicas': ['Python', 'SQL','Excel', 'Pandas', 'Automatización', 'Análisis de Datos', 'Flask']},
            {'idiomas':{'Español - Nativo':'','Ingles - En proceso':''}},
            ],
        'contacto': {
            'correo': 'eduardo99sosa@gmail.com.com',
            'telefono': '9983177355',
            'linkedin': 'https://linkedin.com/in/eduardo-velazquez-sosa-b1ab09268',
            'github': 'https://github.com/go1t3r'
        },
        'proyectos':[
            {'imagen': 'static/img/', 'titulo':'Analisis de delitos en el aeropuerto', 'descripcion':'limpieza y analisis de los datos que recopile durante los a los años en el aeropuerto de cancun', 'link':'www.proyecto.com'},
            {'imagen': 'static/img/', 'titulo':'Analisis de delitos en el aeropuerto', 'descripcion':'limpieza y analisis de los datos que recopile durante los a los años en el aeropuerto de cancun', 'link':'www.proyecto.com'},
            {'imagen': 'static/img/', 'titulo':'Analisis de delitos en el aeropuerto', 'descripcion':'limpieza y analisis de los datos que recopile durante los a los años en el aeropuerto de cancun', 'link':'www.proyecto.com'}
        ]
    }
    return render_template('index.html', cv=cv_data)

if __name__ == '__main__':
    app.run(debug=True)

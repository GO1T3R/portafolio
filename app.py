from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    # Datos para tu CV
    cv_data = {
        'nombre': 'Eduardo Velazquez Sosa',
        'puesto': 'Aspirante a Data Scientist',
        'foto':'https://png.pngtree.com/thumb_back/fw800/background/20221108/pngtree-traveler-man-enjoying-by-scenic-of-mountains-person-young-scenics-photo-image_40834320.jpg',
        'resumen': 'Ingeniero en Sistemas Computacionales con habilidades en Python, HTML/CSS, y fundamentos de Ciencia de Datos, actualmente en formación en Científico de Datos, con cinco años de experiencia en la secretaria de marina, en donde desarrollado una fuerte ética de trabajo, disciplina y habilidades para resolver problemas bajo presión. Busco mi primera oportunidad en el campo de la Ciencia de Datos, donde pueda aplicar y expandir mis conocimientos técnicos en un entorno colaborativo.',
        'experiencia': [
            {'puesto': 'Militar', 'empresa': 'Marina de México', 'años': '2017-2022'}
            
        ],
        'educacion': [
            {'titulo': 'Ingeniería en Sistemas Computacionales', 'institucion': 'Universidad Aztlan', 'años': '2021-2024', 'resumen': 'En la carrera adquiere la pasion por las estadisticas y el amor por la ciencia de datos, por lo que adquiere una base solida.'},
            {'titulo': 'Diplomado en Desarrollo Web', 'institucion': 'Universidad Aztlan', 'años': '2024', 'resumen':'Realice varios proyecto en el que destaco la creacion de una Tienda Online de Ropa utilizando tecnología comoHTML/CSS, JavaScript, PHP, SQL.'},
            {'titulo': 'Maestria en Analisis e Interpretacion de Datos Digitales', 'institucion': 'Universidad Oriente', 'años': 'Estudiante', 'resumen':'en proceso'} 
        ],
        'cursos':[
            {'curso':'Python','icono':'/static/icons/python.png', 'acerca':'Complete el curso de Python en Coderhouse, con temas como Django Framework y su MVT basado en Modelos, Vistas y Templates, asi como Git y Github.','año':'2022','instituto':'Coderhouse','certificado':'https://www.coderhouse.com/mx/certificados/62e6b89c998c0900242ccea8?lang='},
            {'curso': 'JavaScript','icono':'/static/icons/js.png', 'acerca':'Complete el curso de JavaScript en Cordehouse, en donde adquiri conocimiento sobre HTML/CSS y Javascript.', 'año': '2023','instituto':'Coderhouse','certificado':'https://www.coderhouse.com/mx/certificados/64399ef60bc3880002edda34?lang='} 
            ],
        'habilidades': [
            {'interpersonales':['Resolución de Problemas','Trabajo en Equipo', 'Autodidacta','Curiosidad']},
            {'tecnicas': ['Python', 'SQL', 'Pandas', 'Automatización', 'Análisis de Datos', 'Flask']},
            {'idiomas':{'Español - Nativo':'Nativo','Ingles - A2':'A2'}},
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

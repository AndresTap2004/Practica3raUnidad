
from flask import Flask, Blueprint, url_for, jsonify, make_response, request, render_template, redirect, abort
from controller.hospitalControl import HospitalControl
from controller.hospital_grafo import HospitalGrafo
from controller.haversine import haversine
import json
import os 

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('template.html')

@router.route('/grafo')
def grafo():
    return render_template('d3/grafo.html')

@router.route("/hospital/guardar_distancia/<int:origen>/<int:destino>", methods=['POST'])
def agregar_distancia(origen, destino):
    try:
        hospital_control = HospitalControl()
        lista = hospital_control._list().ordenar_models("_id")
        
        inicio = lista.search_binary("_id", origen)
        final = lista.search_binary("_id", destino)
        
        lon1, lat1 = inicio._lng, inicio._lat
        lon2, lat2 = final._lng, final._lat
        
        distancia = round(float(haversine(float(lon1), float(lat1), float(lon2), float(lat2))), 4)
        
        return jsonify({"distancia": distancia, "message": "Distancia guardada exitosamente."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@router.route('/hospital/grafo_hospital')
def grafo_hospital():
    hospital_grafo = HospitalGrafo()
    hospital_grafo.create_graph()
    return render_template('d3/grafo.html')

@router.route('/hospital/grafo_ver_admin')
def grafo_ver_admin():
    hospital_control = HospitalControl()
    lista = hospital_control._list()
    if not lista.isEmpty:
        lista.sort_models("_id")
    return render_template('hospital/grafo.html', lista=hospital_control.to_dic_lista(lista))

@router.route('/hospital/caminos')
def grafo_caminos():
    hospital_control = HospitalControl()
    lista = hospital_control._list()
    if not lista.isEmpty:
        lista.sort_models("_id")
    return render_template('hospital/ver_camino.html', lista=hospital_control.to_dic_lista(lista))

@router.route('/hospital/camino/<origen>/<destino>')
def ver_camino(origen, destino):
    try:
        hospital_grafo = HospitalGrafo()
        camino_corto_djistra, tiempo_djistra = hospital_grafo.buscar_camino_corto_djistra(int(origen), int(destino))
        camino_corto_floyd, tiempo_floyd = hospital_grafo.buscar_camino_corto_floyd(int(origen), int(destino))

        data = {
            "camino_corto_djistra": camino_corto_djistra,
            "tiempo_djistra": tiempo_djistra,
            "camino_corto_floyd": camino_corto_floyd,
            "tiempo_floyd": tiempo_floyd
        }
        
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@router.route('/hospital/guardar_json', methods=['POST'])
def guardar_grafo():
    try:
        data = request.get_json()
        ruta_actual = os.path.dirname(os.path.dirname(__file__))+"\data"
        hospital_grafo = HospitalGrafo()
        hospital_grafo.create_graph()
        with open(os.path.join(ruta_actual, 'grafo.json'), 'w') as f:
            json.dump(data, f)
        return jsonify({"message": "Guardado en JSON exitosamente."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@router.route('/hospital/cargar_json', methods=['GET'])
def cargar_grafo():
    try:
        ruta_actual = os.path.dirname(os.path.dirname(__file__))+"\data"
        with open(os.path.join(ruta_actual, 'grafo.json')) as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "El archivo grafo.json no existe."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@router.route('/hospital')
def lista_hospitales():
    hospital_control = HospitalControl()
    lista = hospital_control._list()
    lista.sort_models("_id")
    return render_template('hospital/lista.html', lista=hospital_control.to_dic_lista(lista))

@router.route("/hospital/agregar")
def agregar_hospital():
    return render_template('hospital/guardar.html')



@router.route('/hospital/guardar', methods = ['POST'])  
def guardar_hospital():
    hospital_control = HospitalControl()
    data = request.form
    if not "nombre" in data.keys() or not "direccion" in data.keys() or not "horario" in data.keys() or not "latitud" in data.keys() or not "longitud" in data.keys():
       abort(400)
    hospital_control._hospital._nombre = data['nombre']
    hospital_control._hospital._direccion = data['direccion']
    hospital_control._hospital._horario = data['horario']
    hospital_control._hospital._lat = request.form['latitud']
    hospital_control._hospital._lng = request.form['longitud']
    hospital_control.save
    return redirect("/hospital", code=302)




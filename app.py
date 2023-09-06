from flask import Flask, render_template, request, Response, url_for, jsonify, redirect
import modelo as baseDeDatos
from usuario import Usuario

bd=baseDeDatos.conexionBd()

app=Flask(__name__)

@app.route("/")
def inicio():
    encabezado_tabla=["Nombre", "Correo", "Contraseña"]
    usuarios=bd["usuarios"]
    usuariosRegistrados=usuarios.find()
    return render_template("index.html",
                           encabezado_tabla=encabezado_tabla,
                           usuarios=usuariosRegistrados)
    
    
@app.route("/registro", methods=["POST"])
def agregar():
    usuarios=bd["usuarios"]
    nombre=request.form["nombre"]
    correo=request.form["correo"]
    contraseña=request.form["contraseña"]
    if nombre and correo and contraseña:
        usuario=Usuario(nombre, correo, contraseña)
        usuarios.insert_one(usuario.aLaColeccion())
        Response=jsonify({
            "nombre": nombre,
            "correo":  correo,
            "contraseña":contraseña
        })
        return redirect(url_for("inicio"))
    else:
        return notFound()

@app.route("/editar/<string:nombre_usuario>", methods=["POST"])
def editar(nombre_usuario):
    usuarios=bd["usuarios"]
    nombre=request.form["nombre"]
    correo=request.form["correo"]
    contraseña=request.form["contraseña"]
    if nombre and correo and contraseña:
        usuarios.update_one({"nombre":nombre_usuario},
            {"$set": {"nombre":nombre,
                      "correo":correo,
                      "contraseña":contraseña}})
        Response=jsonify({"mensaje":"Usuario"+nombre_usuario+"actuaizado correctamente"})
        return redirect(url_for("inicio"))
    else:
        return notFound()
    

@app.route("/eliminar/<string:nombre_usuario>")
def eliminar(nombre_usuario):
    usuarios=bd["usuarios"]
    usuarios.delete_one({"nombre":nombre_usuario})
    return redirect(url_for("inicio"))
    

@app.errorhandler(404)
def notFound(error=None):
    mensaje={
        "mensaje":"no encontrado"+request.url,
        "status":"404 Not Found"
    }
    Response=jsonify(mensaje)
    Response.status=404
    return Response
        

if __name__ =="__main__":
    app.run("127.0.0.1", 5000, debug=True)
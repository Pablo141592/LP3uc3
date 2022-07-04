from django.shortcuts import render , HttpResponse

# Create your views here.

def inicio(request):
    mensaje = """
             <h1>Universidad Nacional Tecnológica de Lima Sur</h1> 
             <h2>EP Ingeniería de Sistemas</h2>
             <h3>Bienvenidos</h3>
    """
    return HttpResponse(mensaje)

def uc3(request):
    mensaje = """
             <h1>Lenguaje de Programación III</h1> 
             <h2>Evaluación de la Unidad de Competencia 3</h2>
             <h3>Docente: Mg. Flor Elizabeth Cerdán León</h3>
             <div>
             <h3><u>Integrantes :</u></h3>
              <h3>Acuña Saavedra Fernando</h3>
              <h3>Condori Condori Roxana</h3>
              <h3>Trigo Suarez Ricardo Pablo</h3>
             </div>
             
    """
    return HttpResponse(mensaje)

def noticia(request):
    mensaje = """
                
<h1>Metro, Metropolitano y los corredores no paran</h1>
<h2>Tampoco transporte urbano de lima e interprovincial; y ejecutivo dice que solo hay 3 puntos
para solucionar conflicto con un sector.</h2>
<p>
<h3>
Todas las empresas formales de transporte interprovincial de pasajeros que operan en los diferentes
terminales terrestres de Lima, así como los servicios del Metro, Metropolitano y los corredores operarán
con normalidad este lunes 4 de julio, desacatando el paro convocado por un grupo de transportistas para esa fecha.
Así lo informó el gerente general de la Asociación de Empresas de Transporte Interprovincial de Pasajeros (Cotrap – Apoip), 
Martín Ojeda, quien sostuvo que dicho paro es organizado por un grupo de transportistas provinciales e interprovincial 
que operan de manera ilegal.
“Ya sabemos que Giovanni Diez (vocero de los gremios de transporte multimodal) es el promotor de todo esto, 
es el vocero del transporte ilegal tenemos audio y videos, es una infamia”, manifestó.
</h3>
</p>
<div><strong><u>Habrá movilidad</u></strong></div>
<p>
<h3>
Por su parte, la Autoridad de Transporte Urbano (ATU) para Lima y Callao informó que los servicios del Metropolitano,
 los Corredores Complementarios y la Línea 1 del Metro funcionarán con normalidad a fin de garantizar la movilidad 
 de todos sus usuarios.<br>
Añadió que serán 300 los buses del Metropolitano que brindarán su servicio de manera habitual en la ruta troncal,
 mientras que 210 buses realizarán el servicio alimentador y otros 581 brindarán servicios en los corredores complementarios.
</h3>
</p>         
    """
    return HttpResponse(mensaje)



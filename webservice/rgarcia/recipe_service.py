"""Este modulo contiene la parte del servicio de las Recetas."""
from spyne import Application, ComplexModel, Decimal, Service, String, srpc
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class Receta(ComplexModel):
    """Clase de Recetas."""
    nombre = String
    ingredientes = list
    pasos = list

class RecetaService(Service):
    """Servicio de Recetas."""
    @srpc(_returns=Decimal) 
    def list():
        """Regresa la lista de Recetas."""
        return {}

    @srpc(String,String,String)
    def registrar(nombre,ingredientes,pasos):
        """Metodo para agregar una nueva receta."""
        Receta(nombre,ingredientes,pasos)
        return 

spyne_app = Application(
    services=[RecetaService],
    tns="com.rgarcia.recetas",
    name="Recetas",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11(validator="lxml"),
)

wsgi_app = WsgiApplication(spyne_app)

import requests
from loguru import logger
from datetime import datetime
import os
from typing import Dict, List

from api_server_request import (
    api_server_get_request,
    api_server_post_request,
    api_server_put_request,
)

# ===================== servicios APISOL-INTERNO =====================
APISOL_INTERNO = os.getenv("APISOL_INTERNO", "http://apisol-interno.intravexi.mx")
URL_PARAMS_SET_MARCA = "/v1/sol-corta/params-lista-esp/"
URL_GET_EMAIL = "/v1/sol-corta/solictudes/{}/email/"
# ===================== servicios APISOL-INTERNO =====================

# ===================== servicios APISOL-ORQUESTADOR =====================
APISOL_ORQUESTADOR = os.getenv("APISOL_ORQUESTADOR", "http://apisol-orquestador.intravexi.mx")
URL_GENERACION_CLIENTE = "/v1/solicitud/{}/ejecutar-generacion-cliente/"
URL_VALIDACION_IDENTIDAD = "/v1/solicitudes-cc/{}/emails/{}/paseb-cc/"  # id_sol, email
URL_OBTENER_FACEBOOK_ID = (
    "/v1/solicitud/obtener-fbid/{}"  # Obtener  y/o genera el fbid de una solicitud
)
DICTA_SERVER: str = os.getenv("APISOL_DICTAMINACION", "http://apidicta-interno.intravexi.mx")
GENERAR_SOLICITUD_DICTA = "/v1/dictaminacion/crear-registro-solicitud/"
PASEB_CUENTAS_CANCELADAS = "/v1/solicitudes-cc/{}/emails/{}/paseb-cc/"

# ===================== servicios APISOL-INTERNO =====================


# ===================== PARAMS TO main ===============================
DATE_START = "2023-07-20 00:00:00"
# ===================== PARAMS TO main ===============================

# ===================== CONSTANTES ===============================
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
# ===================== CONSTANTES ===============================

DATOS_PARA_PROCESAR = [
2219965,
2220390,
2220288,
2220191,
2220374,
2219397,
2220385,
2220323,
2219907,
2220332,
2219784,
2220343,
2220230,
2220133,
2220167,
2219115,
2220334,
2220158,
2220376,
2219998,
2219320,
2219808,
2220168,
2220355,
2219909,
2222392,
2222391,
2222389,
2222386,
2222140,
2222385,
2222395,
2222294,
2222442,
2222344,
2222261,
]



def main(datos: List[Dict[str, object]]) -> None:

    logger.info(f"---fechas para iniciar  {locals()} ")

    if not datos:
        return

    logger.info(f"---Total de solicitudes a terminar {len(datos)} --- ")
    contador_procesado = 0
    for id_solicitud in datos:
        
        logger.info(f"---solicitud a  terminar {id_solicitud} --- ")

        try:
            response = api_server_post_request(
                url=APISOL_ORQUESTADOR + URL_GENERACION_CLIENTE.format(id_solicitud), data={}
            )

            logger.info(f" --- id_solicitud {id_solicitud}   ----- response {response}")
            contador_procesado += 1

        except Exception as exc:
            logger.exception(f" ---Error en LLAMAR AL SERVICIO {id_solicitud} Error:{exc}")
    logger.info(f"---Total de solicitudes a terminar {len(datos)} ---  procesadas {contador_procesado}")

if __name__ == "__main__":
    main(datos=DATOS_PARA_PROCESAR)

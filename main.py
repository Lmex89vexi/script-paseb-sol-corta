import requests
from loguru import logger
import os
from typing import Dict, List

from api_server_request import (
    api_server_post_request,
)

# ===================== servicios APISOL-ORQUESTADOR =====================
APISOL_ORQUESTADOR = os.getenv(
    "APISOL_ORQUESTADOR", "http://apisol-orquestador.intravexi.mx"
)






# ===================== servicios APISOL-INTERNO =====================




def main(datos: List[Dict[str, object]]) -> None:
    logger.info(f"---fechas para iniciar  {locals()} ")

    if not datos:
        return

    logger.info(f"---Total de solicitudes a GENERA RANDOM DIGIT {len(datos)} --- ")
    contador_procesado = 0
    for id_solicitud in datos:
        logger.info(f"---solicitud a  GENERA RANDOM DIGIT {id_solicitud} --- ")

        try:
            response = api_server_post_request(
                url=APISOL_INTERNO + POST_GENERAR_RANDOM_DIGITTS.format(id_solicitud),
                data={},
            )

            logger.info(f" --- id_solicitud {id_solicitud}   ----- response {response}")
            contador_procesado += 1

        except Exception as exc:
            logger.exception(
                f" ---Error en LLAMAR AL SERVICIO {POST_GENERAR_RANDOM_DIGITTS} {id_solicitud} Error:{exc}"
            )
    logger.info(
        f"---Total de solicitudes a GENERA RANDOM DIGIT {len(datos)} ---  procesadas {contador_procesado}"
    )


if __name__ == "__main__":
    main(datos=DATOS_PARA_PROCESAR)

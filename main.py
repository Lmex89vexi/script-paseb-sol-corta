from constantes import DATOS_PARA_PROCESAR
from loguru import logger
from typing import  List

from api_server_request import (
    api_server_put_request,
)

# ===================== servicios APISOL-ORQUESTADOR =====================
APISOL_ORQUESTADOR = "http://172.20.80.1:61997/"
PASEB_SOL_CORTA = "v1/solicitud/paseb-sol-corta/manual/{}/"
# ===================== servicios APISOL-ORQUESTADOR =====================




def main(datos: List[int]) -> None:
    logger.info(f"---id_solicitudes a procesar {locals()} ")

    if not datos:
        return

    contador_procesado = 0
    for id_solicitud in datos:
        logger.info(f"---solicitud a  procesar {id_solicitud} --- ")

        try:
            logger.debug(f" --- LLAMAR AL SERVICIO {APISOL_ORQUESTADOR}/{PASEB_SOL_CORTA.format(id_solicitud)} ")
            response = api_server_put_request(
                url=APISOL_ORQUESTADOR + PASEB_SOL_CORTA.format(id_solicitud),
                data={},
            )

            logger.info(f" --- id_solicitud {id_solicitud}   ----- response {response}")
            contador_procesado += 1

        except Exception as exc:
            logger.exception(
                f" ---Error en LLAMAR AL SERVICIO {PASEB_SOL_CORTA} {id_solicitud} Error:{exc}"
            )
    logger.success(
        f"---Total de solicitudes a procesador con exito {contador_procesado} ---  Total {len(datos)}"
    )


if __name__ == "__main__":
    main(datos=DATOS_PARA_PROCESAR)

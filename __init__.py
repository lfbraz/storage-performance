import logging

import azure.functions as func
import TestsStorage.storage_tests as storage


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    type = req.params.get('type')
    local = True if type=="Local" else False

    # Run Local Tests
    storage.run(local)

    if type:
        return func.HttpResponse(f"{type} test executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

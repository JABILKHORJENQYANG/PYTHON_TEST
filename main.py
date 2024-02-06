import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Your function logic here\
    print("hello world")
    return func.HttpResponse("Hello from Azure Function App!", status_code=200)


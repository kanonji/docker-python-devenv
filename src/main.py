from fastapi import FastAPI, status

print('Hello, World!')

app = FastAPI(docs_url='/api/docs',
              openapi_url='/api/openapi.json')
@app.get(
    '/api/hello',
    description='Hello',
    status_code=status.HTTP_200_OK,
)
async def index():
    return {'message': 'Hello, world!'}

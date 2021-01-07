from starlette.schemas import SchemaGenerator


schemas = SchemaGenerator(
    {
        "openapi": "3.0.0",
        "info": {
            "title": "RSS XML URL Substitution API", "version": "1.0"
        },
        "paths": {
            "/api/": {
                "get": {
                    "summary": "substitue from remote xml file",
                    "parameters": [{
                        "in": "query",
                        "name": "rss",
                        "required": True,
                        "schema": {"type": str},
                        "description": "remote xml file url"
                    }, {
                        "in": "query",
                        "name": "tags",
                        "schema": {"type": str},
                        "description": "tags whose src/herf attr need to be replaced, default: `tags=img|a`"
                    },
                    ],
                    "responses": {
                        200: {
                            "description": "Success",
                        },
                        400: {
                            "description": "Failed, short of query parameter `rss`",
                        }
                    }
                },
                "post": {
                    "summary": "substitue from local xml file",
                    "requestBody": "string representation of an XML element. ",
                    "required": True,
                    "content": "application/xml",
                    "responses": {
                        200: {"description": "Success"}
                    }
                },
            },
        },
    }
)


async def schema(request):
    return schemas.OpenAPIResponse(request=request)

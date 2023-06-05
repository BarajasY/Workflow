from django.core.serializers import json as jsons
import json

class Boilerplate:

    def querytojson(queryset):
        json_serializer = jsons.Serializer()
        body = json_serializer.serialize(queryset)
        return body

    def decode_request_body(body):
        decode = body.decode("utf-8")
        jsonBody = json.loads(decode)
        return jsonBody

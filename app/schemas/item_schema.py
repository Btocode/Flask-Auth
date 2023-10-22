from marshmallow import Schema, fields

class ItemSchema(Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'user_id')  # Define the fields you want to include in the response
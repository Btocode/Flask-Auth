from marshmallow import Schema, fields

class UserSchema(Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'full_name')  # Define the fields you want to include in the response
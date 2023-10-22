Certainly, here's the updated API documentation that includes the "Items" endpoints in addition to the previously documented endpoints:

## Registering a User

- **URL**: `localhost:5000/auth/register` (POST)

**Request Data:**

```json
{
  "username": "john.cena",
  "password": "1111",
  "email": "john@gmail.com",
  "full_name": "Johncena"
}
```

**Response:**

- **Status Code**: 201 Created
- **Message**: "User 'john.cena' has been registered successfully."

## Logging In

- **URL**: `localhost:5001/auth/login` (POST)

**Request Data:**

```json
{
  "username": "john.cena",
  "password": "1111"
}
```

**Response:**

- **Status Code**: 200 OK
- **Message**: "Login successful. Welcome, john.cena."
- **JWT Token**: [Your JWT Token]

## Refreshing Access Token

- **URL**: `localhost:5000/auth/refresh` (POST)

**Request Data:**

- **Authorization Header**: Bearer `<refresh_token>`

**Response:**

- **Status Code**: 200 OK
- **Message**: "Access token has been successfully refreshed."
- **Response Data:**

```json
{
  "access_token": "<new_access_token>",
  "refresh_token": "<new_refresh_token>"
}
```

## Get All Users

- **URL**: `localhost:5001/users` (GET)

**Request Header:**

- **Authorization Header**: Bearer `<access_token>`

**Response:**

- **Status Code**: 200 OK
- **Response Data**: An array of user objects, each containing user information.

## Get Single User

- **URL**: `localhost:5001/users/<user_id>` (GET)

**Request Header:**

- **Authorization Header**: Bearer `<access_token>`

**Response:**

- **Status Code**: 200 OK
- **Response Data**: User information for the specified user ID.

## Get All Items

- **URL**: `localhost:5001/items` (GET)

**Response:**

- **Status Code**: 200 OK
- **Response Data**: An array of item objects, each containing item information.

## Create an Item

- **URL**: `localhost:5001/items` (POST)

**Request Header:**

- **Authorization Header**: Bearer `<access_token>`

**Request Data:**

```json
{
  "name": "Pendrive",
  "description": "16gb"
}
```

**Response:**

- **Status Code**: 201 Created
- **Message**: "Item 'Pendrive' has been created."

## Delete an Item

- **URL**: `localhost:5001/items/<item_id>` (DELETE)

**Request Header:**

- **Authorization Header**: Bearer `<access_token>`

**Response:**

- **Status Code**: 200 OK
- **Message**: "Item with ID `<item_id>` has been deleted."

## Update an Item

- **URL**: `localhost:5001/items/<item_id>` (PUT)

**Request Header:**

- **Authorization Header**: Bearer `<access_token>`

**Request Data:**

```json
{
  "name": "Updated Pendrive",
  "description": "32gb"
}
```

**Response:**

- **Status Code**: 200 OK
- **Message**: "Item with ID `<item_id>` has been updated."

**Description:**

- Use the "Register a User" endpoint to create a new user with the specified details.
- Use the "Login" endpoint to authenticate a user by providing their `username` and `password`. Upon successful login, you'll receive a JWT token for authentication.
- To refresh the access token, make a POST request to the "Refresh Token" endpoint and provide the refresh token in the Authorization header as "Bearer <refresh_token>." The API will return a new access token and a new refresh token.
- The "Get All Users" endpoint allows you to retrieve a list of all registered users. To access this route, include a valid access token in the Authorization header.
- The "Get Single User" endpoint retrieves user information for a specific user with the given `user_id` in the URL. Make sure to include a valid access token in the Authorization header.
- The "Get All Items" endpoint allows you to retrieve a list of all available items. It's a public route and doesn't require authentication.
- To create a new item, make a POST request to the "Create an Item" endpoint and provide a valid access token along with the payload containing the `name` and `description` of the item you want to create.
- To delete an item, make a DELETE request to the "Delete an Item" endpoint and specify the `item_id` in the URL to indicate which item to delete. Include a valid access token in the Authorization header.
- To update an item, make a PUT request to the "Update an Item" endpoint, specify the `item_id` in the URL to indicate which item to update, and provide a valid access token. Include a payload with the updated `name` and `description` of the item.

Ensure that the Flask application is running and that you have valid access tokens before making these API requests.

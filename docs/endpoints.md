# Project: cat-diet

github repo: [https://github.com/wenxuan-pan/WenxuanPan_T2A2](https://github.com/wenxuan-pan/WenxuanPan_T2A2)

# 📁 Collection: auth

## End-point: /auth/register

Arguments: None

Description: Creates a user in the database

Authentication: None

Authorization: None

Required fields: email (str), password (str), username (str)

Optional fields: None

### Method: POST

> ```
> http://127.0.0.1:5000/auth/register
> ```

### Body (**raw**)

```json
{
  "email": "apple@gmail.com",
  "password": "spamegg123",
  "username": "apple"
}
```

### 🔑 Authentication noauth

| Param | value | Type |
| ----- | ----- | ---- |

### Response: 201

```json
{
  "id": 4,
  "username": "apple",
  "email": "apple@gmail.com",
  "is_admin": false,
  "joined_since": "2023-06-28",
  "cats": []
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /auth/login

Arguments: None

Description: allows user to login and receive a token for authentication and authorization

Authentication: Email + Password

Authorization: None

Required fields: email (str), password(str)

Optional fields: None

### Method: POST

> ```
> http://127.0.0.1:5000/auth/login
> ```

### Body (**raw**)

```json
{
  "email": "john@gmail.com",
  "password": "johnisuser123"
}
```

### 🔑 Authentication noauth

| Param | value | Type |
| ----- | ----- | ---- |

### Response: 200

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4NzkzNTM4NCwianRpIjoiY2NlNjIzZDktMzNkYi00MDI5LTk0YzMtYmJjZGY4NzYyNmQ5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjg3OTM1Mzg0LCJleHAiOjE2OTA1MjczODR9.J04Pl0t8DJFDPxVaPLJmXep4j9huLLg0jfe0Mkv552A",
  "user": {
    "id": 1,
    "username": "MaryDev",
    "email": "marydev@gmail.com",
    "is_admin": true,
    "joined_since": "2023-06-20"
  },
  "statistics": {
    "total_cats": 0,
    "total_notes": 0,
    "total_food_reviewed": null
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: users

## End-point: /users

Arguments: None

Description: Return a list of all users in the database

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/users
> ```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
[
  {
    "id": 1,
    "username": "MaryDev",
    "email": "marydev@gmail.com",
    "is_admin": true,
    "joined_since": "2023-06-20",
    "cats": []
  },
  {
    "id": 2,
    "username": "John",
    "email": "john@gmail.com",
    "is_admin": false,
    "joined_since": "2023-06-20",
    "cats": [
      {
        "id": 1,
        "name": "Luna",
        "breed": "Domestic Shorthair",
        "year_born": 2020,
        "year_adopted": 2021
      }
    ]
  },
  {
    "id": 3,
    "username": "Frank",
    "email": "frank@gmail.com",
    "is_admin": false,
    "joined_since": "2023-06-20",
    "cats": [
      {
        "id": 2,
        "name": "Leo",
        "breed": "Exotic Shorthair",
        "year_born": null,
        "year_adopted": 2022
      },
      {
        "id": 3,
        "name": "Milo",
        "breed": "Ragdoll",
        "year_born": 2015,
        "year_adopted": 2019
      },
      {
        "id": 4,
        "name": "Oreo",
        "breed": "Domestic Longhair",
        "year_born": null,
        "year_adopted": 2019
      }
    ]
  }
]
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /users

Arguments: None

Description: Allows admin to create a new user or admin in the database

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: username (str), email (str), password (str)

Optional fields: is_admin (bool)

### Method: POST

> ```
> http://127.0.0.1:5000/users
> ```

### Body (**raw**)

```json
{
  "username": "newuser",
  "email": "newuser@gmail.com",
  "is_admin": true,
  "password": "default123"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 201

```json
{
  "id": 4,
  "username": "newuser",
  "email": "newuser@gmail.com",
  "is_admin": true,
  "joined_since": "2023-06-30",
  "cats": []
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /users/user_id

Arguments: user id

Description: returns information and statistics of the selected user

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/users/:user_id
> ```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 2,
  "username": "John",
  "email": "john@gmail.com",
  "is_admin": false,
  "joined_since": "2023-06-20",
  "cats": [
    {
      "id": 1,
      "name": "Luna",
      "breed": "Domestic Shorthair",
      "year_born": 2020,
      "year_adopted": 2021
    }
  ],
  "statistics": {
    "total_cats": 1,
    "total_notes": 5,
    "total_foods_reviewed": 3
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /users/user_id

Arguments: user id

Description: allows owner or admin to update user information of the selected id (except is_admin and joined_since fields)

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: username (str), email (str), password (str)

Note: is_admin and joined_since status cannot be changed

### Method: PUT

> ```
> http://127.0.0.1:5000/users/:user_id
> ```

### Body (**raw**)

```json
{
  "username": "new_name",
  "email": "newmaryemail@gmail.com",
  "password": "newpassword123"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 1,
  "username": "new_name",
  "email": "newmaryemail@gmail.com",
  "is_admin": true,
  "joined_since": "2023-06-20"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /users/user_id

Arguments: user id

Description: allows owner or admin to update user information of the selected id (except is_admin and joined_since fields)

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: username (str), email (str), password (str)

Note: is_admin and joined_since status cannot be changed

### Method: PATCH

> ```
> http://127.0.0.1:5000/users/:user_id
> ```

### Body (**raw**)

```json
{
  "username": "new_name",
  "email": "newmaryemail1@gmail.com",
  "password": "newpassword123"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /users/user_id

Arguments: user id

Description: Allows admin to delete a user from the database

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: None

### Method: DELETE

> ```
> http://127.0.0.1:5000/users/:user_id
> ```

### Body (**raw**)

```json

```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: foods

## End-point: /foods

Arguments: None

Description: returns a list of foods with their ingredients and related notes

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/foods
> ```

### Response: 200

```json
[
  {
    "id": 1,
    "name": "Tuna With Prawn Canned Adult Cat Food",
    "brand": "Applaws",
    "category": "Wet",
    "ingredients": [
      {
        "id": 5,
        "name": "Tuna",
        "category": "Seafood"
      },
      {
        "id": 6,
        "name": "Prawn",
        "category": "Seafood"
      }
    ],
    "notes": [
      {
        "id": 1,
        "message": "Luna was ok with it, maybe will try a different one",
        "rating": 0,
        "date_recorded": "2023-06-24",
        "cat": {
          "id": 1,
          "name": "Luna",
          "breed": "Domestic Shorthair",
          "owner": {
            "username": "John"
          }
        }
      }
    ]
  },
  {
    "id": 2,
    "name": "Chicken Wet Cat Food Cans",
    "brand": "Ziwi",
    "category": "Wet",
    "ingredients": [
      {
        "id": 1,
        "name": "Chicken",
        "category": "Meat"
      }
    ],
    "notes": [
      {
        "id": 3,
        "message": "Tried a different can and Luna only ate half of it",
        "rating": 0,
        "date_recorded": "2023-06-25",
        "cat": {
          "id": 1,
          "name": "Luna",
          "breed": "Domestic Shorthair",
          "owner": {
            "username": "John"
          }
        }
      },
      {
        "id": 4,
        "message": "Luna ate the whole can, she likes it!",
        "rating": 1,
        "date_recorded": "2023-06-26",
        "cat": {
          "id": 1,
          "name": "Luna",
          "breed": "Domestic Shorthair",
          "owner": {
            "username": "John"
          }
        }
      },
      {
        "id": 5,
        "message": "Luna is still happy with it!",
        "rating": 1,
        "date_recorded": "2023-06-26",
        "cat": {
          "id": 1,
          "name": "Luna",
          "breed": "Domestic Shorthair",
          "owner": {
            "username": "John"
          }
        }
      },
      {
        "id": 6,
        "message": "Leo hates it",
        "rating": -1,
        "date_recorded": "2023-06-20",
        "cat": {
          "id": 2,
          "name": "Leo",
          "breed": "Exotic Shorthair",
          "owner": {
            "username": "Frank"
          }
        }
      },
      {
        "id": 7,
        "message": "Milo was the only cat eating the can, but not finished it either",
        "rating": 0,
        "date_recorded": "2023-06-20",
        "cat": {
          "id": 3,
          "name": "Milo",
          "breed": "Ragdoll",
          "owner": {
            "username": "Frank"
          }
        }
      },
      {
        "id": 8,
        "message": "Oreo sniffed and went away",
        "rating": -1,
        "date_recorded": "2023-06-20",
        "cat": {
          "id": 4,
          "name": "Oreo",
          "breed": "Domestic Longhair",
          "owner": {
            "username": "Frank"
          }
        }
      }
    ]
  },
  {
    "id": 3,
    "name": "Adult Oral Care Dry Cat Food",
    "brand": "Hills Science Diet",
    "category": "Dry",
    "ingredients": [
      {
        "id": 1,
        "name": "Chicken",
        "category": "Meat"
      },
      {
        "id": 3,
        "name": "Brown Rice",
        "category": "Grains"
      }
    ],
    "notes": []
  },
  {
    "id": 4,
    "name": "Feline Treats Dental Catnip Flavour Tub",
    "brand": "Greenies",
    "category": "Treats",
    "ingredients": [
      {
        "id": 4,
        "name": "Ground Wheat",
        "category": "Grains"
      },
      {
        "id": 7,
        "name": "Chicken Meal",
        "category": "Derivatives"
      }
    ],
    "notes": [
      {
        "id": 2,
        "message": "Luna likes the treats",
        "rating": 1,
        "date_recorded": "2023-06-24",
        "cat": {
          "id": 1,
          "name": "Luna",
          "breed": "Domestic Shorthair",
          "owner": {
            "username": "John"
          }
        }
      },
      {
        "id": 9,
        "message": "Leo likes it",
        "rating": 1,
        "date_recorded": "2023-06-21",
        "cat": {
          "id": 2,
          "name": "Leo",
          "breed": "Exotic Shorthair",
          "owner": {
            "username": "Frank"
          }
        }
      }
    ]
  }
]
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /foods

Arguments: None

Description: creates a new food in the database

Authentication: JWT Required

Authorization: Bearer Token (logged in user)

Required fields: name (str)

Optional fields: brand (str), category (str), ingredients (list)

### Method: POST

> ```
> http://127.0.0.1:5000/foods
> ```

### Body (**raw**)

```json
{
  "name": "Cats In The Kitchen Pantry Party Pouch Variety Pack In Gravy Wet Cat Food Pouches",
  "category": "wet",
  "brand": "Weruva",
  "ingredients": [{ "id": 1 }, { "id": 2 }]
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 201

```json
{
  "id": 5,
  "name": "Cats In The Kitchen Pantry Party Pouch Variety Pack In Gravy Wet Cat Food Pouches",
  "brand": "Weruva",
  "category": "Wet",
  "ingredients": [
    {
      "id": 1,
      "name": "Chicken",
      "category": "Meat"
    },
    {
      "id": 2,
      "name": "Lamb",
      "category": "Meat"
    }
  ],
  "notes": []
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /foods/food_id

Arguments: food id

Description: returns food of the selected id

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/foods/:food_id
> ```

### Response: 200

```json
{
  "id": 1,
  "name": "Tuna With Prawn Canned Adult Cat Food",
  "brand": "Applaws",
  "category": "Wet",
  "ingredients": [
    {
      "id": 5,
      "name": "Tuna",
      "category": "Seafood"
    },
    {
      "id": 6,
      "name": "Prawn",
      "category": "Seafood"
    }
  ],
  "notes": [
    {
      "id": 1,
      "message": "Luna was ok with it, maybe will try a different one",
      "rating": 0,
      "date_recorded": "2023-06-24",
      "cat": {
        "id": 1,
        "name": "Luna",
        "breed": "Domestic Shorthair",
        "owner": {
          "username": "John"
        }
      }
    }
  ]
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /foods/food_id

Arguments: food id

Description: updates food information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: name (str), brand (str), category (str), ingredients (list)

### Method: PUT

> ```
> http://127.0.0.1:5000/foods/:food_id
> ```

### Body (**raw**)

```json
{
  "brand": "new brand",
  "category": "Freeze-dried",
  "name": "new food",
  "ingredients": [{ "id": 1 }]
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 1,
  "name": "new food",
  "brand": "new brand",
  "category": "Freeze-dried",
  "ingredients": [
    {
      "id": 1,
      "name": "Chicken",
      "category": "Meat"
    }
  ]
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /foods/food_id

Arguments: food id

Description: updates food information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: name (str), brand (str), category (str), ingredients (list)

### Method: PATCH

> ```
> http://127.0.0.1:5000/foods/:food_id
> ```

### Body (**raw**)

```json
{
  "brand": "new brand",
  "category": "Freeze-dried",
  "name": "new food",
  "ingredients": [{ "id": 1 }]
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 1,
  "name": "new food",
  "brand": "new brand",
  "category": "Freeze-dried",
  "ingredients": [
    {
      "id": 1,
      "name": "Chicken",
      "category": "Meat"
    }
  ]
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /foods/food_id

Arguments: food id

Description: allows admin to delete a food from database

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: None

### Method: DELETE

> ```
> http://127.0.0.1:5000/foods/:food_id
> ```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "message": "Food 1 and related notes deleted"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: ingredients

## End-point: /ingredients

Arguments: None

Description: returns a list of ingredients and related foods

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/ingredients
> ```

### Response: 200

```json
[
  {
    "id": 1,
    "name": "Chicken",
    "category": "Meat",
    "foods": [
      {
        "id": 2,
        "name": "Chicken Wet Cat Food Cans",
        "brand": "Ziwi",
        "category": "Wet"
      },
      {
        "id": 3,
        "name": "Adult Oral Care Dry Cat Food",
        "brand": "Hills Science Diet",
        "category": "Dry"
      }
    ]
  },
  {
    "id": 2,
    "name": "Lamb",
    "category": "Meat",
    "foods": []
  },
  {
    "id": 3,
    "name": "Brown Rice",
    "category": "Grains",
    "foods": [
      {
        "id": 3,
        "name": "Adult Oral Care Dry Cat Food",
        "brand": "Hills Science Diet",
        "category": "Dry"
      }
    ]
  },
  {
    "id": 4,
    "name": "Ground Wheat",
    "category": "Grains",
    "foods": [
      {
        "id": 4,
        "name": "Feline Treats Dental Catnip Flavour Tub",
        "brand": "Greenies",
        "category": "Treats"
      }
    ]
  },
  {
    "id": 5,
    "name": "Tuna",
    "category": "Seafood",
    "foods": [
      {
        "id": 1,
        "name": "Tuna With Prawn Canned Adult Cat Food",
        "brand": "Applaws",
        "category": "Wet"
      }
    ]
  },
  {
    "id": 6,
    "name": "Prawn",
    "category": "Seafood",
    "foods": [
      {
        "id": 1,
        "name": "Tuna With Prawn Canned Adult Cat Food",
        "brand": "Applaws",
        "category": "Wet"
      }
    ]
  },
  {
    "id": 7,
    "name": "Chicken Meal",
    "category": "Derivatives",
    "foods": [
      {
        "id": 4,
        "name": "Feline Treats Dental Catnip Flavour Tub",
        "brand": "Greenies",
        "category": "Treats"
      }
    ]
  }
]
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /ingredients

Arguments: None

Description: creates a new ingredient in the database

Authentication: JWT Required

Authorization: Bearer Token (logged in user)

Required fields: name (str)

Optional fields: category (str)

### Method: POST

> ```
> http://127.0.0.1:5000/ingredients
> ```

### Body (**raw**)

```json
{
  "name": "Beef",
  "category": "Meat"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 201

```json
{
  "id": 8,
  "name": "Beef",
  "category": "Meat"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /ingredients/ingredient_id

Arguments: ingredient id

Description: returns ingredient of the selected id

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/ingredients/:ingredient_id
> ```

### Response: 200

```json
{
  "id": 1,
  "name": "Chicken",
  "category": "Meat",
  "foods": [
    {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet"
    },
    {
      "id": 3,
      "name": "Adult Oral Care Dry Cat Food",
      "brand": "Hills Science Diet",
      "category": "Dry"
    }
  ]
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /ingredients/ingredient_id

Arguments: ingredient id

Description: updates ingredient information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: name (str), category (str)

### Method: PUT

> ```
> http://127.0.0.1:5000/ingredients/:ingredient_id
> ```

### Body (**raw**)

```json
{
  "name": "new name",
  "category": "Other"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 1,
  "name": "new name",
  "category": "Other"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /ingredients/ingredient_id

Arguments: ingredient id

Description: updates ingredient information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: name (str), category (str)

### Method: PATCH

> ```
> http://127.0.0.1:5000/ingredients/:ingredient_id
> ```

### Body (**raw**)

```json
{
  "name": "new name",
  "category": "Other"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 1,
  "name": "new name",
  "category": "Other"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /ingredients/ingredient_id

Arguments: ingredient id

Description: allows admin to delete an ingredient from database

Authentication: JWT Required

Authorization: Bearer Token (admin)

Required fields: None

Optional fields: None

### Method: DELETE

> ```
> http://127.0.0.1:5000/ingredients/:ingredient_id
> ```

### Body (**raw**)

```json

```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "message": "Ingredient 1 deleted"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: cats

## End-point: /cats

Arguments: None

Description: returns a list of cats and their owner's name

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/cats
> ```

### Response: 200

```json
[
  {
    "id": 1,
    "name": "Luna",
    "breed": "Domestic Shorthair",
    "year_born": 2020,
    "year_adopted": 2021,
    "owner": {
      "username": "John"
    }
  },
  {
    "id": 2,
    "name": "Leo",
    "breed": "Exotic Shorthair",
    "year_born": null,
    "year_adopted": 2022,
    "owner": {
      "username": "Frank"
    }
  },
  {
    "id": 3,
    "name": "Milo",
    "breed": "Ragdoll",
    "year_born": 2015,
    "year_adopted": 2019,
    "owner": {
      "username": "Frank"
    }
  },
  {
    "id": 4,
    "name": "Oreo",
    "breed": "Domestic Longhair",
    "year_born": null,
    "year_adopted": 2019,
    "owner": {
      "username": "Frank"
    }
  }
]
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /cats

Arguments: None

Description: creates a new cat in the database

Authentication: JWT Required

Authorization: Bearer Token (logged in user)

Required fields: name (str)

Optional fields: breed (str), year_born (int), year_adopted (int)

### Method: POST

> ```
> http://127.0.0.1:5000/cats
> ```

### Body (**raw**)

```json
{
  "name": "new cat",
  "year_born": "2019",
  "year_adopted": "2020",
  "breed": "British Shorthair"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 201

```json
{
  "id": 5,
  "name": "new cat",
  "breed": "British Shorthair",
  "year_born": 2019,
  "year_adopted": 2020,
  "owner": {
    "username": "Frank"
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /cats/cat_id

Arguments: cat id

Description: returns cat of the selected id and their owner name and notes

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/cats/:cat_id
> ```

### Response: 200

```json
{
  "id": 1,
  "name": "Luna",
  "breed": "Domestic Shorthair",
  "year_born": 2020,
  "year_adopted": 2021,
  "owner": {
    "username": "John"
  },
  "notes": [
    {
      "id": 1,
      "message": "Luna was ok with it, maybe will try a different one",
      "rating": 0,
      "date_recorded": "2023-06-24",
      "food": {
        "id": 1,
        "name": "Tuna With Prawn Canned Adult Cat Food",
        "brand": "Applaws",
        "category": "Wet",
        "ingredients": [
          {
            "id": 5,
            "name": "Tuna",
            "category": "Seafood"
          },
          {
            "id": 6,
            "name": "Prawn",
            "category": "Seafood"
          }
        ]
      }
    },
    {
      "id": 2,
      "message": "Luna likes the treats",
      "rating": 1,
      "date_recorded": "2023-06-24",
      "food": {
        "id": 4,
        "name": "Feline Treats Dental Catnip Flavour Tub",
        "brand": "Greenies",
        "category": "Treats",
        "ingredients": [
          {
            "id": 4,
            "name": "Ground Wheat",
            "category": "Grains"
          },
          {
            "id": 7,
            "name": "Chicken Meal",
            "category": "Derivatives"
          }
        ]
      }
    },
    {
      "id": 3,
      "message": "Tried a different can and Luna only ate half of it",
      "rating": 0,
      "date_recorded": "2023-06-25",
      "food": {
        "id": 2,
        "name": "Chicken Wet Cat Food Cans",
        "brand": "Ziwi",
        "category": "Wet",
        "ingredients": [
          {
            "id": 1,
            "name": "Chicken",
            "category": "Meat"
          }
        ]
      }
    },
    {
      "id": 4,
      "message": "Luna ate the whole can, she likes it!",
      "rating": 1,
      "date_recorded": "2023-06-26",
      "food": {
        "id": 2,
        "name": "Chicken Wet Cat Food Cans",
        "brand": "Ziwi",
        "category": "Wet",
        "ingredients": [
          {
            "id": 1,
            "name": "Chicken",
            "category": "Meat"
          }
        ]
      }
    },
    {
      "id": 5,
      "message": "Luna is still happy with it!",
      "rating": 1,
      "date_recorded": "2023-06-26",
      "food": {
        "id": 2,
        "name": "Chicken Wet Cat Food Cans",
        "brand": "Ziwi",
        "category": "Wet",
        "ingredients": [
          {
            "id": 1,
            "name": "Chicken",
            "category": "Meat"
          }
        ]
      }
    }
  ]
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /cats/cat_id

Arguments: cat id

Description: update cat information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: name (str), breed (str), year_born (int), year_adopted (int)

### Method: PUT

> ```
> http://127.0.0.1:5000/cats/:cat_id
> ```

### Body (**raw**)

```json
{
  "name": "new name",
  "year_born": "2020",
  "year_adopted": "2021",
  "breed": "new breed"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 4,
  "name": "new name",
  "breed": "new breed",
  "year_born": 2020,
  "year_adopted": 2021,
  "owner": {
    "username": "Frank"
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /cats/cat_id

Arguments: cat id

Description: update cat information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: name (str), breed (str), year_born (int), year_adopted (int)

### Method: PATCH

> ```
> http://127.0.0.1:5000/cats/:cat_id
> ```

### Body (**raw**)

```json
{
  "name": "new name",
  "year_born": "2020",
  "year_adopted": "2021",
  "breed": "new breed"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 1,
  "name": "new name",
  "breed": "new breed",
  "year_born": 2020,
  "year_adopted": 2021,
  "owner": {
    "username": "John"
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /cats/cat_id

Arguments: cat id

Description: allows admin or owner to delete a cat from database

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: None

### Method: DELETE

> ```
> http://127.0.0.1:5000/cats/:cat_id
> ```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "message": "Cat 2 and related notes deleted"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: cats/cat_id/food

Arguments: cat id

Description: returns a list of foods eaten by the cat, with statistics on total notes and rating

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/cats/:cat_id/food
> ```

### 🔑 Authentication noauth

| Param | value | Type |
| ----- | ----- | ---- |

### Response: 200

```json
[
  {
    "food": {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet",
      "ingredients": [
        {
          "id": 1,
          "name": "Chicken",
          "category": "Meat"
        }
      ]
    },
    "total_notes": 3,
    "total_rating": 2
  },
  {
    "food": {
      "id": 4,
      "name": "Feline Treats Dental Catnip Flavour Tub",
      "brand": "Greenies",
      "category": "Treats",
      "ingredients": [
        {
          "id": 4,
          "name": "Ground Wheat",
          "category": "Grains"
        },
        {
          "id": 7,
          "name": "Chicken Meal",
          "category": "Derivatives"
        }
      ]
    },
    "total_notes": 1,
    "total_rating": 1
  },
  {
    "food": {
      "id": 1,
      "name": "Tuna With Prawn Canned Adult Cat Food",
      "brand": "Applaws",
      "category": "Wet",
      "ingredients": [
        {
          "id": 5,
          "name": "Tuna",
          "category": "Seafood"
        },
        {
          "id": 6,
          "name": "Prawn",
          "category": "Seafood"
        }
      ]
    },
    "total_notes": 1,
    "total_rating": 0
  }
]
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# 📁 Collection: notes

## End-point: /notes

Arguments: None

Description: returns a list of notes, each with its related cat and food information

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/notes
> ```

### Response: 200

```json
[
  {
    "id": 1,
    "message": "Luna was ok with it, maybe will try a different one",
    "rating": 0,
    "date_recorded": "2023-06-24",
    "cat": {
      "id": 1,
      "name": "Luna",
      "breed": "Domestic Shorthair",
      "owner": {
        "username": "John"
      }
    },
    "food": {
      "id": 1,
      "name": "Tuna With Prawn Canned Adult Cat Food",
      "brand": "Applaws",
      "category": "Wet",
      "ingredients": [
        {
          "id": 5,
          "name": "Tuna",
          "category": "Seafood"
        },
        {
          "id": 6,
          "name": "Prawn",
          "category": "Seafood"
        }
      ]
    }
  },
  {
    "id": 2,
    "message": "Luna likes the treats",
    "rating": 1,
    "date_recorded": "2023-06-24",
    "cat": {
      "id": 1,
      "name": "Luna",
      "breed": "Domestic Shorthair",
      "owner": {
        "username": "John"
      }
    },
    "food": {
      "id": 4,
      "name": "Feline Treats Dental Catnip Flavour Tub",
      "brand": "Greenies",
      "category": "Treats",
      "ingredients": [
        {
          "id": 4,
          "name": "Ground Wheat",
          "category": "Grains"
        },
        {
          "id": 7,
          "name": "Chicken Meal",
          "category": "Derivatives"
        }
      ]
    }
  },
  {
    "id": 3,
    "message": "Tried a different can and Luna only ate half of it",
    "rating": 0,
    "date_recorded": "2023-06-25",
    "cat": {
      "id": 1,
      "name": "Luna",
      "breed": "Domestic Shorthair",
      "owner": {
        "username": "John"
      }
    },
    "food": {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet",
      "ingredients": [
        {
          "id": 1,
          "name": "Chicken",
          "category": "Meat"
        }
      ]
    }
  },
  {
    "id": 4,
    "message": "Luna ate the whole can, she likes it!",
    "rating": 1,
    "date_recorded": "2023-06-26",
    "cat": {
      "id": 1,
      "name": "Luna",
      "breed": "Domestic Shorthair",
      "owner": {
        "username": "John"
      }
    },
    "food": {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet",
      "ingredients": [
        {
          "id": 1,
          "name": "Chicken",
          "category": "Meat"
        }
      ]
    }
  },
  {
    "id": 5,
    "message": "Luna is still happy with it!",
    "rating": 1,
    "date_recorded": "2023-06-26",
    "cat": {
      "id": 1,
      "name": "Luna",
      "breed": "Domestic Shorthair",
      "owner": {
        "username": "John"
      }
    },
    "food": {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet",
      "ingredients": [
        {
          "id": 1,
          "name": "Chicken",
          "category": "Meat"
        }
      ]
    }
  },
  {
    "id": 6,
    "message": "Leo hates it",
    "rating": -1,
    "date_recorded": "2023-06-20",
    "cat": {
      "id": 2,
      "name": "Leo",
      "breed": "Exotic Shorthair",
      "owner": {
        "username": "Frank"
      }
    },
    "food": {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet",
      "ingredients": [
        {
          "id": 1,
          "name": "Chicken",
          "category": "Meat"
        }
      ]
    }
  },
  {
    "id": 7,
    "message": "Milo was the only cat eating the can, but not finished it either",
    "rating": 0,
    "date_recorded": "2023-06-20",
    "cat": {
      "id": 3,
      "name": "Milo",
      "breed": "Ragdoll",
      "owner": {
        "username": "Frank"
      }
    },
    "food": {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet",
      "ingredients": [
        {
          "id": 1,
          "name": "Chicken",
          "category": "Meat"
        }
      ]
    }
  },
  {
    "id": 8,
    "message": "Oreo sniffed and went away",
    "rating": -1,
    "date_recorded": "2023-06-20",
    "cat": {
      "id": 4,
      "name": "Oreo",
      "breed": "Domestic Longhair",
      "owner": {
        "username": "Frank"
      }
    },
    "food": {
      "id": 2,
      "name": "Chicken Wet Cat Food Cans",
      "brand": "Ziwi",
      "category": "Wet",
      "ingredients": [
        {
          "id": 1,
          "name": "Chicken",
          "category": "Meat"
        }
      ]
    }
  },
  {
    "id": 9,
    "message": "Leo likes it",
    "rating": 1,
    "date_recorded": "2023-06-21",
    "cat": {
      "id": 2,
      "name": "Leo",
      "breed": "Exotic Shorthair",
      "owner": {
        "username": "Frank"
      }
    },
    "food": {
      "id": 4,
      "name": "Feline Treats Dental Catnip Flavour Tub",
      "brand": "Greenies",
      "category": "Treats",
      "ingredients": [
        {
          "id": 4,
          "name": "Ground Wheat",
          "category": "Grains"
        },
        {
          "id": 7,
          "name": "Chicken Meal",
          "category": "Derivatives"
        }
      ]
    }
  }
]
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /notes

Arguments: None

Description: create a new note in the database

Authentication: JWT Required

Authorization: Bearer Token (logged in user)

Required fields: cat_id (int), food_id (int)

Optional fields: message (str), rating (int), date_recorded (date)

### Method: POST

> ```
> http://127.0.0.1:5000/notes
> ```

### Body (**raw**)

```json
{
  "cat_id": 1,
  "food_id": 2,
  "message": "cat 1 likes food 2",
  "rating": 0,
  "date_recorded": "2023-06-30"
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 201

```json
{
  "id": 10,
  "message": "cat 2 likes food 1",
  "rating": 1,
  "date_recorded": "2023-06-30",
  "cat": {
    "id": 2,
    "name": "Leo",
    "breed": "Exotic Shorthair",
    "owner": {
      "username": "Frank"
    }
  },
  "food": {
    "id": 1,
    "name": "Tuna With Prawn Canned Adult Cat Food",
    "brand": "Applaws",
    "category": "Wet",
    "ingredients": [
      {
        "id": 5,
        "name": "Tuna",
        "category": "Seafood"
      },
      {
        "id": 6,
        "name": "Prawn",
        "category": "Seafood"
      }
    ]
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /notes/note_id

Arguments: note id

Description: returns note of the selected id and the related cat and food information

Authentication: None

Authorization: None

Required fields: None

Optional fields: None

### Method: GET

> ```
> http://127.0.0.1:5000/notes/:note_id
> ```

### Response: 200

```json
{
  "id": 1,
  "message": "Luna was ok with it, maybe will try a different one",
  "rating": 0,
  "date_recorded": "2023-06-24",
  "cat": {
    "id": 1,
    "name": "Luna",
    "breed": "Domestic Shorthair",
    "owner": {
      "username": "John"
    }
  },
  "food": {
    "id": 1,
    "name": "Tuna With Prawn Canned Adult Cat Food",
    "brand": "Applaws",
    "category": "Wet",
    "ingredients": [
      {
        "id": 5,
        "name": "Tuna",
        "category": "Seafood"
      },
      {
        "id": 6,
        "name": "Prawn",
        "category": "Seafood"
      }
    ]
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /notes/note_id

Arguments: note id

Description: updates note information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: cat_id (int), food_id (int), message (str), rating (int), date_recorded (date)

### Method: PUT

> ```
> http://127.0.0.1:5000/notes/:note_id
> ```

### Body (**raw**)

```json
{
  "date_recorded": "2023-05-02",
  "cat_id": 3,
  "food_id": 2,
  "message": "new message",
  "rating": 1
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 6,
  "message": "new message",
  "rating": 1,
  "date_recorded": "2023-05-02",
  "cat": {
    "id": 3,
    "name": "Milo",
    "breed": "Ragdoll",
    "owner": {
      "username": "Frank"
    }
  },
  "food": {
    "id": 2,
    "name": "Chicken Wet Cat Food Cans",
    "brand": "Ziwi",
    "category": "Wet",
    "ingredients": [
      {
        "id": 1,
        "name": "Chicken",
        "category": "Meat"
      }
    ]
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /notes/note_id

Arguments: note id

Description: updates note information of the selected id

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: cat_id (int), food_id (int), message (str), rating (int), date_recorded (date)

### Method: PATCH

> ```
> http://127.0.0.1:5000/notes/:note_id
> ```

### Body (**raw**)

```json
{
  "date_recorded": "2023-05-02",
  "cat_id": 3,
  "food_id": 2,
  "message": "new message",
  "rating": 1
}
```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "id": 6,
  "message": "new message",
  "rating": 1,
  "date_recorded": "2023-05-02",
  "cat": {
    "id": 3,
    "name": "Milo",
    "breed": "Ragdoll",
    "owner": {
      "username": "Frank"
    }
  },
  "food": {
    "id": 2,
    "name": "Chicken Wet Cat Food Cans",
    "brand": "Ziwi",
    "category": "Wet",
    "ingredients": [
      {
        "id": 1,
        "name": "Chicken",
        "category": "Meat"
      }
    ]
  }
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: /notes/note_id

Arguments: note id

Description: allows admin or owner to delete a note from database

Authentication: JWT Required

Authorization: Bearer Token (admin or owner)

Required fields: None

Optional fields: None

### Method: DELETE

> ```
> http://127.0.0.1:5000/notes/:note_id
> ```

### 🔑 Authentication bearer

| Param | value | Type   |
| ----- | ----- | ------ |
| token |       | string |

### Response: 200

```json
{
  "message": "Note 1 deleted"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

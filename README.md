# Social Media API

## Description:
You are tasked with building a RESTful API for a social media platform. The API should allow users to create profiles, follow other users, create and retrieve posts, manage likes and comments, and perform basic social media actions.

---

## Requirements:

### User Registration and Authentication:
- Users should be able to register with their email and password to create an account.
- Users should be able to login with their credentials and receive a token for authentication.
- Users should be able to logout and invalidate their token.

### User Profile:
- Users should be able to create and update their profile, including profile picture, bio, and other details.
- Users should be able to retrieve their own profile and view profiles of other users.
- Users should be able to search for users by username or other criteria.

### Follow/Unfollow:
- Users should be able to follow and unfollow other users.
- Users should be able to view the list of users they are following and the list of users following them.

### Post Creation and Retrieval:
- Users should be able to create new posts with text content and optional media attachments (e.g., images). (Adding images is optional task)
- Users should be able to retrieve their own posts and posts of users they are following.
- Users should be able to retrieve posts by hashtags or other criteria.

### Likes and Comments (Optional):
- Users should be able to like and unlike posts.
- Users should be able to view the list of posts they have liked.
- Users should be able to add comments to posts and view comments on posts.

### Schedule Post creation using Celery (Optional):
- Add possibility to schedule Post creation (you can select the time to create the Post before creating of it).

---

## API Permissions:
- Only authenticated users should be able to perform actions such as creating posts, liking posts, and following/unfollowing users.
- Users should only be able to update and delete their own posts and comments.
- Users should only be able to update and delete their own profile.

---

## API Documentation:
- The API should be well-documented with clear instructions on how to use each endpoint.
- The documentation should include sample API requests and responses for different endpoints.
---

## User Profiles

### 1. Take all profiles
**Endpoint:**
```http
GET {{host}}/api/user/profiles/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`

---

### 2. Take my profile
**Endpoint:**
```http
GET {{host}}/api/user/profiles/?me
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`

---

### 3. Update my profile
**Endpoint:**
```http
PUT {{host}}/api/user/profiles/1/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`
- `Content-Type: application/json`

**Sample Body:**
```json
{
  "email": "lev2@g.com",
  "bio": "I am a software developer with a passion for coding!",
  "profile_picture": null
}
```

---

## Posts

### 1. Create a new post
**Endpoint:**
```http
POST {{host}}/api/action/posts/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`
- `Content-Type: application/json`

**Sample Body:**
```json
{
  "content": "This is new post",
  "media": null
}
```

---

### 2. Update a post
**Endpoint:**
```http
PUT {{host}}/api/action/posts/1/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`
- `Content-Type: application/json`

**Sample Body:**
```json
{
  "content": "Updated post content"
}
```

---

### 3. Delete a post
**Endpoint:**
```http
DELETE {{host}}/api/action/posts/1/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`

---

## Likes

### 1. Add a like to a post
**Endpoint:**
```http
POST {{host}}/api/action/likes/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`
- `Content-Type: application/json`

**Sample Body:**
```json
{
  "post": 1
}
```

---

### 2. Delete a like
**Endpoint:**
```http
DELETE {{host}}/api/action/likes/1/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`

---

## Comments

### 1. Add a comment to a post
**Endpoint:**
```http
POST {{host}}/api/action/comments/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`
- `Content-Type: application/json`

**Sample Body:**
```json
{
  "post": 1,
  "content": "This is new comment"
}
```

---

### 2. Delete a comment
**Endpoint:**
```http
DELETE {{host}}/api/action/comments/4/
```

**Headers:**
- `Accept: application/json`
- `Authorization: Bearer {{access_token}}`

---

## Notes:
- Replace `{{access_token}}` with a valid Bearer token.
- Replace `{{host}}` with the base URL of your API server.
- Ensure that all IDs (e.g., `1`, `4`) in the examples are replaced with actual IDs from your database.
- All timestamps should follow the ISO 8601 format (e.g., `2024-12-28T11:15:19.200Z`).

---

## Technical Requirements:
- Use Django and Django REST framework to build the API.
- Use token-based authentication for user authentication.
- Use appropriate serializers for data validation and representation.
- Use appropriate views and viewsets for handling CRUD operations on models.
- Use appropriate URL routing for different API endpoints.
- Use appropriate permissions and authentication classes to implement API permissions.
- Follow best practices for RESTful API design and documentation.

---

### Note:
You are not required to implement a frontend interface for this task. Focus on building a well-structured and well-documented RESTful API using Django and Django REST framework. This task will test the junior DRF developer's skills in building RESTful APIs, handling authentication and permissions, working with models, serializers, views, and viewsets, and following best practices for API design and documentation.
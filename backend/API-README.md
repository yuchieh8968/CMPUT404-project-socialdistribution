
| Allowed methods        | URI                                                                        | Paginated?              | Description                                                                                                                                                                                                                                                        |
| ---------------------- | -------------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| GET                    | ://service/authors/                                                        | ✅                      | GET (local, remote): Used to view all authors                                                                                                                                                                                                                      |
| GET                    | ://service/authors?page=10&size=5                                          | (example of pagination) | GET (local, remote): retrieve all profiles on the server (paginated)                                                                                                                                                                                               |
| GET, POST              | ://service/authors/{AUTHOR_ID}/                                            |                         | GET (local, remote): retrieve AUTHOR_ID profile.<br><br>POST (local): update AUTHOR_ID profile                                                                                                                                                                     |
| GET                    | ://service/authors/{AUTHOR_ID}/followers                                   |                         |                                                                                                                                                                                                                                                                    |
| GET, PUT, DELETE       | ://service/authors/{AUTHOR_ID}/followers/{FOREIGN_AUTHOR_ID}               |                         |                                                                                                                                                                                                                                                                    |
| GET, POST, DELETE, PUT | ://service/authors/{AUTHOR_ID}/posts/{POST_ID}                             |                         | GET (local, remote) get the public post whose id is POST_ID.<br><br>POST (local) update the post whose id is POST_ID (must be authenticated).<br><br>DELETE (local) remove the post whose id is POST_ID.<br><br>PUT (local) create a post where its id is POST_ID. |
| GET, POST              | ://service/authors/{AUTHOR_ID}/posts/                                      | ✅                      | GET (local, remote) Used to view all posts from a particular author.<br><br>POST (local) create a new post but generate a new id                                                                                                                                   |
| GET                    | ://service/authors/{AUTHOR_ID}/posts?page=10&size=5                        | (example of pagination) | GET (local, remote) get the recent posts from author AUTHOR_ID (paginated)                                                                                                                                                                                         |
| GET                    | ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/image                       |                         |                                                                                                                                                                                                                                                                    |
| GET, POST              | ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments                    | ✅                      |                                                                                                                                                                                                                                                                    |
| POST                   | ://service/authors/{AUTHOR_ID}/inbox/                                      | ✅                      |                                                                                                                                                                                                                                                                    |
| GET                    | ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/likes                       |                         |                                                                                                                                                                                                                                                                    |
| GET                    | ://service/authors/{AUTHOR_ID}/posts/{POST_ID}/comments/{COMMENT_ID}/likes |                         |                                                                                                                                                                                                                                                                    |
| GET                    | ://service/authors/{AUTHOR_ID}/liked                                       |                         |                                                                                                                                                                                                                                                                    |
| GET, POST, DELETE      | ://service/authors/{AUTHOR_ID}/inbox                                       |                         |                                                                                                                                                                                                                                                                    |
|                        |                                                                            |                         |                                                                                                                                                                                                                                                                    |

| Other URI's         | Description         |
| ------------------- | ------------------- |
| ://admin/           | Django admin page   |
| ://api-auth/login/  | API login           |
| ://api-auth/logout/ | API logout          |
| ://api-schema/      | API schema endpoint |
| ://docs/api/        | API docs            |
|                     |                     |
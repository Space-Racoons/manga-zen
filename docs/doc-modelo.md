# Modelo de Dados

### Modelo Entidade-Relacionamento (MER) - Mermaid

```mermaid
erDiagram
    USER ||..o{ COMMENT : maker
    USER ||--o{ MANGA : has
    MANGA ||--|{ CHAPTER : has
    MANGA ||--o{ COMMENT : has
    CHAPTER ||--o{ COMMENT : has

    USER {
        INT id
        VARCHAR  username
        VARCHAR  email
        VARCHAR  password
        VARCHAR  image
    }

    COMMENT{
        INT id
        VARCHAR comment
        DATE date_created
        INT id_user
        INT id_chapter
        INT id_manga
    }

     MANGA{
        INT id
        VARCHAR  author
        VARCHAR  genre
        VARCHAR  status
        INT      views
        VARCHAR  description
        VARCHAR  url
        INT id_user
    }

    CHAPTER{
        INT id
        VARCHAR  name
        VARCHAR  image
        INT id_manga
    }
```
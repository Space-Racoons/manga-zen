# Modelo de Dados

### Modelo Entidade-Relacionamento (MER)

```mermaid
erDiagram
    USER ||..o{ COMMENT : makes
    USER ||--o{ MANGA : has
    MANGA ||--o{ CHAPTER : has
    MANGA ||--o{ COMMENT : has
    CHAPTER ||--o{ COMMENT : has
    GENRE |{--o{  MANGA: has
    STATUS ||--o{ MANGA: has

    USER {
        INT id
        VARCHAR  username
        VARCHAR  email
        VARCHAR  hashed_password
        VARCHAR  image_url
        DATE created_at
    }

    COMMENT{
        INT id
        VARCHAR content
        INT id_user
        INT id_chapter
        INT id_manga
        DATE created_at
    }

    MANGA{
        INT id
        VARCHAR title
        VARCHAR author
        INT views
        VARCHAR description
        VARCHAR url
        INT id_user
        INT id_status
        INT id_status
        DATE created_at
    }

    CHAPTER{
        INT id
        INT  ch_number
        VARCHAR image_url
        INT id_manga
        DATE created_at
    }

    GENRE{
        INT id
        VARCHAR name
        INT manga_id
        DATE date_created
    }

    STATUS{
        INT id
        VARCHAR name
        DATE date_created
    }
```

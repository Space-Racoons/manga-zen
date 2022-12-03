# Modelo de Dados

### Modelo Entidade-Relacionamento (MER) - Mermaid

```mermaid
erDiagram
    USER ||..o{ COMMENT : maker
    USER ||--o{ MANGA : has
    MANGA ||--|{ CHAPTER : has
    MANGA ||--o{ COMMENT : has
    CHAPTER ||--o{ COMMENT : has
    GENRE |{--o{  MANGA: has

    USER {
        INT id
        VARCHAR  username
        VARCHAR  email
        VARCHAR  password
        VARCHAR  image
        DATE date_created
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
        VARCHAR  status
        INT      views
        VARCHAR  description
        DATE date_created
        VARCHAR  url
        INT id_user
        INT id_genre
    }

    CHAPTER{
        INT id
        INT  number_chapter
        VARCHAR  image
        DATE date_created
        INT id_manga
    }

    GENRE{
        INT id
        VARCHAR name_genre
        DATE date_created
    }

```
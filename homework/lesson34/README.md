# Lesson 34 - GraphQL w projekcie Music Fun Beats

Zadanie zostało wykonane w ramach projektu końcowego Music Fun Beats
napisanego w Django i Django REST Framework.

Pełne repozytorium projektu:

https://github.com/Bartosz691/music-fun-beats

## GraphQL

Do projektu została dodana obsługa GraphQL z wykorzystaniem biblioteki
Strawberry GraphQL.

Endpoint GraphQL:

/graphql/

Projekt posiada również interfejs GraphiQL umożliwiający ręczne
wykonywanie zapytań.

## Dostępne zapytania

### Lista albumów

```graphql
query {
  albums {
    id
    title
    artistName
    genres
    labelName
    formatName
    releaseYear
    price
    stock
    isLimitedEdition
  }
}
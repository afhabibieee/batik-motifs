# batik-motifs

## Project Domain
A web application that can classify 15 kinds of batik motifs.

## Problem Definition
Batik is one of the wealth of Indonesian two-dimensional works of art with various distinctive patterns from various regions. In 2015 a study conducted by the Bandung Fe Institute and Sobat Budaya noted that at least 5,849 Indonesian batik motifs spread from Aceh to Papua. I created this program to classify the types of batik based on the motif. Besides the many names of batik, we do not need to remember them or rely on historians to know the name of the batik.

## How to Run This App via Docker
This image is available on Docker hub.
```
 https://hub.docker.com/repository/docker/afhabibieee/batikmotifs
```
- Pull image: `docker push afhabibieee/batikmotifs:1.0`
- Run docker container: `docker run -p 8501:8501 afhabibieee/batikmotifs:1.0`
- Go to : `localhost:8501`

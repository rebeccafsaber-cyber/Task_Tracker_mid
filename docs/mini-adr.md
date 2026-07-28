
# Architecture Decision Record: FastAPI for Task Tracker

## Status
Accepted

## Context
We needed to build a lightweight, high-performance, and easy-to-document backend for the Task Tracker application as part of the mid-term project requirements. 

## Decision
We chose **FastAPI** as the primary framework because:
1. It provides automatic interactive API documentation (Swagger UI / ReDoc).
2. It offers high performance on par with NodeJS and Go due to Starlette and Pydantic.
3. It has native support for asynchronous programming and clean data validation.

## Consequences
* **Positive:** Faster development time, strict data validation using Pydantic models, and auto-generated documentation.
* **Negative:** Slightly steeper learning curve for asynchronous dependency injection compared to micro-frameworks like Flask, though easily manageable.

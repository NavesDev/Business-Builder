# API Blueprint Generator Prompt

## Role
You are a Senior API Designer specialising in RESTful and GraphQL contract design.

## Task
Given the business idea and its business architecture, produce a high-level API blueprint that includes:

1. **Base URL & Versioning** — Suggest the base URL pattern and versioning strategy.
2. **Authentication** — Specify the auth mechanism (OAuth 2.0, API Keys, JWT, etc.).
3. **Endpoints** — For each domain, list the key endpoints with method, path, request body (summary), and response body (summary).
4. **Error Handling** — Define the standard error response format and common error codes.
5. **Rate Limiting & Pagination** — Describe the strategy for rate limiting and paginating list responses.

## Output Format
Return a structured Markdown document with a section for each of the five areas above. Use tables for endpoint listings.

## Business Idea
{{idea}}

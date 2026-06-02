# Logistics FAQ Support Assistant

## Task Overview

A logistics company built a Flask-based internal FAQ tool to help support agents quickly answer common shipping and delivery questions. The tool loads a small set of FAQ documents into a LlamaIndex knowledge base and exposes a single `POST /ask` endpoint. The index loading and query engine setup work correctly, but the API endpoint has bugs that cause crashes on valid requests and returns unhelpful responses without source citations. Fixing this is important because support agents need reliable, source-backed answers they can reference when handling customer tickets.

## Helpful Tips

- Consider how Flask's `request.json` behaves when a field is missing or when the whole body is not what you expect.
- Review how a LlamaIndex query response object is structured and what attributes it exposes beyond just the answer text.
- Think about what information from `source_nodes` would be most useful to return to an API caller.
- Explore how `try/except` can be used to return a clean JSON error instead of a raw server traceback.

## Objectives

- The `POST /ask` endpoint accepts a JSON body with a `question` field and returns HTTP 200 with a structured JSON response.
- Responses include both an `answer` string and a `sources` list containing at least the filename of each retrieved document chunk.
- Missing or blank `question` values return HTTP 400 with a clear JSON error message instead of a server crash.
- Unexpected runtime errors are caught and return a safe error response rather than a raw traceback.
- The existing index loading and query engine setup remain unchanged.

## How to Verify

- Send a valid POST request with a `question` field and confirm the response contains both `answer` and `sources` keys.
- Confirm that `sources` includes at least one filename or file path from the documents in the `data/` folder.
- Send a request with a missing `question` field and confirm the server returns HTTP 400 with a JSON error body, not a 500 traceback.
- Send a request with a blank string as the `question` value and confirm it also returns HTTP 400.
- Restart the server a second time and confirm the index is reloaded from disk without rebuilding.

Introduction
=========================

**Date:** 25 Oct 2025
**Version:** 0.1.2

``scimodels`` is a lightweight Python module for limited but easy communication with Language Models. It supports both APIs (such as openai) and running models locally (via vllm).

This project mostly oriented towards research. 

SciModels **does** support:

1. Sending multiple queries at once
2. Sending each query multiple times and organizing the results
3. Batch APIs and Async APIs

SciModels **does not** support:

1. Streaming
2. Chat-like conversations, multiple consecutive queries
3. Tool usage APIs (such as in OpenAI API)

Here is an example usage of ``scimodels``::

    import scimodels

    model = scimodels.load("openai", "gpt-5-mini")
    response = model.send("Hello there!")

    print(response.outputs[0])

In this case the ``model`` is a connection to OpenAI's ``gpt-5-mini`` model. The ``response`` is an instance of ``scimodels.Response`` that is used for all models, including Batch API ones.

The call ``openai`` the *Provider* and ``gpt-5-mini`` the *Model*. The provider string also specifies the way ``scimodels`` handles query sending.

Sync Models block the program until all responses are received.

Batch Models send all queries at once and return a Batch ID that can later be used to retrieve the results when they are ready.

Async Models work like Sync Models but using an ``async send`` method. 
.. post:: 2024-08-13
    :tags: Software Architecture, Full-Stack, Javascript, Python, FARM Stack, React, Redux, MongoDB, FastAPI, MongoDB,  OpenAPI, Kiota
    :language: English

.. _sec_neighbors_allotment_garden:

«PoC» Neighbors Allotment Garden
################################

A miniature FARM stack application **WIP - Work-In-Progress**

.. todo:: Resume  ...

.. contents:: Table of Contents
    :local:
    :depth: 2


Purpose
*******

My recent post :ref:`sec_modular_react_redux` has used two of the three ingredients of the FARM stack :cite:p:`2022basset`. This post will add the third one, MongoDB, to create a full-stack application.

..
    The "FARM-Stack" is the acronym

    - :cite:p:`2022basset`
    - :cite:p:`Aleksendric2022`
    - :cite:p:`2022mongodb`
    - :cite:p:`microsoft_kiota_2024`
    - https://www.youtube.com/watch?v=LldmlWM1amg

    - https://learn.microsoft.com/en-us/openapi/kiota/quickstarts/typescript
    - :ref:`sec_modular_react_redux`


Approach
********

- TODO: Set up a viable example by describing it from user's perspective (so create the "stakeholder requirements" in form of user stories). So here UI and UX are dominating the description. In a well designed application the uses don't notice the backend, the underlying architecture. They only see "the application" and interact with it.
- TODO: Derive the purpose of the application from the user stories. Don't forget to baptize the application with a working title.
- TODO: Identify design constraints based on pre-defined system definition (such as: "The application shall be a web application and be hosted on a virtual server at provider X. X = Digital Ocean").
- TODO: Describe the architecture of the application. This includes the data model, the API, the frontend and the backend.
- TODO: Create the data model with FastAPI (pydantic).
- TODO: Create the API with FastAPI.
- TODO: Autogenerate the API client with Kiota (OpenAPI) from the API definition previously created. That API client is the component inside the Frontend which connects to the Backend. It is the "bridge" between the two. It abstracts the API calls and the data model from the Frontend.
- TODO: Create the remaining parts (UI, UX) of frontend with React and Redux to meet the user stories and fit to the data model.





User Stories
************

Purpose of the Application
**************************

Design Constraints
******************

Architectural Design
********************

Data Model
==========

API
===

Frontend
========

Backend
=======


Autogenerate the API client
***************************

Kiota

- https://www.youtube.com/watch?v=nk9BUPKgN_k
- https://learn.microsoft.com/en-us/openapi/kiota/quickstarts/typescript

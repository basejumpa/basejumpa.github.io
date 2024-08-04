.. post:: 2024-08-01
    :tags: React, Redux, Software Architecture, Extensibility, Modularity
    :language: English


React with Redux the Extensible Way
===================================

With this article I try to provide a comprehensive guide to setting up a client-side rendering (CSR) React application using Redux, with a focus on modularity and extensibility.

I will walk you through the steps needed to configure Redux and manage state effectively in a React application, and discuss the design decisions made to ensure the application is easy to extend and maintain.

The Example Application
-----------------------

This article designs an application to satisfy the following software requirements / design constraints:

The user shall be able to interact with the application by entering values and getting calculated values derived from their inputs.

ComponentA shall have a button. When the user presses this button a value is incremented. The button label shows that value. Initial value is 19.

ComponentB shall have a button as well. When pressed it retrieves a value from an API call and adds it to its own value which is displayed in the button label. Initial state of the own variable is 76.

ComponentC displays the sum of the values of ComponentA und ComponentB.

ComponentD has a button to reset the variables to their initial ones. ComponentD has no knowledge of the initial values.


Project Structure
-----------------

Below is the directory structure of our project:

.. code-block:: text
    :linenos:

    /src
      /components
        /A
          component.js
          slice.js
        /B
          component.js
          slice.js
        /C
          component.js
          slice.js
        /D
          component.js
          slice.js
        /E
          slice.js
      /store
        reducerManager.js
        store.js
      /App.js
      /index.js

Setting Up the Project
----------------------

Initialize a React Project
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Install Create React App:

.. code-block:: bash

    npx create-react-app your-app-name
    cd your-app-name

2. Install Redux and related packages:

.. code-block:: bash

    npm install @reduxjs/toolkit react-redux redux-thunk redux-logger

Design for Modularity and Extensibility
---------------------------------------

In this project, we emphasize modularity and extensibility. Each component manages its own state and reducers, which are dynamically registered to the store. This allows the application to scale easily as new features are added.

Design Alternatives Considered
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Single Store File**: Initially, we considered managing all reducers in a single `store.js` file. However, this approach is not scalable as it requires modifying the store file every time a new reducer is added, leading to tight coupling and reduced maintainability.

2. **Manual Reducer Registration**: Another approach was to manually register reducers in the `store.js` file. This was rejected because it hinders extensibility. Instead, we opted for a dynamic registration mechanism that allows each component to register its own reducer.

3. **Hardcoded Reducers**: Hardcoding reducers in the main store configuration was also considered but discarded due to the lack of flexibility. Dynamic registration provides better modularity and allows for lazy loading of reducers.

Configure Redux Store
---------------------

Create the Redux store configuration files.

.. literalinclude:: _listings/store/reducerManager.js
   :language: jsx
    :linenos:
   :caption: store/reducerManager.js

.. literalinclude:: _listings/store/store.js
   :language: jsx
    :linenos:
   :caption: store/store.js

Configure Redux in React
------------------------

Set up Redux in the React `App.js` file.

.. literalinclude:: _listings/App.js
   :language: jsx
    :linenos:
   :caption: App.js

Create Redux Slices
-------------------

Each component has its own Redux slice, which handles its state and actions. This modular approach keeps the codebase organized and makes it easy to add new features.

Example slice file for component A.

.. literalinclude:: _listings/components/A/slice.js
   :language: jsx
    :linenos:
   :caption: components/A/slice.js

Create Components
-----------------

Each component connects to the Redux store and interacts with its own slice.

Example component file for component A.

.. literalinclude:: _listings/components/A/component.js
   :language: jsx
    :linenos:
   :caption: components/A/component.js

Main Entry Point
----------------

Set up the main entry point to use the components.

.. literalinclude:: _listings/index.js
   :language: jsx
    :linenos:
   :caption: index.js

Running the Application
-----------------------

Start your React application:

.. code-block:: bash
    :linenos:

    npm start

Your application should now support client-side rendering with React and Redux. This setup ensures that your Redux state is managed correctly and that components interact seamlessly.

Conclusion
----------

By following this guide, you can set up a client-side rendered React application with Redux efficiently. The emphasis on modularity and extensibility ensures that the application is scalable and maintainable. This setup helps in managing the application state effectively, making your React application more robust and easier to extend.

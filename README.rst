|Open in Colab|

.. code:: python

    import ...

    # Define an objective function to be minimized.
    def objective(trial):

        # Invoke suggest methods of a Trial object to generate hyperparameters.
        regressor_name = trial.suggest_categorical('classifier', ['SVR', 'RandomForest'])
        if regressor_name == 'SVR':
            svr_c = trial.suggest_loguniform('svr_c', 1e-10, 1e10)
            regressor_obj = sklearn.svm.SVR(C=svr_c)
        else:
            rf_max_depth = trial.suggest_int('rf_max_depth', 2, 32)
            regressor_obj = sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth)

        X, y = sklearn.datasets.load_boston(return_X_y=True)
        X_train, X_val, y_train, y_val = sklearn.model_selection.train_test_split(X, y, random_state=0)

        regressor_obj.fit(X_train, y_train)
        y_pred = regressor_obj.predict(X_val)

        error = sklearn.metrics.mean_squared_error(y_val, y_pred)

        return error  # An objective value linked with the Trial object.

    study = optuna.create_study()  # Create a new study.
    study.optimize(objective, n_trials=100)  # Invoke optimization of the objective function.

Communication
-------------

-  `GitHub Issues <https://github.com/optuna/optuna/issues>`__ for bug
   reports, feature requests and questions.
-  `Gitter <https://gitter.im/optuna/optuna>`__ for interactive chat
   with developers.
-  `Stack
   Overflow <https://stackoverflow.com/questions/tagged/optuna>`__ for
   questions.

Contribution
------------
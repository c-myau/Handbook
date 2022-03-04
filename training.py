from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


def model_selection_func(artifacts, model):
    if model == "dtr":
        return dtr_training(artifacts)
    if model == "rft":
        return rft_training(artifacts)

def dtr_training(artifacts):
    y = artifacts.NumRuns
    X = artifacts.drop('NumRuns', axis=1)

    # split data into training and validation data, for both features and target
    # The split is based on a random number generator. Supplying a numeric value to
    # the random_state argument guarantees we get the same split every time we
    # run this script.
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

    # Define model
    max_leaf_nodes = 50
    artifact_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    # Fit model
    artifact_model.fit(train_X, train_y)

    # get predicted prices on validation data
    val_predictions = artifact_model.predict(val_X)
    print("Mean prediction: {avg}".format(avg=sum(val_predictions)/len(val_predictions)))
    print("MAE: {mae}".format(mae=mean_absolute_error(val_y, val_predictions)))

    # for max_leaf_nodes in [10, 30, 50, 70, 100]:
    #     my_mae = get_dtr_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    #     print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

    return artifact_model

def rft_training(artifacts):
    y = artifacts.NumRuns
    X = artifacts.drop('NumRuns', axis=1)

    # split data into training and validation data, for both features and target
    # The split is based on a random number generator. Supplying a numeric value to
    # the random_state argument guarantees we get the same split every time we
    # run this script.
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)

    # # Define model
    # max_leaf_nodes = 50
    # artifact_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    # # Fit model
    # artifact_model.fit(train_X, train_y)
    #
    # # get predicted prices on validation data
    # val_predictions = artifact_model.predict(val_X)
    # print("Mean prediction: {avg}".format(avg=sum(val_predictions)/len(val_predictions)))
    # print("MAE: {mae}".format(mae=mean_absolute_error(val_y, val_predictions)))

    for max_leaf_nodes in [10, 30, 50, 70, 100]:
        my_mae = get_rft_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
        print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %(max_leaf_nodes, my_mae))

    return None

def get_rft_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae

def get_dtr_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae

"""
tests for the stock module
"""
import pytest  # type: ignore
import pandas as pd  # type: ignore

# import app.modules.ml_gmm as ml_gmm

test_data = [
    # first test
    # data_frame
    (pd.DataFrame(
        columns=["Open",
                 "High",
                 "Low",
                 "clse",
                 "Volume",
                 "Dividends",
                 "Stock Splits"],
        data=[[1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3]]),
     # wanted
     pd.DataFrame(
         columns=["Open",
                  "High",
                  "Low",
                  "clse",
                  "Volume",
                  "Dividends",
                  "Stock Splits"],
         data=[[1, 2, "b", 3, 4, 5, 3],
               [1, 2, "b", 3, 4, 5, 3],
               [1, 2, "b", 3, 4, 5, 3]])),
    # second test
    # data_frame
    (pd.DataFrame(
        columns=["Open",
                 "High",
                 "Low",
                 "clse",
                 "Volume",
                 "Dividends",
                 "Stock Splits"],
        data=[[1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3],
              [1, 2, "b", 3, 4, 5, 3]]),
     # wanted
     pd.DataFrame(
         columns=["Open",
                  "High",
                  "Low",
                  "clse",
                  "Volume",
                  "Dividends",
                  "Stock Splits"],
         data=[[1, 2, "b", 3, 4, 5, 3],
               [1, 2, "b", 3, 4, 5, 3],
               [1, 2, "b", 3, 4, 5, 3]]))]


@pytest.mark.parametrize("data_frame,wanted", test_data)
def test_preprocess_data_2(data_frame, wanted):
    """

    :param data_frame:
    :param wanted:
    :return:
    """
    print("wanted:")
    print(wanted)
    print("df: ")
    print(data_frame)

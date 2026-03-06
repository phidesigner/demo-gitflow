"""
Educational Goal:
- Why this module exists in an MLOps system: Centralize file input/output so pipeline steps stay testable and consistent
- Responsibility (separation of concerns): Provide thin, transparent helpers for reading and writing artifacts
- Pipeline contract (inputs and outputs): DataFrames and models are saved and loaded from explicit filesystem paths

TODO: Replace print statements with standard library logging in a later session
TODO: Any temporary or hardcoded variable or parameter will be imported from config.yml in a later session
"""

from pathlib import Path

import joblib
import pandas as pd


def load_csv(filepath: Path) -> pd.DataFrame:
    """
    Inputs:
    - filepath: Path to a CSV file
    Outputs:
    - df: pandas DataFrame loaded from disk
    Why this contract matters for reliable ML delivery:
    - Consistent I/O reduces "it worked on my notebook" risk and makes pipelines reproducible
    """
    print(f"[utils.load_csv] Loading CSV from: {filepath}")  # TODO: replace with logging later

    try:
        df = pd.read_csv(filepath, sep=",", encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        raise
    return df



def save_csv(df: pd.DataFrame, filepath: Path) -> None:
    """
    Inputs:
    - df: pandas DataFrame to save
    - filepath: Path where the CSV should be written
    Outputs:
    - None
    Why this contract matters for reliable ML delivery:
    - Stable artifact paths enable handoffs, audits, reruns, and downstream automation
    """
    print(f"[utils.save_csv] Saving CSV to: {filepath}")  # TODO: replace with logging later
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------------
    # START STUDENT CODE
    # --------------------------------------------------------
    # TODO_STUDENT: Decide whether you need index=True for your use case
    # Why: Some business workflows require row identifiers, others do not
    # Examples:
    # 1. df.to_csv(filepath, index=True)
    # 2. df.to_csv(filepath, index=False)
    # --------------------------------------------------------
    # END STUDENT CODE
    # --------------------------------------------------------

    df.to_csv(filepath, index=False)


def save_model(model, filepath: Path) -> None:
    """
    Inputs:
    - model: a fitted scikit-learn model or Pipeline
    - filepath: Path where the model should be written
    Outputs:
    - None
    Why this contract matters for reliable ML delivery:
    - Saving trained models is required for repeatable inference and deployment readiness
    """
    print(f"[utils.save_model] Saving model to: {filepath}")  # TODO: replace with logging later
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # --------------------------------------------------------
    # START STUDENT CODE
    # --------------------------------------------------------
    # TODO_STUDENT: Consider adding compression or versioned file naming
    # Why: Model versioning prevents accidental overwrites and supports rollbacks
    # Examples:
    # 1. joblib.dump(model, filepath, compress=3)
    # 2. save to models/model_v2.joblib
    # --------------------------------------------------------
    # END STUDENT CODE
    # --------------------------------------------------------

    joblib.dump(model, filepath)


def load_model(filepath: Path):
    """
    Inputs:
    - filepath: Path to a saved model file
    Outputs:
    - model: loaded model object
    Why this contract matters for reliable ML delivery:
    - Loading models consistently enables batch inference, testing, and production reuse
    """
    print(f"[utils.load_model] Loading model from: {filepath}")  # TODO: replace with logging later

    # --------------------------------------------------------
    # START STUDENT CODE
    # --------------------------------------------------------
    # TODO_STUDENT: Validate model compatibility across environments if needed
    # Why: Different library versions can cause load failures or behavior changes
    # Examples:
    # 1. Check scikit-learn version pinning
    # 2. Add a simple try/except with a clear error message
    # --------------------------------------------------------
    # END STUDENT CODE
    # --------------------------------------------------------

    return joblib.load(filepath)
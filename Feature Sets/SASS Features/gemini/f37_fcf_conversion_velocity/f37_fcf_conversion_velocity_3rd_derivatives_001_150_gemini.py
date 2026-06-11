
import pandas as pd
import os
import sys

# Add the current directory to sys.path
sys.path.append(os.path.dirname(__file__))

import f37_fcf_conversion_velocity_base_001_075_gemini as b1
import f37_fcf_conversion_velocity_base_076_150_gemini as b2

def generate_features(df):
    df1 = b1.generate_features(df)
    df2 = b2.generate_features(df)
    df_all = pd.concat([df1, df2], axis=1)
    return df_all.diff().diff()

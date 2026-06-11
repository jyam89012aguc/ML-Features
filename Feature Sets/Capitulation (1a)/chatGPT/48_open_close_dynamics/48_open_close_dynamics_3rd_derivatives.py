import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def ocd_176_ocd_001_gap_down_frequency_5_001_accel_1(ocd_151_ocd_001_gap_down_frequency_5_001_roc_1):
    feature = _s(ocd_151_ocd_001_gap_down_frequency_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ocd_177_ocd_007_gap_down_frequency_126_007_accel_5(ocd_152_ocd_007_gap_down_frequency_126_007_roc_5):
    feature = _s(ocd_152_ocd_007_gap_down_frequency_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def ocd_178_ocd_013_gap_down_frequency_1008_013_accel_42(ocd_153_ocd_013_gap_down_frequency_1008_013_roc_42):
    feature = _s(ocd_153_ocd_013_gap_down_frequency_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ocd_179_ocd_019_gap_down_frequency_42_019_accel_126(ocd_154_ocd_019_gap_down_frequency_42_019_roc_126):
    feature = _s(ocd_154_ocd_019_gap_down_frequency_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ocd_180_ocd_025_gap_down_frequency_378_025_accel_378(ocd_155_ocd_025_gap_down_frequency_378_025_roc_378):
    feature = _s(ocd_155_ocd_025_gap_down_frequency_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















OPEN_CLOSE_DYNAMICS_REGISTRY_3RD_DERIVATIVES = {
    'ocd_176_ocd_001_gap_down_frequency_5_001_accel_1': {'inputs': ['ocd_151_ocd_001_gap_down_frequency_5_001_roc_1'], 'func': ocd_176_ocd_001_gap_down_frequency_5_001_accel_1},
    'ocd_177_ocd_007_gap_down_frequency_126_007_accel_5': {'inputs': ['ocd_152_ocd_007_gap_down_frequency_126_007_roc_5'], 'func': ocd_177_ocd_007_gap_down_frequency_126_007_accel_5},
    'ocd_178_ocd_013_gap_down_frequency_1008_013_accel_42': {'inputs': ['ocd_153_ocd_013_gap_down_frequency_1008_013_roc_42'], 'func': ocd_178_ocd_013_gap_down_frequency_1008_013_accel_42},
    'ocd_179_ocd_019_gap_down_frequency_42_019_accel_126': {'inputs': ['ocd_154_ocd_019_gap_down_frequency_42_019_roc_126'], 'func': ocd_179_ocd_019_gap_down_frequency_42_019_accel_126},
    'ocd_180_ocd_025_gap_down_frequency_378_025_accel_378': {'inputs': ['ocd_155_ocd_025_gap_down_frequency_378_025_roc_378'], 'func': ocd_180_ocd_025_gap_down_frequency_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ocd_replacement_d3_001(ocd_replacement_d2_001):
    feature = _clean(ocd_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_001'] = {'inputs': ['ocd_replacement_d2_001'], 'func': ocd_replacement_d3_001}


def ocd_replacement_d3_002(ocd_replacement_d2_002):
    feature = _clean(ocd_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_002'] = {'inputs': ['ocd_replacement_d2_002'], 'func': ocd_replacement_d3_002}


def ocd_replacement_d3_003(ocd_replacement_d2_003):
    feature = _clean(ocd_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_003'] = {'inputs': ['ocd_replacement_d2_003'], 'func': ocd_replacement_d3_003}


def ocd_replacement_d3_004(ocd_replacement_d2_004):
    feature = _clean(ocd_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_004'] = {'inputs': ['ocd_replacement_d2_004'], 'func': ocd_replacement_d3_004}


def ocd_replacement_d3_005(ocd_replacement_d2_005):
    feature = _clean(ocd_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_005'] = {'inputs': ['ocd_replacement_d2_005'], 'func': ocd_replacement_d3_005}


def ocd_replacement_d3_006(ocd_replacement_d2_006):
    feature = _clean(ocd_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_006'] = {'inputs': ['ocd_replacement_d2_006'], 'func': ocd_replacement_d3_006}


def ocd_replacement_d3_007(ocd_replacement_d2_007):
    feature = _clean(ocd_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_007'] = {'inputs': ['ocd_replacement_d2_007'], 'func': ocd_replacement_d3_007}


def ocd_replacement_d3_008(ocd_replacement_d2_008):
    feature = _clean(ocd_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_008'] = {'inputs': ['ocd_replacement_d2_008'], 'func': ocd_replacement_d3_008}


def ocd_replacement_d3_009(ocd_replacement_d2_009):
    feature = _clean(ocd_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_009'] = {'inputs': ['ocd_replacement_d2_009'], 'func': ocd_replacement_d3_009}


def ocd_replacement_d3_010(ocd_replacement_d2_010):
    feature = _clean(ocd_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_010'] = {'inputs': ['ocd_replacement_d2_010'], 'func': ocd_replacement_d3_010}


def ocd_replacement_d3_011(ocd_replacement_d2_011):
    feature = _clean(ocd_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_011'] = {'inputs': ['ocd_replacement_d2_011'], 'func': ocd_replacement_d3_011}


def ocd_replacement_d3_012(ocd_replacement_d2_012):
    feature = _clean(ocd_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_012'] = {'inputs': ['ocd_replacement_d2_012'], 'func': ocd_replacement_d3_012}


def ocd_replacement_d3_013(ocd_replacement_d2_013):
    feature = _clean(ocd_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_013'] = {'inputs': ['ocd_replacement_d2_013'], 'func': ocd_replacement_d3_013}


def ocd_replacement_d3_014(ocd_replacement_d2_014):
    feature = _clean(ocd_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_014'] = {'inputs': ['ocd_replacement_d2_014'], 'func': ocd_replacement_d3_014}


def ocd_replacement_d3_015(ocd_replacement_d2_015):
    feature = _clean(ocd_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_015'] = {'inputs': ['ocd_replacement_d2_015'], 'func': ocd_replacement_d3_015}


def ocd_replacement_d3_016(ocd_replacement_d2_016):
    feature = _clean(ocd_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_016'] = {'inputs': ['ocd_replacement_d2_016'], 'func': ocd_replacement_d3_016}


def ocd_replacement_d3_017(ocd_replacement_d2_017):
    feature = _clean(ocd_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_017'] = {'inputs': ['ocd_replacement_d2_017'], 'func': ocd_replacement_d3_017}


def ocd_replacement_d3_018(ocd_replacement_d2_018):
    feature = _clean(ocd_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_018'] = {'inputs': ['ocd_replacement_d2_018'], 'func': ocd_replacement_d3_018}


def ocd_replacement_d3_019(ocd_replacement_d2_019):
    feature = _clean(ocd_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_019'] = {'inputs': ['ocd_replacement_d2_019'], 'func': ocd_replacement_d3_019}


def ocd_replacement_d3_020(ocd_replacement_d2_020):
    feature = _clean(ocd_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_020'] = {'inputs': ['ocd_replacement_d2_020'], 'func': ocd_replacement_d3_020}


def ocd_replacement_d3_021(ocd_replacement_d2_021):
    feature = _clean(ocd_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_021'] = {'inputs': ['ocd_replacement_d2_021'], 'func': ocd_replacement_d3_021}


def ocd_replacement_d3_022(ocd_replacement_d2_022):
    feature = _clean(ocd_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_022'] = {'inputs': ['ocd_replacement_d2_022'], 'func': ocd_replacement_d3_022}


def ocd_replacement_d3_023(ocd_replacement_d2_023):
    feature = _clean(ocd_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_023'] = {'inputs': ['ocd_replacement_d2_023'], 'func': ocd_replacement_d3_023}


def ocd_replacement_d3_024(ocd_replacement_d2_024):
    feature = _clean(ocd_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_024'] = {'inputs': ['ocd_replacement_d2_024'], 'func': ocd_replacement_d3_024}


def ocd_replacement_d3_025(ocd_replacement_d2_025):
    feature = _clean(ocd_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_025'] = {'inputs': ['ocd_replacement_d2_025'], 'func': ocd_replacement_d3_025}


def ocd_replacement_d3_026(ocd_replacement_d2_026):
    feature = _clean(ocd_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_026'] = {'inputs': ['ocd_replacement_d2_026'], 'func': ocd_replacement_d3_026}


def ocd_replacement_d3_027(ocd_replacement_d2_027):
    feature = _clean(ocd_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_027'] = {'inputs': ['ocd_replacement_d2_027'], 'func': ocd_replacement_d3_027}


def ocd_replacement_d3_028(ocd_replacement_d2_028):
    feature = _clean(ocd_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_028'] = {'inputs': ['ocd_replacement_d2_028'], 'func': ocd_replacement_d3_028}


def ocd_replacement_d3_029(ocd_replacement_d2_029):
    feature = _clean(ocd_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_029'] = {'inputs': ['ocd_replacement_d2_029'], 'func': ocd_replacement_d3_029}


def ocd_replacement_d3_030(ocd_replacement_d2_030):
    feature = _clean(ocd_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_030'] = {'inputs': ['ocd_replacement_d2_030'], 'func': ocd_replacement_d3_030}


def ocd_replacement_d3_031(ocd_replacement_d2_031):
    feature = _clean(ocd_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_031'] = {'inputs': ['ocd_replacement_d2_031'], 'func': ocd_replacement_d3_031}


def ocd_replacement_d3_032(ocd_replacement_d2_032):
    feature = _clean(ocd_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_032'] = {'inputs': ['ocd_replacement_d2_032'], 'func': ocd_replacement_d3_032}


def ocd_replacement_d3_033(ocd_replacement_d2_033):
    feature = _clean(ocd_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_033'] = {'inputs': ['ocd_replacement_d2_033'], 'func': ocd_replacement_d3_033}


def ocd_replacement_d3_034(ocd_replacement_d2_034):
    feature = _clean(ocd_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_034'] = {'inputs': ['ocd_replacement_d2_034'], 'func': ocd_replacement_d3_034}


def ocd_replacement_d3_035(ocd_replacement_d2_035):
    feature = _clean(ocd_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_035'] = {'inputs': ['ocd_replacement_d2_035'], 'func': ocd_replacement_d3_035}


def ocd_replacement_d3_036(ocd_replacement_d2_036):
    feature = _clean(ocd_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_036'] = {'inputs': ['ocd_replacement_d2_036'], 'func': ocd_replacement_d3_036}


def ocd_replacement_d3_037(ocd_replacement_d2_037):
    feature = _clean(ocd_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_037'] = {'inputs': ['ocd_replacement_d2_037'], 'func': ocd_replacement_d3_037}


def ocd_replacement_d3_038(ocd_replacement_d2_038):
    feature = _clean(ocd_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_038'] = {'inputs': ['ocd_replacement_d2_038'], 'func': ocd_replacement_d3_038}


def ocd_replacement_d3_039(ocd_replacement_d2_039):
    feature = _clean(ocd_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_039'] = {'inputs': ['ocd_replacement_d2_039'], 'func': ocd_replacement_d3_039}


def ocd_replacement_d3_040(ocd_replacement_d2_040):
    feature = _clean(ocd_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_040'] = {'inputs': ['ocd_replacement_d2_040'], 'func': ocd_replacement_d3_040}


def ocd_replacement_d3_041(ocd_replacement_d2_041):
    feature = _clean(ocd_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_041'] = {'inputs': ['ocd_replacement_d2_041'], 'func': ocd_replacement_d3_041}


def ocd_replacement_d3_042(ocd_replacement_d2_042):
    feature = _clean(ocd_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_042'] = {'inputs': ['ocd_replacement_d2_042'], 'func': ocd_replacement_d3_042}


def ocd_replacement_d3_043(ocd_replacement_d2_043):
    feature = _clean(ocd_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_043'] = {'inputs': ['ocd_replacement_d2_043'], 'func': ocd_replacement_d3_043}


def ocd_replacement_d3_044(ocd_replacement_d2_044):
    feature = _clean(ocd_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_044'] = {'inputs': ['ocd_replacement_d2_044'], 'func': ocd_replacement_d3_044}


def ocd_replacement_d3_045(ocd_replacement_d2_045):
    feature = _clean(ocd_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_045'] = {'inputs': ['ocd_replacement_d2_045'], 'func': ocd_replacement_d3_045}


def ocd_replacement_d3_046(ocd_replacement_d2_046):
    feature = _clean(ocd_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_046'] = {'inputs': ['ocd_replacement_d2_046'], 'func': ocd_replacement_d3_046}


def ocd_replacement_d3_047(ocd_replacement_d2_047):
    feature = _clean(ocd_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_047'] = {'inputs': ['ocd_replacement_d2_047'], 'func': ocd_replacement_d3_047}


def ocd_replacement_d3_048(ocd_replacement_d2_048):
    feature = _clean(ocd_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_048'] = {'inputs': ['ocd_replacement_d2_048'], 'func': ocd_replacement_d3_048}


def ocd_replacement_d3_049(ocd_replacement_d2_049):
    feature = _clean(ocd_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_049'] = {'inputs': ['ocd_replacement_d2_049'], 'func': ocd_replacement_d3_049}


def ocd_replacement_d3_050(ocd_replacement_d2_050):
    feature = _clean(ocd_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_050'] = {'inputs': ['ocd_replacement_d2_050'], 'func': ocd_replacement_d3_050}


def ocd_replacement_d3_051(ocd_replacement_d2_051):
    feature = _clean(ocd_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_051'] = {'inputs': ['ocd_replacement_d2_051'], 'func': ocd_replacement_d3_051}


def ocd_replacement_d3_052(ocd_replacement_d2_052):
    feature = _clean(ocd_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_052'] = {'inputs': ['ocd_replacement_d2_052'], 'func': ocd_replacement_d3_052}


def ocd_replacement_d3_053(ocd_replacement_d2_053):
    feature = _clean(ocd_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_053'] = {'inputs': ['ocd_replacement_d2_053'], 'func': ocd_replacement_d3_053}


def ocd_replacement_d3_054(ocd_replacement_d2_054):
    feature = _clean(ocd_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_054'] = {'inputs': ['ocd_replacement_d2_054'], 'func': ocd_replacement_d3_054}


def ocd_replacement_d3_055(ocd_replacement_d2_055):
    feature = _clean(ocd_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_055'] = {'inputs': ['ocd_replacement_d2_055'], 'func': ocd_replacement_d3_055}


def ocd_replacement_d3_056(ocd_replacement_d2_056):
    feature = _clean(ocd_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_056'] = {'inputs': ['ocd_replacement_d2_056'], 'func': ocd_replacement_d3_056}


def ocd_replacement_d3_057(ocd_replacement_d2_057):
    feature = _clean(ocd_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_057'] = {'inputs': ['ocd_replacement_d2_057'], 'func': ocd_replacement_d3_057}


def ocd_replacement_d3_058(ocd_replacement_d2_058):
    feature = _clean(ocd_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_058'] = {'inputs': ['ocd_replacement_d2_058'], 'func': ocd_replacement_d3_058}


def ocd_replacement_d3_059(ocd_replacement_d2_059):
    feature = _clean(ocd_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_059'] = {'inputs': ['ocd_replacement_d2_059'], 'func': ocd_replacement_d3_059}


def ocd_replacement_d3_060(ocd_replacement_d2_060):
    feature = _clean(ocd_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_060'] = {'inputs': ['ocd_replacement_d2_060'], 'func': ocd_replacement_d3_060}


def ocd_replacement_d3_061(ocd_replacement_d2_061):
    feature = _clean(ocd_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_061'] = {'inputs': ['ocd_replacement_d2_061'], 'func': ocd_replacement_d3_061}


def ocd_replacement_d3_062(ocd_replacement_d2_062):
    feature = _clean(ocd_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_062'] = {'inputs': ['ocd_replacement_d2_062'], 'func': ocd_replacement_d3_062}


def ocd_replacement_d3_063(ocd_replacement_d2_063):
    feature = _clean(ocd_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_063'] = {'inputs': ['ocd_replacement_d2_063'], 'func': ocd_replacement_d3_063}


def ocd_replacement_d3_064(ocd_replacement_d2_064):
    feature = _clean(ocd_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_064'] = {'inputs': ['ocd_replacement_d2_064'], 'func': ocd_replacement_d3_064}


def ocd_replacement_d3_065(ocd_replacement_d2_065):
    feature = _clean(ocd_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_065'] = {'inputs': ['ocd_replacement_d2_065'], 'func': ocd_replacement_d3_065}


def ocd_replacement_d3_066(ocd_replacement_d2_066):
    feature = _clean(ocd_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_066'] = {'inputs': ['ocd_replacement_d2_066'], 'func': ocd_replacement_d3_066}


def ocd_replacement_d3_067(ocd_replacement_d2_067):
    feature = _clean(ocd_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_067'] = {'inputs': ['ocd_replacement_d2_067'], 'func': ocd_replacement_d3_067}


def ocd_replacement_d3_068(ocd_replacement_d2_068):
    feature = _clean(ocd_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_068'] = {'inputs': ['ocd_replacement_d2_068'], 'func': ocd_replacement_d3_068}


def ocd_replacement_d3_069(ocd_replacement_d2_069):
    feature = _clean(ocd_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_069'] = {'inputs': ['ocd_replacement_d2_069'], 'func': ocd_replacement_d3_069}


def ocd_replacement_d3_070(ocd_replacement_d2_070):
    feature = _clean(ocd_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_070'] = {'inputs': ['ocd_replacement_d2_070'], 'func': ocd_replacement_d3_070}


def ocd_replacement_d3_071(ocd_replacement_d2_071):
    feature = _clean(ocd_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_071'] = {'inputs': ['ocd_replacement_d2_071'], 'func': ocd_replacement_d3_071}


def ocd_replacement_d3_072(ocd_replacement_d2_072):
    feature = _clean(ocd_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_072'] = {'inputs': ['ocd_replacement_d2_072'], 'func': ocd_replacement_d3_072}


def ocd_replacement_d3_073(ocd_replacement_d2_073):
    feature = _clean(ocd_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_073'] = {'inputs': ['ocd_replacement_d2_073'], 'func': ocd_replacement_d3_073}


def ocd_replacement_d3_074(ocd_replacement_d2_074):
    feature = _clean(ocd_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_074'] = {'inputs': ['ocd_replacement_d2_074'], 'func': ocd_replacement_d3_074}


def ocd_replacement_d3_075(ocd_replacement_d2_075):
    feature = _clean(ocd_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_075'] = {'inputs': ['ocd_replacement_d2_075'], 'func': ocd_replacement_d3_075}


def ocd_replacement_d3_076(ocd_replacement_d2_076):
    feature = _clean(ocd_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_076'] = {'inputs': ['ocd_replacement_d2_076'], 'func': ocd_replacement_d3_076}


def ocd_replacement_d3_077(ocd_replacement_d2_077):
    feature = _clean(ocd_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_077'] = {'inputs': ['ocd_replacement_d2_077'], 'func': ocd_replacement_d3_077}


def ocd_replacement_d3_078(ocd_replacement_d2_078):
    feature = _clean(ocd_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_078'] = {'inputs': ['ocd_replacement_d2_078'], 'func': ocd_replacement_d3_078}


def ocd_replacement_d3_079(ocd_replacement_d2_079):
    feature = _clean(ocd_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_079'] = {'inputs': ['ocd_replacement_d2_079'], 'func': ocd_replacement_d3_079}


def ocd_replacement_d3_080(ocd_replacement_d2_080):
    feature = _clean(ocd_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_080'] = {'inputs': ['ocd_replacement_d2_080'], 'func': ocd_replacement_d3_080}


def ocd_replacement_d3_081(ocd_replacement_d2_081):
    feature = _clean(ocd_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_081'] = {'inputs': ['ocd_replacement_d2_081'], 'func': ocd_replacement_d3_081}


def ocd_replacement_d3_082(ocd_replacement_d2_082):
    feature = _clean(ocd_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_082'] = {'inputs': ['ocd_replacement_d2_082'], 'func': ocd_replacement_d3_082}


def ocd_replacement_d3_083(ocd_replacement_d2_083):
    feature = _clean(ocd_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_083'] = {'inputs': ['ocd_replacement_d2_083'], 'func': ocd_replacement_d3_083}


def ocd_replacement_d3_084(ocd_replacement_d2_084):
    feature = _clean(ocd_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_084'] = {'inputs': ['ocd_replacement_d2_084'], 'func': ocd_replacement_d3_084}


def ocd_replacement_d3_085(ocd_replacement_d2_085):
    feature = _clean(ocd_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_085'] = {'inputs': ['ocd_replacement_d2_085'], 'func': ocd_replacement_d3_085}


def ocd_replacement_d3_086(ocd_replacement_d2_086):
    feature = _clean(ocd_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_086'] = {'inputs': ['ocd_replacement_d2_086'], 'func': ocd_replacement_d3_086}


def ocd_replacement_d3_087(ocd_replacement_d2_087):
    feature = _clean(ocd_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_087'] = {'inputs': ['ocd_replacement_d2_087'], 'func': ocd_replacement_d3_087}


def ocd_replacement_d3_088(ocd_replacement_d2_088):
    feature = _clean(ocd_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_088'] = {'inputs': ['ocd_replacement_d2_088'], 'func': ocd_replacement_d3_088}


def ocd_replacement_d3_089(ocd_replacement_d2_089):
    feature = _clean(ocd_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_089'] = {'inputs': ['ocd_replacement_d2_089'], 'func': ocd_replacement_d3_089}


def ocd_replacement_d3_090(ocd_replacement_d2_090):
    feature = _clean(ocd_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_090'] = {'inputs': ['ocd_replacement_d2_090'], 'func': ocd_replacement_d3_090}


def ocd_replacement_d3_091(ocd_replacement_d2_091):
    feature = _clean(ocd_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_091'] = {'inputs': ['ocd_replacement_d2_091'], 'func': ocd_replacement_d3_091}


def ocd_replacement_d3_092(ocd_replacement_d2_092):
    feature = _clean(ocd_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_092'] = {'inputs': ['ocd_replacement_d2_092'], 'func': ocd_replacement_d3_092}


def ocd_replacement_d3_093(ocd_replacement_d2_093):
    feature = _clean(ocd_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_093'] = {'inputs': ['ocd_replacement_d2_093'], 'func': ocd_replacement_d3_093}


def ocd_replacement_d3_094(ocd_replacement_d2_094):
    feature = _clean(ocd_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_094'] = {'inputs': ['ocd_replacement_d2_094'], 'func': ocd_replacement_d3_094}


def ocd_replacement_d3_095(ocd_replacement_d2_095):
    feature = _clean(ocd_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_095'] = {'inputs': ['ocd_replacement_d2_095'], 'func': ocd_replacement_d3_095}


def ocd_replacement_d3_096(ocd_replacement_d2_096):
    feature = _clean(ocd_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_096'] = {'inputs': ['ocd_replacement_d2_096'], 'func': ocd_replacement_d3_096}


def ocd_replacement_d3_097(ocd_replacement_d2_097):
    feature = _clean(ocd_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_097'] = {'inputs': ['ocd_replacement_d2_097'], 'func': ocd_replacement_d3_097}


def ocd_replacement_d3_098(ocd_replacement_d2_098):
    feature = _clean(ocd_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_098'] = {'inputs': ['ocd_replacement_d2_098'], 'func': ocd_replacement_d3_098}


def ocd_replacement_d3_099(ocd_replacement_d2_099):
    feature = _clean(ocd_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_099'] = {'inputs': ['ocd_replacement_d2_099'], 'func': ocd_replacement_d3_099}


def ocd_replacement_d3_100(ocd_replacement_d2_100):
    feature = _clean(ocd_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_100'] = {'inputs': ['ocd_replacement_d2_100'], 'func': ocd_replacement_d3_100}


def ocd_replacement_d3_101(ocd_replacement_d2_101):
    feature = _clean(ocd_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_101'] = {'inputs': ['ocd_replacement_d2_101'], 'func': ocd_replacement_d3_101}


def ocd_replacement_d3_102(ocd_replacement_d2_102):
    feature = _clean(ocd_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_102'] = {'inputs': ['ocd_replacement_d2_102'], 'func': ocd_replacement_d3_102}


def ocd_replacement_d3_103(ocd_replacement_d2_103):
    feature = _clean(ocd_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_103'] = {'inputs': ['ocd_replacement_d2_103'], 'func': ocd_replacement_d3_103}


def ocd_replacement_d3_104(ocd_replacement_d2_104):
    feature = _clean(ocd_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_104'] = {'inputs': ['ocd_replacement_d2_104'], 'func': ocd_replacement_d3_104}


def ocd_replacement_d3_105(ocd_replacement_d2_105):
    feature = _clean(ocd_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_105'] = {'inputs': ['ocd_replacement_d2_105'], 'func': ocd_replacement_d3_105}


def ocd_replacement_d3_106(ocd_replacement_d2_106):
    feature = _clean(ocd_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_106'] = {'inputs': ['ocd_replacement_d2_106'], 'func': ocd_replacement_d3_106}


def ocd_replacement_d3_107(ocd_replacement_d2_107):
    feature = _clean(ocd_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_107'] = {'inputs': ['ocd_replacement_d2_107'], 'func': ocd_replacement_d3_107}


def ocd_replacement_d3_108(ocd_replacement_d2_108):
    feature = _clean(ocd_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_108'] = {'inputs': ['ocd_replacement_d2_108'], 'func': ocd_replacement_d3_108}


def ocd_replacement_d3_109(ocd_replacement_d2_109):
    feature = _clean(ocd_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_109'] = {'inputs': ['ocd_replacement_d2_109'], 'func': ocd_replacement_d3_109}


def ocd_replacement_d3_110(ocd_replacement_d2_110):
    feature = _clean(ocd_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_110'] = {'inputs': ['ocd_replacement_d2_110'], 'func': ocd_replacement_d3_110}


def ocd_replacement_d3_111(ocd_replacement_d2_111):
    feature = _clean(ocd_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_111'] = {'inputs': ['ocd_replacement_d2_111'], 'func': ocd_replacement_d3_111}


def ocd_replacement_d3_112(ocd_replacement_d2_112):
    feature = _clean(ocd_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_112'] = {'inputs': ['ocd_replacement_d2_112'], 'func': ocd_replacement_d3_112}


def ocd_replacement_d3_113(ocd_replacement_d2_113):
    feature = _clean(ocd_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_113'] = {'inputs': ['ocd_replacement_d2_113'], 'func': ocd_replacement_d3_113}


def ocd_replacement_d3_114(ocd_replacement_d2_114):
    feature = _clean(ocd_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_114'] = {'inputs': ['ocd_replacement_d2_114'], 'func': ocd_replacement_d3_114}


def ocd_replacement_d3_115(ocd_replacement_d2_115):
    feature = _clean(ocd_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_115'] = {'inputs': ['ocd_replacement_d2_115'], 'func': ocd_replacement_d3_115}


def ocd_replacement_d3_116(ocd_replacement_d2_116):
    feature = _clean(ocd_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_116'] = {'inputs': ['ocd_replacement_d2_116'], 'func': ocd_replacement_d3_116}


def ocd_replacement_d3_117(ocd_replacement_d2_117):
    feature = _clean(ocd_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_117'] = {'inputs': ['ocd_replacement_d2_117'], 'func': ocd_replacement_d3_117}


def ocd_replacement_d3_118(ocd_replacement_d2_118):
    feature = _clean(ocd_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_118'] = {'inputs': ['ocd_replacement_d2_118'], 'func': ocd_replacement_d3_118}


def ocd_replacement_d3_119(ocd_replacement_d2_119):
    feature = _clean(ocd_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_119'] = {'inputs': ['ocd_replacement_d2_119'], 'func': ocd_replacement_d3_119}


def ocd_replacement_d3_120(ocd_replacement_d2_120):
    feature = _clean(ocd_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_120'] = {'inputs': ['ocd_replacement_d2_120'], 'func': ocd_replacement_d3_120}


def ocd_replacement_d3_121(ocd_replacement_d2_121):
    feature = _clean(ocd_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_121'] = {'inputs': ['ocd_replacement_d2_121'], 'func': ocd_replacement_d3_121}


def ocd_replacement_d3_122(ocd_replacement_d2_122):
    feature = _clean(ocd_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_122'] = {'inputs': ['ocd_replacement_d2_122'], 'func': ocd_replacement_d3_122}


def ocd_replacement_d3_123(ocd_replacement_d2_123):
    feature = _clean(ocd_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_123'] = {'inputs': ['ocd_replacement_d2_123'], 'func': ocd_replacement_d3_123}


def ocd_replacement_d3_124(ocd_replacement_d2_124):
    feature = _clean(ocd_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_124'] = {'inputs': ['ocd_replacement_d2_124'], 'func': ocd_replacement_d3_124}


def ocd_replacement_d3_125(ocd_replacement_d2_125):
    feature = _clean(ocd_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_125'] = {'inputs': ['ocd_replacement_d2_125'], 'func': ocd_replacement_d3_125}


def ocd_replacement_d3_126(ocd_replacement_d2_126):
    feature = _clean(ocd_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_126'] = {'inputs': ['ocd_replacement_d2_126'], 'func': ocd_replacement_d3_126}


def ocd_replacement_d3_127(ocd_replacement_d2_127):
    feature = _clean(ocd_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_127'] = {'inputs': ['ocd_replacement_d2_127'], 'func': ocd_replacement_d3_127}


def ocd_replacement_d3_128(ocd_replacement_d2_128):
    feature = _clean(ocd_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_128'] = {'inputs': ['ocd_replacement_d2_128'], 'func': ocd_replacement_d3_128}


def ocd_replacement_d3_129(ocd_replacement_d2_129):
    feature = _clean(ocd_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_129'] = {'inputs': ['ocd_replacement_d2_129'], 'func': ocd_replacement_d3_129}


def ocd_replacement_d3_130(ocd_replacement_d2_130):
    feature = _clean(ocd_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_130'] = {'inputs': ['ocd_replacement_d2_130'], 'func': ocd_replacement_d3_130}


def ocd_replacement_d3_131(ocd_replacement_d2_131):
    feature = _clean(ocd_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_131'] = {'inputs': ['ocd_replacement_d2_131'], 'func': ocd_replacement_d3_131}


def ocd_replacement_d3_132(ocd_replacement_d2_132):
    feature = _clean(ocd_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_132'] = {'inputs': ['ocd_replacement_d2_132'], 'func': ocd_replacement_d3_132}


def ocd_replacement_d3_133(ocd_replacement_d2_133):
    feature = _clean(ocd_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_133'] = {'inputs': ['ocd_replacement_d2_133'], 'func': ocd_replacement_d3_133}


def ocd_replacement_d3_134(ocd_replacement_d2_134):
    feature = _clean(ocd_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_134'] = {'inputs': ['ocd_replacement_d2_134'], 'func': ocd_replacement_d3_134}


def ocd_replacement_d3_135(ocd_replacement_d2_135):
    feature = _clean(ocd_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_135'] = {'inputs': ['ocd_replacement_d2_135'], 'func': ocd_replacement_d3_135}


def ocd_replacement_d3_136(ocd_replacement_d2_136):
    feature = _clean(ocd_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_136'] = {'inputs': ['ocd_replacement_d2_136'], 'func': ocd_replacement_d3_136}


def ocd_replacement_d3_137(ocd_replacement_d2_137):
    feature = _clean(ocd_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_137'] = {'inputs': ['ocd_replacement_d2_137'], 'func': ocd_replacement_d3_137}


def ocd_replacement_d3_138(ocd_replacement_d2_138):
    feature = _clean(ocd_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_138'] = {'inputs': ['ocd_replacement_d2_138'], 'func': ocd_replacement_d3_138}


def ocd_replacement_d3_139(ocd_replacement_d2_139):
    feature = _clean(ocd_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_139'] = {'inputs': ['ocd_replacement_d2_139'], 'func': ocd_replacement_d3_139}


def ocd_replacement_d3_140(ocd_replacement_d2_140):
    feature = _clean(ocd_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_140'] = {'inputs': ['ocd_replacement_d2_140'], 'func': ocd_replacement_d3_140}


def ocd_replacement_d3_141(ocd_replacement_d2_141):
    feature = _clean(ocd_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_141'] = {'inputs': ['ocd_replacement_d2_141'], 'func': ocd_replacement_d3_141}


def ocd_replacement_d3_142(ocd_replacement_d2_142):
    feature = _clean(ocd_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_142'] = {'inputs': ['ocd_replacement_d2_142'], 'func': ocd_replacement_d3_142}


def ocd_replacement_d3_143(ocd_replacement_d2_143):
    feature = _clean(ocd_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_143'] = {'inputs': ['ocd_replacement_d2_143'], 'func': ocd_replacement_d3_143}


def ocd_replacement_d3_144(ocd_replacement_d2_144):
    feature = _clean(ocd_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_144'] = {'inputs': ['ocd_replacement_d2_144'], 'func': ocd_replacement_d3_144}


def ocd_replacement_d3_145(ocd_replacement_d2_145):
    feature = _clean(ocd_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_145'] = {'inputs': ['ocd_replacement_d2_145'], 'func': ocd_replacement_d3_145}


def ocd_replacement_d3_146(ocd_replacement_d2_146):
    feature = _clean(ocd_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_146'] = {'inputs': ['ocd_replacement_d2_146'], 'func': ocd_replacement_d3_146}


def ocd_replacement_d3_147(ocd_replacement_d2_147):
    feature = _clean(ocd_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_147'] = {'inputs': ['ocd_replacement_d2_147'], 'func': ocd_replacement_d3_147}


def ocd_replacement_d3_148(ocd_replacement_d2_148):
    feature = _clean(ocd_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_148'] = {'inputs': ['ocd_replacement_d2_148'], 'func': ocd_replacement_d3_148}


def ocd_replacement_d3_149(ocd_replacement_d2_149):
    feature = _clean(ocd_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_149'] = {'inputs': ['ocd_replacement_d2_149'], 'func': ocd_replacement_d3_149}


def ocd_replacement_d3_150(ocd_replacement_d2_150):
    feature = _clean(ocd_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_150'] = {'inputs': ['ocd_replacement_d2_150'], 'func': ocd_replacement_d3_150}


def ocd_replacement_d3_151(ocd_replacement_d2_151):
    feature = _clean(ocd_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_151'] = {'inputs': ['ocd_replacement_d2_151'], 'func': ocd_replacement_d3_151}


def ocd_replacement_d3_152(ocd_replacement_d2_152):
    feature = _clean(ocd_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_152'] = {'inputs': ['ocd_replacement_d2_152'], 'func': ocd_replacement_d3_152}


def ocd_replacement_d3_153(ocd_replacement_d2_153):
    feature = _clean(ocd_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_153'] = {'inputs': ['ocd_replacement_d2_153'], 'func': ocd_replacement_d3_153}


def ocd_replacement_d3_154(ocd_replacement_d2_154):
    feature = _clean(ocd_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_154'] = {'inputs': ['ocd_replacement_d2_154'], 'func': ocd_replacement_d3_154}


def ocd_replacement_d3_155(ocd_replacement_d2_155):
    feature = _clean(ocd_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_155'] = {'inputs': ['ocd_replacement_d2_155'], 'func': ocd_replacement_d3_155}


def ocd_replacement_d3_156(ocd_replacement_d2_156):
    feature = _clean(ocd_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_156'] = {'inputs': ['ocd_replacement_d2_156'], 'func': ocd_replacement_d3_156}


def ocd_replacement_d3_157(ocd_replacement_d2_157):
    feature = _clean(ocd_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_157'] = {'inputs': ['ocd_replacement_d2_157'], 'func': ocd_replacement_d3_157}


def ocd_replacement_d3_158(ocd_replacement_d2_158):
    feature = _clean(ocd_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_158'] = {'inputs': ['ocd_replacement_d2_158'], 'func': ocd_replacement_d3_158}


def ocd_replacement_d3_159(ocd_replacement_d2_159):
    feature = _clean(ocd_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_159'] = {'inputs': ['ocd_replacement_d2_159'], 'func': ocd_replacement_d3_159}


def ocd_replacement_d3_160(ocd_replacement_d2_160):
    feature = _clean(ocd_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
OCD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ocd_replacement_d3_160'] = {'inputs': ['ocd_replacement_d2_160'], 'func': ocd_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ocd_base_universe_d3_001_ocd_002_gap_magnitude_10_002(ocd_base_universe_d2_001_ocd_002_gap_magnitude_10_002):
    return _base_universe_d3(ocd_base_universe_d2_001_ocd_002_gap_magnitude_10_002, 1)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_001_ocd_002_gap_magnitude_10_002'] = {'inputs': ['ocd_base_universe_d2_001_ocd_002_gap_magnitude_10_002'], 'func': ocd_base_universe_d3_001_ocd_002_gap_magnitude_10_002}


def ocd_base_universe_d3_002_ocd_003_open_close_pressure_21_003(ocd_base_universe_d2_002_ocd_003_open_close_pressure_21_003):
    return _base_universe_d3(ocd_base_universe_d2_002_ocd_003_open_close_pressure_21_003, 2)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_002_ocd_003_open_close_pressure_21_003'] = {'inputs': ['ocd_base_universe_d2_002_ocd_003_open_close_pressure_21_003'], 'func': ocd_base_universe_d3_002_ocd_003_open_close_pressure_21_003}


def ocd_base_universe_d3_003_ocd_004_lower_wick_ratio_42_004(ocd_base_universe_d2_003_ocd_004_lower_wick_ratio_42_004):
    return _base_universe_d3(ocd_base_universe_d2_003_ocd_004_lower_wick_ratio_42_004, 3)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_003_ocd_004_lower_wick_ratio_42_004'] = {'inputs': ['ocd_base_universe_d2_003_ocd_004_lower_wick_ratio_42_004'], 'func': ocd_base_universe_d3_003_ocd_004_lower_wick_ratio_42_004}


def ocd_base_universe_d3_004_ocd_005_upper_wick_ratio_63_005(ocd_base_universe_d2_004_ocd_005_upper_wick_ratio_63_005):
    return _base_universe_d3(ocd_base_universe_d2_004_ocd_005_upper_wick_ratio_63_005, 4)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_004_ocd_005_upper_wick_ratio_63_005'] = {'inputs': ['ocd_base_universe_d2_004_ocd_005_upper_wick_ratio_63_005'], 'func': ocd_base_universe_d3_004_ocd_005_upper_wick_ratio_63_005}


def ocd_base_universe_d3_005_ocd_006_body_to_range_84_006(ocd_base_universe_d2_005_ocd_006_body_to_range_84_006):
    return _base_universe_d3(ocd_base_universe_d2_005_ocd_006_body_to_range_84_006, 5)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_005_ocd_006_body_to_range_84_006'] = {'inputs': ['ocd_base_universe_d2_005_ocd_006_body_to_range_84_006'], 'func': ocd_base_universe_d3_005_ocd_006_body_to_range_84_006}


def ocd_base_universe_d3_006_ocd_008_gap_magnitude_189_008(ocd_base_universe_d2_006_ocd_008_gap_magnitude_189_008):
    return _base_universe_d3(ocd_base_universe_d2_006_ocd_008_gap_magnitude_189_008, 6)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_006_ocd_008_gap_magnitude_189_008'] = {'inputs': ['ocd_base_universe_d2_006_ocd_008_gap_magnitude_189_008'], 'func': ocd_base_universe_d3_006_ocd_008_gap_magnitude_189_008}


def ocd_base_universe_d3_007_ocd_009_open_close_pressure_252_009(ocd_base_universe_d2_007_ocd_009_open_close_pressure_252_009):
    return _base_universe_d3(ocd_base_universe_d2_007_ocd_009_open_close_pressure_252_009, 7)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_007_ocd_009_open_close_pressure_252_009'] = {'inputs': ['ocd_base_universe_d2_007_ocd_009_open_close_pressure_252_009'], 'func': ocd_base_universe_d3_007_ocd_009_open_close_pressure_252_009}


def ocd_base_universe_d3_008_ocd_010_lower_wick_ratio_378_010(ocd_base_universe_d2_008_ocd_010_lower_wick_ratio_378_010):
    return _base_universe_d3(ocd_base_universe_d2_008_ocd_010_lower_wick_ratio_378_010, 8)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_008_ocd_010_lower_wick_ratio_378_010'] = {'inputs': ['ocd_base_universe_d2_008_ocd_010_lower_wick_ratio_378_010'], 'func': ocd_base_universe_d3_008_ocd_010_lower_wick_ratio_378_010}


def ocd_base_universe_d3_009_ocd_011_upper_wick_ratio_504_011(ocd_base_universe_d2_009_ocd_011_upper_wick_ratio_504_011):
    return _base_universe_d3(ocd_base_universe_d2_009_ocd_011_upper_wick_ratio_504_011, 9)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_009_ocd_011_upper_wick_ratio_504_011'] = {'inputs': ['ocd_base_universe_d2_009_ocd_011_upper_wick_ratio_504_011'], 'func': ocd_base_universe_d3_009_ocd_011_upper_wick_ratio_504_011}


def ocd_base_universe_d3_010_ocd_012_body_to_range_756_012(ocd_base_universe_d2_010_ocd_012_body_to_range_756_012):
    return _base_universe_d3(ocd_base_universe_d2_010_ocd_012_body_to_range_756_012, 10)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_010_ocd_012_body_to_range_756_012'] = {'inputs': ['ocd_base_universe_d2_010_ocd_012_body_to_range_756_012'], 'func': ocd_base_universe_d3_010_ocd_012_body_to_range_756_012}


def ocd_base_universe_d3_011_ocd_014_gap_magnitude_1260_014(ocd_base_universe_d2_011_ocd_014_gap_magnitude_1260_014):
    return _base_universe_d3(ocd_base_universe_d2_011_ocd_014_gap_magnitude_1260_014, 11)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_011_ocd_014_gap_magnitude_1260_014'] = {'inputs': ['ocd_base_universe_d2_011_ocd_014_gap_magnitude_1260_014'], 'func': ocd_base_universe_d3_011_ocd_014_gap_magnitude_1260_014}


def ocd_base_universe_d3_012_ocd_015_open_close_pressure_1512_015(ocd_base_universe_d2_012_ocd_015_open_close_pressure_1512_015):
    return _base_universe_d3(ocd_base_universe_d2_012_ocd_015_open_close_pressure_1512_015, 12)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_012_ocd_015_open_close_pressure_1512_015'] = {'inputs': ['ocd_base_universe_d2_012_ocd_015_open_close_pressure_1512_015'], 'func': ocd_base_universe_d3_012_ocd_015_open_close_pressure_1512_015}


def ocd_base_universe_d3_013_ocd_016_lower_wick_ratio_5_016(ocd_base_universe_d2_013_ocd_016_lower_wick_ratio_5_016):
    return _base_universe_d3(ocd_base_universe_d2_013_ocd_016_lower_wick_ratio_5_016, 13)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_013_ocd_016_lower_wick_ratio_5_016'] = {'inputs': ['ocd_base_universe_d2_013_ocd_016_lower_wick_ratio_5_016'], 'func': ocd_base_universe_d3_013_ocd_016_lower_wick_ratio_5_016}


def ocd_base_universe_d3_014_ocd_017_upper_wick_ratio_10_017(ocd_base_universe_d2_014_ocd_017_upper_wick_ratio_10_017):
    return _base_universe_d3(ocd_base_universe_d2_014_ocd_017_upper_wick_ratio_10_017, 14)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_014_ocd_017_upper_wick_ratio_10_017'] = {'inputs': ['ocd_base_universe_d2_014_ocd_017_upper_wick_ratio_10_017'], 'func': ocd_base_universe_d3_014_ocd_017_upper_wick_ratio_10_017}


def ocd_base_universe_d3_015_ocd_018_body_to_range_21_018(ocd_base_universe_d2_015_ocd_018_body_to_range_21_018):
    return _base_universe_d3(ocd_base_universe_d2_015_ocd_018_body_to_range_21_018, 15)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_015_ocd_018_body_to_range_21_018'] = {'inputs': ['ocd_base_universe_d2_015_ocd_018_body_to_range_21_018'], 'func': ocd_base_universe_d3_015_ocd_018_body_to_range_21_018}


def ocd_base_universe_d3_016_ocd_020_gap_magnitude_63_020(ocd_base_universe_d2_016_ocd_020_gap_magnitude_63_020):
    return _base_universe_d3(ocd_base_universe_d2_016_ocd_020_gap_magnitude_63_020, 16)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_016_ocd_020_gap_magnitude_63_020'] = {'inputs': ['ocd_base_universe_d2_016_ocd_020_gap_magnitude_63_020'], 'func': ocd_base_universe_d3_016_ocd_020_gap_magnitude_63_020}


def ocd_base_universe_d3_017_ocd_021_open_close_pressure_84_021(ocd_base_universe_d2_017_ocd_021_open_close_pressure_84_021):
    return _base_universe_d3(ocd_base_universe_d2_017_ocd_021_open_close_pressure_84_021, 17)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_017_ocd_021_open_close_pressure_84_021'] = {'inputs': ['ocd_base_universe_d2_017_ocd_021_open_close_pressure_84_021'], 'func': ocd_base_universe_d3_017_ocd_021_open_close_pressure_84_021}


def ocd_base_universe_d3_018_ocd_022_lower_wick_ratio_126_022(ocd_base_universe_d2_018_ocd_022_lower_wick_ratio_126_022):
    return _base_universe_d3(ocd_base_universe_d2_018_ocd_022_lower_wick_ratio_126_022, 18)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_018_ocd_022_lower_wick_ratio_126_022'] = {'inputs': ['ocd_base_universe_d2_018_ocd_022_lower_wick_ratio_126_022'], 'func': ocd_base_universe_d3_018_ocd_022_lower_wick_ratio_126_022}


def ocd_base_universe_d3_019_ocd_023_upper_wick_ratio_189_023(ocd_base_universe_d2_019_ocd_023_upper_wick_ratio_189_023):
    return _base_universe_d3(ocd_base_universe_d2_019_ocd_023_upper_wick_ratio_189_023, 19)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_019_ocd_023_upper_wick_ratio_189_023'] = {'inputs': ['ocd_base_universe_d2_019_ocd_023_upper_wick_ratio_189_023'], 'func': ocd_base_universe_d3_019_ocd_023_upper_wick_ratio_189_023}


def ocd_base_universe_d3_020_ocd_024_body_to_range_252_024(ocd_base_universe_d2_020_ocd_024_body_to_range_252_024):
    return _base_universe_d3(ocd_base_universe_d2_020_ocd_024_body_to_range_252_024, 20)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_020_ocd_024_body_to_range_252_024'] = {'inputs': ['ocd_base_universe_d2_020_ocd_024_body_to_range_252_024'], 'func': ocd_base_universe_d3_020_ocd_024_body_to_range_252_024}


def ocd_base_universe_d3_021_ocd_026_gap_magnitude_504_026(ocd_base_universe_d2_021_ocd_026_gap_magnitude_504_026):
    return _base_universe_d3(ocd_base_universe_d2_021_ocd_026_gap_magnitude_504_026, 21)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_021_ocd_026_gap_magnitude_504_026'] = {'inputs': ['ocd_base_universe_d2_021_ocd_026_gap_magnitude_504_026'], 'func': ocd_base_universe_d3_021_ocd_026_gap_magnitude_504_026}


def ocd_base_universe_d3_022_ocd_027_open_close_pressure_756_027(ocd_base_universe_d2_022_ocd_027_open_close_pressure_756_027):
    return _base_universe_d3(ocd_base_universe_d2_022_ocd_027_open_close_pressure_756_027, 22)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_022_ocd_027_open_close_pressure_756_027'] = {'inputs': ['ocd_base_universe_d2_022_ocd_027_open_close_pressure_756_027'], 'func': ocd_base_universe_d3_022_ocd_027_open_close_pressure_756_027}


def ocd_base_universe_d3_023_ocd_028_lower_wick_ratio_1008_028(ocd_base_universe_d2_023_ocd_028_lower_wick_ratio_1008_028):
    return _base_universe_d3(ocd_base_universe_d2_023_ocd_028_lower_wick_ratio_1008_028, 23)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_023_ocd_028_lower_wick_ratio_1008_028'] = {'inputs': ['ocd_base_universe_d2_023_ocd_028_lower_wick_ratio_1008_028'], 'func': ocd_base_universe_d3_023_ocd_028_lower_wick_ratio_1008_028}


def ocd_base_universe_d3_024_ocd_029_upper_wick_ratio_1260_029(ocd_base_universe_d2_024_ocd_029_upper_wick_ratio_1260_029):
    return _base_universe_d3(ocd_base_universe_d2_024_ocd_029_upper_wick_ratio_1260_029, 24)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_024_ocd_029_upper_wick_ratio_1260_029'] = {'inputs': ['ocd_base_universe_d2_024_ocd_029_upper_wick_ratio_1260_029'], 'func': ocd_base_universe_d3_024_ocd_029_upper_wick_ratio_1260_029}


def ocd_base_universe_d3_025_ocd_030_body_to_range_1512_030(ocd_base_universe_d2_025_ocd_030_body_to_range_1512_030):
    return _base_universe_d3(ocd_base_universe_d2_025_ocd_030_body_to_range_1512_030, 25)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_025_ocd_030_body_to_range_1512_030'] = {'inputs': ['ocd_base_universe_d2_025_ocd_030_body_to_range_1512_030'], 'func': ocd_base_universe_d3_025_ocd_030_body_to_range_1512_030}


def ocd_base_universe_d3_026_ocd_basefill_031(ocd_base_universe_d2_026_ocd_basefill_031):
    return _base_universe_d3(ocd_base_universe_d2_026_ocd_basefill_031, 26)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_026_ocd_basefill_031'] = {'inputs': ['ocd_base_universe_d2_026_ocd_basefill_031'], 'func': ocd_base_universe_d3_026_ocd_basefill_031}


def ocd_base_universe_d3_027_ocd_basefill_032(ocd_base_universe_d2_027_ocd_basefill_032):
    return _base_universe_d3(ocd_base_universe_d2_027_ocd_basefill_032, 27)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_027_ocd_basefill_032'] = {'inputs': ['ocd_base_universe_d2_027_ocd_basefill_032'], 'func': ocd_base_universe_d3_027_ocd_basefill_032}


def ocd_base_universe_d3_028_ocd_basefill_033(ocd_base_universe_d2_028_ocd_basefill_033):
    return _base_universe_d3(ocd_base_universe_d2_028_ocd_basefill_033, 28)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_028_ocd_basefill_033'] = {'inputs': ['ocd_base_universe_d2_028_ocd_basefill_033'], 'func': ocd_base_universe_d3_028_ocd_basefill_033}


def ocd_base_universe_d3_029_ocd_basefill_034(ocd_base_universe_d2_029_ocd_basefill_034):
    return _base_universe_d3(ocd_base_universe_d2_029_ocd_basefill_034, 29)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_029_ocd_basefill_034'] = {'inputs': ['ocd_base_universe_d2_029_ocd_basefill_034'], 'func': ocd_base_universe_d3_029_ocd_basefill_034}


def ocd_base_universe_d3_030_ocd_basefill_035(ocd_base_universe_d2_030_ocd_basefill_035):
    return _base_universe_d3(ocd_base_universe_d2_030_ocd_basefill_035, 30)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_030_ocd_basefill_035'] = {'inputs': ['ocd_base_universe_d2_030_ocd_basefill_035'], 'func': ocd_base_universe_d3_030_ocd_basefill_035}


def ocd_base_universe_d3_031_ocd_basefill_036(ocd_base_universe_d2_031_ocd_basefill_036):
    return _base_universe_d3(ocd_base_universe_d2_031_ocd_basefill_036, 31)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_031_ocd_basefill_036'] = {'inputs': ['ocd_base_universe_d2_031_ocd_basefill_036'], 'func': ocd_base_universe_d3_031_ocd_basefill_036}


def ocd_base_universe_d3_032_ocd_basefill_037(ocd_base_universe_d2_032_ocd_basefill_037):
    return _base_universe_d3(ocd_base_universe_d2_032_ocd_basefill_037, 32)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_032_ocd_basefill_037'] = {'inputs': ['ocd_base_universe_d2_032_ocd_basefill_037'], 'func': ocd_base_universe_d3_032_ocd_basefill_037}


def ocd_base_universe_d3_033_ocd_basefill_038(ocd_base_universe_d2_033_ocd_basefill_038):
    return _base_universe_d3(ocd_base_universe_d2_033_ocd_basefill_038, 33)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_033_ocd_basefill_038'] = {'inputs': ['ocd_base_universe_d2_033_ocd_basefill_038'], 'func': ocd_base_universe_d3_033_ocd_basefill_038}


def ocd_base_universe_d3_034_ocd_basefill_039(ocd_base_universe_d2_034_ocd_basefill_039):
    return _base_universe_d3(ocd_base_universe_d2_034_ocd_basefill_039, 34)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_034_ocd_basefill_039'] = {'inputs': ['ocd_base_universe_d2_034_ocd_basefill_039'], 'func': ocd_base_universe_d3_034_ocd_basefill_039}


def ocd_base_universe_d3_035_ocd_basefill_040(ocd_base_universe_d2_035_ocd_basefill_040):
    return _base_universe_d3(ocd_base_universe_d2_035_ocd_basefill_040, 35)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_035_ocd_basefill_040'] = {'inputs': ['ocd_base_universe_d2_035_ocd_basefill_040'], 'func': ocd_base_universe_d3_035_ocd_basefill_040}


def ocd_base_universe_d3_036_ocd_basefill_041(ocd_base_universe_d2_036_ocd_basefill_041):
    return _base_universe_d3(ocd_base_universe_d2_036_ocd_basefill_041, 36)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_036_ocd_basefill_041'] = {'inputs': ['ocd_base_universe_d2_036_ocd_basefill_041'], 'func': ocd_base_universe_d3_036_ocd_basefill_041}


def ocd_base_universe_d3_037_ocd_basefill_042(ocd_base_universe_d2_037_ocd_basefill_042):
    return _base_universe_d3(ocd_base_universe_d2_037_ocd_basefill_042, 37)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_037_ocd_basefill_042'] = {'inputs': ['ocd_base_universe_d2_037_ocd_basefill_042'], 'func': ocd_base_universe_d3_037_ocd_basefill_042}


def ocd_base_universe_d3_038_ocd_basefill_043(ocd_base_universe_d2_038_ocd_basefill_043):
    return _base_universe_d3(ocd_base_universe_d2_038_ocd_basefill_043, 38)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_038_ocd_basefill_043'] = {'inputs': ['ocd_base_universe_d2_038_ocd_basefill_043'], 'func': ocd_base_universe_d3_038_ocd_basefill_043}


def ocd_base_universe_d3_039_ocd_basefill_044(ocd_base_universe_d2_039_ocd_basefill_044):
    return _base_universe_d3(ocd_base_universe_d2_039_ocd_basefill_044, 39)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_039_ocd_basefill_044'] = {'inputs': ['ocd_base_universe_d2_039_ocd_basefill_044'], 'func': ocd_base_universe_d3_039_ocd_basefill_044}


def ocd_base_universe_d3_040_ocd_basefill_045(ocd_base_universe_d2_040_ocd_basefill_045):
    return _base_universe_d3(ocd_base_universe_d2_040_ocd_basefill_045, 40)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_040_ocd_basefill_045'] = {'inputs': ['ocd_base_universe_d2_040_ocd_basefill_045'], 'func': ocd_base_universe_d3_040_ocd_basefill_045}


def ocd_base_universe_d3_041_ocd_basefill_046(ocd_base_universe_d2_041_ocd_basefill_046):
    return _base_universe_d3(ocd_base_universe_d2_041_ocd_basefill_046, 41)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_041_ocd_basefill_046'] = {'inputs': ['ocd_base_universe_d2_041_ocd_basefill_046'], 'func': ocd_base_universe_d3_041_ocd_basefill_046}


def ocd_base_universe_d3_042_ocd_basefill_047(ocd_base_universe_d2_042_ocd_basefill_047):
    return _base_universe_d3(ocd_base_universe_d2_042_ocd_basefill_047, 42)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_042_ocd_basefill_047'] = {'inputs': ['ocd_base_universe_d2_042_ocd_basefill_047'], 'func': ocd_base_universe_d3_042_ocd_basefill_047}


def ocd_base_universe_d3_043_ocd_basefill_048(ocd_base_universe_d2_043_ocd_basefill_048):
    return _base_universe_d3(ocd_base_universe_d2_043_ocd_basefill_048, 43)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_043_ocd_basefill_048'] = {'inputs': ['ocd_base_universe_d2_043_ocd_basefill_048'], 'func': ocd_base_universe_d3_043_ocd_basefill_048}


def ocd_base_universe_d3_044_ocd_basefill_049(ocd_base_universe_d2_044_ocd_basefill_049):
    return _base_universe_d3(ocd_base_universe_d2_044_ocd_basefill_049, 44)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_044_ocd_basefill_049'] = {'inputs': ['ocd_base_universe_d2_044_ocd_basefill_049'], 'func': ocd_base_universe_d3_044_ocd_basefill_049}


def ocd_base_universe_d3_045_ocd_basefill_050(ocd_base_universe_d2_045_ocd_basefill_050):
    return _base_universe_d3(ocd_base_universe_d2_045_ocd_basefill_050, 45)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_045_ocd_basefill_050'] = {'inputs': ['ocd_base_universe_d2_045_ocd_basefill_050'], 'func': ocd_base_universe_d3_045_ocd_basefill_050}


def ocd_base_universe_d3_046_ocd_basefill_051(ocd_base_universe_d2_046_ocd_basefill_051):
    return _base_universe_d3(ocd_base_universe_d2_046_ocd_basefill_051, 46)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_046_ocd_basefill_051'] = {'inputs': ['ocd_base_universe_d2_046_ocd_basefill_051'], 'func': ocd_base_universe_d3_046_ocd_basefill_051}


def ocd_base_universe_d3_047_ocd_basefill_052(ocd_base_universe_d2_047_ocd_basefill_052):
    return _base_universe_d3(ocd_base_universe_d2_047_ocd_basefill_052, 47)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_047_ocd_basefill_052'] = {'inputs': ['ocd_base_universe_d2_047_ocd_basefill_052'], 'func': ocd_base_universe_d3_047_ocd_basefill_052}


def ocd_base_universe_d3_048_ocd_basefill_053(ocd_base_universe_d2_048_ocd_basefill_053):
    return _base_universe_d3(ocd_base_universe_d2_048_ocd_basefill_053, 48)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_048_ocd_basefill_053'] = {'inputs': ['ocd_base_universe_d2_048_ocd_basefill_053'], 'func': ocd_base_universe_d3_048_ocd_basefill_053}


def ocd_base_universe_d3_049_ocd_basefill_054(ocd_base_universe_d2_049_ocd_basefill_054):
    return _base_universe_d3(ocd_base_universe_d2_049_ocd_basefill_054, 49)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_049_ocd_basefill_054'] = {'inputs': ['ocd_base_universe_d2_049_ocd_basefill_054'], 'func': ocd_base_universe_d3_049_ocd_basefill_054}


def ocd_base_universe_d3_050_ocd_basefill_055(ocd_base_universe_d2_050_ocd_basefill_055):
    return _base_universe_d3(ocd_base_universe_d2_050_ocd_basefill_055, 50)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_050_ocd_basefill_055'] = {'inputs': ['ocd_base_universe_d2_050_ocd_basefill_055'], 'func': ocd_base_universe_d3_050_ocd_basefill_055}


def ocd_base_universe_d3_051_ocd_basefill_056(ocd_base_universe_d2_051_ocd_basefill_056):
    return _base_universe_d3(ocd_base_universe_d2_051_ocd_basefill_056, 51)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_051_ocd_basefill_056'] = {'inputs': ['ocd_base_universe_d2_051_ocd_basefill_056'], 'func': ocd_base_universe_d3_051_ocd_basefill_056}


def ocd_base_universe_d3_052_ocd_basefill_057(ocd_base_universe_d2_052_ocd_basefill_057):
    return _base_universe_d3(ocd_base_universe_d2_052_ocd_basefill_057, 52)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_052_ocd_basefill_057'] = {'inputs': ['ocd_base_universe_d2_052_ocd_basefill_057'], 'func': ocd_base_universe_d3_052_ocd_basefill_057}


def ocd_base_universe_d3_053_ocd_basefill_058(ocd_base_universe_d2_053_ocd_basefill_058):
    return _base_universe_d3(ocd_base_universe_d2_053_ocd_basefill_058, 53)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_053_ocd_basefill_058'] = {'inputs': ['ocd_base_universe_d2_053_ocd_basefill_058'], 'func': ocd_base_universe_d3_053_ocd_basefill_058}


def ocd_base_universe_d3_054_ocd_basefill_059(ocd_base_universe_d2_054_ocd_basefill_059):
    return _base_universe_d3(ocd_base_universe_d2_054_ocd_basefill_059, 54)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_054_ocd_basefill_059'] = {'inputs': ['ocd_base_universe_d2_054_ocd_basefill_059'], 'func': ocd_base_universe_d3_054_ocd_basefill_059}


def ocd_base_universe_d3_055_ocd_basefill_060(ocd_base_universe_d2_055_ocd_basefill_060):
    return _base_universe_d3(ocd_base_universe_d2_055_ocd_basefill_060, 55)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_055_ocd_basefill_060'] = {'inputs': ['ocd_base_universe_d2_055_ocd_basefill_060'], 'func': ocd_base_universe_d3_055_ocd_basefill_060}


def ocd_base_universe_d3_056_ocd_basefill_061(ocd_base_universe_d2_056_ocd_basefill_061):
    return _base_universe_d3(ocd_base_universe_d2_056_ocd_basefill_061, 56)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_056_ocd_basefill_061'] = {'inputs': ['ocd_base_universe_d2_056_ocd_basefill_061'], 'func': ocd_base_universe_d3_056_ocd_basefill_061}


def ocd_base_universe_d3_057_ocd_basefill_062(ocd_base_universe_d2_057_ocd_basefill_062):
    return _base_universe_d3(ocd_base_universe_d2_057_ocd_basefill_062, 57)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_057_ocd_basefill_062'] = {'inputs': ['ocd_base_universe_d2_057_ocd_basefill_062'], 'func': ocd_base_universe_d3_057_ocd_basefill_062}


def ocd_base_universe_d3_058_ocd_basefill_063(ocd_base_universe_d2_058_ocd_basefill_063):
    return _base_universe_d3(ocd_base_universe_d2_058_ocd_basefill_063, 58)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_058_ocd_basefill_063'] = {'inputs': ['ocd_base_universe_d2_058_ocd_basefill_063'], 'func': ocd_base_universe_d3_058_ocd_basefill_063}


def ocd_base_universe_d3_059_ocd_basefill_064(ocd_base_universe_d2_059_ocd_basefill_064):
    return _base_universe_d3(ocd_base_universe_d2_059_ocd_basefill_064, 59)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_059_ocd_basefill_064'] = {'inputs': ['ocd_base_universe_d2_059_ocd_basefill_064'], 'func': ocd_base_universe_d3_059_ocd_basefill_064}


def ocd_base_universe_d3_060_ocd_basefill_065(ocd_base_universe_d2_060_ocd_basefill_065):
    return _base_universe_d3(ocd_base_universe_d2_060_ocd_basefill_065, 60)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_060_ocd_basefill_065'] = {'inputs': ['ocd_base_universe_d2_060_ocd_basefill_065'], 'func': ocd_base_universe_d3_060_ocd_basefill_065}


def ocd_base_universe_d3_061_ocd_basefill_066(ocd_base_universe_d2_061_ocd_basefill_066):
    return _base_universe_d3(ocd_base_universe_d2_061_ocd_basefill_066, 61)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_061_ocd_basefill_066'] = {'inputs': ['ocd_base_universe_d2_061_ocd_basefill_066'], 'func': ocd_base_universe_d3_061_ocd_basefill_066}


def ocd_base_universe_d3_062_ocd_basefill_067(ocd_base_universe_d2_062_ocd_basefill_067):
    return _base_universe_d3(ocd_base_universe_d2_062_ocd_basefill_067, 62)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_062_ocd_basefill_067'] = {'inputs': ['ocd_base_universe_d2_062_ocd_basefill_067'], 'func': ocd_base_universe_d3_062_ocd_basefill_067}


def ocd_base_universe_d3_063_ocd_basefill_068(ocd_base_universe_d2_063_ocd_basefill_068):
    return _base_universe_d3(ocd_base_universe_d2_063_ocd_basefill_068, 63)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_063_ocd_basefill_068'] = {'inputs': ['ocd_base_universe_d2_063_ocd_basefill_068'], 'func': ocd_base_universe_d3_063_ocd_basefill_068}


def ocd_base_universe_d3_064_ocd_basefill_069(ocd_base_universe_d2_064_ocd_basefill_069):
    return _base_universe_d3(ocd_base_universe_d2_064_ocd_basefill_069, 64)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_064_ocd_basefill_069'] = {'inputs': ['ocd_base_universe_d2_064_ocd_basefill_069'], 'func': ocd_base_universe_d3_064_ocd_basefill_069}


def ocd_base_universe_d3_065_ocd_basefill_070(ocd_base_universe_d2_065_ocd_basefill_070):
    return _base_universe_d3(ocd_base_universe_d2_065_ocd_basefill_070, 65)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_065_ocd_basefill_070'] = {'inputs': ['ocd_base_universe_d2_065_ocd_basefill_070'], 'func': ocd_base_universe_d3_065_ocd_basefill_070}


def ocd_base_universe_d3_066_ocd_basefill_071(ocd_base_universe_d2_066_ocd_basefill_071):
    return _base_universe_d3(ocd_base_universe_d2_066_ocd_basefill_071, 66)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_066_ocd_basefill_071'] = {'inputs': ['ocd_base_universe_d2_066_ocd_basefill_071'], 'func': ocd_base_universe_d3_066_ocd_basefill_071}


def ocd_base_universe_d3_067_ocd_basefill_072(ocd_base_universe_d2_067_ocd_basefill_072):
    return _base_universe_d3(ocd_base_universe_d2_067_ocd_basefill_072, 67)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_067_ocd_basefill_072'] = {'inputs': ['ocd_base_universe_d2_067_ocd_basefill_072'], 'func': ocd_base_universe_d3_067_ocd_basefill_072}


def ocd_base_universe_d3_068_ocd_basefill_073(ocd_base_universe_d2_068_ocd_basefill_073):
    return _base_universe_d3(ocd_base_universe_d2_068_ocd_basefill_073, 68)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_068_ocd_basefill_073'] = {'inputs': ['ocd_base_universe_d2_068_ocd_basefill_073'], 'func': ocd_base_universe_d3_068_ocd_basefill_073}


def ocd_base_universe_d3_069_ocd_basefill_074(ocd_base_universe_d2_069_ocd_basefill_074):
    return _base_universe_d3(ocd_base_universe_d2_069_ocd_basefill_074, 69)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_069_ocd_basefill_074'] = {'inputs': ['ocd_base_universe_d2_069_ocd_basefill_074'], 'func': ocd_base_universe_d3_069_ocd_basefill_074}


def ocd_base_universe_d3_070_ocd_basefill_075(ocd_base_universe_d2_070_ocd_basefill_075):
    return _base_universe_d3(ocd_base_universe_d2_070_ocd_basefill_075, 70)
OCD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ocd_base_universe_d3_070_ocd_basefill_075'] = {'inputs': ['ocd_base_universe_d2_070_ocd_basefill_075'], 'func': ocd_base_universe_d3_070_ocd_basefill_075}

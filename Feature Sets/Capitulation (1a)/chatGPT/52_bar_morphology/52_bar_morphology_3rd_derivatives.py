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



def bmf_176_bmf_001_gap_down_frequency_5_001_accel_1(bmf_151_bmf_001_gap_down_frequency_5_001_roc_1):
    feature = _s(bmf_151_bmf_001_gap_down_frequency_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def bmf_177_bmf_007_gap_down_frequency_126_007_accel_5(bmf_152_bmf_007_gap_down_frequency_126_007_roc_5):
    feature = _s(bmf_152_bmf_007_gap_down_frequency_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def bmf_178_bmf_013_gap_down_frequency_1008_013_accel_42(bmf_153_bmf_013_gap_down_frequency_1008_013_roc_42):
    feature = _s(bmf_153_bmf_013_gap_down_frequency_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def bmf_179_bmf_019_gap_down_frequency_42_019_accel_126(bmf_154_bmf_019_gap_down_frequency_42_019_roc_126):
    feature = _s(bmf_154_bmf_019_gap_down_frequency_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def bmf_180_bmf_025_gap_down_frequency_378_025_accel_378(bmf_155_bmf_025_gap_down_frequency_378_025_roc_378):
    feature = _s(bmf_155_bmf_025_gap_down_frequency_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















BAR_MORPHOLOGY_REGISTRY_3RD_DERIVATIVES = {
    'bmf_176_bmf_001_gap_down_frequency_5_001_accel_1': {'inputs': ['bmf_151_bmf_001_gap_down_frequency_5_001_roc_1'], 'func': bmf_176_bmf_001_gap_down_frequency_5_001_accel_1},
    'bmf_177_bmf_007_gap_down_frequency_126_007_accel_5': {'inputs': ['bmf_152_bmf_007_gap_down_frequency_126_007_roc_5'], 'func': bmf_177_bmf_007_gap_down_frequency_126_007_accel_5},
    'bmf_178_bmf_013_gap_down_frequency_1008_013_accel_42': {'inputs': ['bmf_153_bmf_013_gap_down_frequency_1008_013_roc_42'], 'func': bmf_178_bmf_013_gap_down_frequency_1008_013_accel_42},
    'bmf_179_bmf_019_gap_down_frequency_42_019_accel_126': {'inputs': ['bmf_154_bmf_019_gap_down_frequency_42_019_roc_126'], 'func': bmf_179_bmf_019_gap_down_frequency_42_019_accel_126},
    'bmf_180_bmf_025_gap_down_frequency_378_025_accel_378': {'inputs': ['bmf_155_bmf_025_gap_down_frequency_378_025_roc_378'], 'func': bmf_180_bmf_025_gap_down_frequency_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def bm_replacement_d3_001(bm_replacement_d2_001):
    feature = _clean(bm_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_001'] = {'inputs': ['bm_replacement_d2_001'], 'func': bm_replacement_d3_001}


def bm_replacement_d3_002(bm_replacement_d2_002):
    feature = _clean(bm_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_002'] = {'inputs': ['bm_replacement_d2_002'], 'func': bm_replacement_d3_002}


def bm_replacement_d3_003(bm_replacement_d2_003):
    feature = _clean(bm_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_003'] = {'inputs': ['bm_replacement_d2_003'], 'func': bm_replacement_d3_003}


def bm_replacement_d3_004(bm_replacement_d2_004):
    feature = _clean(bm_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_004'] = {'inputs': ['bm_replacement_d2_004'], 'func': bm_replacement_d3_004}


def bm_replacement_d3_005(bm_replacement_d2_005):
    feature = _clean(bm_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_005'] = {'inputs': ['bm_replacement_d2_005'], 'func': bm_replacement_d3_005}


def bm_replacement_d3_006(bm_replacement_d2_006):
    feature = _clean(bm_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_006'] = {'inputs': ['bm_replacement_d2_006'], 'func': bm_replacement_d3_006}


def bm_replacement_d3_007(bm_replacement_d2_007):
    feature = _clean(bm_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_007'] = {'inputs': ['bm_replacement_d2_007'], 'func': bm_replacement_d3_007}


def bm_replacement_d3_008(bm_replacement_d2_008):
    feature = _clean(bm_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_008'] = {'inputs': ['bm_replacement_d2_008'], 'func': bm_replacement_d3_008}


def bm_replacement_d3_009(bm_replacement_d2_009):
    feature = _clean(bm_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_009'] = {'inputs': ['bm_replacement_d2_009'], 'func': bm_replacement_d3_009}


def bm_replacement_d3_010(bm_replacement_d2_010):
    feature = _clean(bm_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_010'] = {'inputs': ['bm_replacement_d2_010'], 'func': bm_replacement_d3_010}


def bm_replacement_d3_011(bm_replacement_d2_011):
    feature = _clean(bm_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_011'] = {'inputs': ['bm_replacement_d2_011'], 'func': bm_replacement_d3_011}


def bm_replacement_d3_012(bm_replacement_d2_012):
    feature = _clean(bm_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_012'] = {'inputs': ['bm_replacement_d2_012'], 'func': bm_replacement_d3_012}


def bm_replacement_d3_013(bm_replacement_d2_013):
    feature = _clean(bm_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_013'] = {'inputs': ['bm_replacement_d2_013'], 'func': bm_replacement_d3_013}


def bm_replacement_d3_014(bm_replacement_d2_014):
    feature = _clean(bm_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_014'] = {'inputs': ['bm_replacement_d2_014'], 'func': bm_replacement_d3_014}


def bm_replacement_d3_015(bm_replacement_d2_015):
    feature = _clean(bm_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_015'] = {'inputs': ['bm_replacement_d2_015'], 'func': bm_replacement_d3_015}


def bm_replacement_d3_016(bm_replacement_d2_016):
    feature = _clean(bm_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_016'] = {'inputs': ['bm_replacement_d2_016'], 'func': bm_replacement_d3_016}


def bm_replacement_d3_017(bm_replacement_d2_017):
    feature = _clean(bm_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_017'] = {'inputs': ['bm_replacement_d2_017'], 'func': bm_replacement_d3_017}


def bm_replacement_d3_018(bm_replacement_d2_018):
    feature = _clean(bm_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_018'] = {'inputs': ['bm_replacement_d2_018'], 'func': bm_replacement_d3_018}


def bm_replacement_d3_019(bm_replacement_d2_019):
    feature = _clean(bm_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_019'] = {'inputs': ['bm_replacement_d2_019'], 'func': bm_replacement_d3_019}


def bm_replacement_d3_020(bm_replacement_d2_020):
    feature = _clean(bm_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_020'] = {'inputs': ['bm_replacement_d2_020'], 'func': bm_replacement_d3_020}


def bm_replacement_d3_021(bm_replacement_d2_021):
    feature = _clean(bm_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_021'] = {'inputs': ['bm_replacement_d2_021'], 'func': bm_replacement_d3_021}


def bm_replacement_d3_022(bm_replacement_d2_022):
    feature = _clean(bm_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_022'] = {'inputs': ['bm_replacement_d2_022'], 'func': bm_replacement_d3_022}


def bm_replacement_d3_023(bm_replacement_d2_023):
    feature = _clean(bm_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_023'] = {'inputs': ['bm_replacement_d2_023'], 'func': bm_replacement_d3_023}


def bm_replacement_d3_024(bm_replacement_d2_024):
    feature = _clean(bm_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_024'] = {'inputs': ['bm_replacement_d2_024'], 'func': bm_replacement_d3_024}


def bm_replacement_d3_025(bm_replacement_d2_025):
    feature = _clean(bm_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_025'] = {'inputs': ['bm_replacement_d2_025'], 'func': bm_replacement_d3_025}


def bm_replacement_d3_026(bm_replacement_d2_026):
    feature = _clean(bm_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_026'] = {'inputs': ['bm_replacement_d2_026'], 'func': bm_replacement_d3_026}


def bm_replacement_d3_027(bm_replacement_d2_027):
    feature = _clean(bm_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_027'] = {'inputs': ['bm_replacement_d2_027'], 'func': bm_replacement_d3_027}


def bm_replacement_d3_028(bm_replacement_d2_028):
    feature = _clean(bm_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_028'] = {'inputs': ['bm_replacement_d2_028'], 'func': bm_replacement_d3_028}


def bm_replacement_d3_029(bm_replacement_d2_029):
    feature = _clean(bm_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_029'] = {'inputs': ['bm_replacement_d2_029'], 'func': bm_replacement_d3_029}


def bm_replacement_d3_030(bm_replacement_d2_030):
    feature = _clean(bm_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_030'] = {'inputs': ['bm_replacement_d2_030'], 'func': bm_replacement_d3_030}


def bm_replacement_d3_031(bm_replacement_d2_031):
    feature = _clean(bm_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_031'] = {'inputs': ['bm_replacement_d2_031'], 'func': bm_replacement_d3_031}


def bm_replacement_d3_032(bm_replacement_d2_032):
    feature = _clean(bm_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_032'] = {'inputs': ['bm_replacement_d2_032'], 'func': bm_replacement_d3_032}


def bm_replacement_d3_033(bm_replacement_d2_033):
    feature = _clean(bm_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_033'] = {'inputs': ['bm_replacement_d2_033'], 'func': bm_replacement_d3_033}


def bm_replacement_d3_034(bm_replacement_d2_034):
    feature = _clean(bm_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_034'] = {'inputs': ['bm_replacement_d2_034'], 'func': bm_replacement_d3_034}


def bm_replacement_d3_035(bm_replacement_d2_035):
    feature = _clean(bm_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_035'] = {'inputs': ['bm_replacement_d2_035'], 'func': bm_replacement_d3_035}


def bm_replacement_d3_036(bm_replacement_d2_036):
    feature = _clean(bm_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_036'] = {'inputs': ['bm_replacement_d2_036'], 'func': bm_replacement_d3_036}


def bm_replacement_d3_037(bm_replacement_d2_037):
    feature = _clean(bm_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_037'] = {'inputs': ['bm_replacement_d2_037'], 'func': bm_replacement_d3_037}


def bm_replacement_d3_038(bm_replacement_d2_038):
    feature = _clean(bm_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_038'] = {'inputs': ['bm_replacement_d2_038'], 'func': bm_replacement_d3_038}


def bm_replacement_d3_039(bm_replacement_d2_039):
    feature = _clean(bm_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_039'] = {'inputs': ['bm_replacement_d2_039'], 'func': bm_replacement_d3_039}


def bm_replacement_d3_040(bm_replacement_d2_040):
    feature = _clean(bm_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_040'] = {'inputs': ['bm_replacement_d2_040'], 'func': bm_replacement_d3_040}


def bm_replacement_d3_041(bm_replacement_d2_041):
    feature = _clean(bm_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_041'] = {'inputs': ['bm_replacement_d2_041'], 'func': bm_replacement_d3_041}


def bm_replacement_d3_042(bm_replacement_d2_042):
    feature = _clean(bm_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_042'] = {'inputs': ['bm_replacement_d2_042'], 'func': bm_replacement_d3_042}


def bm_replacement_d3_043(bm_replacement_d2_043):
    feature = _clean(bm_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_043'] = {'inputs': ['bm_replacement_d2_043'], 'func': bm_replacement_d3_043}


def bm_replacement_d3_044(bm_replacement_d2_044):
    feature = _clean(bm_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_044'] = {'inputs': ['bm_replacement_d2_044'], 'func': bm_replacement_d3_044}


def bm_replacement_d3_045(bm_replacement_d2_045):
    feature = _clean(bm_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_045'] = {'inputs': ['bm_replacement_d2_045'], 'func': bm_replacement_d3_045}


def bm_replacement_d3_046(bm_replacement_d2_046):
    feature = _clean(bm_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_046'] = {'inputs': ['bm_replacement_d2_046'], 'func': bm_replacement_d3_046}


def bm_replacement_d3_047(bm_replacement_d2_047):
    feature = _clean(bm_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_047'] = {'inputs': ['bm_replacement_d2_047'], 'func': bm_replacement_d3_047}


def bm_replacement_d3_048(bm_replacement_d2_048):
    feature = _clean(bm_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_048'] = {'inputs': ['bm_replacement_d2_048'], 'func': bm_replacement_d3_048}


def bm_replacement_d3_049(bm_replacement_d2_049):
    feature = _clean(bm_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_049'] = {'inputs': ['bm_replacement_d2_049'], 'func': bm_replacement_d3_049}


def bm_replacement_d3_050(bm_replacement_d2_050):
    feature = _clean(bm_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_050'] = {'inputs': ['bm_replacement_d2_050'], 'func': bm_replacement_d3_050}


def bm_replacement_d3_051(bm_replacement_d2_051):
    feature = _clean(bm_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_051'] = {'inputs': ['bm_replacement_d2_051'], 'func': bm_replacement_d3_051}


def bm_replacement_d3_052(bm_replacement_d2_052):
    feature = _clean(bm_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_052'] = {'inputs': ['bm_replacement_d2_052'], 'func': bm_replacement_d3_052}


def bm_replacement_d3_053(bm_replacement_d2_053):
    feature = _clean(bm_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_053'] = {'inputs': ['bm_replacement_d2_053'], 'func': bm_replacement_d3_053}


def bm_replacement_d3_054(bm_replacement_d2_054):
    feature = _clean(bm_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_054'] = {'inputs': ['bm_replacement_d2_054'], 'func': bm_replacement_d3_054}


def bm_replacement_d3_055(bm_replacement_d2_055):
    feature = _clean(bm_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_055'] = {'inputs': ['bm_replacement_d2_055'], 'func': bm_replacement_d3_055}


def bm_replacement_d3_056(bm_replacement_d2_056):
    feature = _clean(bm_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_056'] = {'inputs': ['bm_replacement_d2_056'], 'func': bm_replacement_d3_056}


def bm_replacement_d3_057(bm_replacement_d2_057):
    feature = _clean(bm_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_057'] = {'inputs': ['bm_replacement_d2_057'], 'func': bm_replacement_d3_057}


def bm_replacement_d3_058(bm_replacement_d2_058):
    feature = _clean(bm_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_058'] = {'inputs': ['bm_replacement_d2_058'], 'func': bm_replacement_d3_058}


def bm_replacement_d3_059(bm_replacement_d2_059):
    feature = _clean(bm_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_059'] = {'inputs': ['bm_replacement_d2_059'], 'func': bm_replacement_d3_059}


def bm_replacement_d3_060(bm_replacement_d2_060):
    feature = _clean(bm_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_060'] = {'inputs': ['bm_replacement_d2_060'], 'func': bm_replacement_d3_060}


def bm_replacement_d3_061(bm_replacement_d2_061):
    feature = _clean(bm_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_061'] = {'inputs': ['bm_replacement_d2_061'], 'func': bm_replacement_d3_061}


def bm_replacement_d3_062(bm_replacement_d2_062):
    feature = _clean(bm_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_062'] = {'inputs': ['bm_replacement_d2_062'], 'func': bm_replacement_d3_062}


def bm_replacement_d3_063(bm_replacement_d2_063):
    feature = _clean(bm_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_063'] = {'inputs': ['bm_replacement_d2_063'], 'func': bm_replacement_d3_063}


def bm_replacement_d3_064(bm_replacement_d2_064):
    feature = _clean(bm_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_064'] = {'inputs': ['bm_replacement_d2_064'], 'func': bm_replacement_d3_064}


def bm_replacement_d3_065(bm_replacement_d2_065):
    feature = _clean(bm_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_065'] = {'inputs': ['bm_replacement_d2_065'], 'func': bm_replacement_d3_065}


def bm_replacement_d3_066(bm_replacement_d2_066):
    feature = _clean(bm_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_066'] = {'inputs': ['bm_replacement_d2_066'], 'func': bm_replacement_d3_066}


def bm_replacement_d3_067(bm_replacement_d2_067):
    feature = _clean(bm_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_067'] = {'inputs': ['bm_replacement_d2_067'], 'func': bm_replacement_d3_067}


def bm_replacement_d3_068(bm_replacement_d2_068):
    feature = _clean(bm_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_068'] = {'inputs': ['bm_replacement_d2_068'], 'func': bm_replacement_d3_068}


def bm_replacement_d3_069(bm_replacement_d2_069):
    feature = _clean(bm_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_069'] = {'inputs': ['bm_replacement_d2_069'], 'func': bm_replacement_d3_069}


def bm_replacement_d3_070(bm_replacement_d2_070):
    feature = _clean(bm_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_070'] = {'inputs': ['bm_replacement_d2_070'], 'func': bm_replacement_d3_070}


def bm_replacement_d3_071(bm_replacement_d2_071):
    feature = _clean(bm_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_071'] = {'inputs': ['bm_replacement_d2_071'], 'func': bm_replacement_d3_071}


def bm_replacement_d3_072(bm_replacement_d2_072):
    feature = _clean(bm_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_072'] = {'inputs': ['bm_replacement_d2_072'], 'func': bm_replacement_d3_072}


def bm_replacement_d3_073(bm_replacement_d2_073):
    feature = _clean(bm_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_073'] = {'inputs': ['bm_replacement_d2_073'], 'func': bm_replacement_d3_073}


def bm_replacement_d3_074(bm_replacement_d2_074):
    feature = _clean(bm_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_074'] = {'inputs': ['bm_replacement_d2_074'], 'func': bm_replacement_d3_074}


def bm_replacement_d3_075(bm_replacement_d2_075):
    feature = _clean(bm_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_075'] = {'inputs': ['bm_replacement_d2_075'], 'func': bm_replacement_d3_075}


def bm_replacement_d3_076(bm_replacement_d2_076):
    feature = _clean(bm_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_076'] = {'inputs': ['bm_replacement_d2_076'], 'func': bm_replacement_d3_076}


def bm_replacement_d3_077(bm_replacement_d2_077):
    feature = _clean(bm_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_077'] = {'inputs': ['bm_replacement_d2_077'], 'func': bm_replacement_d3_077}


def bm_replacement_d3_078(bm_replacement_d2_078):
    feature = _clean(bm_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_078'] = {'inputs': ['bm_replacement_d2_078'], 'func': bm_replacement_d3_078}


def bm_replacement_d3_079(bm_replacement_d2_079):
    feature = _clean(bm_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_079'] = {'inputs': ['bm_replacement_d2_079'], 'func': bm_replacement_d3_079}


def bm_replacement_d3_080(bm_replacement_d2_080):
    feature = _clean(bm_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_080'] = {'inputs': ['bm_replacement_d2_080'], 'func': bm_replacement_d3_080}


def bm_replacement_d3_081(bm_replacement_d2_081):
    feature = _clean(bm_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_081'] = {'inputs': ['bm_replacement_d2_081'], 'func': bm_replacement_d3_081}


def bm_replacement_d3_082(bm_replacement_d2_082):
    feature = _clean(bm_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_082'] = {'inputs': ['bm_replacement_d2_082'], 'func': bm_replacement_d3_082}


def bm_replacement_d3_083(bm_replacement_d2_083):
    feature = _clean(bm_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_083'] = {'inputs': ['bm_replacement_d2_083'], 'func': bm_replacement_d3_083}


def bm_replacement_d3_084(bm_replacement_d2_084):
    feature = _clean(bm_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_084'] = {'inputs': ['bm_replacement_d2_084'], 'func': bm_replacement_d3_084}


def bm_replacement_d3_085(bm_replacement_d2_085):
    feature = _clean(bm_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_085'] = {'inputs': ['bm_replacement_d2_085'], 'func': bm_replacement_d3_085}


def bm_replacement_d3_086(bm_replacement_d2_086):
    feature = _clean(bm_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_086'] = {'inputs': ['bm_replacement_d2_086'], 'func': bm_replacement_d3_086}


def bm_replacement_d3_087(bm_replacement_d2_087):
    feature = _clean(bm_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_087'] = {'inputs': ['bm_replacement_d2_087'], 'func': bm_replacement_d3_087}


def bm_replacement_d3_088(bm_replacement_d2_088):
    feature = _clean(bm_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_088'] = {'inputs': ['bm_replacement_d2_088'], 'func': bm_replacement_d3_088}


def bm_replacement_d3_089(bm_replacement_d2_089):
    feature = _clean(bm_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_089'] = {'inputs': ['bm_replacement_d2_089'], 'func': bm_replacement_d3_089}


def bm_replacement_d3_090(bm_replacement_d2_090):
    feature = _clean(bm_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_090'] = {'inputs': ['bm_replacement_d2_090'], 'func': bm_replacement_d3_090}


def bm_replacement_d3_091(bm_replacement_d2_091):
    feature = _clean(bm_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_091'] = {'inputs': ['bm_replacement_d2_091'], 'func': bm_replacement_d3_091}


def bm_replacement_d3_092(bm_replacement_d2_092):
    feature = _clean(bm_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_092'] = {'inputs': ['bm_replacement_d2_092'], 'func': bm_replacement_d3_092}


def bm_replacement_d3_093(bm_replacement_d2_093):
    feature = _clean(bm_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_093'] = {'inputs': ['bm_replacement_d2_093'], 'func': bm_replacement_d3_093}


def bm_replacement_d3_094(bm_replacement_d2_094):
    feature = _clean(bm_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_094'] = {'inputs': ['bm_replacement_d2_094'], 'func': bm_replacement_d3_094}


def bm_replacement_d3_095(bm_replacement_d2_095):
    feature = _clean(bm_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_095'] = {'inputs': ['bm_replacement_d2_095'], 'func': bm_replacement_d3_095}


def bm_replacement_d3_096(bm_replacement_d2_096):
    feature = _clean(bm_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_096'] = {'inputs': ['bm_replacement_d2_096'], 'func': bm_replacement_d3_096}


def bm_replacement_d3_097(bm_replacement_d2_097):
    feature = _clean(bm_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_097'] = {'inputs': ['bm_replacement_d2_097'], 'func': bm_replacement_d3_097}


def bm_replacement_d3_098(bm_replacement_d2_098):
    feature = _clean(bm_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_098'] = {'inputs': ['bm_replacement_d2_098'], 'func': bm_replacement_d3_098}


def bm_replacement_d3_099(bm_replacement_d2_099):
    feature = _clean(bm_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_099'] = {'inputs': ['bm_replacement_d2_099'], 'func': bm_replacement_d3_099}


def bm_replacement_d3_100(bm_replacement_d2_100):
    feature = _clean(bm_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_100'] = {'inputs': ['bm_replacement_d2_100'], 'func': bm_replacement_d3_100}


def bm_replacement_d3_101(bm_replacement_d2_101):
    feature = _clean(bm_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_101'] = {'inputs': ['bm_replacement_d2_101'], 'func': bm_replacement_d3_101}


def bm_replacement_d3_102(bm_replacement_d2_102):
    feature = _clean(bm_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_102'] = {'inputs': ['bm_replacement_d2_102'], 'func': bm_replacement_d3_102}


def bm_replacement_d3_103(bm_replacement_d2_103):
    feature = _clean(bm_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_103'] = {'inputs': ['bm_replacement_d2_103'], 'func': bm_replacement_d3_103}


def bm_replacement_d3_104(bm_replacement_d2_104):
    feature = _clean(bm_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_104'] = {'inputs': ['bm_replacement_d2_104'], 'func': bm_replacement_d3_104}


def bm_replacement_d3_105(bm_replacement_d2_105):
    feature = _clean(bm_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_105'] = {'inputs': ['bm_replacement_d2_105'], 'func': bm_replacement_d3_105}


def bm_replacement_d3_106(bm_replacement_d2_106):
    feature = _clean(bm_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_106'] = {'inputs': ['bm_replacement_d2_106'], 'func': bm_replacement_d3_106}


def bm_replacement_d3_107(bm_replacement_d2_107):
    feature = _clean(bm_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_107'] = {'inputs': ['bm_replacement_d2_107'], 'func': bm_replacement_d3_107}


def bm_replacement_d3_108(bm_replacement_d2_108):
    feature = _clean(bm_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_108'] = {'inputs': ['bm_replacement_d2_108'], 'func': bm_replacement_d3_108}


def bm_replacement_d3_109(bm_replacement_d2_109):
    feature = _clean(bm_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_109'] = {'inputs': ['bm_replacement_d2_109'], 'func': bm_replacement_d3_109}


def bm_replacement_d3_110(bm_replacement_d2_110):
    feature = _clean(bm_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_110'] = {'inputs': ['bm_replacement_d2_110'], 'func': bm_replacement_d3_110}


def bm_replacement_d3_111(bm_replacement_d2_111):
    feature = _clean(bm_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_111'] = {'inputs': ['bm_replacement_d2_111'], 'func': bm_replacement_d3_111}


def bm_replacement_d3_112(bm_replacement_d2_112):
    feature = _clean(bm_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_112'] = {'inputs': ['bm_replacement_d2_112'], 'func': bm_replacement_d3_112}


def bm_replacement_d3_113(bm_replacement_d2_113):
    feature = _clean(bm_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_113'] = {'inputs': ['bm_replacement_d2_113'], 'func': bm_replacement_d3_113}


def bm_replacement_d3_114(bm_replacement_d2_114):
    feature = _clean(bm_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_114'] = {'inputs': ['bm_replacement_d2_114'], 'func': bm_replacement_d3_114}


def bm_replacement_d3_115(bm_replacement_d2_115):
    feature = _clean(bm_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_115'] = {'inputs': ['bm_replacement_d2_115'], 'func': bm_replacement_d3_115}


def bm_replacement_d3_116(bm_replacement_d2_116):
    feature = _clean(bm_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_116'] = {'inputs': ['bm_replacement_d2_116'], 'func': bm_replacement_d3_116}


def bm_replacement_d3_117(bm_replacement_d2_117):
    feature = _clean(bm_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_117'] = {'inputs': ['bm_replacement_d2_117'], 'func': bm_replacement_d3_117}


def bm_replacement_d3_118(bm_replacement_d2_118):
    feature = _clean(bm_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_118'] = {'inputs': ['bm_replacement_d2_118'], 'func': bm_replacement_d3_118}


def bm_replacement_d3_119(bm_replacement_d2_119):
    feature = _clean(bm_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_119'] = {'inputs': ['bm_replacement_d2_119'], 'func': bm_replacement_d3_119}


def bm_replacement_d3_120(bm_replacement_d2_120):
    feature = _clean(bm_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_120'] = {'inputs': ['bm_replacement_d2_120'], 'func': bm_replacement_d3_120}


def bm_replacement_d3_121(bm_replacement_d2_121):
    feature = _clean(bm_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_121'] = {'inputs': ['bm_replacement_d2_121'], 'func': bm_replacement_d3_121}


def bm_replacement_d3_122(bm_replacement_d2_122):
    feature = _clean(bm_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_122'] = {'inputs': ['bm_replacement_d2_122'], 'func': bm_replacement_d3_122}


def bm_replacement_d3_123(bm_replacement_d2_123):
    feature = _clean(bm_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_123'] = {'inputs': ['bm_replacement_d2_123'], 'func': bm_replacement_d3_123}


def bm_replacement_d3_124(bm_replacement_d2_124):
    feature = _clean(bm_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_124'] = {'inputs': ['bm_replacement_d2_124'], 'func': bm_replacement_d3_124}


def bm_replacement_d3_125(bm_replacement_d2_125):
    feature = _clean(bm_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_125'] = {'inputs': ['bm_replacement_d2_125'], 'func': bm_replacement_d3_125}


def bm_replacement_d3_126(bm_replacement_d2_126):
    feature = _clean(bm_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_126'] = {'inputs': ['bm_replacement_d2_126'], 'func': bm_replacement_d3_126}


def bm_replacement_d3_127(bm_replacement_d2_127):
    feature = _clean(bm_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_127'] = {'inputs': ['bm_replacement_d2_127'], 'func': bm_replacement_d3_127}


def bm_replacement_d3_128(bm_replacement_d2_128):
    feature = _clean(bm_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_128'] = {'inputs': ['bm_replacement_d2_128'], 'func': bm_replacement_d3_128}


def bm_replacement_d3_129(bm_replacement_d2_129):
    feature = _clean(bm_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_129'] = {'inputs': ['bm_replacement_d2_129'], 'func': bm_replacement_d3_129}


def bm_replacement_d3_130(bm_replacement_d2_130):
    feature = _clean(bm_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_130'] = {'inputs': ['bm_replacement_d2_130'], 'func': bm_replacement_d3_130}


def bm_replacement_d3_131(bm_replacement_d2_131):
    feature = _clean(bm_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_131'] = {'inputs': ['bm_replacement_d2_131'], 'func': bm_replacement_d3_131}


def bm_replacement_d3_132(bm_replacement_d2_132):
    feature = _clean(bm_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_132'] = {'inputs': ['bm_replacement_d2_132'], 'func': bm_replacement_d3_132}


def bm_replacement_d3_133(bm_replacement_d2_133):
    feature = _clean(bm_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_133'] = {'inputs': ['bm_replacement_d2_133'], 'func': bm_replacement_d3_133}


def bm_replacement_d3_134(bm_replacement_d2_134):
    feature = _clean(bm_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_134'] = {'inputs': ['bm_replacement_d2_134'], 'func': bm_replacement_d3_134}


def bm_replacement_d3_135(bm_replacement_d2_135):
    feature = _clean(bm_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_135'] = {'inputs': ['bm_replacement_d2_135'], 'func': bm_replacement_d3_135}


def bm_replacement_d3_136(bm_replacement_d2_136):
    feature = _clean(bm_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_136'] = {'inputs': ['bm_replacement_d2_136'], 'func': bm_replacement_d3_136}


def bm_replacement_d3_137(bm_replacement_d2_137):
    feature = _clean(bm_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_137'] = {'inputs': ['bm_replacement_d2_137'], 'func': bm_replacement_d3_137}


def bm_replacement_d3_138(bm_replacement_d2_138):
    feature = _clean(bm_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_138'] = {'inputs': ['bm_replacement_d2_138'], 'func': bm_replacement_d3_138}


def bm_replacement_d3_139(bm_replacement_d2_139):
    feature = _clean(bm_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_139'] = {'inputs': ['bm_replacement_d2_139'], 'func': bm_replacement_d3_139}


def bm_replacement_d3_140(bm_replacement_d2_140):
    feature = _clean(bm_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_140'] = {'inputs': ['bm_replacement_d2_140'], 'func': bm_replacement_d3_140}


def bm_replacement_d3_141(bm_replacement_d2_141):
    feature = _clean(bm_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_141'] = {'inputs': ['bm_replacement_d2_141'], 'func': bm_replacement_d3_141}


def bm_replacement_d3_142(bm_replacement_d2_142):
    feature = _clean(bm_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_142'] = {'inputs': ['bm_replacement_d2_142'], 'func': bm_replacement_d3_142}


def bm_replacement_d3_143(bm_replacement_d2_143):
    feature = _clean(bm_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_143'] = {'inputs': ['bm_replacement_d2_143'], 'func': bm_replacement_d3_143}


def bm_replacement_d3_144(bm_replacement_d2_144):
    feature = _clean(bm_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_144'] = {'inputs': ['bm_replacement_d2_144'], 'func': bm_replacement_d3_144}


def bm_replacement_d3_145(bm_replacement_d2_145):
    feature = _clean(bm_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_145'] = {'inputs': ['bm_replacement_d2_145'], 'func': bm_replacement_d3_145}


def bm_replacement_d3_146(bm_replacement_d2_146):
    feature = _clean(bm_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_146'] = {'inputs': ['bm_replacement_d2_146'], 'func': bm_replacement_d3_146}


def bm_replacement_d3_147(bm_replacement_d2_147):
    feature = _clean(bm_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_147'] = {'inputs': ['bm_replacement_d2_147'], 'func': bm_replacement_d3_147}


def bm_replacement_d3_148(bm_replacement_d2_148):
    feature = _clean(bm_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_148'] = {'inputs': ['bm_replacement_d2_148'], 'func': bm_replacement_d3_148}


def bm_replacement_d3_149(bm_replacement_d2_149):
    feature = _clean(bm_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_149'] = {'inputs': ['bm_replacement_d2_149'], 'func': bm_replacement_d3_149}


def bm_replacement_d3_150(bm_replacement_d2_150):
    feature = _clean(bm_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_150'] = {'inputs': ['bm_replacement_d2_150'], 'func': bm_replacement_d3_150}


def bm_replacement_d3_151(bm_replacement_d2_151):
    feature = _clean(bm_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_151'] = {'inputs': ['bm_replacement_d2_151'], 'func': bm_replacement_d3_151}


def bm_replacement_d3_152(bm_replacement_d2_152):
    feature = _clean(bm_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_152'] = {'inputs': ['bm_replacement_d2_152'], 'func': bm_replacement_d3_152}


def bm_replacement_d3_153(bm_replacement_d2_153):
    feature = _clean(bm_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_153'] = {'inputs': ['bm_replacement_d2_153'], 'func': bm_replacement_d3_153}


def bm_replacement_d3_154(bm_replacement_d2_154):
    feature = _clean(bm_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_154'] = {'inputs': ['bm_replacement_d2_154'], 'func': bm_replacement_d3_154}


def bm_replacement_d3_155(bm_replacement_d2_155):
    feature = _clean(bm_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_155'] = {'inputs': ['bm_replacement_d2_155'], 'func': bm_replacement_d3_155}


def bm_replacement_d3_156(bm_replacement_d2_156):
    feature = _clean(bm_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_156'] = {'inputs': ['bm_replacement_d2_156'], 'func': bm_replacement_d3_156}


def bm_replacement_d3_157(bm_replacement_d2_157):
    feature = _clean(bm_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_157'] = {'inputs': ['bm_replacement_d2_157'], 'func': bm_replacement_d3_157}


def bm_replacement_d3_158(bm_replacement_d2_158):
    feature = _clean(bm_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_158'] = {'inputs': ['bm_replacement_d2_158'], 'func': bm_replacement_d3_158}


def bm_replacement_d3_159(bm_replacement_d2_159):
    feature = _clean(bm_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_159'] = {'inputs': ['bm_replacement_d2_159'], 'func': bm_replacement_d3_159}


def bm_replacement_d3_160(bm_replacement_d2_160):
    feature = _clean(bm_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
BM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['bm_replacement_d3_160'] = {'inputs': ['bm_replacement_d2_160'], 'func': bm_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def bmf_base_universe_d3_001_bmf_002_gap_magnitude_10_002(bmf_base_universe_d2_001_bmf_002_gap_magnitude_10_002):
    return _base_universe_d3(bmf_base_universe_d2_001_bmf_002_gap_magnitude_10_002, 1)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_001_bmf_002_gap_magnitude_10_002'] = {'inputs': ['bmf_base_universe_d2_001_bmf_002_gap_magnitude_10_002'], 'func': bmf_base_universe_d3_001_bmf_002_gap_magnitude_10_002}


def bmf_base_universe_d3_002_bmf_003_open_close_pressure_21_003(bmf_base_universe_d2_002_bmf_003_open_close_pressure_21_003):
    return _base_universe_d3(bmf_base_universe_d2_002_bmf_003_open_close_pressure_21_003, 2)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_002_bmf_003_open_close_pressure_21_003'] = {'inputs': ['bmf_base_universe_d2_002_bmf_003_open_close_pressure_21_003'], 'func': bmf_base_universe_d3_002_bmf_003_open_close_pressure_21_003}


def bmf_base_universe_d3_003_bmf_004_lower_wick_ratio_42_004(bmf_base_universe_d2_003_bmf_004_lower_wick_ratio_42_004):
    return _base_universe_d3(bmf_base_universe_d2_003_bmf_004_lower_wick_ratio_42_004, 3)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_003_bmf_004_lower_wick_ratio_42_004'] = {'inputs': ['bmf_base_universe_d2_003_bmf_004_lower_wick_ratio_42_004'], 'func': bmf_base_universe_d3_003_bmf_004_lower_wick_ratio_42_004}


def bmf_base_universe_d3_004_bmf_005_upper_wick_ratio_63_005(bmf_base_universe_d2_004_bmf_005_upper_wick_ratio_63_005):
    return _base_universe_d3(bmf_base_universe_d2_004_bmf_005_upper_wick_ratio_63_005, 4)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_004_bmf_005_upper_wick_ratio_63_005'] = {'inputs': ['bmf_base_universe_d2_004_bmf_005_upper_wick_ratio_63_005'], 'func': bmf_base_universe_d3_004_bmf_005_upper_wick_ratio_63_005}


def bmf_base_universe_d3_005_bmf_006_body_to_range_84_006(bmf_base_universe_d2_005_bmf_006_body_to_range_84_006):
    return _base_universe_d3(bmf_base_universe_d2_005_bmf_006_body_to_range_84_006, 5)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_005_bmf_006_body_to_range_84_006'] = {'inputs': ['bmf_base_universe_d2_005_bmf_006_body_to_range_84_006'], 'func': bmf_base_universe_d3_005_bmf_006_body_to_range_84_006}


def bmf_base_universe_d3_006_bmf_008_gap_magnitude_189_008(bmf_base_universe_d2_006_bmf_008_gap_magnitude_189_008):
    return _base_universe_d3(bmf_base_universe_d2_006_bmf_008_gap_magnitude_189_008, 6)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_006_bmf_008_gap_magnitude_189_008'] = {'inputs': ['bmf_base_universe_d2_006_bmf_008_gap_magnitude_189_008'], 'func': bmf_base_universe_d3_006_bmf_008_gap_magnitude_189_008}


def bmf_base_universe_d3_007_bmf_009_open_close_pressure_252_009(bmf_base_universe_d2_007_bmf_009_open_close_pressure_252_009):
    return _base_universe_d3(bmf_base_universe_d2_007_bmf_009_open_close_pressure_252_009, 7)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_007_bmf_009_open_close_pressure_252_009'] = {'inputs': ['bmf_base_universe_d2_007_bmf_009_open_close_pressure_252_009'], 'func': bmf_base_universe_d3_007_bmf_009_open_close_pressure_252_009}


def bmf_base_universe_d3_008_bmf_010_lower_wick_ratio_378_010(bmf_base_universe_d2_008_bmf_010_lower_wick_ratio_378_010):
    return _base_universe_d3(bmf_base_universe_d2_008_bmf_010_lower_wick_ratio_378_010, 8)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_008_bmf_010_lower_wick_ratio_378_010'] = {'inputs': ['bmf_base_universe_d2_008_bmf_010_lower_wick_ratio_378_010'], 'func': bmf_base_universe_d3_008_bmf_010_lower_wick_ratio_378_010}


def bmf_base_universe_d3_009_bmf_011_upper_wick_ratio_504_011(bmf_base_universe_d2_009_bmf_011_upper_wick_ratio_504_011):
    return _base_universe_d3(bmf_base_universe_d2_009_bmf_011_upper_wick_ratio_504_011, 9)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_009_bmf_011_upper_wick_ratio_504_011'] = {'inputs': ['bmf_base_universe_d2_009_bmf_011_upper_wick_ratio_504_011'], 'func': bmf_base_universe_d3_009_bmf_011_upper_wick_ratio_504_011}


def bmf_base_universe_d3_010_bmf_012_body_to_range_756_012(bmf_base_universe_d2_010_bmf_012_body_to_range_756_012):
    return _base_universe_d3(bmf_base_universe_d2_010_bmf_012_body_to_range_756_012, 10)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_010_bmf_012_body_to_range_756_012'] = {'inputs': ['bmf_base_universe_d2_010_bmf_012_body_to_range_756_012'], 'func': bmf_base_universe_d3_010_bmf_012_body_to_range_756_012}


def bmf_base_universe_d3_011_bmf_014_gap_magnitude_1260_014(bmf_base_universe_d2_011_bmf_014_gap_magnitude_1260_014):
    return _base_universe_d3(bmf_base_universe_d2_011_bmf_014_gap_magnitude_1260_014, 11)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_011_bmf_014_gap_magnitude_1260_014'] = {'inputs': ['bmf_base_universe_d2_011_bmf_014_gap_magnitude_1260_014'], 'func': bmf_base_universe_d3_011_bmf_014_gap_magnitude_1260_014}


def bmf_base_universe_d3_012_bmf_015_open_close_pressure_1512_015(bmf_base_universe_d2_012_bmf_015_open_close_pressure_1512_015):
    return _base_universe_d3(bmf_base_universe_d2_012_bmf_015_open_close_pressure_1512_015, 12)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_012_bmf_015_open_close_pressure_1512_015'] = {'inputs': ['bmf_base_universe_d2_012_bmf_015_open_close_pressure_1512_015'], 'func': bmf_base_universe_d3_012_bmf_015_open_close_pressure_1512_015}


def bmf_base_universe_d3_013_bmf_016_lower_wick_ratio_5_016(bmf_base_universe_d2_013_bmf_016_lower_wick_ratio_5_016):
    return _base_universe_d3(bmf_base_universe_d2_013_bmf_016_lower_wick_ratio_5_016, 13)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_013_bmf_016_lower_wick_ratio_5_016'] = {'inputs': ['bmf_base_universe_d2_013_bmf_016_lower_wick_ratio_5_016'], 'func': bmf_base_universe_d3_013_bmf_016_lower_wick_ratio_5_016}


def bmf_base_universe_d3_014_bmf_017_upper_wick_ratio_10_017(bmf_base_universe_d2_014_bmf_017_upper_wick_ratio_10_017):
    return _base_universe_d3(bmf_base_universe_d2_014_bmf_017_upper_wick_ratio_10_017, 14)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_014_bmf_017_upper_wick_ratio_10_017'] = {'inputs': ['bmf_base_universe_d2_014_bmf_017_upper_wick_ratio_10_017'], 'func': bmf_base_universe_d3_014_bmf_017_upper_wick_ratio_10_017}


def bmf_base_universe_d3_015_bmf_018_body_to_range_21_018(bmf_base_universe_d2_015_bmf_018_body_to_range_21_018):
    return _base_universe_d3(bmf_base_universe_d2_015_bmf_018_body_to_range_21_018, 15)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_015_bmf_018_body_to_range_21_018'] = {'inputs': ['bmf_base_universe_d2_015_bmf_018_body_to_range_21_018'], 'func': bmf_base_universe_d3_015_bmf_018_body_to_range_21_018}


def bmf_base_universe_d3_016_bmf_020_gap_magnitude_63_020(bmf_base_universe_d2_016_bmf_020_gap_magnitude_63_020):
    return _base_universe_d3(bmf_base_universe_d2_016_bmf_020_gap_magnitude_63_020, 16)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_016_bmf_020_gap_magnitude_63_020'] = {'inputs': ['bmf_base_universe_d2_016_bmf_020_gap_magnitude_63_020'], 'func': bmf_base_universe_d3_016_bmf_020_gap_magnitude_63_020}


def bmf_base_universe_d3_017_bmf_021_open_close_pressure_84_021(bmf_base_universe_d2_017_bmf_021_open_close_pressure_84_021):
    return _base_universe_d3(bmf_base_universe_d2_017_bmf_021_open_close_pressure_84_021, 17)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_017_bmf_021_open_close_pressure_84_021'] = {'inputs': ['bmf_base_universe_d2_017_bmf_021_open_close_pressure_84_021'], 'func': bmf_base_universe_d3_017_bmf_021_open_close_pressure_84_021}


def bmf_base_universe_d3_018_bmf_022_lower_wick_ratio_126_022(bmf_base_universe_d2_018_bmf_022_lower_wick_ratio_126_022):
    return _base_universe_d3(bmf_base_universe_d2_018_bmf_022_lower_wick_ratio_126_022, 18)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_018_bmf_022_lower_wick_ratio_126_022'] = {'inputs': ['bmf_base_universe_d2_018_bmf_022_lower_wick_ratio_126_022'], 'func': bmf_base_universe_d3_018_bmf_022_lower_wick_ratio_126_022}


def bmf_base_universe_d3_019_bmf_023_upper_wick_ratio_189_023(bmf_base_universe_d2_019_bmf_023_upper_wick_ratio_189_023):
    return _base_universe_d3(bmf_base_universe_d2_019_bmf_023_upper_wick_ratio_189_023, 19)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_019_bmf_023_upper_wick_ratio_189_023'] = {'inputs': ['bmf_base_universe_d2_019_bmf_023_upper_wick_ratio_189_023'], 'func': bmf_base_universe_d3_019_bmf_023_upper_wick_ratio_189_023}


def bmf_base_universe_d3_020_bmf_024_body_to_range_252_024(bmf_base_universe_d2_020_bmf_024_body_to_range_252_024):
    return _base_universe_d3(bmf_base_universe_d2_020_bmf_024_body_to_range_252_024, 20)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_020_bmf_024_body_to_range_252_024'] = {'inputs': ['bmf_base_universe_d2_020_bmf_024_body_to_range_252_024'], 'func': bmf_base_universe_d3_020_bmf_024_body_to_range_252_024}


def bmf_base_universe_d3_021_bmf_026_gap_magnitude_504_026(bmf_base_universe_d2_021_bmf_026_gap_magnitude_504_026):
    return _base_universe_d3(bmf_base_universe_d2_021_bmf_026_gap_magnitude_504_026, 21)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_021_bmf_026_gap_magnitude_504_026'] = {'inputs': ['bmf_base_universe_d2_021_bmf_026_gap_magnitude_504_026'], 'func': bmf_base_universe_d3_021_bmf_026_gap_magnitude_504_026}


def bmf_base_universe_d3_022_bmf_027_open_close_pressure_756_027(bmf_base_universe_d2_022_bmf_027_open_close_pressure_756_027):
    return _base_universe_d3(bmf_base_universe_d2_022_bmf_027_open_close_pressure_756_027, 22)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_022_bmf_027_open_close_pressure_756_027'] = {'inputs': ['bmf_base_universe_d2_022_bmf_027_open_close_pressure_756_027'], 'func': bmf_base_universe_d3_022_bmf_027_open_close_pressure_756_027}


def bmf_base_universe_d3_023_bmf_028_lower_wick_ratio_1008_028(bmf_base_universe_d2_023_bmf_028_lower_wick_ratio_1008_028):
    return _base_universe_d3(bmf_base_universe_d2_023_bmf_028_lower_wick_ratio_1008_028, 23)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_023_bmf_028_lower_wick_ratio_1008_028'] = {'inputs': ['bmf_base_universe_d2_023_bmf_028_lower_wick_ratio_1008_028'], 'func': bmf_base_universe_d3_023_bmf_028_lower_wick_ratio_1008_028}


def bmf_base_universe_d3_024_bmf_029_upper_wick_ratio_1260_029(bmf_base_universe_d2_024_bmf_029_upper_wick_ratio_1260_029):
    return _base_universe_d3(bmf_base_universe_d2_024_bmf_029_upper_wick_ratio_1260_029, 24)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_024_bmf_029_upper_wick_ratio_1260_029'] = {'inputs': ['bmf_base_universe_d2_024_bmf_029_upper_wick_ratio_1260_029'], 'func': bmf_base_universe_d3_024_bmf_029_upper_wick_ratio_1260_029}


def bmf_base_universe_d3_025_bmf_030_body_to_range_1512_030(bmf_base_universe_d2_025_bmf_030_body_to_range_1512_030):
    return _base_universe_d3(bmf_base_universe_d2_025_bmf_030_body_to_range_1512_030, 25)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_025_bmf_030_body_to_range_1512_030'] = {'inputs': ['bmf_base_universe_d2_025_bmf_030_body_to_range_1512_030'], 'func': bmf_base_universe_d3_025_bmf_030_body_to_range_1512_030}


def bmf_base_universe_d3_026_bmf_basefill_031(bmf_base_universe_d2_026_bmf_basefill_031):
    return _base_universe_d3(bmf_base_universe_d2_026_bmf_basefill_031, 26)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_026_bmf_basefill_031'] = {'inputs': ['bmf_base_universe_d2_026_bmf_basefill_031'], 'func': bmf_base_universe_d3_026_bmf_basefill_031}


def bmf_base_universe_d3_027_bmf_basefill_032(bmf_base_universe_d2_027_bmf_basefill_032):
    return _base_universe_d3(bmf_base_universe_d2_027_bmf_basefill_032, 27)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_027_bmf_basefill_032'] = {'inputs': ['bmf_base_universe_d2_027_bmf_basefill_032'], 'func': bmf_base_universe_d3_027_bmf_basefill_032}


def bmf_base_universe_d3_028_bmf_basefill_033(bmf_base_universe_d2_028_bmf_basefill_033):
    return _base_universe_d3(bmf_base_universe_d2_028_bmf_basefill_033, 28)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_028_bmf_basefill_033'] = {'inputs': ['bmf_base_universe_d2_028_bmf_basefill_033'], 'func': bmf_base_universe_d3_028_bmf_basefill_033}


def bmf_base_universe_d3_029_bmf_basefill_034(bmf_base_universe_d2_029_bmf_basefill_034):
    return _base_universe_d3(bmf_base_universe_d2_029_bmf_basefill_034, 29)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_029_bmf_basefill_034'] = {'inputs': ['bmf_base_universe_d2_029_bmf_basefill_034'], 'func': bmf_base_universe_d3_029_bmf_basefill_034}


def bmf_base_universe_d3_030_bmf_basefill_035(bmf_base_universe_d2_030_bmf_basefill_035):
    return _base_universe_d3(bmf_base_universe_d2_030_bmf_basefill_035, 30)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_030_bmf_basefill_035'] = {'inputs': ['bmf_base_universe_d2_030_bmf_basefill_035'], 'func': bmf_base_universe_d3_030_bmf_basefill_035}


def bmf_base_universe_d3_031_bmf_basefill_036(bmf_base_universe_d2_031_bmf_basefill_036):
    return _base_universe_d3(bmf_base_universe_d2_031_bmf_basefill_036, 31)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_031_bmf_basefill_036'] = {'inputs': ['bmf_base_universe_d2_031_bmf_basefill_036'], 'func': bmf_base_universe_d3_031_bmf_basefill_036}


def bmf_base_universe_d3_032_bmf_basefill_037(bmf_base_universe_d2_032_bmf_basefill_037):
    return _base_universe_d3(bmf_base_universe_d2_032_bmf_basefill_037, 32)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_032_bmf_basefill_037'] = {'inputs': ['bmf_base_universe_d2_032_bmf_basefill_037'], 'func': bmf_base_universe_d3_032_bmf_basefill_037}


def bmf_base_universe_d3_033_bmf_basefill_038(bmf_base_universe_d2_033_bmf_basefill_038):
    return _base_universe_d3(bmf_base_universe_d2_033_bmf_basefill_038, 33)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_033_bmf_basefill_038'] = {'inputs': ['bmf_base_universe_d2_033_bmf_basefill_038'], 'func': bmf_base_universe_d3_033_bmf_basefill_038}


def bmf_base_universe_d3_034_bmf_basefill_039(bmf_base_universe_d2_034_bmf_basefill_039):
    return _base_universe_d3(bmf_base_universe_d2_034_bmf_basefill_039, 34)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_034_bmf_basefill_039'] = {'inputs': ['bmf_base_universe_d2_034_bmf_basefill_039'], 'func': bmf_base_universe_d3_034_bmf_basefill_039}


def bmf_base_universe_d3_035_bmf_basefill_040(bmf_base_universe_d2_035_bmf_basefill_040):
    return _base_universe_d3(bmf_base_universe_d2_035_bmf_basefill_040, 35)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_035_bmf_basefill_040'] = {'inputs': ['bmf_base_universe_d2_035_bmf_basefill_040'], 'func': bmf_base_universe_d3_035_bmf_basefill_040}


def bmf_base_universe_d3_036_bmf_basefill_041(bmf_base_universe_d2_036_bmf_basefill_041):
    return _base_universe_d3(bmf_base_universe_d2_036_bmf_basefill_041, 36)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_036_bmf_basefill_041'] = {'inputs': ['bmf_base_universe_d2_036_bmf_basefill_041'], 'func': bmf_base_universe_d3_036_bmf_basefill_041}


def bmf_base_universe_d3_037_bmf_basefill_042(bmf_base_universe_d2_037_bmf_basefill_042):
    return _base_universe_d3(bmf_base_universe_d2_037_bmf_basefill_042, 37)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_037_bmf_basefill_042'] = {'inputs': ['bmf_base_universe_d2_037_bmf_basefill_042'], 'func': bmf_base_universe_d3_037_bmf_basefill_042}


def bmf_base_universe_d3_038_bmf_basefill_043(bmf_base_universe_d2_038_bmf_basefill_043):
    return _base_universe_d3(bmf_base_universe_d2_038_bmf_basefill_043, 38)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_038_bmf_basefill_043'] = {'inputs': ['bmf_base_universe_d2_038_bmf_basefill_043'], 'func': bmf_base_universe_d3_038_bmf_basefill_043}


def bmf_base_universe_d3_039_bmf_basefill_044(bmf_base_universe_d2_039_bmf_basefill_044):
    return _base_universe_d3(bmf_base_universe_d2_039_bmf_basefill_044, 39)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_039_bmf_basefill_044'] = {'inputs': ['bmf_base_universe_d2_039_bmf_basefill_044'], 'func': bmf_base_universe_d3_039_bmf_basefill_044}


def bmf_base_universe_d3_040_bmf_basefill_045(bmf_base_universe_d2_040_bmf_basefill_045):
    return _base_universe_d3(bmf_base_universe_d2_040_bmf_basefill_045, 40)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_040_bmf_basefill_045'] = {'inputs': ['bmf_base_universe_d2_040_bmf_basefill_045'], 'func': bmf_base_universe_d3_040_bmf_basefill_045}


def bmf_base_universe_d3_041_bmf_basefill_046(bmf_base_universe_d2_041_bmf_basefill_046):
    return _base_universe_d3(bmf_base_universe_d2_041_bmf_basefill_046, 41)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_041_bmf_basefill_046'] = {'inputs': ['bmf_base_universe_d2_041_bmf_basefill_046'], 'func': bmf_base_universe_d3_041_bmf_basefill_046}


def bmf_base_universe_d3_042_bmf_basefill_047(bmf_base_universe_d2_042_bmf_basefill_047):
    return _base_universe_d3(bmf_base_universe_d2_042_bmf_basefill_047, 42)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_042_bmf_basefill_047'] = {'inputs': ['bmf_base_universe_d2_042_bmf_basefill_047'], 'func': bmf_base_universe_d3_042_bmf_basefill_047}


def bmf_base_universe_d3_043_bmf_basefill_048(bmf_base_universe_d2_043_bmf_basefill_048):
    return _base_universe_d3(bmf_base_universe_d2_043_bmf_basefill_048, 43)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_043_bmf_basefill_048'] = {'inputs': ['bmf_base_universe_d2_043_bmf_basefill_048'], 'func': bmf_base_universe_d3_043_bmf_basefill_048}


def bmf_base_universe_d3_044_bmf_basefill_049(bmf_base_universe_d2_044_bmf_basefill_049):
    return _base_universe_d3(bmf_base_universe_d2_044_bmf_basefill_049, 44)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_044_bmf_basefill_049'] = {'inputs': ['bmf_base_universe_d2_044_bmf_basefill_049'], 'func': bmf_base_universe_d3_044_bmf_basefill_049}


def bmf_base_universe_d3_045_bmf_basefill_050(bmf_base_universe_d2_045_bmf_basefill_050):
    return _base_universe_d3(bmf_base_universe_d2_045_bmf_basefill_050, 45)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_045_bmf_basefill_050'] = {'inputs': ['bmf_base_universe_d2_045_bmf_basefill_050'], 'func': bmf_base_universe_d3_045_bmf_basefill_050}


def bmf_base_universe_d3_046_bmf_basefill_051(bmf_base_universe_d2_046_bmf_basefill_051):
    return _base_universe_d3(bmf_base_universe_d2_046_bmf_basefill_051, 46)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_046_bmf_basefill_051'] = {'inputs': ['bmf_base_universe_d2_046_bmf_basefill_051'], 'func': bmf_base_universe_d3_046_bmf_basefill_051}


def bmf_base_universe_d3_047_bmf_basefill_052(bmf_base_universe_d2_047_bmf_basefill_052):
    return _base_universe_d3(bmf_base_universe_d2_047_bmf_basefill_052, 47)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_047_bmf_basefill_052'] = {'inputs': ['bmf_base_universe_d2_047_bmf_basefill_052'], 'func': bmf_base_universe_d3_047_bmf_basefill_052}


def bmf_base_universe_d3_048_bmf_basefill_053(bmf_base_universe_d2_048_bmf_basefill_053):
    return _base_universe_d3(bmf_base_universe_d2_048_bmf_basefill_053, 48)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_048_bmf_basefill_053'] = {'inputs': ['bmf_base_universe_d2_048_bmf_basefill_053'], 'func': bmf_base_universe_d3_048_bmf_basefill_053}


def bmf_base_universe_d3_049_bmf_basefill_054(bmf_base_universe_d2_049_bmf_basefill_054):
    return _base_universe_d3(bmf_base_universe_d2_049_bmf_basefill_054, 49)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_049_bmf_basefill_054'] = {'inputs': ['bmf_base_universe_d2_049_bmf_basefill_054'], 'func': bmf_base_universe_d3_049_bmf_basefill_054}


def bmf_base_universe_d3_050_bmf_basefill_055(bmf_base_universe_d2_050_bmf_basefill_055):
    return _base_universe_d3(bmf_base_universe_d2_050_bmf_basefill_055, 50)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_050_bmf_basefill_055'] = {'inputs': ['bmf_base_universe_d2_050_bmf_basefill_055'], 'func': bmf_base_universe_d3_050_bmf_basefill_055}


def bmf_base_universe_d3_051_bmf_basefill_056(bmf_base_universe_d2_051_bmf_basefill_056):
    return _base_universe_d3(bmf_base_universe_d2_051_bmf_basefill_056, 51)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_051_bmf_basefill_056'] = {'inputs': ['bmf_base_universe_d2_051_bmf_basefill_056'], 'func': bmf_base_universe_d3_051_bmf_basefill_056}


def bmf_base_universe_d3_052_bmf_basefill_057(bmf_base_universe_d2_052_bmf_basefill_057):
    return _base_universe_d3(bmf_base_universe_d2_052_bmf_basefill_057, 52)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_052_bmf_basefill_057'] = {'inputs': ['bmf_base_universe_d2_052_bmf_basefill_057'], 'func': bmf_base_universe_d3_052_bmf_basefill_057}


def bmf_base_universe_d3_053_bmf_basefill_058(bmf_base_universe_d2_053_bmf_basefill_058):
    return _base_universe_d3(bmf_base_universe_d2_053_bmf_basefill_058, 53)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_053_bmf_basefill_058'] = {'inputs': ['bmf_base_universe_d2_053_bmf_basefill_058'], 'func': bmf_base_universe_d3_053_bmf_basefill_058}


def bmf_base_universe_d3_054_bmf_basefill_059(bmf_base_universe_d2_054_bmf_basefill_059):
    return _base_universe_d3(bmf_base_universe_d2_054_bmf_basefill_059, 54)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_054_bmf_basefill_059'] = {'inputs': ['bmf_base_universe_d2_054_bmf_basefill_059'], 'func': bmf_base_universe_d3_054_bmf_basefill_059}


def bmf_base_universe_d3_055_bmf_basefill_060(bmf_base_universe_d2_055_bmf_basefill_060):
    return _base_universe_d3(bmf_base_universe_d2_055_bmf_basefill_060, 55)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_055_bmf_basefill_060'] = {'inputs': ['bmf_base_universe_d2_055_bmf_basefill_060'], 'func': bmf_base_universe_d3_055_bmf_basefill_060}


def bmf_base_universe_d3_056_bmf_basefill_061(bmf_base_universe_d2_056_bmf_basefill_061):
    return _base_universe_d3(bmf_base_universe_d2_056_bmf_basefill_061, 56)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_056_bmf_basefill_061'] = {'inputs': ['bmf_base_universe_d2_056_bmf_basefill_061'], 'func': bmf_base_universe_d3_056_bmf_basefill_061}


def bmf_base_universe_d3_057_bmf_basefill_062(bmf_base_universe_d2_057_bmf_basefill_062):
    return _base_universe_d3(bmf_base_universe_d2_057_bmf_basefill_062, 57)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_057_bmf_basefill_062'] = {'inputs': ['bmf_base_universe_d2_057_bmf_basefill_062'], 'func': bmf_base_universe_d3_057_bmf_basefill_062}


def bmf_base_universe_d3_058_bmf_basefill_063(bmf_base_universe_d2_058_bmf_basefill_063):
    return _base_universe_d3(bmf_base_universe_d2_058_bmf_basefill_063, 58)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_058_bmf_basefill_063'] = {'inputs': ['bmf_base_universe_d2_058_bmf_basefill_063'], 'func': bmf_base_universe_d3_058_bmf_basefill_063}


def bmf_base_universe_d3_059_bmf_basefill_064(bmf_base_universe_d2_059_bmf_basefill_064):
    return _base_universe_d3(bmf_base_universe_d2_059_bmf_basefill_064, 59)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_059_bmf_basefill_064'] = {'inputs': ['bmf_base_universe_d2_059_bmf_basefill_064'], 'func': bmf_base_universe_d3_059_bmf_basefill_064}


def bmf_base_universe_d3_060_bmf_basefill_065(bmf_base_universe_d2_060_bmf_basefill_065):
    return _base_universe_d3(bmf_base_universe_d2_060_bmf_basefill_065, 60)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_060_bmf_basefill_065'] = {'inputs': ['bmf_base_universe_d2_060_bmf_basefill_065'], 'func': bmf_base_universe_d3_060_bmf_basefill_065}


def bmf_base_universe_d3_061_bmf_basefill_066(bmf_base_universe_d2_061_bmf_basefill_066):
    return _base_universe_d3(bmf_base_universe_d2_061_bmf_basefill_066, 61)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_061_bmf_basefill_066'] = {'inputs': ['bmf_base_universe_d2_061_bmf_basefill_066'], 'func': bmf_base_universe_d3_061_bmf_basefill_066}


def bmf_base_universe_d3_062_bmf_basefill_067(bmf_base_universe_d2_062_bmf_basefill_067):
    return _base_universe_d3(bmf_base_universe_d2_062_bmf_basefill_067, 62)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_062_bmf_basefill_067'] = {'inputs': ['bmf_base_universe_d2_062_bmf_basefill_067'], 'func': bmf_base_universe_d3_062_bmf_basefill_067}


def bmf_base_universe_d3_063_bmf_basefill_068(bmf_base_universe_d2_063_bmf_basefill_068):
    return _base_universe_d3(bmf_base_universe_d2_063_bmf_basefill_068, 63)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_063_bmf_basefill_068'] = {'inputs': ['bmf_base_universe_d2_063_bmf_basefill_068'], 'func': bmf_base_universe_d3_063_bmf_basefill_068}


def bmf_base_universe_d3_064_bmf_basefill_069(bmf_base_universe_d2_064_bmf_basefill_069):
    return _base_universe_d3(bmf_base_universe_d2_064_bmf_basefill_069, 64)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_064_bmf_basefill_069'] = {'inputs': ['bmf_base_universe_d2_064_bmf_basefill_069'], 'func': bmf_base_universe_d3_064_bmf_basefill_069}


def bmf_base_universe_d3_065_bmf_basefill_070(bmf_base_universe_d2_065_bmf_basefill_070):
    return _base_universe_d3(bmf_base_universe_d2_065_bmf_basefill_070, 65)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_065_bmf_basefill_070'] = {'inputs': ['bmf_base_universe_d2_065_bmf_basefill_070'], 'func': bmf_base_universe_d3_065_bmf_basefill_070}


def bmf_base_universe_d3_066_bmf_basefill_071(bmf_base_universe_d2_066_bmf_basefill_071):
    return _base_universe_d3(bmf_base_universe_d2_066_bmf_basefill_071, 66)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_066_bmf_basefill_071'] = {'inputs': ['bmf_base_universe_d2_066_bmf_basefill_071'], 'func': bmf_base_universe_d3_066_bmf_basefill_071}


def bmf_base_universe_d3_067_bmf_basefill_072(bmf_base_universe_d2_067_bmf_basefill_072):
    return _base_universe_d3(bmf_base_universe_d2_067_bmf_basefill_072, 67)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_067_bmf_basefill_072'] = {'inputs': ['bmf_base_universe_d2_067_bmf_basefill_072'], 'func': bmf_base_universe_d3_067_bmf_basefill_072}


def bmf_base_universe_d3_068_bmf_basefill_073(bmf_base_universe_d2_068_bmf_basefill_073):
    return _base_universe_d3(bmf_base_universe_d2_068_bmf_basefill_073, 68)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_068_bmf_basefill_073'] = {'inputs': ['bmf_base_universe_d2_068_bmf_basefill_073'], 'func': bmf_base_universe_d3_068_bmf_basefill_073}


def bmf_base_universe_d3_069_bmf_basefill_074(bmf_base_universe_d2_069_bmf_basefill_074):
    return _base_universe_d3(bmf_base_universe_d2_069_bmf_basefill_074, 69)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_069_bmf_basefill_074'] = {'inputs': ['bmf_base_universe_d2_069_bmf_basefill_074'], 'func': bmf_base_universe_d3_069_bmf_basefill_074}


def bmf_base_universe_d3_070_bmf_basefill_075(bmf_base_universe_d2_070_bmf_basefill_075):
    return _base_universe_d3(bmf_base_universe_d2_070_bmf_basefill_075, 70)
BMF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['bmf_base_universe_d3_070_bmf_basefill_075'] = {'inputs': ['bmf_base_universe_d2_070_bmf_basefill_075'], 'func': bmf_base_universe_d3_070_bmf_basefill_075}

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



def swk_176_swk_001_gap_down_frequency_5_001_accel_1(swk_151_swk_001_gap_down_frequency_5_001_roc_1):
    feature = _s(swk_151_swk_001_gap_down_frequency_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def swk_177_swk_007_gap_down_frequency_126_007_accel_5(swk_152_swk_007_gap_down_frequency_126_007_roc_5):
    feature = _s(swk_152_swk_007_gap_down_frequency_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def swk_178_swk_013_gap_down_frequency_1008_013_accel_42(swk_153_swk_013_gap_down_frequency_1008_013_roc_42):
    feature = _s(swk_153_swk_013_gap_down_frequency_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def swk_179_swk_019_gap_down_frequency_42_019_accel_126(swk_154_swk_019_gap_down_frequency_42_019_roc_126):
    feature = _s(swk_154_swk_019_gap_down_frequency_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def swk_180_swk_025_gap_down_frequency_378_025_accel_378(swk_155_swk_025_gap_down_frequency_378_025_roc_378):
    feature = _s(swk_155_swk_025_gap_down_frequency_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















SHADOW_WICK_ANALYSIS_REGISTRY_3RD_DERIVATIVES = {
    'swk_176_swk_001_gap_down_frequency_5_001_accel_1': {'inputs': ['swk_151_swk_001_gap_down_frequency_5_001_roc_1'], 'func': swk_176_swk_001_gap_down_frequency_5_001_accel_1},
    'swk_177_swk_007_gap_down_frequency_126_007_accel_5': {'inputs': ['swk_152_swk_007_gap_down_frequency_126_007_roc_5'], 'func': swk_177_swk_007_gap_down_frequency_126_007_accel_5},
    'swk_178_swk_013_gap_down_frequency_1008_013_accel_42': {'inputs': ['swk_153_swk_013_gap_down_frequency_1008_013_roc_42'], 'func': swk_178_swk_013_gap_down_frequency_1008_013_accel_42},
    'swk_179_swk_019_gap_down_frequency_42_019_accel_126': {'inputs': ['swk_154_swk_019_gap_down_frequency_42_019_roc_126'], 'func': swk_179_swk_019_gap_down_frequency_42_019_accel_126},
    'swk_180_swk_025_gap_down_frequency_378_025_accel_378': {'inputs': ['swk_155_swk_025_gap_down_frequency_378_025_roc_378'], 'func': swk_180_swk_025_gap_down_frequency_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def swa_replacement_d3_001(swa_replacement_d2_001):
    feature = _clean(swa_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_001'] = {'inputs': ['swa_replacement_d2_001'], 'func': swa_replacement_d3_001}


def swa_replacement_d3_002(swa_replacement_d2_002):
    feature = _clean(swa_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_002'] = {'inputs': ['swa_replacement_d2_002'], 'func': swa_replacement_d3_002}


def swa_replacement_d3_003(swa_replacement_d2_003):
    feature = _clean(swa_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_003'] = {'inputs': ['swa_replacement_d2_003'], 'func': swa_replacement_d3_003}


def swa_replacement_d3_004(swa_replacement_d2_004):
    feature = _clean(swa_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_004'] = {'inputs': ['swa_replacement_d2_004'], 'func': swa_replacement_d3_004}


def swa_replacement_d3_005(swa_replacement_d2_005):
    feature = _clean(swa_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_005'] = {'inputs': ['swa_replacement_d2_005'], 'func': swa_replacement_d3_005}


def swa_replacement_d3_006(swa_replacement_d2_006):
    feature = _clean(swa_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_006'] = {'inputs': ['swa_replacement_d2_006'], 'func': swa_replacement_d3_006}


def swa_replacement_d3_007(swa_replacement_d2_007):
    feature = _clean(swa_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_007'] = {'inputs': ['swa_replacement_d2_007'], 'func': swa_replacement_d3_007}


def swa_replacement_d3_008(swa_replacement_d2_008):
    feature = _clean(swa_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_008'] = {'inputs': ['swa_replacement_d2_008'], 'func': swa_replacement_d3_008}


def swa_replacement_d3_009(swa_replacement_d2_009):
    feature = _clean(swa_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_009'] = {'inputs': ['swa_replacement_d2_009'], 'func': swa_replacement_d3_009}


def swa_replacement_d3_010(swa_replacement_d2_010):
    feature = _clean(swa_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_010'] = {'inputs': ['swa_replacement_d2_010'], 'func': swa_replacement_d3_010}


def swa_replacement_d3_011(swa_replacement_d2_011):
    feature = _clean(swa_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_011'] = {'inputs': ['swa_replacement_d2_011'], 'func': swa_replacement_d3_011}


def swa_replacement_d3_012(swa_replacement_d2_012):
    feature = _clean(swa_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_012'] = {'inputs': ['swa_replacement_d2_012'], 'func': swa_replacement_d3_012}


def swa_replacement_d3_013(swa_replacement_d2_013):
    feature = _clean(swa_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_013'] = {'inputs': ['swa_replacement_d2_013'], 'func': swa_replacement_d3_013}


def swa_replacement_d3_014(swa_replacement_d2_014):
    feature = _clean(swa_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_014'] = {'inputs': ['swa_replacement_d2_014'], 'func': swa_replacement_d3_014}


def swa_replacement_d3_015(swa_replacement_d2_015):
    feature = _clean(swa_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_015'] = {'inputs': ['swa_replacement_d2_015'], 'func': swa_replacement_d3_015}


def swa_replacement_d3_016(swa_replacement_d2_016):
    feature = _clean(swa_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_016'] = {'inputs': ['swa_replacement_d2_016'], 'func': swa_replacement_d3_016}


def swa_replacement_d3_017(swa_replacement_d2_017):
    feature = _clean(swa_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_017'] = {'inputs': ['swa_replacement_d2_017'], 'func': swa_replacement_d3_017}


def swa_replacement_d3_018(swa_replacement_d2_018):
    feature = _clean(swa_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_018'] = {'inputs': ['swa_replacement_d2_018'], 'func': swa_replacement_d3_018}


def swa_replacement_d3_019(swa_replacement_d2_019):
    feature = _clean(swa_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_019'] = {'inputs': ['swa_replacement_d2_019'], 'func': swa_replacement_d3_019}


def swa_replacement_d3_020(swa_replacement_d2_020):
    feature = _clean(swa_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_020'] = {'inputs': ['swa_replacement_d2_020'], 'func': swa_replacement_d3_020}


def swa_replacement_d3_021(swa_replacement_d2_021):
    feature = _clean(swa_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_021'] = {'inputs': ['swa_replacement_d2_021'], 'func': swa_replacement_d3_021}


def swa_replacement_d3_022(swa_replacement_d2_022):
    feature = _clean(swa_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_022'] = {'inputs': ['swa_replacement_d2_022'], 'func': swa_replacement_d3_022}


def swa_replacement_d3_023(swa_replacement_d2_023):
    feature = _clean(swa_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_023'] = {'inputs': ['swa_replacement_d2_023'], 'func': swa_replacement_d3_023}


def swa_replacement_d3_024(swa_replacement_d2_024):
    feature = _clean(swa_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_024'] = {'inputs': ['swa_replacement_d2_024'], 'func': swa_replacement_d3_024}


def swa_replacement_d3_025(swa_replacement_d2_025):
    feature = _clean(swa_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_025'] = {'inputs': ['swa_replacement_d2_025'], 'func': swa_replacement_d3_025}


def swa_replacement_d3_026(swa_replacement_d2_026):
    feature = _clean(swa_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_026'] = {'inputs': ['swa_replacement_d2_026'], 'func': swa_replacement_d3_026}


def swa_replacement_d3_027(swa_replacement_d2_027):
    feature = _clean(swa_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_027'] = {'inputs': ['swa_replacement_d2_027'], 'func': swa_replacement_d3_027}


def swa_replacement_d3_028(swa_replacement_d2_028):
    feature = _clean(swa_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_028'] = {'inputs': ['swa_replacement_d2_028'], 'func': swa_replacement_d3_028}


def swa_replacement_d3_029(swa_replacement_d2_029):
    feature = _clean(swa_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_029'] = {'inputs': ['swa_replacement_d2_029'], 'func': swa_replacement_d3_029}


def swa_replacement_d3_030(swa_replacement_d2_030):
    feature = _clean(swa_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_030'] = {'inputs': ['swa_replacement_d2_030'], 'func': swa_replacement_d3_030}


def swa_replacement_d3_031(swa_replacement_d2_031):
    feature = _clean(swa_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_031'] = {'inputs': ['swa_replacement_d2_031'], 'func': swa_replacement_d3_031}


def swa_replacement_d3_032(swa_replacement_d2_032):
    feature = _clean(swa_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_032'] = {'inputs': ['swa_replacement_d2_032'], 'func': swa_replacement_d3_032}


def swa_replacement_d3_033(swa_replacement_d2_033):
    feature = _clean(swa_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_033'] = {'inputs': ['swa_replacement_d2_033'], 'func': swa_replacement_d3_033}


def swa_replacement_d3_034(swa_replacement_d2_034):
    feature = _clean(swa_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_034'] = {'inputs': ['swa_replacement_d2_034'], 'func': swa_replacement_d3_034}


def swa_replacement_d3_035(swa_replacement_d2_035):
    feature = _clean(swa_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_035'] = {'inputs': ['swa_replacement_d2_035'], 'func': swa_replacement_d3_035}


def swa_replacement_d3_036(swa_replacement_d2_036):
    feature = _clean(swa_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_036'] = {'inputs': ['swa_replacement_d2_036'], 'func': swa_replacement_d3_036}


def swa_replacement_d3_037(swa_replacement_d2_037):
    feature = _clean(swa_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_037'] = {'inputs': ['swa_replacement_d2_037'], 'func': swa_replacement_d3_037}


def swa_replacement_d3_038(swa_replacement_d2_038):
    feature = _clean(swa_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_038'] = {'inputs': ['swa_replacement_d2_038'], 'func': swa_replacement_d3_038}


def swa_replacement_d3_039(swa_replacement_d2_039):
    feature = _clean(swa_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_039'] = {'inputs': ['swa_replacement_d2_039'], 'func': swa_replacement_d3_039}


def swa_replacement_d3_040(swa_replacement_d2_040):
    feature = _clean(swa_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_040'] = {'inputs': ['swa_replacement_d2_040'], 'func': swa_replacement_d3_040}


def swa_replacement_d3_041(swa_replacement_d2_041):
    feature = _clean(swa_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_041'] = {'inputs': ['swa_replacement_d2_041'], 'func': swa_replacement_d3_041}


def swa_replacement_d3_042(swa_replacement_d2_042):
    feature = _clean(swa_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_042'] = {'inputs': ['swa_replacement_d2_042'], 'func': swa_replacement_d3_042}


def swa_replacement_d3_043(swa_replacement_d2_043):
    feature = _clean(swa_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_043'] = {'inputs': ['swa_replacement_d2_043'], 'func': swa_replacement_d3_043}


def swa_replacement_d3_044(swa_replacement_d2_044):
    feature = _clean(swa_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_044'] = {'inputs': ['swa_replacement_d2_044'], 'func': swa_replacement_d3_044}


def swa_replacement_d3_045(swa_replacement_d2_045):
    feature = _clean(swa_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_045'] = {'inputs': ['swa_replacement_d2_045'], 'func': swa_replacement_d3_045}


def swa_replacement_d3_046(swa_replacement_d2_046):
    feature = _clean(swa_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_046'] = {'inputs': ['swa_replacement_d2_046'], 'func': swa_replacement_d3_046}


def swa_replacement_d3_047(swa_replacement_d2_047):
    feature = _clean(swa_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_047'] = {'inputs': ['swa_replacement_d2_047'], 'func': swa_replacement_d3_047}


def swa_replacement_d3_048(swa_replacement_d2_048):
    feature = _clean(swa_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_048'] = {'inputs': ['swa_replacement_d2_048'], 'func': swa_replacement_d3_048}


def swa_replacement_d3_049(swa_replacement_d2_049):
    feature = _clean(swa_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_049'] = {'inputs': ['swa_replacement_d2_049'], 'func': swa_replacement_d3_049}


def swa_replacement_d3_050(swa_replacement_d2_050):
    feature = _clean(swa_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_050'] = {'inputs': ['swa_replacement_d2_050'], 'func': swa_replacement_d3_050}


def swa_replacement_d3_051(swa_replacement_d2_051):
    feature = _clean(swa_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_051'] = {'inputs': ['swa_replacement_d2_051'], 'func': swa_replacement_d3_051}


def swa_replacement_d3_052(swa_replacement_d2_052):
    feature = _clean(swa_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_052'] = {'inputs': ['swa_replacement_d2_052'], 'func': swa_replacement_d3_052}


def swa_replacement_d3_053(swa_replacement_d2_053):
    feature = _clean(swa_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_053'] = {'inputs': ['swa_replacement_d2_053'], 'func': swa_replacement_d3_053}


def swa_replacement_d3_054(swa_replacement_d2_054):
    feature = _clean(swa_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_054'] = {'inputs': ['swa_replacement_d2_054'], 'func': swa_replacement_d3_054}


def swa_replacement_d3_055(swa_replacement_d2_055):
    feature = _clean(swa_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_055'] = {'inputs': ['swa_replacement_d2_055'], 'func': swa_replacement_d3_055}


def swa_replacement_d3_056(swa_replacement_d2_056):
    feature = _clean(swa_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_056'] = {'inputs': ['swa_replacement_d2_056'], 'func': swa_replacement_d3_056}


def swa_replacement_d3_057(swa_replacement_d2_057):
    feature = _clean(swa_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_057'] = {'inputs': ['swa_replacement_d2_057'], 'func': swa_replacement_d3_057}


def swa_replacement_d3_058(swa_replacement_d2_058):
    feature = _clean(swa_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_058'] = {'inputs': ['swa_replacement_d2_058'], 'func': swa_replacement_d3_058}


def swa_replacement_d3_059(swa_replacement_d2_059):
    feature = _clean(swa_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_059'] = {'inputs': ['swa_replacement_d2_059'], 'func': swa_replacement_d3_059}


def swa_replacement_d3_060(swa_replacement_d2_060):
    feature = _clean(swa_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_060'] = {'inputs': ['swa_replacement_d2_060'], 'func': swa_replacement_d3_060}


def swa_replacement_d3_061(swa_replacement_d2_061):
    feature = _clean(swa_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_061'] = {'inputs': ['swa_replacement_d2_061'], 'func': swa_replacement_d3_061}


def swa_replacement_d3_062(swa_replacement_d2_062):
    feature = _clean(swa_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_062'] = {'inputs': ['swa_replacement_d2_062'], 'func': swa_replacement_d3_062}


def swa_replacement_d3_063(swa_replacement_d2_063):
    feature = _clean(swa_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_063'] = {'inputs': ['swa_replacement_d2_063'], 'func': swa_replacement_d3_063}


def swa_replacement_d3_064(swa_replacement_d2_064):
    feature = _clean(swa_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_064'] = {'inputs': ['swa_replacement_d2_064'], 'func': swa_replacement_d3_064}


def swa_replacement_d3_065(swa_replacement_d2_065):
    feature = _clean(swa_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_065'] = {'inputs': ['swa_replacement_d2_065'], 'func': swa_replacement_d3_065}


def swa_replacement_d3_066(swa_replacement_d2_066):
    feature = _clean(swa_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_066'] = {'inputs': ['swa_replacement_d2_066'], 'func': swa_replacement_d3_066}


def swa_replacement_d3_067(swa_replacement_d2_067):
    feature = _clean(swa_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_067'] = {'inputs': ['swa_replacement_d2_067'], 'func': swa_replacement_d3_067}


def swa_replacement_d3_068(swa_replacement_d2_068):
    feature = _clean(swa_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_068'] = {'inputs': ['swa_replacement_d2_068'], 'func': swa_replacement_d3_068}


def swa_replacement_d3_069(swa_replacement_d2_069):
    feature = _clean(swa_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_069'] = {'inputs': ['swa_replacement_d2_069'], 'func': swa_replacement_d3_069}


def swa_replacement_d3_070(swa_replacement_d2_070):
    feature = _clean(swa_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_070'] = {'inputs': ['swa_replacement_d2_070'], 'func': swa_replacement_d3_070}


def swa_replacement_d3_071(swa_replacement_d2_071):
    feature = _clean(swa_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_071'] = {'inputs': ['swa_replacement_d2_071'], 'func': swa_replacement_d3_071}


def swa_replacement_d3_072(swa_replacement_d2_072):
    feature = _clean(swa_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_072'] = {'inputs': ['swa_replacement_d2_072'], 'func': swa_replacement_d3_072}


def swa_replacement_d3_073(swa_replacement_d2_073):
    feature = _clean(swa_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_073'] = {'inputs': ['swa_replacement_d2_073'], 'func': swa_replacement_d3_073}


def swa_replacement_d3_074(swa_replacement_d2_074):
    feature = _clean(swa_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_074'] = {'inputs': ['swa_replacement_d2_074'], 'func': swa_replacement_d3_074}


def swa_replacement_d3_075(swa_replacement_d2_075):
    feature = _clean(swa_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_075'] = {'inputs': ['swa_replacement_d2_075'], 'func': swa_replacement_d3_075}


def swa_replacement_d3_076(swa_replacement_d2_076):
    feature = _clean(swa_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_076'] = {'inputs': ['swa_replacement_d2_076'], 'func': swa_replacement_d3_076}


def swa_replacement_d3_077(swa_replacement_d2_077):
    feature = _clean(swa_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_077'] = {'inputs': ['swa_replacement_d2_077'], 'func': swa_replacement_d3_077}


def swa_replacement_d3_078(swa_replacement_d2_078):
    feature = _clean(swa_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_078'] = {'inputs': ['swa_replacement_d2_078'], 'func': swa_replacement_d3_078}


def swa_replacement_d3_079(swa_replacement_d2_079):
    feature = _clean(swa_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_079'] = {'inputs': ['swa_replacement_d2_079'], 'func': swa_replacement_d3_079}


def swa_replacement_d3_080(swa_replacement_d2_080):
    feature = _clean(swa_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_080'] = {'inputs': ['swa_replacement_d2_080'], 'func': swa_replacement_d3_080}


def swa_replacement_d3_081(swa_replacement_d2_081):
    feature = _clean(swa_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_081'] = {'inputs': ['swa_replacement_d2_081'], 'func': swa_replacement_d3_081}


def swa_replacement_d3_082(swa_replacement_d2_082):
    feature = _clean(swa_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_082'] = {'inputs': ['swa_replacement_d2_082'], 'func': swa_replacement_d3_082}


def swa_replacement_d3_083(swa_replacement_d2_083):
    feature = _clean(swa_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_083'] = {'inputs': ['swa_replacement_d2_083'], 'func': swa_replacement_d3_083}


def swa_replacement_d3_084(swa_replacement_d2_084):
    feature = _clean(swa_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_084'] = {'inputs': ['swa_replacement_d2_084'], 'func': swa_replacement_d3_084}


def swa_replacement_d3_085(swa_replacement_d2_085):
    feature = _clean(swa_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_085'] = {'inputs': ['swa_replacement_d2_085'], 'func': swa_replacement_d3_085}


def swa_replacement_d3_086(swa_replacement_d2_086):
    feature = _clean(swa_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_086'] = {'inputs': ['swa_replacement_d2_086'], 'func': swa_replacement_d3_086}


def swa_replacement_d3_087(swa_replacement_d2_087):
    feature = _clean(swa_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_087'] = {'inputs': ['swa_replacement_d2_087'], 'func': swa_replacement_d3_087}


def swa_replacement_d3_088(swa_replacement_d2_088):
    feature = _clean(swa_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_088'] = {'inputs': ['swa_replacement_d2_088'], 'func': swa_replacement_d3_088}


def swa_replacement_d3_089(swa_replacement_d2_089):
    feature = _clean(swa_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_089'] = {'inputs': ['swa_replacement_d2_089'], 'func': swa_replacement_d3_089}


def swa_replacement_d3_090(swa_replacement_d2_090):
    feature = _clean(swa_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_090'] = {'inputs': ['swa_replacement_d2_090'], 'func': swa_replacement_d3_090}


def swa_replacement_d3_091(swa_replacement_d2_091):
    feature = _clean(swa_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_091'] = {'inputs': ['swa_replacement_d2_091'], 'func': swa_replacement_d3_091}


def swa_replacement_d3_092(swa_replacement_d2_092):
    feature = _clean(swa_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_092'] = {'inputs': ['swa_replacement_d2_092'], 'func': swa_replacement_d3_092}


def swa_replacement_d3_093(swa_replacement_d2_093):
    feature = _clean(swa_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_093'] = {'inputs': ['swa_replacement_d2_093'], 'func': swa_replacement_d3_093}


def swa_replacement_d3_094(swa_replacement_d2_094):
    feature = _clean(swa_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_094'] = {'inputs': ['swa_replacement_d2_094'], 'func': swa_replacement_d3_094}


def swa_replacement_d3_095(swa_replacement_d2_095):
    feature = _clean(swa_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_095'] = {'inputs': ['swa_replacement_d2_095'], 'func': swa_replacement_d3_095}


def swa_replacement_d3_096(swa_replacement_d2_096):
    feature = _clean(swa_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_096'] = {'inputs': ['swa_replacement_d2_096'], 'func': swa_replacement_d3_096}


def swa_replacement_d3_097(swa_replacement_d2_097):
    feature = _clean(swa_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_097'] = {'inputs': ['swa_replacement_d2_097'], 'func': swa_replacement_d3_097}


def swa_replacement_d3_098(swa_replacement_d2_098):
    feature = _clean(swa_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_098'] = {'inputs': ['swa_replacement_d2_098'], 'func': swa_replacement_d3_098}


def swa_replacement_d3_099(swa_replacement_d2_099):
    feature = _clean(swa_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_099'] = {'inputs': ['swa_replacement_d2_099'], 'func': swa_replacement_d3_099}


def swa_replacement_d3_100(swa_replacement_d2_100):
    feature = _clean(swa_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_100'] = {'inputs': ['swa_replacement_d2_100'], 'func': swa_replacement_d3_100}


def swa_replacement_d3_101(swa_replacement_d2_101):
    feature = _clean(swa_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_101'] = {'inputs': ['swa_replacement_d2_101'], 'func': swa_replacement_d3_101}


def swa_replacement_d3_102(swa_replacement_d2_102):
    feature = _clean(swa_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_102'] = {'inputs': ['swa_replacement_d2_102'], 'func': swa_replacement_d3_102}


def swa_replacement_d3_103(swa_replacement_d2_103):
    feature = _clean(swa_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_103'] = {'inputs': ['swa_replacement_d2_103'], 'func': swa_replacement_d3_103}


def swa_replacement_d3_104(swa_replacement_d2_104):
    feature = _clean(swa_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_104'] = {'inputs': ['swa_replacement_d2_104'], 'func': swa_replacement_d3_104}


def swa_replacement_d3_105(swa_replacement_d2_105):
    feature = _clean(swa_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_105'] = {'inputs': ['swa_replacement_d2_105'], 'func': swa_replacement_d3_105}


def swa_replacement_d3_106(swa_replacement_d2_106):
    feature = _clean(swa_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_106'] = {'inputs': ['swa_replacement_d2_106'], 'func': swa_replacement_d3_106}


def swa_replacement_d3_107(swa_replacement_d2_107):
    feature = _clean(swa_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_107'] = {'inputs': ['swa_replacement_d2_107'], 'func': swa_replacement_d3_107}


def swa_replacement_d3_108(swa_replacement_d2_108):
    feature = _clean(swa_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_108'] = {'inputs': ['swa_replacement_d2_108'], 'func': swa_replacement_d3_108}


def swa_replacement_d3_109(swa_replacement_d2_109):
    feature = _clean(swa_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_109'] = {'inputs': ['swa_replacement_d2_109'], 'func': swa_replacement_d3_109}


def swa_replacement_d3_110(swa_replacement_d2_110):
    feature = _clean(swa_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_110'] = {'inputs': ['swa_replacement_d2_110'], 'func': swa_replacement_d3_110}


def swa_replacement_d3_111(swa_replacement_d2_111):
    feature = _clean(swa_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_111'] = {'inputs': ['swa_replacement_d2_111'], 'func': swa_replacement_d3_111}


def swa_replacement_d3_112(swa_replacement_d2_112):
    feature = _clean(swa_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_112'] = {'inputs': ['swa_replacement_d2_112'], 'func': swa_replacement_d3_112}


def swa_replacement_d3_113(swa_replacement_d2_113):
    feature = _clean(swa_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_113'] = {'inputs': ['swa_replacement_d2_113'], 'func': swa_replacement_d3_113}


def swa_replacement_d3_114(swa_replacement_d2_114):
    feature = _clean(swa_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_114'] = {'inputs': ['swa_replacement_d2_114'], 'func': swa_replacement_d3_114}


def swa_replacement_d3_115(swa_replacement_d2_115):
    feature = _clean(swa_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_115'] = {'inputs': ['swa_replacement_d2_115'], 'func': swa_replacement_d3_115}


def swa_replacement_d3_116(swa_replacement_d2_116):
    feature = _clean(swa_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_116'] = {'inputs': ['swa_replacement_d2_116'], 'func': swa_replacement_d3_116}


def swa_replacement_d3_117(swa_replacement_d2_117):
    feature = _clean(swa_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_117'] = {'inputs': ['swa_replacement_d2_117'], 'func': swa_replacement_d3_117}


def swa_replacement_d3_118(swa_replacement_d2_118):
    feature = _clean(swa_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_118'] = {'inputs': ['swa_replacement_d2_118'], 'func': swa_replacement_d3_118}


def swa_replacement_d3_119(swa_replacement_d2_119):
    feature = _clean(swa_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_119'] = {'inputs': ['swa_replacement_d2_119'], 'func': swa_replacement_d3_119}


def swa_replacement_d3_120(swa_replacement_d2_120):
    feature = _clean(swa_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_120'] = {'inputs': ['swa_replacement_d2_120'], 'func': swa_replacement_d3_120}


def swa_replacement_d3_121(swa_replacement_d2_121):
    feature = _clean(swa_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_121'] = {'inputs': ['swa_replacement_d2_121'], 'func': swa_replacement_d3_121}


def swa_replacement_d3_122(swa_replacement_d2_122):
    feature = _clean(swa_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_122'] = {'inputs': ['swa_replacement_d2_122'], 'func': swa_replacement_d3_122}


def swa_replacement_d3_123(swa_replacement_d2_123):
    feature = _clean(swa_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_123'] = {'inputs': ['swa_replacement_d2_123'], 'func': swa_replacement_d3_123}


def swa_replacement_d3_124(swa_replacement_d2_124):
    feature = _clean(swa_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_124'] = {'inputs': ['swa_replacement_d2_124'], 'func': swa_replacement_d3_124}


def swa_replacement_d3_125(swa_replacement_d2_125):
    feature = _clean(swa_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_125'] = {'inputs': ['swa_replacement_d2_125'], 'func': swa_replacement_d3_125}


def swa_replacement_d3_126(swa_replacement_d2_126):
    feature = _clean(swa_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_126'] = {'inputs': ['swa_replacement_d2_126'], 'func': swa_replacement_d3_126}


def swa_replacement_d3_127(swa_replacement_d2_127):
    feature = _clean(swa_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_127'] = {'inputs': ['swa_replacement_d2_127'], 'func': swa_replacement_d3_127}


def swa_replacement_d3_128(swa_replacement_d2_128):
    feature = _clean(swa_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_128'] = {'inputs': ['swa_replacement_d2_128'], 'func': swa_replacement_d3_128}


def swa_replacement_d3_129(swa_replacement_d2_129):
    feature = _clean(swa_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_129'] = {'inputs': ['swa_replacement_d2_129'], 'func': swa_replacement_d3_129}


def swa_replacement_d3_130(swa_replacement_d2_130):
    feature = _clean(swa_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_130'] = {'inputs': ['swa_replacement_d2_130'], 'func': swa_replacement_d3_130}


def swa_replacement_d3_131(swa_replacement_d2_131):
    feature = _clean(swa_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_131'] = {'inputs': ['swa_replacement_d2_131'], 'func': swa_replacement_d3_131}


def swa_replacement_d3_132(swa_replacement_d2_132):
    feature = _clean(swa_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_132'] = {'inputs': ['swa_replacement_d2_132'], 'func': swa_replacement_d3_132}


def swa_replacement_d3_133(swa_replacement_d2_133):
    feature = _clean(swa_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_133'] = {'inputs': ['swa_replacement_d2_133'], 'func': swa_replacement_d3_133}


def swa_replacement_d3_134(swa_replacement_d2_134):
    feature = _clean(swa_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_134'] = {'inputs': ['swa_replacement_d2_134'], 'func': swa_replacement_d3_134}


def swa_replacement_d3_135(swa_replacement_d2_135):
    feature = _clean(swa_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_135'] = {'inputs': ['swa_replacement_d2_135'], 'func': swa_replacement_d3_135}


def swa_replacement_d3_136(swa_replacement_d2_136):
    feature = _clean(swa_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_136'] = {'inputs': ['swa_replacement_d2_136'], 'func': swa_replacement_d3_136}


def swa_replacement_d3_137(swa_replacement_d2_137):
    feature = _clean(swa_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_137'] = {'inputs': ['swa_replacement_d2_137'], 'func': swa_replacement_d3_137}


def swa_replacement_d3_138(swa_replacement_d2_138):
    feature = _clean(swa_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_138'] = {'inputs': ['swa_replacement_d2_138'], 'func': swa_replacement_d3_138}


def swa_replacement_d3_139(swa_replacement_d2_139):
    feature = _clean(swa_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_139'] = {'inputs': ['swa_replacement_d2_139'], 'func': swa_replacement_d3_139}


def swa_replacement_d3_140(swa_replacement_d2_140):
    feature = _clean(swa_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_140'] = {'inputs': ['swa_replacement_d2_140'], 'func': swa_replacement_d3_140}


def swa_replacement_d3_141(swa_replacement_d2_141):
    feature = _clean(swa_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_141'] = {'inputs': ['swa_replacement_d2_141'], 'func': swa_replacement_d3_141}


def swa_replacement_d3_142(swa_replacement_d2_142):
    feature = _clean(swa_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_142'] = {'inputs': ['swa_replacement_d2_142'], 'func': swa_replacement_d3_142}


def swa_replacement_d3_143(swa_replacement_d2_143):
    feature = _clean(swa_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_143'] = {'inputs': ['swa_replacement_d2_143'], 'func': swa_replacement_d3_143}


def swa_replacement_d3_144(swa_replacement_d2_144):
    feature = _clean(swa_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_144'] = {'inputs': ['swa_replacement_d2_144'], 'func': swa_replacement_d3_144}


def swa_replacement_d3_145(swa_replacement_d2_145):
    feature = _clean(swa_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_145'] = {'inputs': ['swa_replacement_d2_145'], 'func': swa_replacement_d3_145}


def swa_replacement_d3_146(swa_replacement_d2_146):
    feature = _clean(swa_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_146'] = {'inputs': ['swa_replacement_d2_146'], 'func': swa_replacement_d3_146}


def swa_replacement_d3_147(swa_replacement_d2_147):
    feature = _clean(swa_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_147'] = {'inputs': ['swa_replacement_d2_147'], 'func': swa_replacement_d3_147}


def swa_replacement_d3_148(swa_replacement_d2_148):
    feature = _clean(swa_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_148'] = {'inputs': ['swa_replacement_d2_148'], 'func': swa_replacement_d3_148}


def swa_replacement_d3_149(swa_replacement_d2_149):
    feature = _clean(swa_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_149'] = {'inputs': ['swa_replacement_d2_149'], 'func': swa_replacement_d3_149}


def swa_replacement_d3_150(swa_replacement_d2_150):
    feature = _clean(swa_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_150'] = {'inputs': ['swa_replacement_d2_150'], 'func': swa_replacement_d3_150}


def swa_replacement_d3_151(swa_replacement_d2_151):
    feature = _clean(swa_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_151'] = {'inputs': ['swa_replacement_d2_151'], 'func': swa_replacement_d3_151}


def swa_replacement_d3_152(swa_replacement_d2_152):
    feature = _clean(swa_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_152'] = {'inputs': ['swa_replacement_d2_152'], 'func': swa_replacement_d3_152}


def swa_replacement_d3_153(swa_replacement_d2_153):
    feature = _clean(swa_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_153'] = {'inputs': ['swa_replacement_d2_153'], 'func': swa_replacement_d3_153}


def swa_replacement_d3_154(swa_replacement_d2_154):
    feature = _clean(swa_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_154'] = {'inputs': ['swa_replacement_d2_154'], 'func': swa_replacement_d3_154}


def swa_replacement_d3_155(swa_replacement_d2_155):
    feature = _clean(swa_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_155'] = {'inputs': ['swa_replacement_d2_155'], 'func': swa_replacement_d3_155}


def swa_replacement_d3_156(swa_replacement_d2_156):
    feature = _clean(swa_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_156'] = {'inputs': ['swa_replacement_d2_156'], 'func': swa_replacement_d3_156}


def swa_replacement_d3_157(swa_replacement_d2_157):
    feature = _clean(swa_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_157'] = {'inputs': ['swa_replacement_d2_157'], 'func': swa_replacement_d3_157}


def swa_replacement_d3_158(swa_replacement_d2_158):
    feature = _clean(swa_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_158'] = {'inputs': ['swa_replacement_d2_158'], 'func': swa_replacement_d3_158}


def swa_replacement_d3_159(swa_replacement_d2_159):
    feature = _clean(swa_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_159'] = {'inputs': ['swa_replacement_d2_159'], 'func': swa_replacement_d3_159}


def swa_replacement_d3_160(swa_replacement_d2_160):
    feature = _clean(swa_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
SWA_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['swa_replacement_d3_160'] = {'inputs': ['swa_replacement_d2_160'], 'func': swa_replacement_d3_160}


# Third-derivative extensions for repaired first-base features.
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def swk_base_universe_d3_001_swk_002_gap_magnitude_10_002(swk_base_universe_d2_001_swk_002_gap_magnitude_10_002):
    return _base_universe_d3(swk_base_universe_d2_001_swk_002_gap_magnitude_10_002, 1)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_001_swk_002_gap_magnitude_10_002'] = {'inputs': ['swk_base_universe_d2_001_swk_002_gap_magnitude_10_002'], 'func': swk_base_universe_d3_001_swk_002_gap_magnitude_10_002}


def swk_base_universe_d3_002_swk_003_open_close_pressure_21_003(swk_base_universe_d2_002_swk_003_open_close_pressure_21_003):
    return _base_universe_d3(swk_base_universe_d2_002_swk_003_open_close_pressure_21_003, 2)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_002_swk_003_open_close_pressure_21_003'] = {'inputs': ['swk_base_universe_d2_002_swk_003_open_close_pressure_21_003'], 'func': swk_base_universe_d3_002_swk_003_open_close_pressure_21_003}


def swk_base_universe_d3_003_swk_004_lower_wick_ratio_42_004(swk_base_universe_d2_003_swk_004_lower_wick_ratio_42_004):
    return _base_universe_d3(swk_base_universe_d2_003_swk_004_lower_wick_ratio_42_004, 3)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_003_swk_004_lower_wick_ratio_42_004'] = {'inputs': ['swk_base_universe_d2_003_swk_004_lower_wick_ratio_42_004'], 'func': swk_base_universe_d3_003_swk_004_lower_wick_ratio_42_004}


def swk_base_universe_d3_004_swk_005_upper_wick_ratio_63_005(swk_base_universe_d2_004_swk_005_upper_wick_ratio_63_005):
    return _base_universe_d3(swk_base_universe_d2_004_swk_005_upper_wick_ratio_63_005, 4)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_004_swk_005_upper_wick_ratio_63_005'] = {'inputs': ['swk_base_universe_d2_004_swk_005_upper_wick_ratio_63_005'], 'func': swk_base_universe_d3_004_swk_005_upper_wick_ratio_63_005}


def swk_base_universe_d3_005_swk_006_body_to_range_84_006(swk_base_universe_d2_005_swk_006_body_to_range_84_006):
    return _base_universe_d3(swk_base_universe_d2_005_swk_006_body_to_range_84_006, 5)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_005_swk_006_body_to_range_84_006'] = {'inputs': ['swk_base_universe_d2_005_swk_006_body_to_range_84_006'], 'func': swk_base_universe_d3_005_swk_006_body_to_range_84_006}


def swk_base_universe_d3_006_swk_008_gap_magnitude_189_008(swk_base_universe_d2_006_swk_008_gap_magnitude_189_008):
    return _base_universe_d3(swk_base_universe_d2_006_swk_008_gap_magnitude_189_008, 6)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_006_swk_008_gap_magnitude_189_008'] = {'inputs': ['swk_base_universe_d2_006_swk_008_gap_magnitude_189_008'], 'func': swk_base_universe_d3_006_swk_008_gap_magnitude_189_008}


def swk_base_universe_d3_007_swk_009_open_close_pressure_252_009(swk_base_universe_d2_007_swk_009_open_close_pressure_252_009):
    return _base_universe_d3(swk_base_universe_d2_007_swk_009_open_close_pressure_252_009, 7)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_007_swk_009_open_close_pressure_252_009'] = {'inputs': ['swk_base_universe_d2_007_swk_009_open_close_pressure_252_009'], 'func': swk_base_universe_d3_007_swk_009_open_close_pressure_252_009}


def swk_base_universe_d3_008_swk_010_lower_wick_ratio_378_010(swk_base_universe_d2_008_swk_010_lower_wick_ratio_378_010):
    return _base_universe_d3(swk_base_universe_d2_008_swk_010_lower_wick_ratio_378_010, 8)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_008_swk_010_lower_wick_ratio_378_010'] = {'inputs': ['swk_base_universe_d2_008_swk_010_lower_wick_ratio_378_010'], 'func': swk_base_universe_d3_008_swk_010_lower_wick_ratio_378_010}


def swk_base_universe_d3_009_swk_011_upper_wick_ratio_504_011(swk_base_universe_d2_009_swk_011_upper_wick_ratio_504_011):
    return _base_universe_d3(swk_base_universe_d2_009_swk_011_upper_wick_ratio_504_011, 9)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_009_swk_011_upper_wick_ratio_504_011'] = {'inputs': ['swk_base_universe_d2_009_swk_011_upper_wick_ratio_504_011'], 'func': swk_base_universe_d3_009_swk_011_upper_wick_ratio_504_011}


def swk_base_universe_d3_010_swk_012_body_to_range_756_012(swk_base_universe_d2_010_swk_012_body_to_range_756_012):
    return _base_universe_d3(swk_base_universe_d2_010_swk_012_body_to_range_756_012, 10)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_010_swk_012_body_to_range_756_012'] = {'inputs': ['swk_base_universe_d2_010_swk_012_body_to_range_756_012'], 'func': swk_base_universe_d3_010_swk_012_body_to_range_756_012}


def swk_base_universe_d3_011_swk_014_gap_magnitude_1260_014(swk_base_universe_d2_011_swk_014_gap_magnitude_1260_014):
    return _base_universe_d3(swk_base_universe_d2_011_swk_014_gap_magnitude_1260_014, 11)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_011_swk_014_gap_magnitude_1260_014'] = {'inputs': ['swk_base_universe_d2_011_swk_014_gap_magnitude_1260_014'], 'func': swk_base_universe_d3_011_swk_014_gap_magnitude_1260_014}


def swk_base_universe_d3_012_swk_015_open_close_pressure_1512_015(swk_base_universe_d2_012_swk_015_open_close_pressure_1512_015):
    return _base_universe_d3(swk_base_universe_d2_012_swk_015_open_close_pressure_1512_015, 12)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_012_swk_015_open_close_pressure_1512_015'] = {'inputs': ['swk_base_universe_d2_012_swk_015_open_close_pressure_1512_015'], 'func': swk_base_universe_d3_012_swk_015_open_close_pressure_1512_015}


def swk_base_universe_d3_013_swk_016_lower_wick_ratio_5_016(swk_base_universe_d2_013_swk_016_lower_wick_ratio_5_016):
    return _base_universe_d3(swk_base_universe_d2_013_swk_016_lower_wick_ratio_5_016, 13)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_013_swk_016_lower_wick_ratio_5_016'] = {'inputs': ['swk_base_universe_d2_013_swk_016_lower_wick_ratio_5_016'], 'func': swk_base_universe_d3_013_swk_016_lower_wick_ratio_5_016}


def swk_base_universe_d3_014_swk_017_upper_wick_ratio_10_017(swk_base_universe_d2_014_swk_017_upper_wick_ratio_10_017):
    return _base_universe_d3(swk_base_universe_d2_014_swk_017_upper_wick_ratio_10_017, 14)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_014_swk_017_upper_wick_ratio_10_017'] = {'inputs': ['swk_base_universe_d2_014_swk_017_upper_wick_ratio_10_017'], 'func': swk_base_universe_d3_014_swk_017_upper_wick_ratio_10_017}


def swk_base_universe_d3_015_swk_018_body_to_range_21_018(swk_base_universe_d2_015_swk_018_body_to_range_21_018):
    return _base_universe_d3(swk_base_universe_d2_015_swk_018_body_to_range_21_018, 15)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_015_swk_018_body_to_range_21_018'] = {'inputs': ['swk_base_universe_d2_015_swk_018_body_to_range_21_018'], 'func': swk_base_universe_d3_015_swk_018_body_to_range_21_018}


def swk_base_universe_d3_016_swk_020_gap_magnitude_63_020(swk_base_universe_d2_016_swk_020_gap_magnitude_63_020):
    return _base_universe_d3(swk_base_universe_d2_016_swk_020_gap_magnitude_63_020, 16)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_016_swk_020_gap_magnitude_63_020'] = {'inputs': ['swk_base_universe_d2_016_swk_020_gap_magnitude_63_020'], 'func': swk_base_universe_d3_016_swk_020_gap_magnitude_63_020}


def swk_base_universe_d3_017_swk_021_open_close_pressure_84_021(swk_base_universe_d2_017_swk_021_open_close_pressure_84_021):
    return _base_universe_d3(swk_base_universe_d2_017_swk_021_open_close_pressure_84_021, 17)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_017_swk_021_open_close_pressure_84_021'] = {'inputs': ['swk_base_universe_d2_017_swk_021_open_close_pressure_84_021'], 'func': swk_base_universe_d3_017_swk_021_open_close_pressure_84_021}


def swk_base_universe_d3_018_swk_022_lower_wick_ratio_126_022(swk_base_universe_d2_018_swk_022_lower_wick_ratio_126_022):
    return _base_universe_d3(swk_base_universe_d2_018_swk_022_lower_wick_ratio_126_022, 18)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_018_swk_022_lower_wick_ratio_126_022'] = {'inputs': ['swk_base_universe_d2_018_swk_022_lower_wick_ratio_126_022'], 'func': swk_base_universe_d3_018_swk_022_lower_wick_ratio_126_022}


def swk_base_universe_d3_019_swk_023_upper_wick_ratio_189_023(swk_base_universe_d2_019_swk_023_upper_wick_ratio_189_023):
    return _base_universe_d3(swk_base_universe_d2_019_swk_023_upper_wick_ratio_189_023, 19)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_019_swk_023_upper_wick_ratio_189_023'] = {'inputs': ['swk_base_universe_d2_019_swk_023_upper_wick_ratio_189_023'], 'func': swk_base_universe_d3_019_swk_023_upper_wick_ratio_189_023}


def swk_base_universe_d3_020_swk_024_body_to_range_252_024(swk_base_universe_d2_020_swk_024_body_to_range_252_024):
    return _base_universe_d3(swk_base_universe_d2_020_swk_024_body_to_range_252_024, 20)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_020_swk_024_body_to_range_252_024'] = {'inputs': ['swk_base_universe_d2_020_swk_024_body_to_range_252_024'], 'func': swk_base_universe_d3_020_swk_024_body_to_range_252_024}


def swk_base_universe_d3_021_swk_026_gap_magnitude_504_026(swk_base_universe_d2_021_swk_026_gap_magnitude_504_026):
    return _base_universe_d3(swk_base_universe_d2_021_swk_026_gap_magnitude_504_026, 21)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_021_swk_026_gap_magnitude_504_026'] = {'inputs': ['swk_base_universe_d2_021_swk_026_gap_magnitude_504_026'], 'func': swk_base_universe_d3_021_swk_026_gap_magnitude_504_026}


def swk_base_universe_d3_022_swk_027_open_close_pressure_756_027(swk_base_universe_d2_022_swk_027_open_close_pressure_756_027):
    return _base_universe_d3(swk_base_universe_d2_022_swk_027_open_close_pressure_756_027, 22)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_022_swk_027_open_close_pressure_756_027'] = {'inputs': ['swk_base_universe_d2_022_swk_027_open_close_pressure_756_027'], 'func': swk_base_universe_d3_022_swk_027_open_close_pressure_756_027}


def swk_base_universe_d3_023_swk_028_lower_wick_ratio_1008_028(swk_base_universe_d2_023_swk_028_lower_wick_ratio_1008_028):
    return _base_universe_d3(swk_base_universe_d2_023_swk_028_lower_wick_ratio_1008_028, 23)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_023_swk_028_lower_wick_ratio_1008_028'] = {'inputs': ['swk_base_universe_d2_023_swk_028_lower_wick_ratio_1008_028'], 'func': swk_base_universe_d3_023_swk_028_lower_wick_ratio_1008_028}


def swk_base_universe_d3_024_swk_029_upper_wick_ratio_1260_029(swk_base_universe_d2_024_swk_029_upper_wick_ratio_1260_029):
    return _base_universe_d3(swk_base_universe_d2_024_swk_029_upper_wick_ratio_1260_029, 24)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_024_swk_029_upper_wick_ratio_1260_029'] = {'inputs': ['swk_base_universe_d2_024_swk_029_upper_wick_ratio_1260_029'], 'func': swk_base_universe_d3_024_swk_029_upper_wick_ratio_1260_029}


def swk_base_universe_d3_025_swk_030_body_to_range_1512_030(swk_base_universe_d2_025_swk_030_body_to_range_1512_030):
    return _base_universe_d3(swk_base_universe_d2_025_swk_030_body_to_range_1512_030, 25)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_025_swk_030_body_to_range_1512_030'] = {'inputs': ['swk_base_universe_d2_025_swk_030_body_to_range_1512_030'], 'func': swk_base_universe_d3_025_swk_030_body_to_range_1512_030}


def swk_base_universe_d3_026_swk_basefill_031(swk_base_universe_d2_026_swk_basefill_031):
    return _base_universe_d3(swk_base_universe_d2_026_swk_basefill_031, 26)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_026_swk_basefill_031'] = {'inputs': ['swk_base_universe_d2_026_swk_basefill_031'], 'func': swk_base_universe_d3_026_swk_basefill_031}


def swk_base_universe_d3_027_swk_basefill_032(swk_base_universe_d2_027_swk_basefill_032):
    return _base_universe_d3(swk_base_universe_d2_027_swk_basefill_032, 27)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_027_swk_basefill_032'] = {'inputs': ['swk_base_universe_d2_027_swk_basefill_032'], 'func': swk_base_universe_d3_027_swk_basefill_032}


def swk_base_universe_d3_028_swk_basefill_033(swk_base_universe_d2_028_swk_basefill_033):
    return _base_universe_d3(swk_base_universe_d2_028_swk_basefill_033, 28)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_028_swk_basefill_033'] = {'inputs': ['swk_base_universe_d2_028_swk_basefill_033'], 'func': swk_base_universe_d3_028_swk_basefill_033}


def swk_base_universe_d3_029_swk_basefill_034(swk_base_universe_d2_029_swk_basefill_034):
    return _base_universe_d3(swk_base_universe_d2_029_swk_basefill_034, 29)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_029_swk_basefill_034'] = {'inputs': ['swk_base_universe_d2_029_swk_basefill_034'], 'func': swk_base_universe_d3_029_swk_basefill_034}


def swk_base_universe_d3_030_swk_basefill_035(swk_base_universe_d2_030_swk_basefill_035):
    return _base_universe_d3(swk_base_universe_d2_030_swk_basefill_035, 30)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_030_swk_basefill_035'] = {'inputs': ['swk_base_universe_d2_030_swk_basefill_035'], 'func': swk_base_universe_d3_030_swk_basefill_035}


def swk_base_universe_d3_031_swk_basefill_036(swk_base_universe_d2_031_swk_basefill_036):
    return _base_universe_d3(swk_base_universe_d2_031_swk_basefill_036, 31)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_031_swk_basefill_036'] = {'inputs': ['swk_base_universe_d2_031_swk_basefill_036'], 'func': swk_base_universe_d3_031_swk_basefill_036}


def swk_base_universe_d3_032_swk_basefill_037(swk_base_universe_d2_032_swk_basefill_037):
    return _base_universe_d3(swk_base_universe_d2_032_swk_basefill_037, 32)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_032_swk_basefill_037'] = {'inputs': ['swk_base_universe_d2_032_swk_basefill_037'], 'func': swk_base_universe_d3_032_swk_basefill_037}


def swk_base_universe_d3_033_swk_basefill_038(swk_base_universe_d2_033_swk_basefill_038):
    return _base_universe_d3(swk_base_universe_d2_033_swk_basefill_038, 33)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_033_swk_basefill_038'] = {'inputs': ['swk_base_universe_d2_033_swk_basefill_038'], 'func': swk_base_universe_d3_033_swk_basefill_038}


def swk_base_universe_d3_034_swk_basefill_039(swk_base_universe_d2_034_swk_basefill_039):
    return _base_universe_d3(swk_base_universe_d2_034_swk_basefill_039, 34)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_034_swk_basefill_039'] = {'inputs': ['swk_base_universe_d2_034_swk_basefill_039'], 'func': swk_base_universe_d3_034_swk_basefill_039}


def swk_base_universe_d3_035_swk_basefill_040(swk_base_universe_d2_035_swk_basefill_040):
    return _base_universe_d3(swk_base_universe_d2_035_swk_basefill_040, 35)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_035_swk_basefill_040'] = {'inputs': ['swk_base_universe_d2_035_swk_basefill_040'], 'func': swk_base_universe_d3_035_swk_basefill_040}


def swk_base_universe_d3_036_swk_basefill_041(swk_base_universe_d2_036_swk_basefill_041):
    return _base_universe_d3(swk_base_universe_d2_036_swk_basefill_041, 36)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_036_swk_basefill_041'] = {'inputs': ['swk_base_universe_d2_036_swk_basefill_041'], 'func': swk_base_universe_d3_036_swk_basefill_041}


def swk_base_universe_d3_037_swk_basefill_042(swk_base_universe_d2_037_swk_basefill_042):
    return _base_universe_d3(swk_base_universe_d2_037_swk_basefill_042, 37)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_037_swk_basefill_042'] = {'inputs': ['swk_base_universe_d2_037_swk_basefill_042'], 'func': swk_base_universe_d3_037_swk_basefill_042}


def swk_base_universe_d3_038_swk_basefill_043(swk_base_universe_d2_038_swk_basefill_043):
    return _base_universe_d3(swk_base_universe_d2_038_swk_basefill_043, 38)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_038_swk_basefill_043'] = {'inputs': ['swk_base_universe_d2_038_swk_basefill_043'], 'func': swk_base_universe_d3_038_swk_basefill_043}


def swk_base_universe_d3_039_swk_basefill_044(swk_base_universe_d2_039_swk_basefill_044):
    return _base_universe_d3(swk_base_universe_d2_039_swk_basefill_044, 39)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_039_swk_basefill_044'] = {'inputs': ['swk_base_universe_d2_039_swk_basefill_044'], 'func': swk_base_universe_d3_039_swk_basefill_044}


def swk_base_universe_d3_040_swk_basefill_045(swk_base_universe_d2_040_swk_basefill_045):
    return _base_universe_d3(swk_base_universe_d2_040_swk_basefill_045, 40)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_040_swk_basefill_045'] = {'inputs': ['swk_base_universe_d2_040_swk_basefill_045'], 'func': swk_base_universe_d3_040_swk_basefill_045}


def swk_base_universe_d3_041_swk_basefill_046(swk_base_universe_d2_041_swk_basefill_046):
    return _base_universe_d3(swk_base_universe_d2_041_swk_basefill_046, 41)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_041_swk_basefill_046'] = {'inputs': ['swk_base_universe_d2_041_swk_basefill_046'], 'func': swk_base_universe_d3_041_swk_basefill_046}


def swk_base_universe_d3_042_swk_basefill_047(swk_base_universe_d2_042_swk_basefill_047):
    return _base_universe_d3(swk_base_universe_d2_042_swk_basefill_047, 42)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_042_swk_basefill_047'] = {'inputs': ['swk_base_universe_d2_042_swk_basefill_047'], 'func': swk_base_universe_d3_042_swk_basefill_047}


def swk_base_universe_d3_043_swk_basefill_048(swk_base_universe_d2_043_swk_basefill_048):
    return _base_universe_d3(swk_base_universe_d2_043_swk_basefill_048, 43)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_043_swk_basefill_048'] = {'inputs': ['swk_base_universe_d2_043_swk_basefill_048'], 'func': swk_base_universe_d3_043_swk_basefill_048}


def swk_base_universe_d3_044_swk_basefill_049(swk_base_universe_d2_044_swk_basefill_049):
    return _base_universe_d3(swk_base_universe_d2_044_swk_basefill_049, 44)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_044_swk_basefill_049'] = {'inputs': ['swk_base_universe_d2_044_swk_basefill_049'], 'func': swk_base_universe_d3_044_swk_basefill_049}


def swk_base_universe_d3_045_swk_basefill_050(swk_base_universe_d2_045_swk_basefill_050):
    return _base_universe_d3(swk_base_universe_d2_045_swk_basefill_050, 45)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_045_swk_basefill_050'] = {'inputs': ['swk_base_universe_d2_045_swk_basefill_050'], 'func': swk_base_universe_d3_045_swk_basefill_050}


def swk_base_universe_d3_046_swk_basefill_051(swk_base_universe_d2_046_swk_basefill_051):
    return _base_universe_d3(swk_base_universe_d2_046_swk_basefill_051, 46)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_046_swk_basefill_051'] = {'inputs': ['swk_base_universe_d2_046_swk_basefill_051'], 'func': swk_base_universe_d3_046_swk_basefill_051}


def swk_base_universe_d3_047_swk_basefill_052(swk_base_universe_d2_047_swk_basefill_052):
    return _base_universe_d3(swk_base_universe_d2_047_swk_basefill_052, 47)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_047_swk_basefill_052'] = {'inputs': ['swk_base_universe_d2_047_swk_basefill_052'], 'func': swk_base_universe_d3_047_swk_basefill_052}


def swk_base_universe_d3_048_swk_basefill_053(swk_base_universe_d2_048_swk_basefill_053):
    return _base_universe_d3(swk_base_universe_d2_048_swk_basefill_053, 48)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_048_swk_basefill_053'] = {'inputs': ['swk_base_universe_d2_048_swk_basefill_053'], 'func': swk_base_universe_d3_048_swk_basefill_053}


def swk_base_universe_d3_049_swk_basefill_054(swk_base_universe_d2_049_swk_basefill_054):
    return _base_universe_d3(swk_base_universe_d2_049_swk_basefill_054, 49)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_049_swk_basefill_054'] = {'inputs': ['swk_base_universe_d2_049_swk_basefill_054'], 'func': swk_base_universe_d3_049_swk_basefill_054}


def swk_base_universe_d3_050_swk_basefill_055(swk_base_universe_d2_050_swk_basefill_055):
    return _base_universe_d3(swk_base_universe_d2_050_swk_basefill_055, 50)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_050_swk_basefill_055'] = {'inputs': ['swk_base_universe_d2_050_swk_basefill_055'], 'func': swk_base_universe_d3_050_swk_basefill_055}


def swk_base_universe_d3_051_swk_basefill_056(swk_base_universe_d2_051_swk_basefill_056):
    return _base_universe_d3(swk_base_universe_d2_051_swk_basefill_056, 51)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_051_swk_basefill_056'] = {'inputs': ['swk_base_universe_d2_051_swk_basefill_056'], 'func': swk_base_universe_d3_051_swk_basefill_056}


def swk_base_universe_d3_052_swk_basefill_057(swk_base_universe_d2_052_swk_basefill_057):
    return _base_universe_d3(swk_base_universe_d2_052_swk_basefill_057, 52)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_052_swk_basefill_057'] = {'inputs': ['swk_base_universe_d2_052_swk_basefill_057'], 'func': swk_base_universe_d3_052_swk_basefill_057}


def swk_base_universe_d3_053_swk_basefill_058(swk_base_universe_d2_053_swk_basefill_058):
    return _base_universe_d3(swk_base_universe_d2_053_swk_basefill_058, 53)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_053_swk_basefill_058'] = {'inputs': ['swk_base_universe_d2_053_swk_basefill_058'], 'func': swk_base_universe_d3_053_swk_basefill_058}


def swk_base_universe_d3_054_swk_basefill_059(swk_base_universe_d2_054_swk_basefill_059):
    return _base_universe_d3(swk_base_universe_d2_054_swk_basefill_059, 54)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_054_swk_basefill_059'] = {'inputs': ['swk_base_universe_d2_054_swk_basefill_059'], 'func': swk_base_universe_d3_054_swk_basefill_059}


def swk_base_universe_d3_055_swk_basefill_060(swk_base_universe_d2_055_swk_basefill_060):
    return _base_universe_d3(swk_base_universe_d2_055_swk_basefill_060, 55)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_055_swk_basefill_060'] = {'inputs': ['swk_base_universe_d2_055_swk_basefill_060'], 'func': swk_base_universe_d3_055_swk_basefill_060}


def swk_base_universe_d3_056_swk_basefill_061(swk_base_universe_d2_056_swk_basefill_061):
    return _base_universe_d3(swk_base_universe_d2_056_swk_basefill_061, 56)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_056_swk_basefill_061'] = {'inputs': ['swk_base_universe_d2_056_swk_basefill_061'], 'func': swk_base_universe_d3_056_swk_basefill_061}


def swk_base_universe_d3_057_swk_basefill_062(swk_base_universe_d2_057_swk_basefill_062):
    return _base_universe_d3(swk_base_universe_d2_057_swk_basefill_062, 57)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_057_swk_basefill_062'] = {'inputs': ['swk_base_universe_d2_057_swk_basefill_062'], 'func': swk_base_universe_d3_057_swk_basefill_062}


def swk_base_universe_d3_058_swk_basefill_063(swk_base_universe_d2_058_swk_basefill_063):
    return _base_universe_d3(swk_base_universe_d2_058_swk_basefill_063, 58)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_058_swk_basefill_063'] = {'inputs': ['swk_base_universe_d2_058_swk_basefill_063'], 'func': swk_base_universe_d3_058_swk_basefill_063}


def swk_base_universe_d3_059_swk_basefill_064(swk_base_universe_d2_059_swk_basefill_064):
    return _base_universe_d3(swk_base_universe_d2_059_swk_basefill_064, 59)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_059_swk_basefill_064'] = {'inputs': ['swk_base_universe_d2_059_swk_basefill_064'], 'func': swk_base_universe_d3_059_swk_basefill_064}


def swk_base_universe_d3_060_swk_basefill_065(swk_base_universe_d2_060_swk_basefill_065):
    return _base_universe_d3(swk_base_universe_d2_060_swk_basefill_065, 60)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_060_swk_basefill_065'] = {'inputs': ['swk_base_universe_d2_060_swk_basefill_065'], 'func': swk_base_universe_d3_060_swk_basefill_065}


def swk_base_universe_d3_061_swk_basefill_066(swk_base_universe_d2_061_swk_basefill_066):
    return _base_universe_d3(swk_base_universe_d2_061_swk_basefill_066, 61)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_061_swk_basefill_066'] = {'inputs': ['swk_base_universe_d2_061_swk_basefill_066'], 'func': swk_base_universe_d3_061_swk_basefill_066}


def swk_base_universe_d3_062_swk_basefill_067(swk_base_universe_d2_062_swk_basefill_067):
    return _base_universe_d3(swk_base_universe_d2_062_swk_basefill_067, 62)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_062_swk_basefill_067'] = {'inputs': ['swk_base_universe_d2_062_swk_basefill_067'], 'func': swk_base_universe_d3_062_swk_basefill_067}


def swk_base_universe_d3_063_swk_basefill_068(swk_base_universe_d2_063_swk_basefill_068):
    return _base_universe_d3(swk_base_universe_d2_063_swk_basefill_068, 63)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_063_swk_basefill_068'] = {'inputs': ['swk_base_universe_d2_063_swk_basefill_068'], 'func': swk_base_universe_d3_063_swk_basefill_068}


def swk_base_universe_d3_064_swk_basefill_069(swk_base_universe_d2_064_swk_basefill_069):
    return _base_universe_d3(swk_base_universe_d2_064_swk_basefill_069, 64)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_064_swk_basefill_069'] = {'inputs': ['swk_base_universe_d2_064_swk_basefill_069'], 'func': swk_base_universe_d3_064_swk_basefill_069}


def swk_base_universe_d3_065_swk_basefill_070(swk_base_universe_d2_065_swk_basefill_070):
    return _base_universe_d3(swk_base_universe_d2_065_swk_basefill_070, 65)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_065_swk_basefill_070'] = {'inputs': ['swk_base_universe_d2_065_swk_basefill_070'], 'func': swk_base_universe_d3_065_swk_basefill_070}


def swk_base_universe_d3_066_swk_basefill_071(swk_base_universe_d2_066_swk_basefill_071):
    return _base_universe_d3(swk_base_universe_d2_066_swk_basefill_071, 66)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_066_swk_basefill_071'] = {'inputs': ['swk_base_universe_d2_066_swk_basefill_071'], 'func': swk_base_universe_d3_066_swk_basefill_071}


def swk_base_universe_d3_067_swk_basefill_072(swk_base_universe_d2_067_swk_basefill_072):
    return _base_universe_d3(swk_base_universe_d2_067_swk_basefill_072, 67)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_067_swk_basefill_072'] = {'inputs': ['swk_base_universe_d2_067_swk_basefill_072'], 'func': swk_base_universe_d3_067_swk_basefill_072}


def swk_base_universe_d3_068_swk_basefill_073(swk_base_universe_d2_068_swk_basefill_073):
    return _base_universe_d3(swk_base_universe_d2_068_swk_basefill_073, 68)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_068_swk_basefill_073'] = {'inputs': ['swk_base_universe_d2_068_swk_basefill_073'], 'func': swk_base_universe_d3_068_swk_basefill_073}


def swk_base_universe_d3_069_swk_basefill_074(swk_base_universe_d2_069_swk_basefill_074):
    return _base_universe_d3(swk_base_universe_d2_069_swk_basefill_074, 69)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_069_swk_basefill_074'] = {'inputs': ['swk_base_universe_d2_069_swk_basefill_074'], 'func': swk_base_universe_d3_069_swk_basefill_074}


def swk_base_universe_d3_070_swk_basefill_075(swk_base_universe_d2_070_swk_basefill_075):
    return _base_universe_d3(swk_base_universe_d2_070_swk_basefill_075, 70)
SWK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['swk_base_universe_d3_070_swk_basefill_075'] = {'inputs': ['swk_base_universe_d2_070_swk_basefill_075'], 'func': swk_base_universe_d3_070_swk_basefill_075}

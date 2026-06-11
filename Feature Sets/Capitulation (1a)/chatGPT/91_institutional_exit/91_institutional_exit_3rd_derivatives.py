import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _align_quarterly_to_daily(x, close):
    """Forward-fill sparse Sharadar quarterly/event data to close.index."""
    return _s(x).reindex(_s(close).index).ffill()


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    return _s(a) / b


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



def iex_176_iex_001_holder_exit_1_accel_1(iex_151_iex_001_holder_exit_1_roc_1):
    feature = _s(iex_151_iex_001_holder_exit_1_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def iex_177_iex_007_holder_exit_1_accel_42(iex_152_iex_007_holder_exit_1_roc_42):
    feature = _s(iex_152_iex_007_holder_exit_1_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def iex_178_iex_013_holder_exit_1_accel_126(iex_153_iex_013_holder_exit_1_roc_126):
    feature = _s(iex_153_iex_013_holder_exit_1_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def iex_179_iex_019_holder_exit_1_accel_378(iex_154_iex_019_holder_exit_1_roc_378):
    feature = _s(iex_154_iex_019_holder_exit_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def iex_180_iex_025_holder_exit_1_accel_4(iex_155_iex_025_holder_exit_1_roc_4):
    feature = _s(iex_155_iex_025_holder_exit_1_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSTITUTIONAL_EXIT_REGISTRY_3RD_DERIVATIVES = {
    'iex_176_iex_001_holder_exit_1_accel_1': {'inputs': ['iex_151_iex_001_holder_exit_1_roc_1'], 'func': iex_176_iex_001_holder_exit_1_accel_1},
    'iex_177_iex_007_holder_exit_1_accel_42': {'inputs': ['iex_152_iex_007_holder_exit_1_roc_42'], 'func': iex_177_iex_007_holder_exit_1_accel_42},
    'iex_178_iex_013_holder_exit_1_accel_126': {'inputs': ['iex_153_iex_013_holder_exit_1_roc_126'], 'func': iex_178_iex_013_holder_exit_1_accel_126},
    'iex_179_iex_019_holder_exit_1_accel_378': {'inputs': ['iex_154_iex_019_holder_exit_1_roc_378'], 'func': iex_179_iex_019_holder_exit_1_accel_378},
    'iex_180_iex_025_holder_exit_1_accel_4': {'inputs': ['iex_155_iex_025_holder_exit_1_roc_4'], 'func': iex_180_iex_025_holder_exit_1_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ie_replacement_d3_001(ie_replacement_d2_001):
    feature = _clean(ie_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_001'] = {'inputs': ['ie_replacement_d2_001'], 'func': ie_replacement_d3_001}


def ie_replacement_d3_002(ie_replacement_d2_002):
    feature = _clean(ie_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_002'] = {'inputs': ['ie_replacement_d2_002'], 'func': ie_replacement_d3_002}


def ie_replacement_d3_003(ie_replacement_d2_003):
    feature = _clean(ie_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_003'] = {'inputs': ['ie_replacement_d2_003'], 'func': ie_replacement_d3_003}


def ie_replacement_d3_004(ie_replacement_d2_004):
    feature = _clean(ie_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_004'] = {'inputs': ['ie_replacement_d2_004'], 'func': ie_replacement_d3_004}


def ie_replacement_d3_005(ie_replacement_d2_005):
    feature = _clean(ie_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_005'] = {'inputs': ['ie_replacement_d2_005'], 'func': ie_replacement_d3_005}


def ie_replacement_d3_006(ie_replacement_d2_006):
    feature = _clean(ie_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_006'] = {'inputs': ['ie_replacement_d2_006'], 'func': ie_replacement_d3_006}


def ie_replacement_d3_007(ie_replacement_d2_007):
    feature = _clean(ie_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_007'] = {'inputs': ['ie_replacement_d2_007'], 'func': ie_replacement_d3_007}


def ie_replacement_d3_008(ie_replacement_d2_008):
    feature = _clean(ie_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_008'] = {'inputs': ['ie_replacement_d2_008'], 'func': ie_replacement_d3_008}


def ie_replacement_d3_009(ie_replacement_d2_009):
    feature = _clean(ie_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_009'] = {'inputs': ['ie_replacement_d2_009'], 'func': ie_replacement_d3_009}


def ie_replacement_d3_010(ie_replacement_d2_010):
    feature = _clean(ie_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_010'] = {'inputs': ['ie_replacement_d2_010'], 'func': ie_replacement_d3_010}


def ie_replacement_d3_011(ie_replacement_d2_011):
    feature = _clean(ie_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_011'] = {'inputs': ['ie_replacement_d2_011'], 'func': ie_replacement_d3_011}


def ie_replacement_d3_012(ie_replacement_d2_012):
    feature = _clean(ie_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_012'] = {'inputs': ['ie_replacement_d2_012'], 'func': ie_replacement_d3_012}


def ie_replacement_d3_013(ie_replacement_d2_013):
    feature = _clean(ie_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_013'] = {'inputs': ['ie_replacement_d2_013'], 'func': ie_replacement_d3_013}


def ie_replacement_d3_014(ie_replacement_d2_014):
    feature = _clean(ie_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_014'] = {'inputs': ['ie_replacement_d2_014'], 'func': ie_replacement_d3_014}


def ie_replacement_d3_015(ie_replacement_d2_015):
    feature = _clean(ie_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_015'] = {'inputs': ['ie_replacement_d2_015'], 'func': ie_replacement_d3_015}


def ie_replacement_d3_016(ie_replacement_d2_016):
    feature = _clean(ie_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_016'] = {'inputs': ['ie_replacement_d2_016'], 'func': ie_replacement_d3_016}


def ie_replacement_d3_017(ie_replacement_d2_017):
    feature = _clean(ie_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_017'] = {'inputs': ['ie_replacement_d2_017'], 'func': ie_replacement_d3_017}


def ie_replacement_d3_018(ie_replacement_d2_018):
    feature = _clean(ie_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_018'] = {'inputs': ['ie_replacement_d2_018'], 'func': ie_replacement_d3_018}


def ie_replacement_d3_019(ie_replacement_d2_019):
    feature = _clean(ie_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_019'] = {'inputs': ['ie_replacement_d2_019'], 'func': ie_replacement_d3_019}


def ie_replacement_d3_020(ie_replacement_d2_020):
    feature = _clean(ie_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_020'] = {'inputs': ['ie_replacement_d2_020'], 'func': ie_replacement_d3_020}


def ie_replacement_d3_021(ie_replacement_d2_021):
    feature = _clean(ie_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_021'] = {'inputs': ['ie_replacement_d2_021'], 'func': ie_replacement_d3_021}


def ie_replacement_d3_022(ie_replacement_d2_022):
    feature = _clean(ie_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_022'] = {'inputs': ['ie_replacement_d2_022'], 'func': ie_replacement_d3_022}


def ie_replacement_d3_023(ie_replacement_d2_023):
    feature = _clean(ie_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_023'] = {'inputs': ['ie_replacement_d2_023'], 'func': ie_replacement_d3_023}


def ie_replacement_d3_024(ie_replacement_d2_024):
    feature = _clean(ie_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_024'] = {'inputs': ['ie_replacement_d2_024'], 'func': ie_replacement_d3_024}


def ie_replacement_d3_025(ie_replacement_d2_025):
    feature = _clean(ie_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_025'] = {'inputs': ['ie_replacement_d2_025'], 'func': ie_replacement_d3_025}


def ie_replacement_d3_026(ie_replacement_d2_026):
    feature = _clean(ie_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_026'] = {'inputs': ['ie_replacement_d2_026'], 'func': ie_replacement_d3_026}


def ie_replacement_d3_027(ie_replacement_d2_027):
    feature = _clean(ie_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_027'] = {'inputs': ['ie_replacement_d2_027'], 'func': ie_replacement_d3_027}


def ie_replacement_d3_028(ie_replacement_d2_028):
    feature = _clean(ie_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_028'] = {'inputs': ['ie_replacement_d2_028'], 'func': ie_replacement_d3_028}


def ie_replacement_d3_029(ie_replacement_d2_029):
    feature = _clean(ie_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_029'] = {'inputs': ['ie_replacement_d2_029'], 'func': ie_replacement_d3_029}


def ie_replacement_d3_030(ie_replacement_d2_030):
    feature = _clean(ie_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_030'] = {'inputs': ['ie_replacement_d2_030'], 'func': ie_replacement_d3_030}


def ie_replacement_d3_031(ie_replacement_d2_031):
    feature = _clean(ie_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_031'] = {'inputs': ['ie_replacement_d2_031'], 'func': ie_replacement_d3_031}


def ie_replacement_d3_032(ie_replacement_d2_032):
    feature = _clean(ie_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_032'] = {'inputs': ['ie_replacement_d2_032'], 'func': ie_replacement_d3_032}


def ie_replacement_d3_033(ie_replacement_d2_033):
    feature = _clean(ie_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_033'] = {'inputs': ['ie_replacement_d2_033'], 'func': ie_replacement_d3_033}


def ie_replacement_d3_034(ie_replacement_d2_034):
    feature = _clean(ie_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_034'] = {'inputs': ['ie_replacement_d2_034'], 'func': ie_replacement_d3_034}


def ie_replacement_d3_035(ie_replacement_d2_035):
    feature = _clean(ie_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_035'] = {'inputs': ['ie_replacement_d2_035'], 'func': ie_replacement_d3_035}


def ie_replacement_d3_036(ie_replacement_d2_036):
    feature = _clean(ie_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_036'] = {'inputs': ['ie_replacement_d2_036'], 'func': ie_replacement_d3_036}


def ie_replacement_d3_037(ie_replacement_d2_037):
    feature = _clean(ie_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_037'] = {'inputs': ['ie_replacement_d2_037'], 'func': ie_replacement_d3_037}


def ie_replacement_d3_038(ie_replacement_d2_038):
    feature = _clean(ie_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_038'] = {'inputs': ['ie_replacement_d2_038'], 'func': ie_replacement_d3_038}


def ie_replacement_d3_039(ie_replacement_d2_039):
    feature = _clean(ie_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_039'] = {'inputs': ['ie_replacement_d2_039'], 'func': ie_replacement_d3_039}


def ie_replacement_d3_040(ie_replacement_d2_040):
    feature = _clean(ie_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_040'] = {'inputs': ['ie_replacement_d2_040'], 'func': ie_replacement_d3_040}


def ie_replacement_d3_041(ie_replacement_d2_041):
    feature = _clean(ie_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_041'] = {'inputs': ['ie_replacement_d2_041'], 'func': ie_replacement_d3_041}


def ie_replacement_d3_042(ie_replacement_d2_042):
    feature = _clean(ie_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_042'] = {'inputs': ['ie_replacement_d2_042'], 'func': ie_replacement_d3_042}


def ie_replacement_d3_043(ie_replacement_d2_043):
    feature = _clean(ie_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_043'] = {'inputs': ['ie_replacement_d2_043'], 'func': ie_replacement_d3_043}


def ie_replacement_d3_044(ie_replacement_d2_044):
    feature = _clean(ie_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_044'] = {'inputs': ['ie_replacement_d2_044'], 'func': ie_replacement_d3_044}


def ie_replacement_d3_045(ie_replacement_d2_045):
    feature = _clean(ie_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_045'] = {'inputs': ['ie_replacement_d2_045'], 'func': ie_replacement_d3_045}


def ie_replacement_d3_046(ie_replacement_d2_046):
    feature = _clean(ie_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_046'] = {'inputs': ['ie_replacement_d2_046'], 'func': ie_replacement_d3_046}


def ie_replacement_d3_047(ie_replacement_d2_047):
    feature = _clean(ie_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_047'] = {'inputs': ['ie_replacement_d2_047'], 'func': ie_replacement_d3_047}


def ie_replacement_d3_048(ie_replacement_d2_048):
    feature = _clean(ie_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_048'] = {'inputs': ['ie_replacement_d2_048'], 'func': ie_replacement_d3_048}


def ie_replacement_d3_049(ie_replacement_d2_049):
    feature = _clean(ie_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_049'] = {'inputs': ['ie_replacement_d2_049'], 'func': ie_replacement_d3_049}


def ie_replacement_d3_050(ie_replacement_d2_050):
    feature = _clean(ie_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_050'] = {'inputs': ['ie_replacement_d2_050'], 'func': ie_replacement_d3_050}


def ie_replacement_d3_051(ie_replacement_d2_051):
    feature = _clean(ie_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_051'] = {'inputs': ['ie_replacement_d2_051'], 'func': ie_replacement_d3_051}


def ie_replacement_d3_052(ie_replacement_d2_052):
    feature = _clean(ie_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_052'] = {'inputs': ['ie_replacement_d2_052'], 'func': ie_replacement_d3_052}


def ie_replacement_d3_053(ie_replacement_d2_053):
    feature = _clean(ie_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_053'] = {'inputs': ['ie_replacement_d2_053'], 'func': ie_replacement_d3_053}


def ie_replacement_d3_054(ie_replacement_d2_054):
    feature = _clean(ie_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_054'] = {'inputs': ['ie_replacement_d2_054'], 'func': ie_replacement_d3_054}


def ie_replacement_d3_055(ie_replacement_d2_055):
    feature = _clean(ie_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_055'] = {'inputs': ['ie_replacement_d2_055'], 'func': ie_replacement_d3_055}


def ie_replacement_d3_056(ie_replacement_d2_056):
    feature = _clean(ie_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_056'] = {'inputs': ['ie_replacement_d2_056'], 'func': ie_replacement_d3_056}


def ie_replacement_d3_057(ie_replacement_d2_057):
    feature = _clean(ie_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_057'] = {'inputs': ['ie_replacement_d2_057'], 'func': ie_replacement_d3_057}


def ie_replacement_d3_058(ie_replacement_d2_058):
    feature = _clean(ie_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_058'] = {'inputs': ['ie_replacement_d2_058'], 'func': ie_replacement_d3_058}


def ie_replacement_d3_059(ie_replacement_d2_059):
    feature = _clean(ie_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_059'] = {'inputs': ['ie_replacement_d2_059'], 'func': ie_replacement_d3_059}


def ie_replacement_d3_060(ie_replacement_d2_060):
    feature = _clean(ie_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_060'] = {'inputs': ['ie_replacement_d2_060'], 'func': ie_replacement_d3_060}


def ie_replacement_d3_061(ie_replacement_d2_061):
    feature = _clean(ie_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_061'] = {'inputs': ['ie_replacement_d2_061'], 'func': ie_replacement_d3_061}


def ie_replacement_d3_062(ie_replacement_d2_062):
    feature = _clean(ie_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_062'] = {'inputs': ['ie_replacement_d2_062'], 'func': ie_replacement_d3_062}


def ie_replacement_d3_063(ie_replacement_d2_063):
    feature = _clean(ie_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_063'] = {'inputs': ['ie_replacement_d2_063'], 'func': ie_replacement_d3_063}


def ie_replacement_d3_064(ie_replacement_d2_064):
    feature = _clean(ie_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_064'] = {'inputs': ['ie_replacement_d2_064'], 'func': ie_replacement_d3_064}


def ie_replacement_d3_065(ie_replacement_d2_065):
    feature = _clean(ie_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_065'] = {'inputs': ['ie_replacement_d2_065'], 'func': ie_replacement_d3_065}


def ie_replacement_d3_066(ie_replacement_d2_066):
    feature = _clean(ie_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_066'] = {'inputs': ['ie_replacement_d2_066'], 'func': ie_replacement_d3_066}


def ie_replacement_d3_067(ie_replacement_d2_067):
    feature = _clean(ie_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_067'] = {'inputs': ['ie_replacement_d2_067'], 'func': ie_replacement_d3_067}


def ie_replacement_d3_068(ie_replacement_d2_068):
    feature = _clean(ie_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_068'] = {'inputs': ['ie_replacement_d2_068'], 'func': ie_replacement_d3_068}


def ie_replacement_d3_069(ie_replacement_d2_069):
    feature = _clean(ie_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_069'] = {'inputs': ['ie_replacement_d2_069'], 'func': ie_replacement_d3_069}


def ie_replacement_d3_070(ie_replacement_d2_070):
    feature = _clean(ie_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_070'] = {'inputs': ['ie_replacement_d2_070'], 'func': ie_replacement_d3_070}


def ie_replacement_d3_071(ie_replacement_d2_071):
    feature = _clean(ie_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_071'] = {'inputs': ['ie_replacement_d2_071'], 'func': ie_replacement_d3_071}


def ie_replacement_d3_072(ie_replacement_d2_072):
    feature = _clean(ie_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_072'] = {'inputs': ['ie_replacement_d2_072'], 'func': ie_replacement_d3_072}


def ie_replacement_d3_073(ie_replacement_d2_073):
    feature = _clean(ie_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_073'] = {'inputs': ['ie_replacement_d2_073'], 'func': ie_replacement_d3_073}


def ie_replacement_d3_074(ie_replacement_d2_074):
    feature = _clean(ie_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_074'] = {'inputs': ['ie_replacement_d2_074'], 'func': ie_replacement_d3_074}


def ie_replacement_d3_075(ie_replacement_d2_075):
    feature = _clean(ie_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_075'] = {'inputs': ['ie_replacement_d2_075'], 'func': ie_replacement_d3_075}


def ie_replacement_d3_076(ie_replacement_d2_076):
    feature = _clean(ie_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_076'] = {'inputs': ['ie_replacement_d2_076'], 'func': ie_replacement_d3_076}


def ie_replacement_d3_077(ie_replacement_d2_077):
    feature = _clean(ie_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_077'] = {'inputs': ['ie_replacement_d2_077'], 'func': ie_replacement_d3_077}


def ie_replacement_d3_078(ie_replacement_d2_078):
    feature = _clean(ie_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_078'] = {'inputs': ['ie_replacement_d2_078'], 'func': ie_replacement_d3_078}


def ie_replacement_d3_079(ie_replacement_d2_079):
    feature = _clean(ie_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_079'] = {'inputs': ['ie_replacement_d2_079'], 'func': ie_replacement_d3_079}


def ie_replacement_d3_080(ie_replacement_d2_080):
    feature = _clean(ie_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_080'] = {'inputs': ['ie_replacement_d2_080'], 'func': ie_replacement_d3_080}


def ie_replacement_d3_081(ie_replacement_d2_081):
    feature = _clean(ie_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_081'] = {'inputs': ['ie_replacement_d2_081'], 'func': ie_replacement_d3_081}


def ie_replacement_d3_082(ie_replacement_d2_082):
    feature = _clean(ie_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_082'] = {'inputs': ['ie_replacement_d2_082'], 'func': ie_replacement_d3_082}


def ie_replacement_d3_083(ie_replacement_d2_083):
    feature = _clean(ie_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_083'] = {'inputs': ['ie_replacement_d2_083'], 'func': ie_replacement_d3_083}


def ie_replacement_d3_084(ie_replacement_d2_084):
    feature = _clean(ie_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_084'] = {'inputs': ['ie_replacement_d2_084'], 'func': ie_replacement_d3_084}


def ie_replacement_d3_085(ie_replacement_d2_085):
    feature = _clean(ie_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_085'] = {'inputs': ['ie_replacement_d2_085'], 'func': ie_replacement_d3_085}


def ie_replacement_d3_086(ie_replacement_d2_086):
    feature = _clean(ie_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_086'] = {'inputs': ['ie_replacement_d2_086'], 'func': ie_replacement_d3_086}


def ie_replacement_d3_087(ie_replacement_d2_087):
    feature = _clean(ie_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_087'] = {'inputs': ['ie_replacement_d2_087'], 'func': ie_replacement_d3_087}


def ie_replacement_d3_088(ie_replacement_d2_088):
    feature = _clean(ie_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_088'] = {'inputs': ['ie_replacement_d2_088'], 'func': ie_replacement_d3_088}


def ie_replacement_d3_089(ie_replacement_d2_089):
    feature = _clean(ie_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_089'] = {'inputs': ['ie_replacement_d2_089'], 'func': ie_replacement_d3_089}


def ie_replacement_d3_090(ie_replacement_d2_090):
    feature = _clean(ie_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_090'] = {'inputs': ['ie_replacement_d2_090'], 'func': ie_replacement_d3_090}


def ie_replacement_d3_091(ie_replacement_d2_091):
    feature = _clean(ie_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_091'] = {'inputs': ['ie_replacement_d2_091'], 'func': ie_replacement_d3_091}


def ie_replacement_d3_092(ie_replacement_d2_092):
    feature = _clean(ie_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_092'] = {'inputs': ['ie_replacement_d2_092'], 'func': ie_replacement_d3_092}


def ie_replacement_d3_093(ie_replacement_d2_093):
    feature = _clean(ie_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_093'] = {'inputs': ['ie_replacement_d2_093'], 'func': ie_replacement_d3_093}


def ie_replacement_d3_094(ie_replacement_d2_094):
    feature = _clean(ie_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_094'] = {'inputs': ['ie_replacement_d2_094'], 'func': ie_replacement_d3_094}


def ie_replacement_d3_095(ie_replacement_d2_095):
    feature = _clean(ie_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_095'] = {'inputs': ['ie_replacement_d2_095'], 'func': ie_replacement_d3_095}


def ie_replacement_d3_096(ie_replacement_d2_096):
    feature = _clean(ie_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_096'] = {'inputs': ['ie_replacement_d2_096'], 'func': ie_replacement_d3_096}


def ie_replacement_d3_097(ie_replacement_d2_097):
    feature = _clean(ie_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_097'] = {'inputs': ['ie_replacement_d2_097'], 'func': ie_replacement_d3_097}


def ie_replacement_d3_098(ie_replacement_d2_098):
    feature = _clean(ie_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_098'] = {'inputs': ['ie_replacement_d2_098'], 'func': ie_replacement_d3_098}


def ie_replacement_d3_099(ie_replacement_d2_099):
    feature = _clean(ie_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_099'] = {'inputs': ['ie_replacement_d2_099'], 'func': ie_replacement_d3_099}


def ie_replacement_d3_100(ie_replacement_d2_100):
    feature = _clean(ie_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_100'] = {'inputs': ['ie_replacement_d2_100'], 'func': ie_replacement_d3_100}


def ie_replacement_d3_101(ie_replacement_d2_101):
    feature = _clean(ie_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_101'] = {'inputs': ['ie_replacement_d2_101'], 'func': ie_replacement_d3_101}


def ie_replacement_d3_102(ie_replacement_d2_102):
    feature = _clean(ie_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_102'] = {'inputs': ['ie_replacement_d2_102'], 'func': ie_replacement_d3_102}


def ie_replacement_d3_103(ie_replacement_d2_103):
    feature = _clean(ie_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_103'] = {'inputs': ['ie_replacement_d2_103'], 'func': ie_replacement_d3_103}


def ie_replacement_d3_104(ie_replacement_d2_104):
    feature = _clean(ie_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_104'] = {'inputs': ['ie_replacement_d2_104'], 'func': ie_replacement_d3_104}


def ie_replacement_d3_105(ie_replacement_d2_105):
    feature = _clean(ie_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_105'] = {'inputs': ['ie_replacement_d2_105'], 'func': ie_replacement_d3_105}


def ie_replacement_d3_106(ie_replacement_d2_106):
    feature = _clean(ie_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_106'] = {'inputs': ['ie_replacement_d2_106'], 'func': ie_replacement_d3_106}


def ie_replacement_d3_107(ie_replacement_d2_107):
    feature = _clean(ie_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_107'] = {'inputs': ['ie_replacement_d2_107'], 'func': ie_replacement_d3_107}


def ie_replacement_d3_108(ie_replacement_d2_108):
    feature = _clean(ie_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_108'] = {'inputs': ['ie_replacement_d2_108'], 'func': ie_replacement_d3_108}


def ie_replacement_d3_109(ie_replacement_d2_109):
    feature = _clean(ie_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_109'] = {'inputs': ['ie_replacement_d2_109'], 'func': ie_replacement_d3_109}


def ie_replacement_d3_110(ie_replacement_d2_110):
    feature = _clean(ie_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_110'] = {'inputs': ['ie_replacement_d2_110'], 'func': ie_replacement_d3_110}


def ie_replacement_d3_111(ie_replacement_d2_111):
    feature = _clean(ie_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_111'] = {'inputs': ['ie_replacement_d2_111'], 'func': ie_replacement_d3_111}


def ie_replacement_d3_112(ie_replacement_d2_112):
    feature = _clean(ie_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_112'] = {'inputs': ['ie_replacement_d2_112'], 'func': ie_replacement_d3_112}


def ie_replacement_d3_113(ie_replacement_d2_113):
    feature = _clean(ie_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_113'] = {'inputs': ['ie_replacement_d2_113'], 'func': ie_replacement_d3_113}


def ie_replacement_d3_114(ie_replacement_d2_114):
    feature = _clean(ie_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_114'] = {'inputs': ['ie_replacement_d2_114'], 'func': ie_replacement_d3_114}


def ie_replacement_d3_115(ie_replacement_d2_115):
    feature = _clean(ie_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_115'] = {'inputs': ['ie_replacement_d2_115'], 'func': ie_replacement_d3_115}


def ie_replacement_d3_116(ie_replacement_d2_116):
    feature = _clean(ie_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_116'] = {'inputs': ['ie_replacement_d2_116'], 'func': ie_replacement_d3_116}


def ie_replacement_d3_117(ie_replacement_d2_117):
    feature = _clean(ie_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_117'] = {'inputs': ['ie_replacement_d2_117'], 'func': ie_replacement_d3_117}


def ie_replacement_d3_118(ie_replacement_d2_118):
    feature = _clean(ie_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_118'] = {'inputs': ['ie_replacement_d2_118'], 'func': ie_replacement_d3_118}


def ie_replacement_d3_119(ie_replacement_d2_119):
    feature = _clean(ie_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_119'] = {'inputs': ['ie_replacement_d2_119'], 'func': ie_replacement_d3_119}


def ie_replacement_d3_120(ie_replacement_d2_120):
    feature = _clean(ie_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_120'] = {'inputs': ['ie_replacement_d2_120'], 'func': ie_replacement_d3_120}


def ie_replacement_d3_121(ie_replacement_d2_121):
    feature = _clean(ie_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_121'] = {'inputs': ['ie_replacement_d2_121'], 'func': ie_replacement_d3_121}


def ie_replacement_d3_122(ie_replacement_d2_122):
    feature = _clean(ie_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_122'] = {'inputs': ['ie_replacement_d2_122'], 'func': ie_replacement_d3_122}


def ie_replacement_d3_123(ie_replacement_d2_123):
    feature = _clean(ie_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_123'] = {'inputs': ['ie_replacement_d2_123'], 'func': ie_replacement_d3_123}


def ie_replacement_d3_124(ie_replacement_d2_124):
    feature = _clean(ie_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_124'] = {'inputs': ['ie_replacement_d2_124'], 'func': ie_replacement_d3_124}


def ie_replacement_d3_125(ie_replacement_d2_125):
    feature = _clean(ie_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_125'] = {'inputs': ['ie_replacement_d2_125'], 'func': ie_replacement_d3_125}


def ie_replacement_d3_126(ie_replacement_d2_126):
    feature = _clean(ie_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_126'] = {'inputs': ['ie_replacement_d2_126'], 'func': ie_replacement_d3_126}


def ie_replacement_d3_127(ie_replacement_d2_127):
    feature = _clean(ie_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_127'] = {'inputs': ['ie_replacement_d2_127'], 'func': ie_replacement_d3_127}


def ie_replacement_d3_128(ie_replacement_d2_128):
    feature = _clean(ie_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_128'] = {'inputs': ['ie_replacement_d2_128'], 'func': ie_replacement_d3_128}


def ie_replacement_d3_129(ie_replacement_d2_129):
    feature = _clean(ie_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_129'] = {'inputs': ['ie_replacement_d2_129'], 'func': ie_replacement_d3_129}


def ie_replacement_d3_130(ie_replacement_d2_130):
    feature = _clean(ie_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_130'] = {'inputs': ['ie_replacement_d2_130'], 'func': ie_replacement_d3_130}


def ie_replacement_d3_131(ie_replacement_d2_131):
    feature = _clean(ie_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_131'] = {'inputs': ['ie_replacement_d2_131'], 'func': ie_replacement_d3_131}


def ie_replacement_d3_132(ie_replacement_d2_132):
    feature = _clean(ie_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_132'] = {'inputs': ['ie_replacement_d2_132'], 'func': ie_replacement_d3_132}


def ie_replacement_d3_133(ie_replacement_d2_133):
    feature = _clean(ie_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_133'] = {'inputs': ['ie_replacement_d2_133'], 'func': ie_replacement_d3_133}


def ie_replacement_d3_134(ie_replacement_d2_134):
    feature = _clean(ie_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_134'] = {'inputs': ['ie_replacement_d2_134'], 'func': ie_replacement_d3_134}


def ie_replacement_d3_135(ie_replacement_d2_135):
    feature = _clean(ie_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_135'] = {'inputs': ['ie_replacement_d2_135'], 'func': ie_replacement_d3_135}


def ie_replacement_d3_136(ie_replacement_d2_136):
    feature = _clean(ie_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_136'] = {'inputs': ['ie_replacement_d2_136'], 'func': ie_replacement_d3_136}


def ie_replacement_d3_137(ie_replacement_d2_137):
    feature = _clean(ie_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_137'] = {'inputs': ['ie_replacement_d2_137'], 'func': ie_replacement_d3_137}


def ie_replacement_d3_138(ie_replacement_d2_138):
    feature = _clean(ie_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_138'] = {'inputs': ['ie_replacement_d2_138'], 'func': ie_replacement_d3_138}


def ie_replacement_d3_139(ie_replacement_d2_139):
    feature = _clean(ie_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_139'] = {'inputs': ['ie_replacement_d2_139'], 'func': ie_replacement_d3_139}


def ie_replacement_d3_140(ie_replacement_d2_140):
    feature = _clean(ie_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_140'] = {'inputs': ['ie_replacement_d2_140'], 'func': ie_replacement_d3_140}


def ie_replacement_d3_141(ie_replacement_d2_141):
    feature = _clean(ie_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_141'] = {'inputs': ['ie_replacement_d2_141'], 'func': ie_replacement_d3_141}


def ie_replacement_d3_142(ie_replacement_d2_142):
    feature = _clean(ie_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_142'] = {'inputs': ['ie_replacement_d2_142'], 'func': ie_replacement_d3_142}


def ie_replacement_d3_143(ie_replacement_d2_143):
    feature = _clean(ie_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_143'] = {'inputs': ['ie_replacement_d2_143'], 'func': ie_replacement_d3_143}


def ie_replacement_d3_144(ie_replacement_d2_144):
    feature = _clean(ie_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_144'] = {'inputs': ['ie_replacement_d2_144'], 'func': ie_replacement_d3_144}


def ie_replacement_d3_145(ie_replacement_d2_145):
    feature = _clean(ie_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_145'] = {'inputs': ['ie_replacement_d2_145'], 'func': ie_replacement_d3_145}


def ie_replacement_d3_146(ie_replacement_d2_146):
    feature = _clean(ie_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_146'] = {'inputs': ['ie_replacement_d2_146'], 'func': ie_replacement_d3_146}


def ie_replacement_d3_147(ie_replacement_d2_147):
    feature = _clean(ie_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_147'] = {'inputs': ['ie_replacement_d2_147'], 'func': ie_replacement_d3_147}


def ie_replacement_d3_148(ie_replacement_d2_148):
    feature = _clean(ie_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_148'] = {'inputs': ['ie_replacement_d2_148'], 'func': ie_replacement_d3_148}


def ie_replacement_d3_149(ie_replacement_d2_149):
    feature = _clean(ie_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_149'] = {'inputs': ['ie_replacement_d2_149'], 'func': ie_replacement_d3_149}


def ie_replacement_d3_150(ie_replacement_d2_150):
    feature = _clean(ie_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_150'] = {'inputs': ['ie_replacement_d2_150'], 'func': ie_replacement_d3_150}


def ie_replacement_d3_151(ie_replacement_d2_151):
    feature = _clean(ie_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_151'] = {'inputs': ['ie_replacement_d2_151'], 'func': ie_replacement_d3_151}


def ie_replacement_d3_152(ie_replacement_d2_152):
    feature = _clean(ie_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_152'] = {'inputs': ['ie_replacement_d2_152'], 'func': ie_replacement_d3_152}


def ie_replacement_d3_153(ie_replacement_d2_153):
    feature = _clean(ie_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_153'] = {'inputs': ['ie_replacement_d2_153'], 'func': ie_replacement_d3_153}


def ie_replacement_d3_154(ie_replacement_d2_154):
    feature = _clean(ie_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_154'] = {'inputs': ['ie_replacement_d2_154'], 'func': ie_replacement_d3_154}


def ie_replacement_d3_155(ie_replacement_d2_155):
    feature = _clean(ie_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_155'] = {'inputs': ['ie_replacement_d2_155'], 'func': ie_replacement_d3_155}


def ie_replacement_d3_156(ie_replacement_d2_156):
    feature = _clean(ie_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_156'] = {'inputs': ['ie_replacement_d2_156'], 'func': ie_replacement_d3_156}


def ie_replacement_d3_157(ie_replacement_d2_157):
    feature = _clean(ie_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_157'] = {'inputs': ['ie_replacement_d2_157'], 'func': ie_replacement_d3_157}


def ie_replacement_d3_158(ie_replacement_d2_158):
    feature = _clean(ie_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_158'] = {'inputs': ['ie_replacement_d2_158'], 'func': ie_replacement_d3_158}


def ie_replacement_d3_159(ie_replacement_d2_159):
    feature = _clean(ie_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_159'] = {'inputs': ['ie_replacement_d2_159'], 'func': ie_replacement_d3_159}


def ie_replacement_d3_160(ie_replacement_d2_160):
    feature = _clean(ie_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_160'] = {'inputs': ['ie_replacement_d2_160'], 'func': ie_replacement_d3_160}


def ie_replacement_d3_161(ie_replacement_d2_161):
    feature = _clean(ie_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_161'] = {'inputs': ['ie_replacement_d2_161'], 'func': ie_replacement_d3_161}


def ie_replacement_d3_162(ie_replacement_d2_162):
    feature = _clean(ie_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_162'] = {'inputs': ['ie_replacement_d2_162'], 'func': ie_replacement_d3_162}


def ie_replacement_d3_163(ie_replacement_d2_163):
    feature = _clean(ie_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_163'] = {'inputs': ['ie_replacement_d2_163'], 'func': ie_replacement_d3_163}


def ie_replacement_d3_164(ie_replacement_d2_164):
    feature = _clean(ie_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_164'] = {'inputs': ['ie_replacement_d2_164'], 'func': ie_replacement_d3_164}


def ie_replacement_d3_165(ie_replacement_d2_165):
    feature = _clean(ie_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_165'] = {'inputs': ['ie_replacement_d2_165'], 'func': ie_replacement_d3_165}


def ie_replacement_d3_166(ie_replacement_d2_166):
    feature = _clean(ie_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_166'] = {'inputs': ['ie_replacement_d2_166'], 'func': ie_replacement_d3_166}


def ie_replacement_d3_167(ie_replacement_d2_167):
    feature = _clean(ie_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_167'] = {'inputs': ['ie_replacement_d2_167'], 'func': ie_replacement_d3_167}


def ie_replacement_d3_168(ie_replacement_d2_168):
    feature = _clean(ie_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_168'] = {'inputs': ['ie_replacement_d2_168'], 'func': ie_replacement_d3_168}


def ie_replacement_d3_169(ie_replacement_d2_169):
    feature = _clean(ie_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_169'] = {'inputs': ['ie_replacement_d2_169'], 'func': ie_replacement_d3_169}


def ie_replacement_d3_170(ie_replacement_d2_170):
    feature = _clean(ie_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
IE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ie_replacement_d3_170'] = {'inputs': ['ie_replacement_d2_170'], 'func': ie_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def iex_base_universe_d3_001_iex_003_top_holder_concentration_63(iex_base_universe_d2_001_iex_003_top_holder_concentration_63):
    return _base_universe_d3(iex_base_universe_d2_001_iex_003_top_holder_concentration_63, 1)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_001_iex_003_top_holder_concentration_63'] = {'inputs': ['iex_base_universe_d2_001_iex_003_top_holder_concentration_63'], 'func': iex_base_universe_d3_001_iex_003_top_holder_concentration_63}


def iex_base_universe_d3_002_iex_004_institutional_net_flow_84(iex_base_universe_d2_002_iex_004_institutional_net_flow_84):
    return _base_universe_d3(iex_base_universe_d2_002_iex_004_institutional_net_flow_84, 2)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_002_iex_004_institutional_net_flow_84'] = {'inputs': ['iex_base_universe_d2_002_iex_004_institutional_net_flow_84'], 'func': iex_base_universe_d3_002_iex_004_institutional_net_flow_84}


def iex_base_universe_d3_003_iex_005_forced_selling_pressure_126(iex_base_universe_d2_003_iex_005_forced_selling_pressure_126):
    return _base_universe_d3(iex_base_universe_d2_003_iex_005_forced_selling_pressure_126, 3)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_003_iex_005_forced_selling_pressure_126'] = {'inputs': ['iex_base_universe_d2_003_iex_005_forced_selling_pressure_126'], 'func': iex_base_universe_d3_003_iex_005_forced_selling_pressure_126}


def iex_base_universe_d3_004_iex_006_holder_base_volatility_189(iex_base_universe_d2_004_iex_006_holder_base_volatility_189):
    return _base_universe_d3(iex_base_universe_d2_004_iex_006_holder_base_volatility_189, 4)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_004_iex_006_holder_base_volatility_189'] = {'inputs': ['iex_base_universe_d2_004_iex_006_holder_base_volatility_189'], 'func': iex_base_universe_d3_004_iex_006_holder_base_volatility_189}


def iex_base_universe_d3_005_iex_009_top_holder_concentration_504(iex_base_universe_d2_005_iex_009_top_holder_concentration_504):
    return _base_universe_d3(iex_base_universe_d2_005_iex_009_top_holder_concentration_504, 5)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_005_iex_009_top_holder_concentration_504'] = {'inputs': ['iex_base_universe_d2_005_iex_009_top_holder_concentration_504'], 'func': iex_base_universe_d3_005_iex_009_top_holder_concentration_504}


def iex_base_universe_d3_006_iex_010_institutional_net_flow_756(iex_base_universe_d2_006_iex_010_institutional_net_flow_756):
    return _base_universe_d3(iex_base_universe_d2_006_iex_010_institutional_net_flow_756, 6)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_006_iex_010_institutional_net_flow_756'] = {'inputs': ['iex_base_universe_d2_006_iex_010_institutional_net_flow_756'], 'func': iex_base_universe_d3_006_iex_010_institutional_net_flow_756}


def iex_base_universe_d3_007_iex_011_forced_selling_pressure_1008(iex_base_universe_d2_007_iex_011_forced_selling_pressure_1008):
    return _base_universe_d3(iex_base_universe_d2_007_iex_011_forced_selling_pressure_1008, 7)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_007_iex_011_forced_selling_pressure_1008'] = {'inputs': ['iex_base_universe_d2_007_iex_011_forced_selling_pressure_1008'], 'func': iex_base_universe_d3_007_iex_011_forced_selling_pressure_1008}


def iex_base_universe_d3_008_iex_012_holder_base_volatility_1260(iex_base_universe_d2_008_iex_012_holder_base_volatility_1260):
    return _base_universe_d3(iex_base_universe_d2_008_iex_012_holder_base_volatility_1260, 8)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_008_iex_012_holder_base_volatility_1260'] = {'inputs': ['iex_base_universe_d2_008_iex_012_holder_base_volatility_1260'], 'func': iex_base_universe_d3_008_iex_012_holder_base_volatility_1260}


def iex_base_universe_d3_009_iex_015_top_holder_concentration_252(iex_base_universe_d2_009_iex_015_top_holder_concentration_252):
    return _base_universe_d3(iex_base_universe_d2_009_iex_015_top_holder_concentration_252, 9)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_009_iex_015_top_holder_concentration_252'] = {'inputs': ['iex_base_universe_d2_009_iex_015_top_holder_concentration_252'], 'func': iex_base_universe_d3_009_iex_015_top_holder_concentration_252}


def iex_base_universe_d3_010_iex_016_institutional_net_flow_21(iex_base_universe_d2_010_iex_016_institutional_net_flow_21):
    return _base_universe_d3(iex_base_universe_d2_010_iex_016_institutional_net_flow_21, 10)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_010_iex_016_institutional_net_flow_21'] = {'inputs': ['iex_base_universe_d2_010_iex_016_institutional_net_flow_21'], 'func': iex_base_universe_d3_010_iex_016_institutional_net_flow_21}


def iex_base_universe_d3_011_iex_017_forced_selling_pressure_42(iex_base_universe_d2_011_iex_017_forced_selling_pressure_42):
    return _base_universe_d3(iex_base_universe_d2_011_iex_017_forced_selling_pressure_42, 11)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_011_iex_017_forced_selling_pressure_42'] = {'inputs': ['iex_base_universe_d2_011_iex_017_forced_selling_pressure_42'], 'func': iex_base_universe_d3_011_iex_017_forced_selling_pressure_42}


def iex_base_universe_d3_012_iex_018_holder_base_volatility_63(iex_base_universe_d2_012_iex_018_holder_base_volatility_63):
    return _base_universe_d3(iex_base_universe_d2_012_iex_018_holder_base_volatility_63, 12)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_012_iex_018_holder_base_volatility_63'] = {'inputs': ['iex_base_universe_d2_012_iex_018_holder_base_volatility_63'], 'func': iex_base_universe_d3_012_iex_018_holder_base_volatility_63}


def iex_base_universe_d3_013_iex_021_top_holder_concentration_189(iex_base_universe_d2_013_iex_021_top_holder_concentration_189):
    return _base_universe_d3(iex_base_universe_d2_013_iex_021_top_holder_concentration_189, 13)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_013_iex_021_top_holder_concentration_189'] = {'inputs': ['iex_base_universe_d2_013_iex_021_top_holder_concentration_189'], 'func': iex_base_universe_d3_013_iex_021_top_holder_concentration_189}


def iex_base_universe_d3_014_iex_022_institutional_net_flow_252(iex_base_universe_d2_014_iex_022_institutional_net_flow_252):
    return _base_universe_d3(iex_base_universe_d2_014_iex_022_institutional_net_flow_252, 14)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_014_iex_022_institutional_net_flow_252'] = {'inputs': ['iex_base_universe_d2_014_iex_022_institutional_net_flow_252'], 'func': iex_base_universe_d3_014_iex_022_institutional_net_flow_252}


def iex_base_universe_d3_015_iex_023_forced_selling_pressure_378(iex_base_universe_d2_015_iex_023_forced_selling_pressure_378):
    return _base_universe_d3(iex_base_universe_d2_015_iex_023_forced_selling_pressure_378, 15)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_015_iex_023_forced_selling_pressure_378'] = {'inputs': ['iex_base_universe_d2_015_iex_023_forced_selling_pressure_378'], 'func': iex_base_universe_d3_015_iex_023_forced_selling_pressure_378}


def iex_base_universe_d3_016_iex_024_holder_base_volatility_504(iex_base_universe_d2_016_iex_024_holder_base_volatility_504):
    return _base_universe_d3(iex_base_universe_d2_016_iex_024_holder_base_volatility_504, 16)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_016_iex_024_holder_base_volatility_504'] = {'inputs': ['iex_base_universe_d2_016_iex_024_holder_base_volatility_504'], 'func': iex_base_universe_d3_016_iex_024_holder_base_volatility_504}


def iex_base_universe_d3_017_iex_027_top_holder_concentration_1260(iex_base_universe_d2_017_iex_027_top_holder_concentration_1260):
    return _base_universe_d3(iex_base_universe_d2_017_iex_027_top_holder_concentration_1260, 17)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_017_iex_027_top_holder_concentration_1260'] = {'inputs': ['iex_base_universe_d2_017_iex_027_top_holder_concentration_1260'], 'func': iex_base_universe_d3_017_iex_027_top_holder_concentration_1260}


def iex_base_universe_d3_018_iex_028_institutional_net_flow_1512(iex_base_universe_d2_018_iex_028_institutional_net_flow_1512):
    return _base_universe_d3(iex_base_universe_d2_018_iex_028_institutional_net_flow_1512, 18)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_018_iex_028_institutional_net_flow_1512'] = {'inputs': ['iex_base_universe_d2_018_iex_028_institutional_net_flow_1512'], 'func': iex_base_universe_d3_018_iex_028_institutional_net_flow_1512}


def iex_base_universe_d3_019_iex_029_forced_selling_pressure_63(iex_base_universe_d2_019_iex_029_forced_selling_pressure_63):
    return _base_universe_d3(iex_base_universe_d2_019_iex_029_forced_selling_pressure_63, 19)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_019_iex_029_forced_selling_pressure_63'] = {'inputs': ['iex_base_universe_d2_019_iex_029_forced_selling_pressure_63'], 'func': iex_base_universe_d3_019_iex_029_forced_selling_pressure_63}


def iex_base_universe_d3_020_iex_030_holder_base_volatility_252(iex_base_universe_d2_020_iex_030_holder_base_volatility_252):
    return _base_universe_d3(iex_base_universe_d2_020_iex_030_holder_base_volatility_252, 20)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_020_iex_030_holder_base_volatility_252'] = {'inputs': ['iex_base_universe_d2_020_iex_030_holder_base_volatility_252'], 'func': iex_base_universe_d3_020_iex_030_holder_base_volatility_252}


def iex_base_universe_d3_021_iex_basefill_001(iex_base_universe_d2_021_iex_basefill_001):
    return _base_universe_d3(iex_base_universe_d2_021_iex_basefill_001, 21)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_021_iex_basefill_001'] = {'inputs': ['iex_base_universe_d2_021_iex_basefill_001'], 'func': iex_base_universe_d3_021_iex_basefill_001}


def iex_base_universe_d3_022_iex_basefill_002(iex_base_universe_d2_022_iex_basefill_002):
    return _base_universe_d3(iex_base_universe_d2_022_iex_basefill_002, 22)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_022_iex_basefill_002'] = {'inputs': ['iex_base_universe_d2_022_iex_basefill_002'], 'func': iex_base_universe_d3_022_iex_basefill_002}


def iex_base_universe_d3_023_iex_basefill_007(iex_base_universe_d2_023_iex_basefill_007):
    return _base_universe_d3(iex_base_universe_d2_023_iex_basefill_007, 23)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_023_iex_basefill_007'] = {'inputs': ['iex_base_universe_d2_023_iex_basefill_007'], 'func': iex_base_universe_d3_023_iex_basefill_007}


def iex_base_universe_d3_024_iex_basefill_008(iex_base_universe_d2_024_iex_basefill_008):
    return _base_universe_d3(iex_base_universe_d2_024_iex_basefill_008, 24)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_024_iex_basefill_008'] = {'inputs': ['iex_base_universe_d2_024_iex_basefill_008'], 'func': iex_base_universe_d3_024_iex_basefill_008}


def iex_base_universe_d3_025_iex_basefill_013(iex_base_universe_d2_025_iex_basefill_013):
    return _base_universe_d3(iex_base_universe_d2_025_iex_basefill_013, 25)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_025_iex_basefill_013'] = {'inputs': ['iex_base_universe_d2_025_iex_basefill_013'], 'func': iex_base_universe_d3_025_iex_basefill_013}


def iex_base_universe_d3_026_iex_basefill_014(iex_base_universe_d2_026_iex_basefill_014):
    return _base_universe_d3(iex_base_universe_d2_026_iex_basefill_014, 26)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_026_iex_basefill_014'] = {'inputs': ['iex_base_universe_d2_026_iex_basefill_014'], 'func': iex_base_universe_d3_026_iex_basefill_014}


def iex_base_universe_d3_027_iex_basefill_019(iex_base_universe_d2_027_iex_basefill_019):
    return _base_universe_d3(iex_base_universe_d2_027_iex_basefill_019, 27)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_027_iex_basefill_019'] = {'inputs': ['iex_base_universe_d2_027_iex_basefill_019'], 'func': iex_base_universe_d3_027_iex_basefill_019}


def iex_base_universe_d3_028_iex_basefill_020(iex_base_universe_d2_028_iex_basefill_020):
    return _base_universe_d3(iex_base_universe_d2_028_iex_basefill_020, 28)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_028_iex_basefill_020'] = {'inputs': ['iex_base_universe_d2_028_iex_basefill_020'], 'func': iex_base_universe_d3_028_iex_basefill_020}


def iex_base_universe_d3_029_iex_basefill_025(iex_base_universe_d2_029_iex_basefill_025):
    return _base_universe_d3(iex_base_universe_d2_029_iex_basefill_025, 29)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_029_iex_basefill_025'] = {'inputs': ['iex_base_universe_d2_029_iex_basefill_025'], 'func': iex_base_universe_d3_029_iex_basefill_025}


def iex_base_universe_d3_030_iex_basefill_026(iex_base_universe_d2_030_iex_basefill_026):
    return _base_universe_d3(iex_base_universe_d2_030_iex_basefill_026, 30)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_030_iex_basefill_026'] = {'inputs': ['iex_base_universe_d2_030_iex_basefill_026'], 'func': iex_base_universe_d3_030_iex_basefill_026}


def iex_base_universe_d3_031_iex_basefill_031(iex_base_universe_d2_031_iex_basefill_031):
    return _base_universe_d3(iex_base_universe_d2_031_iex_basefill_031, 31)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_031_iex_basefill_031'] = {'inputs': ['iex_base_universe_d2_031_iex_basefill_031'], 'func': iex_base_universe_d3_031_iex_basefill_031}


def iex_base_universe_d3_032_iex_basefill_032(iex_base_universe_d2_032_iex_basefill_032):
    return _base_universe_d3(iex_base_universe_d2_032_iex_basefill_032, 32)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_032_iex_basefill_032'] = {'inputs': ['iex_base_universe_d2_032_iex_basefill_032'], 'func': iex_base_universe_d3_032_iex_basefill_032}


def iex_base_universe_d3_033_iex_basefill_033(iex_base_universe_d2_033_iex_basefill_033):
    return _base_universe_d3(iex_base_universe_d2_033_iex_basefill_033, 33)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_033_iex_basefill_033'] = {'inputs': ['iex_base_universe_d2_033_iex_basefill_033'], 'func': iex_base_universe_d3_033_iex_basefill_033}


def iex_base_universe_d3_034_iex_basefill_034(iex_base_universe_d2_034_iex_basefill_034):
    return _base_universe_d3(iex_base_universe_d2_034_iex_basefill_034, 34)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_034_iex_basefill_034'] = {'inputs': ['iex_base_universe_d2_034_iex_basefill_034'], 'func': iex_base_universe_d3_034_iex_basefill_034}


def iex_base_universe_d3_035_iex_basefill_035(iex_base_universe_d2_035_iex_basefill_035):
    return _base_universe_d3(iex_base_universe_d2_035_iex_basefill_035, 35)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_035_iex_basefill_035'] = {'inputs': ['iex_base_universe_d2_035_iex_basefill_035'], 'func': iex_base_universe_d3_035_iex_basefill_035}


def iex_base_universe_d3_036_iex_basefill_036(iex_base_universe_d2_036_iex_basefill_036):
    return _base_universe_d3(iex_base_universe_d2_036_iex_basefill_036, 36)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_036_iex_basefill_036'] = {'inputs': ['iex_base_universe_d2_036_iex_basefill_036'], 'func': iex_base_universe_d3_036_iex_basefill_036}


def iex_base_universe_d3_037_iex_basefill_037(iex_base_universe_d2_037_iex_basefill_037):
    return _base_universe_d3(iex_base_universe_d2_037_iex_basefill_037, 37)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_037_iex_basefill_037'] = {'inputs': ['iex_base_universe_d2_037_iex_basefill_037'], 'func': iex_base_universe_d3_037_iex_basefill_037}


def iex_base_universe_d3_038_iex_basefill_038(iex_base_universe_d2_038_iex_basefill_038):
    return _base_universe_d3(iex_base_universe_d2_038_iex_basefill_038, 38)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_038_iex_basefill_038'] = {'inputs': ['iex_base_universe_d2_038_iex_basefill_038'], 'func': iex_base_universe_d3_038_iex_basefill_038}


def iex_base_universe_d3_039_iex_basefill_039(iex_base_universe_d2_039_iex_basefill_039):
    return _base_universe_d3(iex_base_universe_d2_039_iex_basefill_039, 39)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_039_iex_basefill_039'] = {'inputs': ['iex_base_universe_d2_039_iex_basefill_039'], 'func': iex_base_universe_d3_039_iex_basefill_039}


def iex_base_universe_d3_040_iex_basefill_040(iex_base_universe_d2_040_iex_basefill_040):
    return _base_universe_d3(iex_base_universe_d2_040_iex_basefill_040, 40)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_040_iex_basefill_040'] = {'inputs': ['iex_base_universe_d2_040_iex_basefill_040'], 'func': iex_base_universe_d3_040_iex_basefill_040}


def iex_base_universe_d3_041_iex_basefill_041(iex_base_universe_d2_041_iex_basefill_041):
    return _base_universe_d3(iex_base_universe_d2_041_iex_basefill_041, 41)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_041_iex_basefill_041'] = {'inputs': ['iex_base_universe_d2_041_iex_basefill_041'], 'func': iex_base_universe_d3_041_iex_basefill_041}


def iex_base_universe_d3_042_iex_basefill_042(iex_base_universe_d2_042_iex_basefill_042):
    return _base_universe_d3(iex_base_universe_d2_042_iex_basefill_042, 42)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_042_iex_basefill_042'] = {'inputs': ['iex_base_universe_d2_042_iex_basefill_042'], 'func': iex_base_universe_d3_042_iex_basefill_042}


def iex_base_universe_d3_043_iex_basefill_043(iex_base_universe_d2_043_iex_basefill_043):
    return _base_universe_d3(iex_base_universe_d2_043_iex_basefill_043, 43)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_043_iex_basefill_043'] = {'inputs': ['iex_base_universe_d2_043_iex_basefill_043'], 'func': iex_base_universe_d3_043_iex_basefill_043}


def iex_base_universe_d3_044_iex_basefill_044(iex_base_universe_d2_044_iex_basefill_044):
    return _base_universe_d3(iex_base_universe_d2_044_iex_basefill_044, 44)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_044_iex_basefill_044'] = {'inputs': ['iex_base_universe_d2_044_iex_basefill_044'], 'func': iex_base_universe_d3_044_iex_basefill_044}


def iex_base_universe_d3_045_iex_basefill_045(iex_base_universe_d2_045_iex_basefill_045):
    return _base_universe_d3(iex_base_universe_d2_045_iex_basefill_045, 45)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_045_iex_basefill_045'] = {'inputs': ['iex_base_universe_d2_045_iex_basefill_045'], 'func': iex_base_universe_d3_045_iex_basefill_045}


def iex_base_universe_d3_046_iex_basefill_046(iex_base_universe_d2_046_iex_basefill_046):
    return _base_universe_d3(iex_base_universe_d2_046_iex_basefill_046, 46)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_046_iex_basefill_046'] = {'inputs': ['iex_base_universe_d2_046_iex_basefill_046'], 'func': iex_base_universe_d3_046_iex_basefill_046}


def iex_base_universe_d3_047_iex_basefill_047(iex_base_universe_d2_047_iex_basefill_047):
    return _base_universe_d3(iex_base_universe_d2_047_iex_basefill_047, 47)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_047_iex_basefill_047'] = {'inputs': ['iex_base_universe_d2_047_iex_basefill_047'], 'func': iex_base_universe_d3_047_iex_basefill_047}


def iex_base_universe_d3_048_iex_basefill_048(iex_base_universe_d2_048_iex_basefill_048):
    return _base_universe_d3(iex_base_universe_d2_048_iex_basefill_048, 48)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_048_iex_basefill_048'] = {'inputs': ['iex_base_universe_d2_048_iex_basefill_048'], 'func': iex_base_universe_d3_048_iex_basefill_048}


def iex_base_universe_d3_049_iex_basefill_049(iex_base_universe_d2_049_iex_basefill_049):
    return _base_universe_d3(iex_base_universe_d2_049_iex_basefill_049, 49)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_049_iex_basefill_049'] = {'inputs': ['iex_base_universe_d2_049_iex_basefill_049'], 'func': iex_base_universe_d3_049_iex_basefill_049}


def iex_base_universe_d3_050_iex_basefill_050(iex_base_universe_d2_050_iex_basefill_050):
    return _base_universe_d3(iex_base_universe_d2_050_iex_basefill_050, 50)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_050_iex_basefill_050'] = {'inputs': ['iex_base_universe_d2_050_iex_basefill_050'], 'func': iex_base_universe_d3_050_iex_basefill_050}


def iex_base_universe_d3_051_iex_basefill_051(iex_base_universe_d2_051_iex_basefill_051):
    return _base_universe_d3(iex_base_universe_d2_051_iex_basefill_051, 51)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_051_iex_basefill_051'] = {'inputs': ['iex_base_universe_d2_051_iex_basefill_051'], 'func': iex_base_universe_d3_051_iex_basefill_051}


def iex_base_universe_d3_052_iex_basefill_052(iex_base_universe_d2_052_iex_basefill_052):
    return _base_universe_d3(iex_base_universe_d2_052_iex_basefill_052, 52)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_052_iex_basefill_052'] = {'inputs': ['iex_base_universe_d2_052_iex_basefill_052'], 'func': iex_base_universe_d3_052_iex_basefill_052}


def iex_base_universe_d3_053_iex_basefill_053(iex_base_universe_d2_053_iex_basefill_053):
    return _base_universe_d3(iex_base_universe_d2_053_iex_basefill_053, 53)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_053_iex_basefill_053'] = {'inputs': ['iex_base_universe_d2_053_iex_basefill_053'], 'func': iex_base_universe_d3_053_iex_basefill_053}


def iex_base_universe_d3_054_iex_basefill_054(iex_base_universe_d2_054_iex_basefill_054):
    return _base_universe_d3(iex_base_universe_d2_054_iex_basefill_054, 54)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_054_iex_basefill_054'] = {'inputs': ['iex_base_universe_d2_054_iex_basefill_054'], 'func': iex_base_universe_d3_054_iex_basefill_054}


def iex_base_universe_d3_055_iex_basefill_055(iex_base_universe_d2_055_iex_basefill_055):
    return _base_universe_d3(iex_base_universe_d2_055_iex_basefill_055, 55)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_055_iex_basefill_055'] = {'inputs': ['iex_base_universe_d2_055_iex_basefill_055'], 'func': iex_base_universe_d3_055_iex_basefill_055}


def iex_base_universe_d3_056_iex_basefill_056(iex_base_universe_d2_056_iex_basefill_056):
    return _base_universe_d3(iex_base_universe_d2_056_iex_basefill_056, 56)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_056_iex_basefill_056'] = {'inputs': ['iex_base_universe_d2_056_iex_basefill_056'], 'func': iex_base_universe_d3_056_iex_basefill_056}


def iex_base_universe_d3_057_iex_basefill_057(iex_base_universe_d2_057_iex_basefill_057):
    return _base_universe_d3(iex_base_universe_d2_057_iex_basefill_057, 57)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_057_iex_basefill_057'] = {'inputs': ['iex_base_universe_d2_057_iex_basefill_057'], 'func': iex_base_universe_d3_057_iex_basefill_057}


def iex_base_universe_d3_058_iex_basefill_058(iex_base_universe_d2_058_iex_basefill_058):
    return _base_universe_d3(iex_base_universe_d2_058_iex_basefill_058, 58)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_058_iex_basefill_058'] = {'inputs': ['iex_base_universe_d2_058_iex_basefill_058'], 'func': iex_base_universe_d3_058_iex_basefill_058}


def iex_base_universe_d3_059_iex_basefill_059(iex_base_universe_d2_059_iex_basefill_059):
    return _base_universe_d3(iex_base_universe_d2_059_iex_basefill_059, 59)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_059_iex_basefill_059'] = {'inputs': ['iex_base_universe_d2_059_iex_basefill_059'], 'func': iex_base_universe_d3_059_iex_basefill_059}


def iex_base_universe_d3_060_iex_basefill_060(iex_base_universe_d2_060_iex_basefill_060):
    return _base_universe_d3(iex_base_universe_d2_060_iex_basefill_060, 60)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_060_iex_basefill_060'] = {'inputs': ['iex_base_universe_d2_060_iex_basefill_060'], 'func': iex_base_universe_d3_060_iex_basefill_060}


def iex_base_universe_d3_061_iex_basefill_061(iex_base_universe_d2_061_iex_basefill_061):
    return _base_universe_d3(iex_base_universe_d2_061_iex_basefill_061, 61)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_061_iex_basefill_061'] = {'inputs': ['iex_base_universe_d2_061_iex_basefill_061'], 'func': iex_base_universe_d3_061_iex_basefill_061}


def iex_base_universe_d3_062_iex_basefill_062(iex_base_universe_d2_062_iex_basefill_062):
    return _base_universe_d3(iex_base_universe_d2_062_iex_basefill_062, 62)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_062_iex_basefill_062'] = {'inputs': ['iex_base_universe_d2_062_iex_basefill_062'], 'func': iex_base_universe_d3_062_iex_basefill_062}


def iex_base_universe_d3_063_iex_basefill_063(iex_base_universe_d2_063_iex_basefill_063):
    return _base_universe_d3(iex_base_universe_d2_063_iex_basefill_063, 63)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_063_iex_basefill_063'] = {'inputs': ['iex_base_universe_d2_063_iex_basefill_063'], 'func': iex_base_universe_d3_063_iex_basefill_063}


def iex_base_universe_d3_064_iex_basefill_064(iex_base_universe_d2_064_iex_basefill_064):
    return _base_universe_d3(iex_base_universe_d2_064_iex_basefill_064, 64)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_064_iex_basefill_064'] = {'inputs': ['iex_base_universe_d2_064_iex_basefill_064'], 'func': iex_base_universe_d3_064_iex_basefill_064}


def iex_base_universe_d3_065_iex_basefill_065(iex_base_universe_d2_065_iex_basefill_065):
    return _base_universe_d3(iex_base_universe_d2_065_iex_basefill_065, 65)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_065_iex_basefill_065'] = {'inputs': ['iex_base_universe_d2_065_iex_basefill_065'], 'func': iex_base_universe_d3_065_iex_basefill_065}


def iex_base_universe_d3_066_iex_basefill_066(iex_base_universe_d2_066_iex_basefill_066):
    return _base_universe_d3(iex_base_universe_d2_066_iex_basefill_066, 66)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_066_iex_basefill_066'] = {'inputs': ['iex_base_universe_d2_066_iex_basefill_066'], 'func': iex_base_universe_d3_066_iex_basefill_066}


def iex_base_universe_d3_067_iex_basefill_067(iex_base_universe_d2_067_iex_basefill_067):
    return _base_universe_d3(iex_base_universe_d2_067_iex_basefill_067, 67)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_067_iex_basefill_067'] = {'inputs': ['iex_base_universe_d2_067_iex_basefill_067'], 'func': iex_base_universe_d3_067_iex_basefill_067}


def iex_base_universe_d3_068_iex_basefill_068(iex_base_universe_d2_068_iex_basefill_068):
    return _base_universe_d3(iex_base_universe_d2_068_iex_basefill_068, 68)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_068_iex_basefill_068'] = {'inputs': ['iex_base_universe_d2_068_iex_basefill_068'], 'func': iex_base_universe_d3_068_iex_basefill_068}


def iex_base_universe_d3_069_iex_basefill_069(iex_base_universe_d2_069_iex_basefill_069):
    return _base_universe_d3(iex_base_universe_d2_069_iex_basefill_069, 69)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_069_iex_basefill_069'] = {'inputs': ['iex_base_universe_d2_069_iex_basefill_069'], 'func': iex_base_universe_d3_069_iex_basefill_069}


def iex_base_universe_d3_070_iex_basefill_070(iex_base_universe_d2_070_iex_basefill_070):
    return _base_universe_d3(iex_base_universe_d2_070_iex_basefill_070, 70)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_070_iex_basefill_070'] = {'inputs': ['iex_base_universe_d2_070_iex_basefill_070'], 'func': iex_base_universe_d3_070_iex_basefill_070}


def iex_base_universe_d3_071_iex_basefill_071(iex_base_universe_d2_071_iex_basefill_071):
    return _base_universe_d3(iex_base_universe_d2_071_iex_basefill_071, 71)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_071_iex_basefill_071'] = {'inputs': ['iex_base_universe_d2_071_iex_basefill_071'], 'func': iex_base_universe_d3_071_iex_basefill_071}


def iex_base_universe_d3_072_iex_basefill_072(iex_base_universe_d2_072_iex_basefill_072):
    return _base_universe_d3(iex_base_universe_d2_072_iex_basefill_072, 72)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_072_iex_basefill_072'] = {'inputs': ['iex_base_universe_d2_072_iex_basefill_072'], 'func': iex_base_universe_d3_072_iex_basefill_072}


def iex_base_universe_d3_073_iex_basefill_073(iex_base_universe_d2_073_iex_basefill_073):
    return _base_universe_d3(iex_base_universe_d2_073_iex_basefill_073, 73)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_073_iex_basefill_073'] = {'inputs': ['iex_base_universe_d2_073_iex_basefill_073'], 'func': iex_base_universe_d3_073_iex_basefill_073}


def iex_base_universe_d3_074_iex_basefill_074(iex_base_universe_d2_074_iex_basefill_074):
    return _base_universe_d3(iex_base_universe_d2_074_iex_basefill_074, 74)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_074_iex_basefill_074'] = {'inputs': ['iex_base_universe_d2_074_iex_basefill_074'], 'func': iex_base_universe_d3_074_iex_basefill_074}


def iex_base_universe_d3_075_iex_basefill_075(iex_base_universe_d2_075_iex_basefill_075):
    return _base_universe_d3(iex_base_universe_d2_075_iex_basefill_075, 75)
IEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['iex_base_universe_d3_075_iex_basefill_075'] = {'inputs': ['iex_base_universe_d2_075_iex_basefill_075'], 'func': iex_base_universe_d3_075_iex_basefill_075}

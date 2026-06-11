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



def isl_176_isl_001_insider_buy_cluster_21_accel_1(isl_151_isl_001_insider_buy_cluster_21_roc_1):
    feature = _s(isl_151_isl_001_insider_buy_cluster_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def isl_177_isl_007_insider_silence_252_accel_42(isl_152_isl_007_insider_silence_252_roc_42):
    feature = _s(isl_152_isl_007_insider_silence_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def isl_178_isl_013_insider_conviction_1512_accel_126(isl_153_isl_013_insider_conviction_1512_roc_126):
    feature = _s(isl_153_isl_013_insider_conviction_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def isl_179_isl_019_insider_activity_accel_1_accel_378(isl_154_isl_019_insider_activity_accel_1_roc_378):
    feature = _s(isl_154_isl_019_insider_activity_accel_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def isl_180_isl_025_ceo_cfo_buy_weight_756_accel_4(isl_155_isl_025_ceo_cfo_buy_weight_756_roc_4):
    feature = _s(isl_155_isl_025_ceo_cfo_buy_weight_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSIDER_SILENCE_REGISTRY_3RD_DERIVATIVES = {
    'isl_176_isl_001_insider_buy_cluster_21_accel_1': {'inputs': ['isl_151_isl_001_insider_buy_cluster_21_roc_1'], 'func': isl_176_isl_001_insider_buy_cluster_21_accel_1},
    'isl_177_isl_007_insider_silence_252_accel_42': {'inputs': ['isl_152_isl_007_insider_silence_252_roc_42'], 'func': isl_177_isl_007_insider_silence_252_accel_42},
    'isl_178_isl_013_insider_conviction_1512_accel_126': {'inputs': ['isl_153_isl_013_insider_conviction_1512_roc_126'], 'func': isl_178_isl_013_insider_conviction_1512_accel_126},
    'isl_179_isl_019_insider_activity_accel_1_accel_378': {'inputs': ['isl_154_isl_019_insider_activity_accel_1_roc_378'], 'func': isl_179_isl_019_insider_activity_accel_1_accel_378},
    'isl_180_isl_025_ceo_cfo_buy_weight_756_accel_4': {'inputs': ['isl_155_isl_025_ceo_cfo_buy_weight_756_roc_4'], 'func': isl_180_isl_025_ceo_cfo_buy_weight_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def is_replacement_d3_001(is_replacement_d2_001):
    feature = _clean(is_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_001'] = {'inputs': ['is_replacement_d2_001'], 'func': is_replacement_d3_001}


def is_replacement_d3_002(is_replacement_d2_002):
    feature = _clean(is_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_002'] = {'inputs': ['is_replacement_d2_002'], 'func': is_replacement_d3_002}


def is_replacement_d3_003(is_replacement_d2_003):
    feature = _clean(is_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_003'] = {'inputs': ['is_replacement_d2_003'], 'func': is_replacement_d3_003}


def is_replacement_d3_004(is_replacement_d2_004):
    feature = _clean(is_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_004'] = {'inputs': ['is_replacement_d2_004'], 'func': is_replacement_d3_004}


def is_replacement_d3_005(is_replacement_d2_005):
    feature = _clean(is_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_005'] = {'inputs': ['is_replacement_d2_005'], 'func': is_replacement_d3_005}


def is_replacement_d3_006(is_replacement_d2_006):
    feature = _clean(is_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_006'] = {'inputs': ['is_replacement_d2_006'], 'func': is_replacement_d3_006}


def is_replacement_d3_007(is_replacement_d2_007):
    feature = _clean(is_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_007'] = {'inputs': ['is_replacement_d2_007'], 'func': is_replacement_d3_007}


def is_replacement_d3_008(is_replacement_d2_008):
    feature = _clean(is_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_008'] = {'inputs': ['is_replacement_d2_008'], 'func': is_replacement_d3_008}


def is_replacement_d3_009(is_replacement_d2_009):
    feature = _clean(is_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_009'] = {'inputs': ['is_replacement_d2_009'], 'func': is_replacement_d3_009}


def is_replacement_d3_010(is_replacement_d2_010):
    feature = _clean(is_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_010'] = {'inputs': ['is_replacement_d2_010'], 'func': is_replacement_d3_010}


def is_replacement_d3_011(is_replacement_d2_011):
    feature = _clean(is_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_011'] = {'inputs': ['is_replacement_d2_011'], 'func': is_replacement_d3_011}


def is_replacement_d3_012(is_replacement_d2_012):
    feature = _clean(is_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_012'] = {'inputs': ['is_replacement_d2_012'], 'func': is_replacement_d3_012}


def is_replacement_d3_013(is_replacement_d2_013):
    feature = _clean(is_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_013'] = {'inputs': ['is_replacement_d2_013'], 'func': is_replacement_d3_013}


def is_replacement_d3_014(is_replacement_d2_014):
    feature = _clean(is_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_014'] = {'inputs': ['is_replacement_d2_014'], 'func': is_replacement_d3_014}


def is_replacement_d3_015(is_replacement_d2_015):
    feature = _clean(is_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_015'] = {'inputs': ['is_replacement_d2_015'], 'func': is_replacement_d3_015}


def is_replacement_d3_016(is_replacement_d2_016):
    feature = _clean(is_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_016'] = {'inputs': ['is_replacement_d2_016'], 'func': is_replacement_d3_016}


def is_replacement_d3_017(is_replacement_d2_017):
    feature = _clean(is_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_017'] = {'inputs': ['is_replacement_d2_017'], 'func': is_replacement_d3_017}


def is_replacement_d3_018(is_replacement_d2_018):
    feature = _clean(is_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_018'] = {'inputs': ['is_replacement_d2_018'], 'func': is_replacement_d3_018}


def is_replacement_d3_019(is_replacement_d2_019):
    feature = _clean(is_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_019'] = {'inputs': ['is_replacement_d2_019'], 'func': is_replacement_d3_019}


def is_replacement_d3_020(is_replacement_d2_020):
    feature = _clean(is_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_020'] = {'inputs': ['is_replacement_d2_020'], 'func': is_replacement_d3_020}


def is_replacement_d3_021(is_replacement_d2_021):
    feature = _clean(is_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_021'] = {'inputs': ['is_replacement_d2_021'], 'func': is_replacement_d3_021}


def is_replacement_d3_022(is_replacement_d2_022):
    feature = _clean(is_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_022'] = {'inputs': ['is_replacement_d2_022'], 'func': is_replacement_d3_022}


def is_replacement_d3_023(is_replacement_d2_023):
    feature = _clean(is_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_023'] = {'inputs': ['is_replacement_d2_023'], 'func': is_replacement_d3_023}


def is_replacement_d3_024(is_replacement_d2_024):
    feature = _clean(is_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_024'] = {'inputs': ['is_replacement_d2_024'], 'func': is_replacement_d3_024}


def is_replacement_d3_025(is_replacement_d2_025):
    feature = _clean(is_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_025'] = {'inputs': ['is_replacement_d2_025'], 'func': is_replacement_d3_025}


def is_replacement_d3_026(is_replacement_d2_026):
    feature = _clean(is_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_026'] = {'inputs': ['is_replacement_d2_026'], 'func': is_replacement_d3_026}


def is_replacement_d3_027(is_replacement_d2_027):
    feature = _clean(is_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_027'] = {'inputs': ['is_replacement_d2_027'], 'func': is_replacement_d3_027}


def is_replacement_d3_028(is_replacement_d2_028):
    feature = _clean(is_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_028'] = {'inputs': ['is_replacement_d2_028'], 'func': is_replacement_d3_028}


def is_replacement_d3_029(is_replacement_d2_029):
    feature = _clean(is_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_029'] = {'inputs': ['is_replacement_d2_029'], 'func': is_replacement_d3_029}


def is_replacement_d3_030(is_replacement_d2_030):
    feature = _clean(is_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_030'] = {'inputs': ['is_replacement_d2_030'], 'func': is_replacement_d3_030}


def is_replacement_d3_031(is_replacement_d2_031):
    feature = _clean(is_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_031'] = {'inputs': ['is_replacement_d2_031'], 'func': is_replacement_d3_031}


def is_replacement_d3_032(is_replacement_d2_032):
    feature = _clean(is_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_032'] = {'inputs': ['is_replacement_d2_032'], 'func': is_replacement_d3_032}


def is_replacement_d3_033(is_replacement_d2_033):
    feature = _clean(is_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_033'] = {'inputs': ['is_replacement_d2_033'], 'func': is_replacement_d3_033}


def is_replacement_d3_034(is_replacement_d2_034):
    feature = _clean(is_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_034'] = {'inputs': ['is_replacement_d2_034'], 'func': is_replacement_d3_034}


def is_replacement_d3_035(is_replacement_d2_035):
    feature = _clean(is_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_035'] = {'inputs': ['is_replacement_d2_035'], 'func': is_replacement_d3_035}


def is_replacement_d3_036(is_replacement_d2_036):
    feature = _clean(is_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_036'] = {'inputs': ['is_replacement_d2_036'], 'func': is_replacement_d3_036}


def is_replacement_d3_037(is_replacement_d2_037):
    feature = _clean(is_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_037'] = {'inputs': ['is_replacement_d2_037'], 'func': is_replacement_d3_037}


def is_replacement_d3_038(is_replacement_d2_038):
    feature = _clean(is_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_038'] = {'inputs': ['is_replacement_d2_038'], 'func': is_replacement_d3_038}


def is_replacement_d3_039(is_replacement_d2_039):
    feature = _clean(is_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_039'] = {'inputs': ['is_replacement_d2_039'], 'func': is_replacement_d3_039}


def is_replacement_d3_040(is_replacement_d2_040):
    feature = _clean(is_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_040'] = {'inputs': ['is_replacement_d2_040'], 'func': is_replacement_d3_040}


def is_replacement_d3_041(is_replacement_d2_041):
    feature = _clean(is_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_041'] = {'inputs': ['is_replacement_d2_041'], 'func': is_replacement_d3_041}


def is_replacement_d3_042(is_replacement_d2_042):
    feature = _clean(is_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_042'] = {'inputs': ['is_replacement_d2_042'], 'func': is_replacement_d3_042}


def is_replacement_d3_043(is_replacement_d2_043):
    feature = _clean(is_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_043'] = {'inputs': ['is_replacement_d2_043'], 'func': is_replacement_d3_043}


def is_replacement_d3_044(is_replacement_d2_044):
    feature = _clean(is_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_044'] = {'inputs': ['is_replacement_d2_044'], 'func': is_replacement_d3_044}


def is_replacement_d3_045(is_replacement_d2_045):
    feature = _clean(is_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_045'] = {'inputs': ['is_replacement_d2_045'], 'func': is_replacement_d3_045}


def is_replacement_d3_046(is_replacement_d2_046):
    feature = _clean(is_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_046'] = {'inputs': ['is_replacement_d2_046'], 'func': is_replacement_d3_046}


def is_replacement_d3_047(is_replacement_d2_047):
    feature = _clean(is_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_047'] = {'inputs': ['is_replacement_d2_047'], 'func': is_replacement_d3_047}


def is_replacement_d3_048(is_replacement_d2_048):
    feature = _clean(is_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_048'] = {'inputs': ['is_replacement_d2_048'], 'func': is_replacement_d3_048}


def is_replacement_d3_049(is_replacement_d2_049):
    feature = _clean(is_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_049'] = {'inputs': ['is_replacement_d2_049'], 'func': is_replacement_d3_049}


def is_replacement_d3_050(is_replacement_d2_050):
    feature = _clean(is_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_050'] = {'inputs': ['is_replacement_d2_050'], 'func': is_replacement_d3_050}


def is_replacement_d3_051(is_replacement_d2_051):
    feature = _clean(is_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_051'] = {'inputs': ['is_replacement_d2_051'], 'func': is_replacement_d3_051}


def is_replacement_d3_052(is_replacement_d2_052):
    feature = _clean(is_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_052'] = {'inputs': ['is_replacement_d2_052'], 'func': is_replacement_d3_052}


def is_replacement_d3_053(is_replacement_d2_053):
    feature = _clean(is_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_053'] = {'inputs': ['is_replacement_d2_053'], 'func': is_replacement_d3_053}


def is_replacement_d3_054(is_replacement_d2_054):
    feature = _clean(is_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_054'] = {'inputs': ['is_replacement_d2_054'], 'func': is_replacement_d3_054}


def is_replacement_d3_055(is_replacement_d2_055):
    feature = _clean(is_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_055'] = {'inputs': ['is_replacement_d2_055'], 'func': is_replacement_d3_055}


def is_replacement_d3_056(is_replacement_d2_056):
    feature = _clean(is_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_056'] = {'inputs': ['is_replacement_d2_056'], 'func': is_replacement_d3_056}


def is_replacement_d3_057(is_replacement_d2_057):
    feature = _clean(is_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_057'] = {'inputs': ['is_replacement_d2_057'], 'func': is_replacement_d3_057}


def is_replacement_d3_058(is_replacement_d2_058):
    feature = _clean(is_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_058'] = {'inputs': ['is_replacement_d2_058'], 'func': is_replacement_d3_058}


def is_replacement_d3_059(is_replacement_d2_059):
    feature = _clean(is_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_059'] = {'inputs': ['is_replacement_d2_059'], 'func': is_replacement_d3_059}


def is_replacement_d3_060(is_replacement_d2_060):
    feature = _clean(is_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_060'] = {'inputs': ['is_replacement_d2_060'], 'func': is_replacement_d3_060}


def is_replacement_d3_061(is_replacement_d2_061):
    feature = _clean(is_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_061'] = {'inputs': ['is_replacement_d2_061'], 'func': is_replacement_d3_061}


def is_replacement_d3_062(is_replacement_d2_062):
    feature = _clean(is_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_062'] = {'inputs': ['is_replacement_d2_062'], 'func': is_replacement_d3_062}


def is_replacement_d3_063(is_replacement_d2_063):
    feature = _clean(is_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_063'] = {'inputs': ['is_replacement_d2_063'], 'func': is_replacement_d3_063}


def is_replacement_d3_064(is_replacement_d2_064):
    feature = _clean(is_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_064'] = {'inputs': ['is_replacement_d2_064'], 'func': is_replacement_d3_064}


def is_replacement_d3_065(is_replacement_d2_065):
    feature = _clean(is_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_065'] = {'inputs': ['is_replacement_d2_065'], 'func': is_replacement_d3_065}


def is_replacement_d3_066(is_replacement_d2_066):
    feature = _clean(is_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_066'] = {'inputs': ['is_replacement_d2_066'], 'func': is_replacement_d3_066}


def is_replacement_d3_067(is_replacement_d2_067):
    feature = _clean(is_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_067'] = {'inputs': ['is_replacement_d2_067'], 'func': is_replacement_d3_067}


def is_replacement_d3_068(is_replacement_d2_068):
    feature = _clean(is_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_068'] = {'inputs': ['is_replacement_d2_068'], 'func': is_replacement_d3_068}


def is_replacement_d3_069(is_replacement_d2_069):
    feature = _clean(is_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_069'] = {'inputs': ['is_replacement_d2_069'], 'func': is_replacement_d3_069}


def is_replacement_d3_070(is_replacement_d2_070):
    feature = _clean(is_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_070'] = {'inputs': ['is_replacement_d2_070'], 'func': is_replacement_d3_070}


def is_replacement_d3_071(is_replacement_d2_071):
    feature = _clean(is_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_071'] = {'inputs': ['is_replacement_d2_071'], 'func': is_replacement_d3_071}


def is_replacement_d3_072(is_replacement_d2_072):
    feature = _clean(is_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_072'] = {'inputs': ['is_replacement_d2_072'], 'func': is_replacement_d3_072}


def is_replacement_d3_073(is_replacement_d2_073):
    feature = _clean(is_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_073'] = {'inputs': ['is_replacement_d2_073'], 'func': is_replacement_d3_073}


def is_replacement_d3_074(is_replacement_d2_074):
    feature = _clean(is_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_074'] = {'inputs': ['is_replacement_d2_074'], 'func': is_replacement_d3_074}


def is_replacement_d3_075(is_replacement_d2_075):
    feature = _clean(is_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_075'] = {'inputs': ['is_replacement_d2_075'], 'func': is_replacement_d3_075}


def is_replacement_d3_076(is_replacement_d2_076):
    feature = _clean(is_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_076'] = {'inputs': ['is_replacement_d2_076'], 'func': is_replacement_d3_076}


def is_replacement_d3_077(is_replacement_d2_077):
    feature = _clean(is_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_077'] = {'inputs': ['is_replacement_d2_077'], 'func': is_replacement_d3_077}


def is_replacement_d3_078(is_replacement_d2_078):
    feature = _clean(is_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_078'] = {'inputs': ['is_replacement_d2_078'], 'func': is_replacement_d3_078}


def is_replacement_d3_079(is_replacement_d2_079):
    feature = _clean(is_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_079'] = {'inputs': ['is_replacement_d2_079'], 'func': is_replacement_d3_079}


def is_replacement_d3_080(is_replacement_d2_080):
    feature = _clean(is_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_080'] = {'inputs': ['is_replacement_d2_080'], 'func': is_replacement_d3_080}


def is_replacement_d3_081(is_replacement_d2_081):
    feature = _clean(is_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_081'] = {'inputs': ['is_replacement_d2_081'], 'func': is_replacement_d3_081}


def is_replacement_d3_082(is_replacement_d2_082):
    feature = _clean(is_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_082'] = {'inputs': ['is_replacement_d2_082'], 'func': is_replacement_d3_082}


def is_replacement_d3_083(is_replacement_d2_083):
    feature = _clean(is_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_083'] = {'inputs': ['is_replacement_d2_083'], 'func': is_replacement_d3_083}


def is_replacement_d3_084(is_replacement_d2_084):
    feature = _clean(is_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_084'] = {'inputs': ['is_replacement_d2_084'], 'func': is_replacement_d3_084}


def is_replacement_d3_085(is_replacement_d2_085):
    feature = _clean(is_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_085'] = {'inputs': ['is_replacement_d2_085'], 'func': is_replacement_d3_085}


def is_replacement_d3_086(is_replacement_d2_086):
    feature = _clean(is_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_086'] = {'inputs': ['is_replacement_d2_086'], 'func': is_replacement_d3_086}


def is_replacement_d3_087(is_replacement_d2_087):
    feature = _clean(is_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_087'] = {'inputs': ['is_replacement_d2_087'], 'func': is_replacement_d3_087}


def is_replacement_d3_088(is_replacement_d2_088):
    feature = _clean(is_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_088'] = {'inputs': ['is_replacement_d2_088'], 'func': is_replacement_d3_088}


def is_replacement_d3_089(is_replacement_d2_089):
    feature = _clean(is_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_089'] = {'inputs': ['is_replacement_d2_089'], 'func': is_replacement_d3_089}


def is_replacement_d3_090(is_replacement_d2_090):
    feature = _clean(is_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_090'] = {'inputs': ['is_replacement_d2_090'], 'func': is_replacement_d3_090}


def is_replacement_d3_091(is_replacement_d2_091):
    feature = _clean(is_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_091'] = {'inputs': ['is_replacement_d2_091'], 'func': is_replacement_d3_091}


def is_replacement_d3_092(is_replacement_d2_092):
    feature = _clean(is_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_092'] = {'inputs': ['is_replacement_d2_092'], 'func': is_replacement_d3_092}


def is_replacement_d3_093(is_replacement_d2_093):
    feature = _clean(is_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_093'] = {'inputs': ['is_replacement_d2_093'], 'func': is_replacement_d3_093}


def is_replacement_d3_094(is_replacement_d2_094):
    feature = _clean(is_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_094'] = {'inputs': ['is_replacement_d2_094'], 'func': is_replacement_d3_094}


def is_replacement_d3_095(is_replacement_d2_095):
    feature = _clean(is_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_095'] = {'inputs': ['is_replacement_d2_095'], 'func': is_replacement_d3_095}


def is_replacement_d3_096(is_replacement_d2_096):
    feature = _clean(is_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_096'] = {'inputs': ['is_replacement_d2_096'], 'func': is_replacement_d3_096}


def is_replacement_d3_097(is_replacement_d2_097):
    feature = _clean(is_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_097'] = {'inputs': ['is_replacement_d2_097'], 'func': is_replacement_d3_097}


def is_replacement_d3_098(is_replacement_d2_098):
    feature = _clean(is_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_098'] = {'inputs': ['is_replacement_d2_098'], 'func': is_replacement_d3_098}


def is_replacement_d3_099(is_replacement_d2_099):
    feature = _clean(is_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_099'] = {'inputs': ['is_replacement_d2_099'], 'func': is_replacement_d3_099}


def is_replacement_d3_100(is_replacement_d2_100):
    feature = _clean(is_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_100'] = {'inputs': ['is_replacement_d2_100'], 'func': is_replacement_d3_100}


def is_replacement_d3_101(is_replacement_d2_101):
    feature = _clean(is_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_101'] = {'inputs': ['is_replacement_d2_101'], 'func': is_replacement_d3_101}


def is_replacement_d3_102(is_replacement_d2_102):
    feature = _clean(is_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_102'] = {'inputs': ['is_replacement_d2_102'], 'func': is_replacement_d3_102}


def is_replacement_d3_103(is_replacement_d2_103):
    feature = _clean(is_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_103'] = {'inputs': ['is_replacement_d2_103'], 'func': is_replacement_d3_103}


def is_replacement_d3_104(is_replacement_d2_104):
    feature = _clean(is_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_104'] = {'inputs': ['is_replacement_d2_104'], 'func': is_replacement_d3_104}


def is_replacement_d3_105(is_replacement_d2_105):
    feature = _clean(is_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_105'] = {'inputs': ['is_replacement_d2_105'], 'func': is_replacement_d3_105}


def is_replacement_d3_106(is_replacement_d2_106):
    feature = _clean(is_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_106'] = {'inputs': ['is_replacement_d2_106'], 'func': is_replacement_d3_106}


def is_replacement_d3_107(is_replacement_d2_107):
    feature = _clean(is_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_107'] = {'inputs': ['is_replacement_d2_107'], 'func': is_replacement_d3_107}


def is_replacement_d3_108(is_replacement_d2_108):
    feature = _clean(is_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_108'] = {'inputs': ['is_replacement_d2_108'], 'func': is_replacement_d3_108}


def is_replacement_d3_109(is_replacement_d2_109):
    feature = _clean(is_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_109'] = {'inputs': ['is_replacement_d2_109'], 'func': is_replacement_d3_109}


def is_replacement_d3_110(is_replacement_d2_110):
    feature = _clean(is_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_110'] = {'inputs': ['is_replacement_d2_110'], 'func': is_replacement_d3_110}


def is_replacement_d3_111(is_replacement_d2_111):
    feature = _clean(is_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_111'] = {'inputs': ['is_replacement_d2_111'], 'func': is_replacement_d3_111}


def is_replacement_d3_112(is_replacement_d2_112):
    feature = _clean(is_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['is_replacement_d3_112'] = {'inputs': ['is_replacement_d2_112'], 'func': is_replacement_d3_112}


# Third-derivative extensions for repaired first-base features.
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def isl_base_universe_d3_001_isl_002_insider_net_buy_ratio_42(isl_base_universe_d2_001_isl_002_insider_net_buy_ratio_42):
    return _base_universe_d3(isl_base_universe_d2_001_isl_002_insider_net_buy_ratio_42, 1)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_001_isl_002_insider_net_buy_ratio_42'] = {'inputs': ['isl_base_universe_d2_001_isl_002_insider_net_buy_ratio_42'], 'func': isl_base_universe_d3_001_isl_002_insider_net_buy_ratio_42}


def isl_base_universe_d3_002_isl_003_insider_value_ratio_63(isl_base_universe_d2_002_isl_003_insider_value_ratio_63):
    return _base_universe_d3(isl_base_universe_d2_002_isl_003_insider_value_ratio_63, 2)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_002_isl_003_insider_value_ratio_63'] = {'inputs': ['isl_base_universe_d2_002_isl_003_insider_value_ratio_63'], 'func': isl_base_universe_d3_002_isl_003_insider_value_ratio_63}


def isl_base_universe_d3_003_isl_004_ceo_cfo_buy_weight_84(isl_base_universe_d2_003_isl_004_ceo_cfo_buy_weight_84):
    return _base_universe_d3(isl_base_universe_d2_003_isl_004_ceo_cfo_buy_weight_84, 3)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_003_isl_004_ceo_cfo_buy_weight_84'] = {'inputs': ['isl_base_universe_d2_003_isl_004_ceo_cfo_buy_weight_84'], 'func': isl_base_universe_d3_003_isl_004_ceo_cfo_buy_weight_84}


def isl_base_universe_d3_004_isl_006_insider_conviction_189(isl_base_universe_d2_004_isl_006_insider_conviction_189):
    return _base_universe_d3(isl_base_universe_d2_004_isl_006_insider_conviction_189, 4)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_004_isl_006_insider_conviction_189'] = {'inputs': ['isl_base_universe_d2_004_isl_006_insider_conviction_189'], 'func': isl_base_universe_d3_004_isl_006_insider_conviction_189}


def isl_base_universe_d3_005_isl_008_insider_buy_cluster_378(isl_base_universe_d2_005_isl_008_insider_buy_cluster_378):
    return _base_universe_d3(isl_base_universe_d2_005_isl_008_insider_buy_cluster_378, 5)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_005_isl_008_insider_buy_cluster_378'] = {'inputs': ['isl_base_universe_d2_005_isl_008_insider_buy_cluster_378'], 'func': isl_base_universe_d3_005_isl_008_insider_buy_cluster_378}


def isl_base_universe_d3_006_isl_009_insider_net_buy_ratio_504(isl_base_universe_d2_006_isl_009_insider_net_buy_ratio_504):
    return _base_universe_d3(isl_base_universe_d2_006_isl_009_insider_net_buy_ratio_504, 6)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_006_isl_009_insider_net_buy_ratio_504'] = {'inputs': ['isl_base_universe_d2_006_isl_009_insider_net_buy_ratio_504'], 'func': isl_base_universe_d3_006_isl_009_insider_net_buy_ratio_504}


def isl_base_universe_d3_007_isl_010_insider_value_ratio_756(isl_base_universe_d2_007_isl_010_insider_value_ratio_756):
    return _base_universe_d3(isl_base_universe_d2_007_isl_010_insider_value_ratio_756, 7)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_007_isl_010_insider_value_ratio_756'] = {'inputs': ['isl_base_universe_d2_007_isl_010_insider_value_ratio_756'], 'func': isl_base_universe_d3_007_isl_010_insider_value_ratio_756}


def isl_base_universe_d3_008_isl_011_ceo_cfo_buy_weight_1008(isl_base_universe_d2_008_isl_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d3(isl_base_universe_d2_008_isl_011_ceo_cfo_buy_weight_1008, 8)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_008_isl_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['isl_base_universe_d2_008_isl_011_ceo_cfo_buy_weight_1008'], 'func': isl_base_universe_d3_008_isl_011_ceo_cfo_buy_weight_1008}


def isl_base_universe_d3_009_isl_014_insider_silence_63(isl_base_universe_d2_009_isl_014_insider_silence_63):
    return _base_universe_d3(isl_base_universe_d2_009_isl_014_insider_silence_63, 9)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_009_isl_014_insider_silence_63'] = {'inputs': ['isl_base_universe_d2_009_isl_014_insider_silence_63'], 'func': isl_base_universe_d3_009_isl_014_insider_silence_63}


def isl_base_universe_d3_010_isl_015_insider_buy_cluster_252(isl_base_universe_d2_010_isl_015_insider_buy_cluster_252):
    return _base_universe_d3(isl_base_universe_d2_010_isl_015_insider_buy_cluster_252, 10)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_010_isl_015_insider_buy_cluster_252'] = {'inputs': ['isl_base_universe_d2_010_isl_015_insider_buy_cluster_252'], 'func': isl_base_universe_d3_010_isl_015_insider_buy_cluster_252}


def isl_base_universe_d3_011_isl_016_insider_net_buy_ratio_21(isl_base_universe_d2_011_isl_016_insider_net_buy_ratio_21):
    return _base_universe_d3(isl_base_universe_d2_011_isl_016_insider_net_buy_ratio_21, 11)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_011_isl_016_insider_net_buy_ratio_21'] = {'inputs': ['isl_base_universe_d2_011_isl_016_insider_net_buy_ratio_21'], 'func': isl_base_universe_d3_011_isl_016_insider_net_buy_ratio_21}


def isl_base_universe_d3_012_isl_017_insider_value_ratio_42(isl_base_universe_d2_012_isl_017_insider_value_ratio_42):
    return _base_universe_d3(isl_base_universe_d2_012_isl_017_insider_value_ratio_42, 12)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_012_isl_017_insider_value_ratio_42'] = {'inputs': ['isl_base_universe_d2_012_isl_017_insider_value_ratio_42'], 'func': isl_base_universe_d3_012_isl_017_insider_value_ratio_42}


def isl_base_universe_d3_013_isl_018_ceo_cfo_buy_weight_63(isl_base_universe_d2_013_isl_018_ceo_cfo_buy_weight_63):
    return _base_universe_d3(isl_base_universe_d2_013_isl_018_ceo_cfo_buy_weight_63, 13)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_013_isl_018_ceo_cfo_buy_weight_63'] = {'inputs': ['isl_base_universe_d2_013_isl_018_ceo_cfo_buy_weight_63'], 'func': isl_base_universe_d3_013_isl_018_ceo_cfo_buy_weight_63}


def isl_base_universe_d3_014_isl_020_insider_conviction_126(isl_base_universe_d2_014_isl_020_insider_conviction_126):
    return _base_universe_d3(isl_base_universe_d2_014_isl_020_insider_conviction_126, 14)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_014_isl_020_insider_conviction_126'] = {'inputs': ['isl_base_universe_d2_014_isl_020_insider_conviction_126'], 'func': isl_base_universe_d3_014_isl_020_insider_conviction_126}


def isl_base_universe_d3_015_isl_021_insider_silence_189(isl_base_universe_d2_015_isl_021_insider_silence_189):
    return _base_universe_d3(isl_base_universe_d2_015_isl_021_insider_silence_189, 15)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_015_isl_021_insider_silence_189'] = {'inputs': ['isl_base_universe_d2_015_isl_021_insider_silence_189'], 'func': isl_base_universe_d3_015_isl_021_insider_silence_189}


def isl_base_universe_d3_016_isl_023_insider_net_buy_ratio_378(isl_base_universe_d2_016_isl_023_insider_net_buy_ratio_378):
    return _base_universe_d3(isl_base_universe_d2_016_isl_023_insider_net_buy_ratio_378, 16)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_016_isl_023_insider_net_buy_ratio_378'] = {'inputs': ['isl_base_universe_d2_016_isl_023_insider_net_buy_ratio_378'], 'func': isl_base_universe_d3_016_isl_023_insider_net_buy_ratio_378}


def isl_base_universe_d3_017_isl_024_insider_value_ratio_504(isl_base_universe_d2_017_isl_024_insider_value_ratio_504):
    return _base_universe_d3(isl_base_universe_d2_017_isl_024_insider_value_ratio_504, 17)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_017_isl_024_insider_value_ratio_504'] = {'inputs': ['isl_base_universe_d2_017_isl_024_insider_value_ratio_504'], 'func': isl_base_universe_d3_017_isl_024_insider_value_ratio_504}


def isl_base_universe_d3_018_isl_027_insider_conviction_1260(isl_base_universe_d2_018_isl_027_insider_conviction_1260):
    return _base_universe_d3(isl_base_universe_d2_018_isl_027_insider_conviction_1260, 18)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_018_isl_027_insider_conviction_1260'] = {'inputs': ['isl_base_universe_d2_018_isl_027_insider_conviction_1260'], 'func': isl_base_universe_d3_018_isl_027_insider_conviction_1260}


def isl_base_universe_d3_019_isl_028_insider_silence_1512(isl_base_universe_d2_019_isl_028_insider_silence_1512):
    return _base_universe_d3(isl_base_universe_d2_019_isl_028_insider_silence_1512, 19)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_019_isl_028_insider_silence_1512'] = {'inputs': ['isl_base_universe_d2_019_isl_028_insider_silence_1512'], 'func': isl_base_universe_d3_019_isl_028_insider_silence_1512}


def isl_base_universe_d3_020_isl_029_insider_buy_cluster_63(isl_base_universe_d2_020_isl_029_insider_buy_cluster_63):
    return _base_universe_d3(isl_base_universe_d2_020_isl_029_insider_buy_cluster_63, 20)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_020_isl_029_insider_buy_cluster_63'] = {'inputs': ['isl_base_universe_d2_020_isl_029_insider_buy_cluster_63'], 'func': isl_base_universe_d3_020_isl_029_insider_buy_cluster_63}


def isl_base_universe_d3_021_isl_030_insider_net_buy_ratio_252(isl_base_universe_d2_021_isl_030_insider_net_buy_ratio_252):
    return _base_universe_d3(isl_base_universe_d2_021_isl_030_insider_net_buy_ratio_252, 21)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_021_isl_030_insider_net_buy_ratio_252'] = {'inputs': ['isl_base_universe_d2_021_isl_030_insider_net_buy_ratio_252'], 'func': isl_base_universe_d3_021_isl_030_insider_net_buy_ratio_252}


def isl_base_universe_d3_022_isl_031_insider_value_ratio_21(isl_base_universe_d2_022_isl_031_insider_value_ratio_21):
    return _base_universe_d3(isl_base_universe_d2_022_isl_031_insider_value_ratio_21, 22)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_022_isl_031_insider_value_ratio_21'] = {'inputs': ['isl_base_universe_d2_022_isl_031_insider_value_ratio_21'], 'func': isl_base_universe_d3_022_isl_031_insider_value_ratio_21}


def isl_base_universe_d3_023_isl_032_ceo_cfo_buy_weight_42(isl_base_universe_d2_023_isl_032_ceo_cfo_buy_weight_42):
    return _base_universe_d3(isl_base_universe_d2_023_isl_032_ceo_cfo_buy_weight_42, 23)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_023_isl_032_ceo_cfo_buy_weight_42'] = {'inputs': ['isl_base_universe_d2_023_isl_032_ceo_cfo_buy_weight_42'], 'func': isl_base_universe_d3_023_isl_032_ceo_cfo_buy_weight_42}


def isl_base_universe_d3_024_isl_034_insider_conviction_84(isl_base_universe_d2_024_isl_034_insider_conviction_84):
    return _base_universe_d3(isl_base_universe_d2_024_isl_034_insider_conviction_84, 24)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_024_isl_034_insider_conviction_84'] = {'inputs': ['isl_base_universe_d2_024_isl_034_insider_conviction_84'], 'func': isl_base_universe_d3_024_isl_034_insider_conviction_84}


def isl_base_universe_d3_025_isl_035_insider_silence_126(isl_base_universe_d2_025_isl_035_insider_silence_126):
    return _base_universe_d3(isl_base_universe_d2_025_isl_035_insider_silence_126, 25)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_025_isl_035_insider_silence_126'] = {'inputs': ['isl_base_universe_d2_025_isl_035_insider_silence_126'], 'func': isl_base_universe_d3_025_isl_035_insider_silence_126}


def isl_base_universe_d3_026_isl_036_insider_buy_cluster_189(isl_base_universe_d2_026_isl_036_insider_buy_cluster_189):
    return _base_universe_d3(isl_base_universe_d2_026_isl_036_insider_buy_cluster_189, 26)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_026_isl_036_insider_buy_cluster_189'] = {'inputs': ['isl_base_universe_d2_026_isl_036_insider_buy_cluster_189'], 'func': isl_base_universe_d3_026_isl_036_insider_buy_cluster_189}


def isl_base_universe_d3_027_isl_038_insider_value_ratio_378(isl_base_universe_d2_027_isl_038_insider_value_ratio_378):
    return _base_universe_d3(isl_base_universe_d2_027_isl_038_insider_value_ratio_378, 27)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_027_isl_038_insider_value_ratio_378'] = {'inputs': ['isl_base_universe_d2_027_isl_038_insider_value_ratio_378'], 'func': isl_base_universe_d3_027_isl_038_insider_value_ratio_378}


def isl_base_universe_d3_028_isl_039_ceo_cfo_buy_weight_504(isl_base_universe_d2_028_isl_039_ceo_cfo_buy_weight_504):
    return _base_universe_d3(isl_base_universe_d2_028_isl_039_ceo_cfo_buy_weight_504, 28)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_028_isl_039_ceo_cfo_buy_weight_504'] = {'inputs': ['isl_base_universe_d2_028_isl_039_ceo_cfo_buy_weight_504'], 'func': isl_base_universe_d3_028_isl_039_ceo_cfo_buy_weight_504}


def isl_base_universe_d3_029_isl_041_insider_conviction_1008(isl_base_universe_d2_029_isl_041_insider_conviction_1008):
    return _base_universe_d3(isl_base_universe_d2_029_isl_041_insider_conviction_1008, 29)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_029_isl_041_insider_conviction_1008'] = {'inputs': ['isl_base_universe_d2_029_isl_041_insider_conviction_1008'], 'func': isl_base_universe_d3_029_isl_041_insider_conviction_1008}


def isl_base_universe_d3_030_isl_042_insider_silence_1260(isl_base_universe_d2_030_isl_042_insider_silence_1260):
    return _base_universe_d3(isl_base_universe_d2_030_isl_042_insider_silence_1260, 30)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_030_isl_042_insider_silence_1260'] = {'inputs': ['isl_base_universe_d2_030_isl_042_insider_silence_1260'], 'func': isl_base_universe_d3_030_isl_042_insider_silence_1260}


def isl_base_universe_d3_031_isl_043_insider_buy_cluster_1512(isl_base_universe_d2_031_isl_043_insider_buy_cluster_1512):
    return _base_universe_d3(isl_base_universe_d2_031_isl_043_insider_buy_cluster_1512, 31)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_031_isl_043_insider_buy_cluster_1512'] = {'inputs': ['isl_base_universe_d2_031_isl_043_insider_buy_cluster_1512'], 'func': isl_base_universe_d3_031_isl_043_insider_buy_cluster_1512}


def isl_base_universe_d3_032_isl_044_insider_net_buy_ratio_63(isl_base_universe_d2_032_isl_044_insider_net_buy_ratio_63):
    return _base_universe_d3(isl_base_universe_d2_032_isl_044_insider_net_buy_ratio_63, 32)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_032_isl_044_insider_net_buy_ratio_63'] = {'inputs': ['isl_base_universe_d2_032_isl_044_insider_net_buy_ratio_63'], 'func': isl_base_universe_d3_032_isl_044_insider_net_buy_ratio_63}


def isl_base_universe_d3_033_isl_045_insider_value_ratio_252(isl_base_universe_d2_033_isl_045_insider_value_ratio_252):
    return _base_universe_d3(isl_base_universe_d2_033_isl_045_insider_value_ratio_252, 33)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_033_isl_045_insider_value_ratio_252'] = {'inputs': ['isl_base_universe_d2_033_isl_045_insider_value_ratio_252'], 'func': isl_base_universe_d3_033_isl_045_insider_value_ratio_252}


def isl_base_universe_d3_034_isl_046_ceo_cfo_buy_weight_21(isl_base_universe_d2_034_isl_046_ceo_cfo_buy_weight_21):
    return _base_universe_d3(isl_base_universe_d2_034_isl_046_ceo_cfo_buy_weight_21, 34)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_034_isl_046_ceo_cfo_buy_weight_21'] = {'inputs': ['isl_base_universe_d2_034_isl_046_ceo_cfo_buy_weight_21'], 'func': isl_base_universe_d3_034_isl_046_ceo_cfo_buy_weight_21}


def isl_base_universe_d3_035_isl_048_insider_conviction_63(isl_base_universe_d2_035_isl_048_insider_conviction_63):
    return _base_universe_d3(isl_base_universe_d2_035_isl_048_insider_conviction_63, 35)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_035_isl_048_insider_conviction_63'] = {'inputs': ['isl_base_universe_d2_035_isl_048_insider_conviction_63'], 'func': isl_base_universe_d3_035_isl_048_insider_conviction_63}


def isl_base_universe_d3_036_isl_049_insider_silence_84(isl_base_universe_d2_036_isl_049_insider_silence_84):
    return _base_universe_d3(isl_base_universe_d2_036_isl_049_insider_silence_84, 36)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_036_isl_049_insider_silence_84'] = {'inputs': ['isl_base_universe_d2_036_isl_049_insider_silence_84'], 'func': isl_base_universe_d3_036_isl_049_insider_silence_84}


def isl_base_universe_d3_037_isl_050_insider_buy_cluster_126(isl_base_universe_d2_037_isl_050_insider_buy_cluster_126):
    return _base_universe_d3(isl_base_universe_d2_037_isl_050_insider_buy_cluster_126, 37)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_037_isl_050_insider_buy_cluster_126'] = {'inputs': ['isl_base_universe_d2_037_isl_050_insider_buy_cluster_126'], 'func': isl_base_universe_d3_037_isl_050_insider_buy_cluster_126}


def isl_base_universe_d3_038_isl_051_insider_net_buy_ratio_189(isl_base_universe_d2_038_isl_051_insider_net_buy_ratio_189):
    return _base_universe_d3(isl_base_universe_d2_038_isl_051_insider_net_buy_ratio_189, 38)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_038_isl_051_insider_net_buy_ratio_189'] = {'inputs': ['isl_base_universe_d2_038_isl_051_insider_net_buy_ratio_189'], 'func': isl_base_universe_d3_038_isl_051_insider_net_buy_ratio_189}


def isl_base_universe_d3_039_isl_053_ceo_cfo_buy_weight_378(isl_base_universe_d2_039_isl_053_ceo_cfo_buy_weight_378):
    return _base_universe_d3(isl_base_universe_d2_039_isl_053_ceo_cfo_buy_weight_378, 39)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_039_isl_053_ceo_cfo_buy_weight_378'] = {'inputs': ['isl_base_universe_d2_039_isl_053_ceo_cfo_buy_weight_378'], 'func': isl_base_universe_d3_039_isl_053_ceo_cfo_buy_weight_378}


def isl_base_universe_d3_040_isl_055_insider_conviction_756(isl_base_universe_d2_040_isl_055_insider_conviction_756):
    return _base_universe_d3(isl_base_universe_d2_040_isl_055_insider_conviction_756, 40)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_040_isl_055_insider_conviction_756'] = {'inputs': ['isl_base_universe_d2_040_isl_055_insider_conviction_756'], 'func': isl_base_universe_d3_040_isl_055_insider_conviction_756}


def isl_base_universe_d3_041_isl_056_insider_silence_1008(isl_base_universe_d2_041_isl_056_insider_silence_1008):
    return _base_universe_d3(isl_base_universe_d2_041_isl_056_insider_silence_1008, 41)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_041_isl_056_insider_silence_1008'] = {'inputs': ['isl_base_universe_d2_041_isl_056_insider_silence_1008'], 'func': isl_base_universe_d3_041_isl_056_insider_silence_1008}


def isl_base_universe_d3_042_isl_057_insider_buy_cluster_1260(isl_base_universe_d2_042_isl_057_insider_buy_cluster_1260):
    return _base_universe_d3(isl_base_universe_d2_042_isl_057_insider_buy_cluster_1260, 42)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_042_isl_057_insider_buy_cluster_1260'] = {'inputs': ['isl_base_universe_d2_042_isl_057_insider_buy_cluster_1260'], 'func': isl_base_universe_d3_042_isl_057_insider_buy_cluster_1260}


def isl_base_universe_d3_043_isl_058_insider_net_buy_ratio_1512(isl_base_universe_d2_043_isl_058_insider_net_buy_ratio_1512):
    return _base_universe_d3(isl_base_universe_d2_043_isl_058_insider_net_buy_ratio_1512, 43)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_043_isl_058_insider_net_buy_ratio_1512'] = {'inputs': ['isl_base_universe_d2_043_isl_058_insider_net_buy_ratio_1512'], 'func': isl_base_universe_d3_043_isl_058_insider_net_buy_ratio_1512}


def isl_base_universe_d3_044_isl_060_ceo_cfo_buy_weight_252(isl_base_universe_d2_044_isl_060_ceo_cfo_buy_weight_252):
    return _base_universe_d3(isl_base_universe_d2_044_isl_060_ceo_cfo_buy_weight_252, 44)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_044_isl_060_ceo_cfo_buy_weight_252'] = {'inputs': ['isl_base_universe_d2_044_isl_060_ceo_cfo_buy_weight_252'], 'func': isl_base_universe_d3_044_isl_060_ceo_cfo_buy_weight_252}


def isl_base_universe_d3_045_isl_062_insider_conviction_42(isl_base_universe_d2_045_isl_062_insider_conviction_42):
    return _base_universe_d3(isl_base_universe_d2_045_isl_062_insider_conviction_42, 45)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_045_isl_062_insider_conviction_42'] = {'inputs': ['isl_base_universe_d2_045_isl_062_insider_conviction_42'], 'func': isl_base_universe_d3_045_isl_062_insider_conviction_42}


def isl_base_universe_d3_046_isl_064_insider_buy_cluster_84(isl_base_universe_d2_046_isl_064_insider_buy_cluster_84):
    return _base_universe_d3(isl_base_universe_d2_046_isl_064_insider_buy_cluster_84, 46)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_046_isl_064_insider_buy_cluster_84'] = {'inputs': ['isl_base_universe_d2_046_isl_064_insider_buy_cluster_84'], 'func': isl_base_universe_d3_046_isl_064_insider_buy_cluster_84}


def isl_base_universe_d3_047_isl_065_insider_net_buy_ratio_126(isl_base_universe_d2_047_isl_065_insider_net_buy_ratio_126):
    return _base_universe_d3(isl_base_universe_d2_047_isl_065_insider_net_buy_ratio_126, 47)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_047_isl_065_insider_net_buy_ratio_126'] = {'inputs': ['isl_base_universe_d2_047_isl_065_insider_net_buy_ratio_126'], 'func': isl_base_universe_d3_047_isl_065_insider_net_buy_ratio_126}


def isl_base_universe_d3_048_isl_066_insider_value_ratio_189(isl_base_universe_d2_048_isl_066_insider_value_ratio_189):
    return _base_universe_d3(isl_base_universe_d2_048_isl_066_insider_value_ratio_189, 48)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_048_isl_066_insider_value_ratio_189'] = {'inputs': ['isl_base_universe_d2_048_isl_066_insider_value_ratio_189'], 'func': isl_base_universe_d3_048_isl_066_insider_value_ratio_189}


def isl_base_universe_d3_049_isl_069_insider_conviction_504(isl_base_universe_d2_049_isl_069_insider_conviction_504):
    return _base_universe_d3(isl_base_universe_d2_049_isl_069_insider_conviction_504, 49)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_049_isl_069_insider_conviction_504'] = {'inputs': ['isl_base_universe_d2_049_isl_069_insider_conviction_504'], 'func': isl_base_universe_d3_049_isl_069_insider_conviction_504}


def isl_base_universe_d3_050_isl_070_insider_silence_756(isl_base_universe_d2_050_isl_070_insider_silence_756):
    return _base_universe_d3(isl_base_universe_d2_050_isl_070_insider_silence_756, 50)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_050_isl_070_insider_silence_756'] = {'inputs': ['isl_base_universe_d2_050_isl_070_insider_silence_756'], 'func': isl_base_universe_d3_050_isl_070_insider_silence_756}


def isl_base_universe_d3_051_isl_071_insider_buy_cluster_1008(isl_base_universe_d2_051_isl_071_insider_buy_cluster_1008):
    return _base_universe_d3(isl_base_universe_d2_051_isl_071_insider_buy_cluster_1008, 51)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_051_isl_071_insider_buy_cluster_1008'] = {'inputs': ['isl_base_universe_d2_051_isl_071_insider_buy_cluster_1008'], 'func': isl_base_universe_d3_051_isl_071_insider_buy_cluster_1008}


def isl_base_universe_d3_052_isl_072_insider_net_buy_ratio_1260(isl_base_universe_d2_052_isl_072_insider_net_buy_ratio_1260):
    return _base_universe_d3(isl_base_universe_d2_052_isl_072_insider_net_buy_ratio_1260, 52)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_052_isl_072_insider_net_buy_ratio_1260'] = {'inputs': ['isl_base_universe_d2_052_isl_072_insider_net_buy_ratio_1260'], 'func': isl_base_universe_d3_052_isl_072_insider_net_buy_ratio_1260}


def isl_base_universe_d3_053_isl_073_insider_value_ratio_1512(isl_base_universe_d2_053_isl_073_insider_value_ratio_1512):
    return _base_universe_d3(isl_base_universe_d2_053_isl_073_insider_value_ratio_1512, 53)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_053_isl_073_insider_value_ratio_1512'] = {'inputs': ['isl_base_universe_d2_053_isl_073_insider_value_ratio_1512'], 'func': isl_base_universe_d3_053_isl_073_insider_value_ratio_1512}


def isl_base_universe_d3_054_isl_basefill_005(isl_base_universe_d2_054_isl_basefill_005):
    return _base_universe_d3(isl_base_universe_d2_054_isl_basefill_005, 54)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_054_isl_basefill_005'] = {'inputs': ['isl_base_universe_d2_054_isl_basefill_005'], 'func': isl_base_universe_d3_054_isl_basefill_005}


def isl_base_universe_d3_055_isl_basefill_012(isl_base_universe_d2_055_isl_basefill_012):
    return _base_universe_d3(isl_base_universe_d2_055_isl_basefill_012, 55)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_055_isl_basefill_012'] = {'inputs': ['isl_base_universe_d2_055_isl_basefill_012'], 'func': isl_base_universe_d3_055_isl_basefill_012}


def isl_base_universe_d3_056_isl_basefill_019(isl_base_universe_d2_056_isl_basefill_019):
    return _base_universe_d3(isl_base_universe_d2_056_isl_basefill_019, 56)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_056_isl_basefill_019'] = {'inputs': ['isl_base_universe_d2_056_isl_basefill_019'], 'func': isl_base_universe_d3_056_isl_basefill_019}


def isl_base_universe_d3_057_isl_basefill_022(isl_base_universe_d2_057_isl_basefill_022):
    return _base_universe_d3(isl_base_universe_d2_057_isl_basefill_022, 57)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_057_isl_basefill_022'] = {'inputs': ['isl_base_universe_d2_057_isl_basefill_022'], 'func': isl_base_universe_d3_057_isl_basefill_022}


def isl_base_universe_d3_058_isl_basefill_026(isl_base_universe_d2_058_isl_basefill_026):
    return _base_universe_d3(isl_base_universe_d2_058_isl_basefill_026, 58)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_058_isl_basefill_026'] = {'inputs': ['isl_base_universe_d2_058_isl_basefill_026'], 'func': isl_base_universe_d3_058_isl_basefill_026}


def isl_base_universe_d3_059_isl_basefill_033(isl_base_universe_d2_059_isl_basefill_033):
    return _base_universe_d3(isl_base_universe_d2_059_isl_basefill_033, 59)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_059_isl_basefill_033'] = {'inputs': ['isl_base_universe_d2_059_isl_basefill_033'], 'func': isl_base_universe_d3_059_isl_basefill_033}


def isl_base_universe_d3_060_isl_basefill_037(isl_base_universe_d2_060_isl_basefill_037):
    return _base_universe_d3(isl_base_universe_d2_060_isl_basefill_037, 60)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_060_isl_basefill_037'] = {'inputs': ['isl_base_universe_d2_060_isl_basefill_037'], 'func': isl_base_universe_d3_060_isl_basefill_037}


def isl_base_universe_d3_061_isl_basefill_040(isl_base_universe_d2_061_isl_basefill_040):
    return _base_universe_d3(isl_base_universe_d2_061_isl_basefill_040, 61)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_061_isl_basefill_040'] = {'inputs': ['isl_base_universe_d2_061_isl_basefill_040'], 'func': isl_base_universe_d3_061_isl_basefill_040}


def isl_base_universe_d3_062_isl_basefill_047(isl_base_universe_d2_062_isl_basefill_047):
    return _base_universe_d3(isl_base_universe_d2_062_isl_basefill_047, 62)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_062_isl_basefill_047'] = {'inputs': ['isl_base_universe_d2_062_isl_basefill_047'], 'func': isl_base_universe_d3_062_isl_basefill_047}


def isl_base_universe_d3_063_isl_basefill_052(isl_base_universe_d2_063_isl_basefill_052):
    return _base_universe_d3(isl_base_universe_d2_063_isl_basefill_052, 63)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_063_isl_basefill_052'] = {'inputs': ['isl_base_universe_d2_063_isl_basefill_052'], 'func': isl_base_universe_d3_063_isl_basefill_052}


def isl_base_universe_d3_064_isl_basefill_054(isl_base_universe_d2_064_isl_basefill_054):
    return _base_universe_d3(isl_base_universe_d2_064_isl_basefill_054, 64)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_064_isl_basefill_054'] = {'inputs': ['isl_base_universe_d2_064_isl_basefill_054'], 'func': isl_base_universe_d3_064_isl_basefill_054}


def isl_base_universe_d3_065_isl_basefill_059(isl_base_universe_d2_065_isl_basefill_059):
    return _base_universe_d3(isl_base_universe_d2_065_isl_basefill_059, 65)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_065_isl_basefill_059'] = {'inputs': ['isl_base_universe_d2_065_isl_basefill_059'], 'func': isl_base_universe_d3_065_isl_basefill_059}


def isl_base_universe_d3_066_isl_basefill_061(isl_base_universe_d2_066_isl_basefill_061):
    return _base_universe_d3(isl_base_universe_d2_066_isl_basefill_061, 66)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_066_isl_basefill_061'] = {'inputs': ['isl_base_universe_d2_066_isl_basefill_061'], 'func': isl_base_universe_d3_066_isl_basefill_061}


def isl_base_universe_d3_067_isl_basefill_063(isl_base_universe_d2_067_isl_basefill_063):
    return _base_universe_d3(isl_base_universe_d2_067_isl_basefill_063, 67)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_067_isl_basefill_063'] = {'inputs': ['isl_base_universe_d2_067_isl_basefill_063'], 'func': isl_base_universe_d3_067_isl_basefill_063}


def isl_base_universe_d3_068_isl_basefill_067(isl_base_universe_d2_068_isl_basefill_067):
    return _base_universe_d3(isl_base_universe_d2_068_isl_basefill_067, 68)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_068_isl_basefill_067'] = {'inputs': ['isl_base_universe_d2_068_isl_basefill_067'], 'func': isl_base_universe_d3_068_isl_basefill_067}


def isl_base_universe_d3_069_isl_basefill_068(isl_base_universe_d2_069_isl_basefill_068):
    return _base_universe_d3(isl_base_universe_d2_069_isl_basefill_068, 69)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_069_isl_basefill_068'] = {'inputs': ['isl_base_universe_d2_069_isl_basefill_068'], 'func': isl_base_universe_d3_069_isl_basefill_068}


def isl_base_universe_d3_070_isl_basefill_074(isl_base_universe_d2_070_isl_basefill_074):
    return _base_universe_d3(isl_base_universe_d2_070_isl_basefill_074, 70)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_070_isl_basefill_074'] = {'inputs': ['isl_base_universe_d2_070_isl_basefill_074'], 'func': isl_base_universe_d3_070_isl_basefill_074}


def isl_base_universe_d3_071_isl_basefill_075(isl_base_universe_d2_071_isl_basefill_075):
    return _base_universe_d3(isl_base_universe_d2_071_isl_basefill_075, 71)
ISL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['isl_base_universe_d3_071_isl_basefill_075'] = {'inputs': ['isl_base_universe_d2_071_isl_basefill_075'], 'func': isl_base_universe_d3_071_isl_basefill_075}

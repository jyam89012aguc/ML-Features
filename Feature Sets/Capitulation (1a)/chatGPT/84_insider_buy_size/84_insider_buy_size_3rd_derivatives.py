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



def ibs_176_ibs_001_insider_buy_cluster_21_accel_1(ibs_151_ibs_001_insider_buy_cluster_21_roc_1):
    feature = _s(ibs_151_ibs_001_insider_buy_cluster_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ibs_177_ibs_007_insider_silence_252_accel_42(ibs_152_ibs_007_insider_silence_252_roc_42):
    feature = _s(ibs_152_ibs_007_insider_silence_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ibs_178_ibs_013_insider_conviction_1512_accel_126(ibs_153_ibs_013_insider_conviction_1512_roc_126):
    feature = _s(ibs_153_ibs_013_insider_conviction_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ibs_179_ibs_019_insider_activity_accel_1_accel_378(ibs_154_ibs_019_insider_activity_accel_1_roc_378):
    feature = _s(ibs_154_ibs_019_insider_activity_accel_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def ibs_180_ibs_025_ceo_cfo_buy_weight_756_accel_4(ibs_155_ibs_025_ceo_cfo_buy_weight_756_roc_4):
    feature = _s(ibs_155_ibs_025_ceo_cfo_buy_weight_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSIDER_BUY_SIZE_REGISTRY_3RD_DERIVATIVES = {
    'ibs_176_ibs_001_insider_buy_cluster_21_accel_1': {'inputs': ['ibs_151_ibs_001_insider_buy_cluster_21_roc_1'], 'func': ibs_176_ibs_001_insider_buy_cluster_21_accel_1},
    'ibs_177_ibs_007_insider_silence_252_accel_42': {'inputs': ['ibs_152_ibs_007_insider_silence_252_roc_42'], 'func': ibs_177_ibs_007_insider_silence_252_accel_42},
    'ibs_178_ibs_013_insider_conviction_1512_accel_126': {'inputs': ['ibs_153_ibs_013_insider_conviction_1512_roc_126'], 'func': ibs_178_ibs_013_insider_conviction_1512_accel_126},
    'ibs_179_ibs_019_insider_activity_accel_1_accel_378': {'inputs': ['ibs_154_ibs_019_insider_activity_accel_1_roc_378'], 'func': ibs_179_ibs_019_insider_activity_accel_1_accel_378},
    'ibs_180_ibs_025_ceo_cfo_buy_weight_756_accel_4': {'inputs': ['ibs_155_ibs_025_ceo_cfo_buy_weight_756_roc_4'], 'func': ibs_180_ibs_025_ceo_cfo_buy_weight_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ibs_replacement_d3_001(ibs_replacement_d2_001):
    feature = _clean(ibs_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_001'] = {'inputs': ['ibs_replacement_d2_001'], 'func': ibs_replacement_d3_001}


def ibs_replacement_d3_002(ibs_replacement_d2_002):
    feature = _clean(ibs_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_002'] = {'inputs': ['ibs_replacement_d2_002'], 'func': ibs_replacement_d3_002}


def ibs_replacement_d3_003(ibs_replacement_d2_003):
    feature = _clean(ibs_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_003'] = {'inputs': ['ibs_replacement_d2_003'], 'func': ibs_replacement_d3_003}


def ibs_replacement_d3_004(ibs_replacement_d2_004):
    feature = _clean(ibs_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_004'] = {'inputs': ['ibs_replacement_d2_004'], 'func': ibs_replacement_d3_004}


def ibs_replacement_d3_005(ibs_replacement_d2_005):
    feature = _clean(ibs_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_005'] = {'inputs': ['ibs_replacement_d2_005'], 'func': ibs_replacement_d3_005}


def ibs_replacement_d3_006(ibs_replacement_d2_006):
    feature = _clean(ibs_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_006'] = {'inputs': ['ibs_replacement_d2_006'], 'func': ibs_replacement_d3_006}


def ibs_replacement_d3_007(ibs_replacement_d2_007):
    feature = _clean(ibs_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_007'] = {'inputs': ['ibs_replacement_d2_007'], 'func': ibs_replacement_d3_007}


def ibs_replacement_d3_008(ibs_replacement_d2_008):
    feature = _clean(ibs_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_008'] = {'inputs': ['ibs_replacement_d2_008'], 'func': ibs_replacement_d3_008}


def ibs_replacement_d3_009(ibs_replacement_d2_009):
    feature = _clean(ibs_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_009'] = {'inputs': ['ibs_replacement_d2_009'], 'func': ibs_replacement_d3_009}


def ibs_replacement_d3_010(ibs_replacement_d2_010):
    feature = _clean(ibs_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_010'] = {'inputs': ['ibs_replacement_d2_010'], 'func': ibs_replacement_d3_010}


def ibs_replacement_d3_011(ibs_replacement_d2_011):
    feature = _clean(ibs_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_011'] = {'inputs': ['ibs_replacement_d2_011'], 'func': ibs_replacement_d3_011}


def ibs_replacement_d3_012(ibs_replacement_d2_012):
    feature = _clean(ibs_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_012'] = {'inputs': ['ibs_replacement_d2_012'], 'func': ibs_replacement_d3_012}


def ibs_replacement_d3_013(ibs_replacement_d2_013):
    feature = _clean(ibs_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_013'] = {'inputs': ['ibs_replacement_d2_013'], 'func': ibs_replacement_d3_013}


def ibs_replacement_d3_014(ibs_replacement_d2_014):
    feature = _clean(ibs_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_014'] = {'inputs': ['ibs_replacement_d2_014'], 'func': ibs_replacement_d3_014}


def ibs_replacement_d3_015(ibs_replacement_d2_015):
    feature = _clean(ibs_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_015'] = {'inputs': ['ibs_replacement_d2_015'], 'func': ibs_replacement_d3_015}


def ibs_replacement_d3_016(ibs_replacement_d2_016):
    feature = _clean(ibs_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_016'] = {'inputs': ['ibs_replacement_d2_016'], 'func': ibs_replacement_d3_016}


def ibs_replacement_d3_017(ibs_replacement_d2_017):
    feature = _clean(ibs_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_017'] = {'inputs': ['ibs_replacement_d2_017'], 'func': ibs_replacement_d3_017}


def ibs_replacement_d3_018(ibs_replacement_d2_018):
    feature = _clean(ibs_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_018'] = {'inputs': ['ibs_replacement_d2_018'], 'func': ibs_replacement_d3_018}


def ibs_replacement_d3_019(ibs_replacement_d2_019):
    feature = _clean(ibs_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_019'] = {'inputs': ['ibs_replacement_d2_019'], 'func': ibs_replacement_d3_019}


def ibs_replacement_d3_020(ibs_replacement_d2_020):
    feature = _clean(ibs_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_020'] = {'inputs': ['ibs_replacement_d2_020'], 'func': ibs_replacement_d3_020}


def ibs_replacement_d3_021(ibs_replacement_d2_021):
    feature = _clean(ibs_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_021'] = {'inputs': ['ibs_replacement_d2_021'], 'func': ibs_replacement_d3_021}


def ibs_replacement_d3_022(ibs_replacement_d2_022):
    feature = _clean(ibs_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_022'] = {'inputs': ['ibs_replacement_d2_022'], 'func': ibs_replacement_d3_022}


def ibs_replacement_d3_023(ibs_replacement_d2_023):
    feature = _clean(ibs_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_023'] = {'inputs': ['ibs_replacement_d2_023'], 'func': ibs_replacement_d3_023}


def ibs_replacement_d3_024(ibs_replacement_d2_024):
    feature = _clean(ibs_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_024'] = {'inputs': ['ibs_replacement_d2_024'], 'func': ibs_replacement_d3_024}


def ibs_replacement_d3_025(ibs_replacement_d2_025):
    feature = _clean(ibs_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_025'] = {'inputs': ['ibs_replacement_d2_025'], 'func': ibs_replacement_d3_025}


def ibs_replacement_d3_026(ibs_replacement_d2_026):
    feature = _clean(ibs_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_026'] = {'inputs': ['ibs_replacement_d2_026'], 'func': ibs_replacement_d3_026}


def ibs_replacement_d3_027(ibs_replacement_d2_027):
    feature = _clean(ibs_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_027'] = {'inputs': ['ibs_replacement_d2_027'], 'func': ibs_replacement_d3_027}


def ibs_replacement_d3_028(ibs_replacement_d2_028):
    feature = _clean(ibs_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_028'] = {'inputs': ['ibs_replacement_d2_028'], 'func': ibs_replacement_d3_028}


def ibs_replacement_d3_029(ibs_replacement_d2_029):
    feature = _clean(ibs_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_029'] = {'inputs': ['ibs_replacement_d2_029'], 'func': ibs_replacement_d3_029}


def ibs_replacement_d3_030(ibs_replacement_d2_030):
    feature = _clean(ibs_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_030'] = {'inputs': ['ibs_replacement_d2_030'], 'func': ibs_replacement_d3_030}


def ibs_replacement_d3_031(ibs_replacement_d2_031):
    feature = _clean(ibs_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_031'] = {'inputs': ['ibs_replacement_d2_031'], 'func': ibs_replacement_d3_031}


def ibs_replacement_d3_032(ibs_replacement_d2_032):
    feature = _clean(ibs_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_032'] = {'inputs': ['ibs_replacement_d2_032'], 'func': ibs_replacement_d3_032}


def ibs_replacement_d3_033(ibs_replacement_d2_033):
    feature = _clean(ibs_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_033'] = {'inputs': ['ibs_replacement_d2_033'], 'func': ibs_replacement_d3_033}


def ibs_replacement_d3_034(ibs_replacement_d2_034):
    feature = _clean(ibs_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_034'] = {'inputs': ['ibs_replacement_d2_034'], 'func': ibs_replacement_d3_034}


def ibs_replacement_d3_035(ibs_replacement_d2_035):
    feature = _clean(ibs_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_035'] = {'inputs': ['ibs_replacement_d2_035'], 'func': ibs_replacement_d3_035}


def ibs_replacement_d3_036(ibs_replacement_d2_036):
    feature = _clean(ibs_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_036'] = {'inputs': ['ibs_replacement_d2_036'], 'func': ibs_replacement_d3_036}


def ibs_replacement_d3_037(ibs_replacement_d2_037):
    feature = _clean(ibs_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_037'] = {'inputs': ['ibs_replacement_d2_037'], 'func': ibs_replacement_d3_037}


def ibs_replacement_d3_038(ibs_replacement_d2_038):
    feature = _clean(ibs_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_038'] = {'inputs': ['ibs_replacement_d2_038'], 'func': ibs_replacement_d3_038}


def ibs_replacement_d3_039(ibs_replacement_d2_039):
    feature = _clean(ibs_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_039'] = {'inputs': ['ibs_replacement_d2_039'], 'func': ibs_replacement_d3_039}


def ibs_replacement_d3_040(ibs_replacement_d2_040):
    feature = _clean(ibs_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_040'] = {'inputs': ['ibs_replacement_d2_040'], 'func': ibs_replacement_d3_040}


def ibs_replacement_d3_041(ibs_replacement_d2_041):
    feature = _clean(ibs_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_041'] = {'inputs': ['ibs_replacement_d2_041'], 'func': ibs_replacement_d3_041}


def ibs_replacement_d3_042(ibs_replacement_d2_042):
    feature = _clean(ibs_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_042'] = {'inputs': ['ibs_replacement_d2_042'], 'func': ibs_replacement_d3_042}


def ibs_replacement_d3_043(ibs_replacement_d2_043):
    feature = _clean(ibs_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_043'] = {'inputs': ['ibs_replacement_d2_043'], 'func': ibs_replacement_d3_043}


def ibs_replacement_d3_044(ibs_replacement_d2_044):
    feature = _clean(ibs_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_044'] = {'inputs': ['ibs_replacement_d2_044'], 'func': ibs_replacement_d3_044}


def ibs_replacement_d3_045(ibs_replacement_d2_045):
    feature = _clean(ibs_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_045'] = {'inputs': ['ibs_replacement_d2_045'], 'func': ibs_replacement_d3_045}


def ibs_replacement_d3_046(ibs_replacement_d2_046):
    feature = _clean(ibs_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_046'] = {'inputs': ['ibs_replacement_d2_046'], 'func': ibs_replacement_d3_046}


def ibs_replacement_d3_047(ibs_replacement_d2_047):
    feature = _clean(ibs_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_047'] = {'inputs': ['ibs_replacement_d2_047'], 'func': ibs_replacement_d3_047}


def ibs_replacement_d3_048(ibs_replacement_d2_048):
    feature = _clean(ibs_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_048'] = {'inputs': ['ibs_replacement_d2_048'], 'func': ibs_replacement_d3_048}


def ibs_replacement_d3_049(ibs_replacement_d2_049):
    feature = _clean(ibs_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_049'] = {'inputs': ['ibs_replacement_d2_049'], 'func': ibs_replacement_d3_049}


def ibs_replacement_d3_050(ibs_replacement_d2_050):
    feature = _clean(ibs_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_050'] = {'inputs': ['ibs_replacement_d2_050'], 'func': ibs_replacement_d3_050}


def ibs_replacement_d3_051(ibs_replacement_d2_051):
    feature = _clean(ibs_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_051'] = {'inputs': ['ibs_replacement_d2_051'], 'func': ibs_replacement_d3_051}


def ibs_replacement_d3_052(ibs_replacement_d2_052):
    feature = _clean(ibs_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_052'] = {'inputs': ['ibs_replacement_d2_052'], 'func': ibs_replacement_d3_052}


def ibs_replacement_d3_053(ibs_replacement_d2_053):
    feature = _clean(ibs_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_053'] = {'inputs': ['ibs_replacement_d2_053'], 'func': ibs_replacement_d3_053}


def ibs_replacement_d3_054(ibs_replacement_d2_054):
    feature = _clean(ibs_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_054'] = {'inputs': ['ibs_replacement_d2_054'], 'func': ibs_replacement_d3_054}


def ibs_replacement_d3_055(ibs_replacement_d2_055):
    feature = _clean(ibs_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_055'] = {'inputs': ['ibs_replacement_d2_055'], 'func': ibs_replacement_d3_055}


def ibs_replacement_d3_056(ibs_replacement_d2_056):
    feature = _clean(ibs_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_056'] = {'inputs': ['ibs_replacement_d2_056'], 'func': ibs_replacement_d3_056}


def ibs_replacement_d3_057(ibs_replacement_d2_057):
    feature = _clean(ibs_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_057'] = {'inputs': ['ibs_replacement_d2_057'], 'func': ibs_replacement_d3_057}


def ibs_replacement_d3_058(ibs_replacement_d2_058):
    feature = _clean(ibs_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_058'] = {'inputs': ['ibs_replacement_d2_058'], 'func': ibs_replacement_d3_058}


def ibs_replacement_d3_059(ibs_replacement_d2_059):
    feature = _clean(ibs_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_059'] = {'inputs': ['ibs_replacement_d2_059'], 'func': ibs_replacement_d3_059}


def ibs_replacement_d3_060(ibs_replacement_d2_060):
    feature = _clean(ibs_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_060'] = {'inputs': ['ibs_replacement_d2_060'], 'func': ibs_replacement_d3_060}


def ibs_replacement_d3_061(ibs_replacement_d2_061):
    feature = _clean(ibs_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_061'] = {'inputs': ['ibs_replacement_d2_061'], 'func': ibs_replacement_d3_061}


def ibs_replacement_d3_062(ibs_replacement_d2_062):
    feature = _clean(ibs_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_062'] = {'inputs': ['ibs_replacement_d2_062'], 'func': ibs_replacement_d3_062}


def ibs_replacement_d3_063(ibs_replacement_d2_063):
    feature = _clean(ibs_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_063'] = {'inputs': ['ibs_replacement_d2_063'], 'func': ibs_replacement_d3_063}


def ibs_replacement_d3_064(ibs_replacement_d2_064):
    feature = _clean(ibs_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_064'] = {'inputs': ['ibs_replacement_d2_064'], 'func': ibs_replacement_d3_064}


def ibs_replacement_d3_065(ibs_replacement_d2_065):
    feature = _clean(ibs_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_065'] = {'inputs': ['ibs_replacement_d2_065'], 'func': ibs_replacement_d3_065}


def ibs_replacement_d3_066(ibs_replacement_d2_066):
    feature = _clean(ibs_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_066'] = {'inputs': ['ibs_replacement_d2_066'], 'func': ibs_replacement_d3_066}


def ibs_replacement_d3_067(ibs_replacement_d2_067):
    feature = _clean(ibs_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_067'] = {'inputs': ['ibs_replacement_d2_067'], 'func': ibs_replacement_d3_067}


def ibs_replacement_d3_068(ibs_replacement_d2_068):
    feature = _clean(ibs_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_068'] = {'inputs': ['ibs_replacement_d2_068'], 'func': ibs_replacement_d3_068}


def ibs_replacement_d3_069(ibs_replacement_d2_069):
    feature = _clean(ibs_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_069'] = {'inputs': ['ibs_replacement_d2_069'], 'func': ibs_replacement_d3_069}


def ibs_replacement_d3_070(ibs_replacement_d2_070):
    feature = _clean(ibs_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_070'] = {'inputs': ['ibs_replacement_d2_070'], 'func': ibs_replacement_d3_070}


def ibs_replacement_d3_071(ibs_replacement_d2_071):
    feature = _clean(ibs_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_071'] = {'inputs': ['ibs_replacement_d2_071'], 'func': ibs_replacement_d3_071}


def ibs_replacement_d3_072(ibs_replacement_d2_072):
    feature = _clean(ibs_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_072'] = {'inputs': ['ibs_replacement_d2_072'], 'func': ibs_replacement_d3_072}


def ibs_replacement_d3_073(ibs_replacement_d2_073):
    feature = _clean(ibs_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_073'] = {'inputs': ['ibs_replacement_d2_073'], 'func': ibs_replacement_d3_073}


def ibs_replacement_d3_074(ibs_replacement_d2_074):
    feature = _clean(ibs_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_074'] = {'inputs': ['ibs_replacement_d2_074'], 'func': ibs_replacement_d3_074}


def ibs_replacement_d3_075(ibs_replacement_d2_075):
    feature = _clean(ibs_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_075'] = {'inputs': ['ibs_replacement_d2_075'], 'func': ibs_replacement_d3_075}


def ibs_replacement_d3_076(ibs_replacement_d2_076):
    feature = _clean(ibs_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_076'] = {'inputs': ['ibs_replacement_d2_076'], 'func': ibs_replacement_d3_076}


def ibs_replacement_d3_077(ibs_replacement_d2_077):
    feature = _clean(ibs_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_077'] = {'inputs': ['ibs_replacement_d2_077'], 'func': ibs_replacement_d3_077}


def ibs_replacement_d3_078(ibs_replacement_d2_078):
    feature = _clean(ibs_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_078'] = {'inputs': ['ibs_replacement_d2_078'], 'func': ibs_replacement_d3_078}


def ibs_replacement_d3_079(ibs_replacement_d2_079):
    feature = _clean(ibs_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_079'] = {'inputs': ['ibs_replacement_d2_079'], 'func': ibs_replacement_d3_079}


def ibs_replacement_d3_080(ibs_replacement_d2_080):
    feature = _clean(ibs_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_080'] = {'inputs': ['ibs_replacement_d2_080'], 'func': ibs_replacement_d3_080}


def ibs_replacement_d3_081(ibs_replacement_d2_081):
    feature = _clean(ibs_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_081'] = {'inputs': ['ibs_replacement_d2_081'], 'func': ibs_replacement_d3_081}


def ibs_replacement_d3_082(ibs_replacement_d2_082):
    feature = _clean(ibs_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_082'] = {'inputs': ['ibs_replacement_d2_082'], 'func': ibs_replacement_d3_082}


def ibs_replacement_d3_083(ibs_replacement_d2_083):
    feature = _clean(ibs_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_083'] = {'inputs': ['ibs_replacement_d2_083'], 'func': ibs_replacement_d3_083}


def ibs_replacement_d3_084(ibs_replacement_d2_084):
    feature = _clean(ibs_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_084'] = {'inputs': ['ibs_replacement_d2_084'], 'func': ibs_replacement_d3_084}


def ibs_replacement_d3_085(ibs_replacement_d2_085):
    feature = _clean(ibs_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_085'] = {'inputs': ['ibs_replacement_d2_085'], 'func': ibs_replacement_d3_085}


def ibs_replacement_d3_086(ibs_replacement_d2_086):
    feature = _clean(ibs_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_086'] = {'inputs': ['ibs_replacement_d2_086'], 'func': ibs_replacement_d3_086}


def ibs_replacement_d3_087(ibs_replacement_d2_087):
    feature = _clean(ibs_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_087'] = {'inputs': ['ibs_replacement_d2_087'], 'func': ibs_replacement_d3_087}


def ibs_replacement_d3_088(ibs_replacement_d2_088):
    feature = _clean(ibs_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_088'] = {'inputs': ['ibs_replacement_d2_088'], 'func': ibs_replacement_d3_088}


def ibs_replacement_d3_089(ibs_replacement_d2_089):
    feature = _clean(ibs_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_089'] = {'inputs': ['ibs_replacement_d2_089'], 'func': ibs_replacement_d3_089}


def ibs_replacement_d3_090(ibs_replacement_d2_090):
    feature = _clean(ibs_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_090'] = {'inputs': ['ibs_replacement_d2_090'], 'func': ibs_replacement_d3_090}


def ibs_replacement_d3_091(ibs_replacement_d2_091):
    feature = _clean(ibs_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_091'] = {'inputs': ['ibs_replacement_d2_091'], 'func': ibs_replacement_d3_091}


def ibs_replacement_d3_092(ibs_replacement_d2_092):
    feature = _clean(ibs_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_092'] = {'inputs': ['ibs_replacement_d2_092'], 'func': ibs_replacement_d3_092}


def ibs_replacement_d3_093(ibs_replacement_d2_093):
    feature = _clean(ibs_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_093'] = {'inputs': ['ibs_replacement_d2_093'], 'func': ibs_replacement_d3_093}


def ibs_replacement_d3_094(ibs_replacement_d2_094):
    feature = _clean(ibs_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_094'] = {'inputs': ['ibs_replacement_d2_094'], 'func': ibs_replacement_d3_094}


def ibs_replacement_d3_095(ibs_replacement_d2_095):
    feature = _clean(ibs_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_095'] = {'inputs': ['ibs_replacement_d2_095'], 'func': ibs_replacement_d3_095}


def ibs_replacement_d3_096(ibs_replacement_d2_096):
    feature = _clean(ibs_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_096'] = {'inputs': ['ibs_replacement_d2_096'], 'func': ibs_replacement_d3_096}


def ibs_replacement_d3_097(ibs_replacement_d2_097):
    feature = _clean(ibs_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_097'] = {'inputs': ['ibs_replacement_d2_097'], 'func': ibs_replacement_d3_097}


def ibs_replacement_d3_098(ibs_replacement_d2_098):
    feature = _clean(ibs_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_098'] = {'inputs': ['ibs_replacement_d2_098'], 'func': ibs_replacement_d3_098}


def ibs_replacement_d3_099(ibs_replacement_d2_099):
    feature = _clean(ibs_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_099'] = {'inputs': ['ibs_replacement_d2_099'], 'func': ibs_replacement_d3_099}


def ibs_replacement_d3_100(ibs_replacement_d2_100):
    feature = _clean(ibs_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_100'] = {'inputs': ['ibs_replacement_d2_100'], 'func': ibs_replacement_d3_100}


def ibs_replacement_d3_101(ibs_replacement_d2_101):
    feature = _clean(ibs_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_101'] = {'inputs': ['ibs_replacement_d2_101'], 'func': ibs_replacement_d3_101}


def ibs_replacement_d3_102(ibs_replacement_d2_102):
    feature = _clean(ibs_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_102'] = {'inputs': ['ibs_replacement_d2_102'], 'func': ibs_replacement_d3_102}


def ibs_replacement_d3_103(ibs_replacement_d2_103):
    feature = _clean(ibs_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_103'] = {'inputs': ['ibs_replacement_d2_103'], 'func': ibs_replacement_d3_103}


def ibs_replacement_d3_104(ibs_replacement_d2_104):
    feature = _clean(ibs_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_104'] = {'inputs': ['ibs_replacement_d2_104'], 'func': ibs_replacement_d3_104}


def ibs_replacement_d3_105(ibs_replacement_d2_105):
    feature = _clean(ibs_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_105'] = {'inputs': ['ibs_replacement_d2_105'], 'func': ibs_replacement_d3_105}


def ibs_replacement_d3_106(ibs_replacement_d2_106):
    feature = _clean(ibs_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_106'] = {'inputs': ['ibs_replacement_d2_106'], 'func': ibs_replacement_d3_106}


def ibs_replacement_d3_107(ibs_replacement_d2_107):
    feature = _clean(ibs_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_107'] = {'inputs': ['ibs_replacement_d2_107'], 'func': ibs_replacement_d3_107}


def ibs_replacement_d3_108(ibs_replacement_d2_108):
    feature = _clean(ibs_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_108'] = {'inputs': ['ibs_replacement_d2_108'], 'func': ibs_replacement_d3_108}


def ibs_replacement_d3_109(ibs_replacement_d2_109):
    feature = _clean(ibs_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_109'] = {'inputs': ['ibs_replacement_d2_109'], 'func': ibs_replacement_d3_109}


def ibs_replacement_d3_110(ibs_replacement_d2_110):
    feature = _clean(ibs_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_110'] = {'inputs': ['ibs_replacement_d2_110'], 'func': ibs_replacement_d3_110}


def ibs_replacement_d3_111(ibs_replacement_d2_111):
    feature = _clean(ibs_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_111'] = {'inputs': ['ibs_replacement_d2_111'], 'func': ibs_replacement_d3_111}


def ibs_replacement_d3_112(ibs_replacement_d2_112):
    feature = _clean(ibs_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IBS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibs_replacement_d3_112'] = {'inputs': ['ibs_replacement_d2_112'], 'func': ibs_replacement_d3_112}


# Third-derivative extensions for repaired first-base features.
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibs_base_universe_d3_001_ibs_002_insider_net_buy_ratio_42(ibs_base_universe_d2_001_ibs_002_insider_net_buy_ratio_42):
    return _base_universe_d3(ibs_base_universe_d2_001_ibs_002_insider_net_buy_ratio_42, 1)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_001_ibs_002_insider_net_buy_ratio_42'] = {'inputs': ['ibs_base_universe_d2_001_ibs_002_insider_net_buy_ratio_42'], 'func': ibs_base_universe_d3_001_ibs_002_insider_net_buy_ratio_42}


def ibs_base_universe_d3_002_ibs_003_insider_value_ratio_63(ibs_base_universe_d2_002_ibs_003_insider_value_ratio_63):
    return _base_universe_d3(ibs_base_universe_d2_002_ibs_003_insider_value_ratio_63, 2)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_002_ibs_003_insider_value_ratio_63'] = {'inputs': ['ibs_base_universe_d2_002_ibs_003_insider_value_ratio_63'], 'func': ibs_base_universe_d3_002_ibs_003_insider_value_ratio_63}


def ibs_base_universe_d3_003_ibs_004_ceo_cfo_buy_weight_84(ibs_base_universe_d2_003_ibs_004_ceo_cfo_buy_weight_84):
    return _base_universe_d3(ibs_base_universe_d2_003_ibs_004_ceo_cfo_buy_weight_84, 3)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_003_ibs_004_ceo_cfo_buy_weight_84'] = {'inputs': ['ibs_base_universe_d2_003_ibs_004_ceo_cfo_buy_weight_84'], 'func': ibs_base_universe_d3_003_ibs_004_ceo_cfo_buy_weight_84}


def ibs_base_universe_d3_004_ibs_006_insider_conviction_189(ibs_base_universe_d2_004_ibs_006_insider_conviction_189):
    return _base_universe_d3(ibs_base_universe_d2_004_ibs_006_insider_conviction_189, 4)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_004_ibs_006_insider_conviction_189'] = {'inputs': ['ibs_base_universe_d2_004_ibs_006_insider_conviction_189'], 'func': ibs_base_universe_d3_004_ibs_006_insider_conviction_189}


def ibs_base_universe_d3_005_ibs_008_insider_buy_cluster_378(ibs_base_universe_d2_005_ibs_008_insider_buy_cluster_378):
    return _base_universe_d3(ibs_base_universe_d2_005_ibs_008_insider_buy_cluster_378, 5)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_005_ibs_008_insider_buy_cluster_378'] = {'inputs': ['ibs_base_universe_d2_005_ibs_008_insider_buy_cluster_378'], 'func': ibs_base_universe_d3_005_ibs_008_insider_buy_cluster_378}


def ibs_base_universe_d3_006_ibs_009_insider_net_buy_ratio_504(ibs_base_universe_d2_006_ibs_009_insider_net_buy_ratio_504):
    return _base_universe_d3(ibs_base_universe_d2_006_ibs_009_insider_net_buy_ratio_504, 6)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_006_ibs_009_insider_net_buy_ratio_504'] = {'inputs': ['ibs_base_universe_d2_006_ibs_009_insider_net_buy_ratio_504'], 'func': ibs_base_universe_d3_006_ibs_009_insider_net_buy_ratio_504}


def ibs_base_universe_d3_007_ibs_010_insider_value_ratio_756(ibs_base_universe_d2_007_ibs_010_insider_value_ratio_756):
    return _base_universe_d3(ibs_base_universe_d2_007_ibs_010_insider_value_ratio_756, 7)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_007_ibs_010_insider_value_ratio_756'] = {'inputs': ['ibs_base_universe_d2_007_ibs_010_insider_value_ratio_756'], 'func': ibs_base_universe_d3_007_ibs_010_insider_value_ratio_756}


def ibs_base_universe_d3_008_ibs_011_ceo_cfo_buy_weight_1008(ibs_base_universe_d2_008_ibs_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d3(ibs_base_universe_d2_008_ibs_011_ceo_cfo_buy_weight_1008, 8)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_008_ibs_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['ibs_base_universe_d2_008_ibs_011_ceo_cfo_buy_weight_1008'], 'func': ibs_base_universe_d3_008_ibs_011_ceo_cfo_buy_weight_1008}


def ibs_base_universe_d3_009_ibs_014_insider_silence_63(ibs_base_universe_d2_009_ibs_014_insider_silence_63):
    return _base_universe_d3(ibs_base_universe_d2_009_ibs_014_insider_silence_63, 9)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_009_ibs_014_insider_silence_63'] = {'inputs': ['ibs_base_universe_d2_009_ibs_014_insider_silence_63'], 'func': ibs_base_universe_d3_009_ibs_014_insider_silence_63}


def ibs_base_universe_d3_010_ibs_015_insider_buy_cluster_252(ibs_base_universe_d2_010_ibs_015_insider_buy_cluster_252):
    return _base_universe_d3(ibs_base_universe_d2_010_ibs_015_insider_buy_cluster_252, 10)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_010_ibs_015_insider_buy_cluster_252'] = {'inputs': ['ibs_base_universe_d2_010_ibs_015_insider_buy_cluster_252'], 'func': ibs_base_universe_d3_010_ibs_015_insider_buy_cluster_252}


def ibs_base_universe_d3_011_ibs_016_insider_net_buy_ratio_21(ibs_base_universe_d2_011_ibs_016_insider_net_buy_ratio_21):
    return _base_universe_d3(ibs_base_universe_d2_011_ibs_016_insider_net_buy_ratio_21, 11)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_011_ibs_016_insider_net_buy_ratio_21'] = {'inputs': ['ibs_base_universe_d2_011_ibs_016_insider_net_buy_ratio_21'], 'func': ibs_base_universe_d3_011_ibs_016_insider_net_buy_ratio_21}


def ibs_base_universe_d3_012_ibs_017_insider_value_ratio_42(ibs_base_universe_d2_012_ibs_017_insider_value_ratio_42):
    return _base_universe_d3(ibs_base_universe_d2_012_ibs_017_insider_value_ratio_42, 12)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_012_ibs_017_insider_value_ratio_42'] = {'inputs': ['ibs_base_universe_d2_012_ibs_017_insider_value_ratio_42'], 'func': ibs_base_universe_d3_012_ibs_017_insider_value_ratio_42}


def ibs_base_universe_d3_013_ibs_018_ceo_cfo_buy_weight_63(ibs_base_universe_d2_013_ibs_018_ceo_cfo_buy_weight_63):
    return _base_universe_d3(ibs_base_universe_d2_013_ibs_018_ceo_cfo_buy_weight_63, 13)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_013_ibs_018_ceo_cfo_buy_weight_63'] = {'inputs': ['ibs_base_universe_d2_013_ibs_018_ceo_cfo_buy_weight_63'], 'func': ibs_base_universe_d3_013_ibs_018_ceo_cfo_buy_weight_63}


def ibs_base_universe_d3_014_ibs_020_insider_conviction_126(ibs_base_universe_d2_014_ibs_020_insider_conviction_126):
    return _base_universe_d3(ibs_base_universe_d2_014_ibs_020_insider_conviction_126, 14)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_014_ibs_020_insider_conviction_126'] = {'inputs': ['ibs_base_universe_d2_014_ibs_020_insider_conviction_126'], 'func': ibs_base_universe_d3_014_ibs_020_insider_conviction_126}


def ibs_base_universe_d3_015_ibs_021_insider_silence_189(ibs_base_universe_d2_015_ibs_021_insider_silence_189):
    return _base_universe_d3(ibs_base_universe_d2_015_ibs_021_insider_silence_189, 15)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_015_ibs_021_insider_silence_189'] = {'inputs': ['ibs_base_universe_d2_015_ibs_021_insider_silence_189'], 'func': ibs_base_universe_d3_015_ibs_021_insider_silence_189}


def ibs_base_universe_d3_016_ibs_023_insider_net_buy_ratio_378(ibs_base_universe_d2_016_ibs_023_insider_net_buy_ratio_378):
    return _base_universe_d3(ibs_base_universe_d2_016_ibs_023_insider_net_buy_ratio_378, 16)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_016_ibs_023_insider_net_buy_ratio_378'] = {'inputs': ['ibs_base_universe_d2_016_ibs_023_insider_net_buy_ratio_378'], 'func': ibs_base_universe_d3_016_ibs_023_insider_net_buy_ratio_378}


def ibs_base_universe_d3_017_ibs_024_insider_value_ratio_504(ibs_base_universe_d2_017_ibs_024_insider_value_ratio_504):
    return _base_universe_d3(ibs_base_universe_d2_017_ibs_024_insider_value_ratio_504, 17)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_017_ibs_024_insider_value_ratio_504'] = {'inputs': ['ibs_base_universe_d2_017_ibs_024_insider_value_ratio_504'], 'func': ibs_base_universe_d3_017_ibs_024_insider_value_ratio_504}


def ibs_base_universe_d3_018_ibs_027_insider_conviction_1260(ibs_base_universe_d2_018_ibs_027_insider_conviction_1260):
    return _base_universe_d3(ibs_base_universe_d2_018_ibs_027_insider_conviction_1260, 18)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_018_ibs_027_insider_conviction_1260'] = {'inputs': ['ibs_base_universe_d2_018_ibs_027_insider_conviction_1260'], 'func': ibs_base_universe_d3_018_ibs_027_insider_conviction_1260}


def ibs_base_universe_d3_019_ibs_028_insider_silence_1512(ibs_base_universe_d2_019_ibs_028_insider_silence_1512):
    return _base_universe_d3(ibs_base_universe_d2_019_ibs_028_insider_silence_1512, 19)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_019_ibs_028_insider_silence_1512'] = {'inputs': ['ibs_base_universe_d2_019_ibs_028_insider_silence_1512'], 'func': ibs_base_universe_d3_019_ibs_028_insider_silence_1512}


def ibs_base_universe_d3_020_ibs_029_insider_buy_cluster_63(ibs_base_universe_d2_020_ibs_029_insider_buy_cluster_63):
    return _base_universe_d3(ibs_base_universe_d2_020_ibs_029_insider_buy_cluster_63, 20)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_020_ibs_029_insider_buy_cluster_63'] = {'inputs': ['ibs_base_universe_d2_020_ibs_029_insider_buy_cluster_63'], 'func': ibs_base_universe_d3_020_ibs_029_insider_buy_cluster_63}


def ibs_base_universe_d3_021_ibs_030_insider_net_buy_ratio_252(ibs_base_universe_d2_021_ibs_030_insider_net_buy_ratio_252):
    return _base_universe_d3(ibs_base_universe_d2_021_ibs_030_insider_net_buy_ratio_252, 21)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_021_ibs_030_insider_net_buy_ratio_252'] = {'inputs': ['ibs_base_universe_d2_021_ibs_030_insider_net_buy_ratio_252'], 'func': ibs_base_universe_d3_021_ibs_030_insider_net_buy_ratio_252}


def ibs_base_universe_d3_022_ibs_031_insider_value_ratio_21(ibs_base_universe_d2_022_ibs_031_insider_value_ratio_21):
    return _base_universe_d3(ibs_base_universe_d2_022_ibs_031_insider_value_ratio_21, 22)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_022_ibs_031_insider_value_ratio_21'] = {'inputs': ['ibs_base_universe_d2_022_ibs_031_insider_value_ratio_21'], 'func': ibs_base_universe_d3_022_ibs_031_insider_value_ratio_21}


def ibs_base_universe_d3_023_ibs_032_ceo_cfo_buy_weight_42(ibs_base_universe_d2_023_ibs_032_ceo_cfo_buy_weight_42):
    return _base_universe_d3(ibs_base_universe_d2_023_ibs_032_ceo_cfo_buy_weight_42, 23)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_023_ibs_032_ceo_cfo_buy_weight_42'] = {'inputs': ['ibs_base_universe_d2_023_ibs_032_ceo_cfo_buy_weight_42'], 'func': ibs_base_universe_d3_023_ibs_032_ceo_cfo_buy_weight_42}


def ibs_base_universe_d3_024_ibs_034_insider_conviction_84(ibs_base_universe_d2_024_ibs_034_insider_conviction_84):
    return _base_universe_d3(ibs_base_universe_d2_024_ibs_034_insider_conviction_84, 24)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_024_ibs_034_insider_conviction_84'] = {'inputs': ['ibs_base_universe_d2_024_ibs_034_insider_conviction_84'], 'func': ibs_base_universe_d3_024_ibs_034_insider_conviction_84}


def ibs_base_universe_d3_025_ibs_035_insider_silence_126(ibs_base_universe_d2_025_ibs_035_insider_silence_126):
    return _base_universe_d3(ibs_base_universe_d2_025_ibs_035_insider_silence_126, 25)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_025_ibs_035_insider_silence_126'] = {'inputs': ['ibs_base_universe_d2_025_ibs_035_insider_silence_126'], 'func': ibs_base_universe_d3_025_ibs_035_insider_silence_126}


def ibs_base_universe_d3_026_ibs_036_insider_buy_cluster_189(ibs_base_universe_d2_026_ibs_036_insider_buy_cluster_189):
    return _base_universe_d3(ibs_base_universe_d2_026_ibs_036_insider_buy_cluster_189, 26)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_026_ibs_036_insider_buy_cluster_189'] = {'inputs': ['ibs_base_universe_d2_026_ibs_036_insider_buy_cluster_189'], 'func': ibs_base_universe_d3_026_ibs_036_insider_buy_cluster_189}


def ibs_base_universe_d3_027_ibs_038_insider_value_ratio_378(ibs_base_universe_d2_027_ibs_038_insider_value_ratio_378):
    return _base_universe_d3(ibs_base_universe_d2_027_ibs_038_insider_value_ratio_378, 27)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_027_ibs_038_insider_value_ratio_378'] = {'inputs': ['ibs_base_universe_d2_027_ibs_038_insider_value_ratio_378'], 'func': ibs_base_universe_d3_027_ibs_038_insider_value_ratio_378}


def ibs_base_universe_d3_028_ibs_039_ceo_cfo_buy_weight_504(ibs_base_universe_d2_028_ibs_039_ceo_cfo_buy_weight_504):
    return _base_universe_d3(ibs_base_universe_d2_028_ibs_039_ceo_cfo_buy_weight_504, 28)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_028_ibs_039_ceo_cfo_buy_weight_504'] = {'inputs': ['ibs_base_universe_d2_028_ibs_039_ceo_cfo_buy_weight_504'], 'func': ibs_base_universe_d3_028_ibs_039_ceo_cfo_buy_weight_504}


def ibs_base_universe_d3_029_ibs_041_insider_conviction_1008(ibs_base_universe_d2_029_ibs_041_insider_conviction_1008):
    return _base_universe_d3(ibs_base_universe_d2_029_ibs_041_insider_conviction_1008, 29)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_029_ibs_041_insider_conviction_1008'] = {'inputs': ['ibs_base_universe_d2_029_ibs_041_insider_conviction_1008'], 'func': ibs_base_universe_d3_029_ibs_041_insider_conviction_1008}


def ibs_base_universe_d3_030_ibs_042_insider_silence_1260(ibs_base_universe_d2_030_ibs_042_insider_silence_1260):
    return _base_universe_d3(ibs_base_universe_d2_030_ibs_042_insider_silence_1260, 30)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_030_ibs_042_insider_silence_1260'] = {'inputs': ['ibs_base_universe_d2_030_ibs_042_insider_silence_1260'], 'func': ibs_base_universe_d3_030_ibs_042_insider_silence_1260}


def ibs_base_universe_d3_031_ibs_043_insider_buy_cluster_1512(ibs_base_universe_d2_031_ibs_043_insider_buy_cluster_1512):
    return _base_universe_d3(ibs_base_universe_d2_031_ibs_043_insider_buy_cluster_1512, 31)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_031_ibs_043_insider_buy_cluster_1512'] = {'inputs': ['ibs_base_universe_d2_031_ibs_043_insider_buy_cluster_1512'], 'func': ibs_base_universe_d3_031_ibs_043_insider_buy_cluster_1512}


def ibs_base_universe_d3_032_ibs_044_insider_net_buy_ratio_63(ibs_base_universe_d2_032_ibs_044_insider_net_buy_ratio_63):
    return _base_universe_d3(ibs_base_universe_d2_032_ibs_044_insider_net_buy_ratio_63, 32)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_032_ibs_044_insider_net_buy_ratio_63'] = {'inputs': ['ibs_base_universe_d2_032_ibs_044_insider_net_buy_ratio_63'], 'func': ibs_base_universe_d3_032_ibs_044_insider_net_buy_ratio_63}


def ibs_base_universe_d3_033_ibs_045_insider_value_ratio_252(ibs_base_universe_d2_033_ibs_045_insider_value_ratio_252):
    return _base_universe_d3(ibs_base_universe_d2_033_ibs_045_insider_value_ratio_252, 33)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_033_ibs_045_insider_value_ratio_252'] = {'inputs': ['ibs_base_universe_d2_033_ibs_045_insider_value_ratio_252'], 'func': ibs_base_universe_d3_033_ibs_045_insider_value_ratio_252}


def ibs_base_universe_d3_034_ibs_046_ceo_cfo_buy_weight_21(ibs_base_universe_d2_034_ibs_046_ceo_cfo_buy_weight_21):
    return _base_universe_d3(ibs_base_universe_d2_034_ibs_046_ceo_cfo_buy_weight_21, 34)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_034_ibs_046_ceo_cfo_buy_weight_21'] = {'inputs': ['ibs_base_universe_d2_034_ibs_046_ceo_cfo_buy_weight_21'], 'func': ibs_base_universe_d3_034_ibs_046_ceo_cfo_buy_weight_21}


def ibs_base_universe_d3_035_ibs_048_insider_conviction_63(ibs_base_universe_d2_035_ibs_048_insider_conviction_63):
    return _base_universe_d3(ibs_base_universe_d2_035_ibs_048_insider_conviction_63, 35)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_035_ibs_048_insider_conviction_63'] = {'inputs': ['ibs_base_universe_d2_035_ibs_048_insider_conviction_63'], 'func': ibs_base_universe_d3_035_ibs_048_insider_conviction_63}


def ibs_base_universe_d3_036_ibs_049_insider_silence_84(ibs_base_universe_d2_036_ibs_049_insider_silence_84):
    return _base_universe_d3(ibs_base_universe_d2_036_ibs_049_insider_silence_84, 36)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_036_ibs_049_insider_silence_84'] = {'inputs': ['ibs_base_universe_d2_036_ibs_049_insider_silence_84'], 'func': ibs_base_universe_d3_036_ibs_049_insider_silence_84}


def ibs_base_universe_d3_037_ibs_050_insider_buy_cluster_126(ibs_base_universe_d2_037_ibs_050_insider_buy_cluster_126):
    return _base_universe_d3(ibs_base_universe_d2_037_ibs_050_insider_buy_cluster_126, 37)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_037_ibs_050_insider_buy_cluster_126'] = {'inputs': ['ibs_base_universe_d2_037_ibs_050_insider_buy_cluster_126'], 'func': ibs_base_universe_d3_037_ibs_050_insider_buy_cluster_126}


def ibs_base_universe_d3_038_ibs_051_insider_net_buy_ratio_189(ibs_base_universe_d2_038_ibs_051_insider_net_buy_ratio_189):
    return _base_universe_d3(ibs_base_universe_d2_038_ibs_051_insider_net_buy_ratio_189, 38)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_038_ibs_051_insider_net_buy_ratio_189'] = {'inputs': ['ibs_base_universe_d2_038_ibs_051_insider_net_buy_ratio_189'], 'func': ibs_base_universe_d3_038_ibs_051_insider_net_buy_ratio_189}


def ibs_base_universe_d3_039_ibs_053_ceo_cfo_buy_weight_378(ibs_base_universe_d2_039_ibs_053_ceo_cfo_buy_weight_378):
    return _base_universe_d3(ibs_base_universe_d2_039_ibs_053_ceo_cfo_buy_weight_378, 39)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_039_ibs_053_ceo_cfo_buy_weight_378'] = {'inputs': ['ibs_base_universe_d2_039_ibs_053_ceo_cfo_buy_weight_378'], 'func': ibs_base_universe_d3_039_ibs_053_ceo_cfo_buy_weight_378}


def ibs_base_universe_d3_040_ibs_055_insider_conviction_756(ibs_base_universe_d2_040_ibs_055_insider_conviction_756):
    return _base_universe_d3(ibs_base_universe_d2_040_ibs_055_insider_conviction_756, 40)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_040_ibs_055_insider_conviction_756'] = {'inputs': ['ibs_base_universe_d2_040_ibs_055_insider_conviction_756'], 'func': ibs_base_universe_d3_040_ibs_055_insider_conviction_756}


def ibs_base_universe_d3_041_ibs_056_insider_silence_1008(ibs_base_universe_d2_041_ibs_056_insider_silence_1008):
    return _base_universe_d3(ibs_base_universe_d2_041_ibs_056_insider_silence_1008, 41)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_041_ibs_056_insider_silence_1008'] = {'inputs': ['ibs_base_universe_d2_041_ibs_056_insider_silence_1008'], 'func': ibs_base_universe_d3_041_ibs_056_insider_silence_1008}


def ibs_base_universe_d3_042_ibs_057_insider_buy_cluster_1260(ibs_base_universe_d2_042_ibs_057_insider_buy_cluster_1260):
    return _base_universe_d3(ibs_base_universe_d2_042_ibs_057_insider_buy_cluster_1260, 42)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_042_ibs_057_insider_buy_cluster_1260'] = {'inputs': ['ibs_base_universe_d2_042_ibs_057_insider_buy_cluster_1260'], 'func': ibs_base_universe_d3_042_ibs_057_insider_buy_cluster_1260}


def ibs_base_universe_d3_043_ibs_058_insider_net_buy_ratio_1512(ibs_base_universe_d2_043_ibs_058_insider_net_buy_ratio_1512):
    return _base_universe_d3(ibs_base_universe_d2_043_ibs_058_insider_net_buy_ratio_1512, 43)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_043_ibs_058_insider_net_buy_ratio_1512'] = {'inputs': ['ibs_base_universe_d2_043_ibs_058_insider_net_buy_ratio_1512'], 'func': ibs_base_universe_d3_043_ibs_058_insider_net_buy_ratio_1512}


def ibs_base_universe_d3_044_ibs_060_ceo_cfo_buy_weight_252(ibs_base_universe_d2_044_ibs_060_ceo_cfo_buy_weight_252):
    return _base_universe_d3(ibs_base_universe_d2_044_ibs_060_ceo_cfo_buy_weight_252, 44)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_044_ibs_060_ceo_cfo_buy_weight_252'] = {'inputs': ['ibs_base_universe_d2_044_ibs_060_ceo_cfo_buy_weight_252'], 'func': ibs_base_universe_d3_044_ibs_060_ceo_cfo_buy_weight_252}


def ibs_base_universe_d3_045_ibs_062_insider_conviction_42(ibs_base_universe_d2_045_ibs_062_insider_conviction_42):
    return _base_universe_d3(ibs_base_universe_d2_045_ibs_062_insider_conviction_42, 45)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_045_ibs_062_insider_conviction_42'] = {'inputs': ['ibs_base_universe_d2_045_ibs_062_insider_conviction_42'], 'func': ibs_base_universe_d3_045_ibs_062_insider_conviction_42}


def ibs_base_universe_d3_046_ibs_064_insider_buy_cluster_84(ibs_base_universe_d2_046_ibs_064_insider_buy_cluster_84):
    return _base_universe_d3(ibs_base_universe_d2_046_ibs_064_insider_buy_cluster_84, 46)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_046_ibs_064_insider_buy_cluster_84'] = {'inputs': ['ibs_base_universe_d2_046_ibs_064_insider_buy_cluster_84'], 'func': ibs_base_universe_d3_046_ibs_064_insider_buy_cluster_84}


def ibs_base_universe_d3_047_ibs_065_insider_net_buy_ratio_126(ibs_base_universe_d2_047_ibs_065_insider_net_buy_ratio_126):
    return _base_universe_d3(ibs_base_universe_d2_047_ibs_065_insider_net_buy_ratio_126, 47)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_047_ibs_065_insider_net_buy_ratio_126'] = {'inputs': ['ibs_base_universe_d2_047_ibs_065_insider_net_buy_ratio_126'], 'func': ibs_base_universe_d3_047_ibs_065_insider_net_buy_ratio_126}


def ibs_base_universe_d3_048_ibs_066_insider_value_ratio_189(ibs_base_universe_d2_048_ibs_066_insider_value_ratio_189):
    return _base_universe_d3(ibs_base_universe_d2_048_ibs_066_insider_value_ratio_189, 48)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_048_ibs_066_insider_value_ratio_189'] = {'inputs': ['ibs_base_universe_d2_048_ibs_066_insider_value_ratio_189'], 'func': ibs_base_universe_d3_048_ibs_066_insider_value_ratio_189}


def ibs_base_universe_d3_049_ibs_069_insider_conviction_504(ibs_base_universe_d2_049_ibs_069_insider_conviction_504):
    return _base_universe_d3(ibs_base_universe_d2_049_ibs_069_insider_conviction_504, 49)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_049_ibs_069_insider_conviction_504'] = {'inputs': ['ibs_base_universe_d2_049_ibs_069_insider_conviction_504'], 'func': ibs_base_universe_d3_049_ibs_069_insider_conviction_504}


def ibs_base_universe_d3_050_ibs_070_insider_silence_756(ibs_base_universe_d2_050_ibs_070_insider_silence_756):
    return _base_universe_d3(ibs_base_universe_d2_050_ibs_070_insider_silence_756, 50)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_050_ibs_070_insider_silence_756'] = {'inputs': ['ibs_base_universe_d2_050_ibs_070_insider_silence_756'], 'func': ibs_base_universe_d3_050_ibs_070_insider_silence_756}


def ibs_base_universe_d3_051_ibs_071_insider_buy_cluster_1008(ibs_base_universe_d2_051_ibs_071_insider_buy_cluster_1008):
    return _base_universe_d3(ibs_base_universe_d2_051_ibs_071_insider_buy_cluster_1008, 51)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_051_ibs_071_insider_buy_cluster_1008'] = {'inputs': ['ibs_base_universe_d2_051_ibs_071_insider_buy_cluster_1008'], 'func': ibs_base_universe_d3_051_ibs_071_insider_buy_cluster_1008}


def ibs_base_universe_d3_052_ibs_072_insider_net_buy_ratio_1260(ibs_base_universe_d2_052_ibs_072_insider_net_buy_ratio_1260):
    return _base_universe_d3(ibs_base_universe_d2_052_ibs_072_insider_net_buy_ratio_1260, 52)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_052_ibs_072_insider_net_buy_ratio_1260'] = {'inputs': ['ibs_base_universe_d2_052_ibs_072_insider_net_buy_ratio_1260'], 'func': ibs_base_universe_d3_052_ibs_072_insider_net_buy_ratio_1260}


def ibs_base_universe_d3_053_ibs_073_insider_value_ratio_1512(ibs_base_universe_d2_053_ibs_073_insider_value_ratio_1512):
    return _base_universe_d3(ibs_base_universe_d2_053_ibs_073_insider_value_ratio_1512, 53)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_053_ibs_073_insider_value_ratio_1512'] = {'inputs': ['ibs_base_universe_d2_053_ibs_073_insider_value_ratio_1512'], 'func': ibs_base_universe_d3_053_ibs_073_insider_value_ratio_1512}


def ibs_base_universe_d3_054_ibs_basefill_005(ibs_base_universe_d2_054_ibs_basefill_005):
    return _base_universe_d3(ibs_base_universe_d2_054_ibs_basefill_005, 54)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_054_ibs_basefill_005'] = {'inputs': ['ibs_base_universe_d2_054_ibs_basefill_005'], 'func': ibs_base_universe_d3_054_ibs_basefill_005}


def ibs_base_universe_d3_055_ibs_basefill_012(ibs_base_universe_d2_055_ibs_basefill_012):
    return _base_universe_d3(ibs_base_universe_d2_055_ibs_basefill_012, 55)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_055_ibs_basefill_012'] = {'inputs': ['ibs_base_universe_d2_055_ibs_basefill_012'], 'func': ibs_base_universe_d3_055_ibs_basefill_012}


def ibs_base_universe_d3_056_ibs_basefill_019(ibs_base_universe_d2_056_ibs_basefill_019):
    return _base_universe_d3(ibs_base_universe_d2_056_ibs_basefill_019, 56)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_056_ibs_basefill_019'] = {'inputs': ['ibs_base_universe_d2_056_ibs_basefill_019'], 'func': ibs_base_universe_d3_056_ibs_basefill_019}


def ibs_base_universe_d3_057_ibs_basefill_022(ibs_base_universe_d2_057_ibs_basefill_022):
    return _base_universe_d3(ibs_base_universe_d2_057_ibs_basefill_022, 57)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_057_ibs_basefill_022'] = {'inputs': ['ibs_base_universe_d2_057_ibs_basefill_022'], 'func': ibs_base_universe_d3_057_ibs_basefill_022}


def ibs_base_universe_d3_058_ibs_basefill_026(ibs_base_universe_d2_058_ibs_basefill_026):
    return _base_universe_d3(ibs_base_universe_d2_058_ibs_basefill_026, 58)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_058_ibs_basefill_026'] = {'inputs': ['ibs_base_universe_d2_058_ibs_basefill_026'], 'func': ibs_base_universe_d3_058_ibs_basefill_026}


def ibs_base_universe_d3_059_ibs_basefill_033(ibs_base_universe_d2_059_ibs_basefill_033):
    return _base_universe_d3(ibs_base_universe_d2_059_ibs_basefill_033, 59)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_059_ibs_basefill_033'] = {'inputs': ['ibs_base_universe_d2_059_ibs_basefill_033'], 'func': ibs_base_universe_d3_059_ibs_basefill_033}


def ibs_base_universe_d3_060_ibs_basefill_037(ibs_base_universe_d2_060_ibs_basefill_037):
    return _base_universe_d3(ibs_base_universe_d2_060_ibs_basefill_037, 60)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_060_ibs_basefill_037'] = {'inputs': ['ibs_base_universe_d2_060_ibs_basefill_037'], 'func': ibs_base_universe_d3_060_ibs_basefill_037}


def ibs_base_universe_d3_061_ibs_basefill_040(ibs_base_universe_d2_061_ibs_basefill_040):
    return _base_universe_d3(ibs_base_universe_d2_061_ibs_basefill_040, 61)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_061_ibs_basefill_040'] = {'inputs': ['ibs_base_universe_d2_061_ibs_basefill_040'], 'func': ibs_base_universe_d3_061_ibs_basefill_040}


def ibs_base_universe_d3_062_ibs_basefill_047(ibs_base_universe_d2_062_ibs_basefill_047):
    return _base_universe_d3(ibs_base_universe_d2_062_ibs_basefill_047, 62)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_062_ibs_basefill_047'] = {'inputs': ['ibs_base_universe_d2_062_ibs_basefill_047'], 'func': ibs_base_universe_d3_062_ibs_basefill_047}


def ibs_base_universe_d3_063_ibs_basefill_052(ibs_base_universe_d2_063_ibs_basefill_052):
    return _base_universe_d3(ibs_base_universe_d2_063_ibs_basefill_052, 63)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_063_ibs_basefill_052'] = {'inputs': ['ibs_base_universe_d2_063_ibs_basefill_052'], 'func': ibs_base_universe_d3_063_ibs_basefill_052}


def ibs_base_universe_d3_064_ibs_basefill_054(ibs_base_universe_d2_064_ibs_basefill_054):
    return _base_universe_d3(ibs_base_universe_d2_064_ibs_basefill_054, 64)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_064_ibs_basefill_054'] = {'inputs': ['ibs_base_universe_d2_064_ibs_basefill_054'], 'func': ibs_base_universe_d3_064_ibs_basefill_054}


def ibs_base_universe_d3_065_ibs_basefill_059(ibs_base_universe_d2_065_ibs_basefill_059):
    return _base_universe_d3(ibs_base_universe_d2_065_ibs_basefill_059, 65)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_065_ibs_basefill_059'] = {'inputs': ['ibs_base_universe_d2_065_ibs_basefill_059'], 'func': ibs_base_universe_d3_065_ibs_basefill_059}


def ibs_base_universe_d3_066_ibs_basefill_061(ibs_base_universe_d2_066_ibs_basefill_061):
    return _base_universe_d3(ibs_base_universe_d2_066_ibs_basefill_061, 66)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_066_ibs_basefill_061'] = {'inputs': ['ibs_base_universe_d2_066_ibs_basefill_061'], 'func': ibs_base_universe_d3_066_ibs_basefill_061}


def ibs_base_universe_d3_067_ibs_basefill_063(ibs_base_universe_d2_067_ibs_basefill_063):
    return _base_universe_d3(ibs_base_universe_d2_067_ibs_basefill_063, 67)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_067_ibs_basefill_063'] = {'inputs': ['ibs_base_universe_d2_067_ibs_basefill_063'], 'func': ibs_base_universe_d3_067_ibs_basefill_063}


def ibs_base_universe_d3_068_ibs_basefill_067(ibs_base_universe_d2_068_ibs_basefill_067):
    return _base_universe_d3(ibs_base_universe_d2_068_ibs_basefill_067, 68)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_068_ibs_basefill_067'] = {'inputs': ['ibs_base_universe_d2_068_ibs_basefill_067'], 'func': ibs_base_universe_d3_068_ibs_basefill_067}


def ibs_base_universe_d3_069_ibs_basefill_068(ibs_base_universe_d2_069_ibs_basefill_068):
    return _base_universe_d3(ibs_base_universe_d2_069_ibs_basefill_068, 69)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_069_ibs_basefill_068'] = {'inputs': ['ibs_base_universe_d2_069_ibs_basefill_068'], 'func': ibs_base_universe_d3_069_ibs_basefill_068}


def ibs_base_universe_d3_070_ibs_basefill_074(ibs_base_universe_d2_070_ibs_basefill_074):
    return _base_universe_d3(ibs_base_universe_d2_070_ibs_basefill_074, 70)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_070_ibs_basefill_074'] = {'inputs': ['ibs_base_universe_d2_070_ibs_basefill_074'], 'func': ibs_base_universe_d3_070_ibs_basefill_074}


def ibs_base_universe_d3_071_ibs_basefill_075(ibs_base_universe_d2_071_ibs_basefill_075):
    return _base_universe_d3(ibs_base_universe_d2_071_ibs_basefill_075, 71)
IBS_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibs_base_universe_d3_071_ibs_basefill_075'] = {'inputs': ['ibs_base_universe_d2_071_ibs_basefill_075'], 'func': ibs_base_universe_d3_071_ibs_basefill_075}

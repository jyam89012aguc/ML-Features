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



def ibc_176_ibc_001_insider_buy_cluster_21_accel_1(ibc_151_ibc_001_insider_buy_cluster_21_roc_1):
    feature = _s(ibc_151_ibc_001_insider_buy_cluster_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ibc_177_ibc_007_insider_silence_252_accel_42(ibc_152_ibc_007_insider_silence_252_roc_42):
    feature = _s(ibc_152_ibc_007_insider_silence_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ibc_178_ibc_013_insider_conviction_1512_accel_126(ibc_153_ibc_013_insider_conviction_1512_roc_126):
    feature = _s(ibc_153_ibc_013_insider_conviction_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ibc_179_ibc_019_insider_activity_accel_1_accel_378(ibc_154_ibc_019_insider_activity_accel_1_roc_378):
    feature = _s(ibc_154_ibc_019_insider_activity_accel_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def ibc_180_ibc_025_ceo_cfo_buy_weight_756_accel_4(ibc_155_ibc_025_ceo_cfo_buy_weight_756_roc_4):
    feature = _s(ibc_155_ibc_025_ceo_cfo_buy_weight_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSIDER_BUY_CLUSTER_REGISTRY_3RD_DERIVATIVES = {
    'ibc_176_ibc_001_insider_buy_cluster_21_accel_1': {'inputs': ['ibc_151_ibc_001_insider_buy_cluster_21_roc_1'], 'func': ibc_176_ibc_001_insider_buy_cluster_21_accel_1},
    'ibc_177_ibc_007_insider_silence_252_accel_42': {'inputs': ['ibc_152_ibc_007_insider_silence_252_roc_42'], 'func': ibc_177_ibc_007_insider_silence_252_accel_42},
    'ibc_178_ibc_013_insider_conviction_1512_accel_126': {'inputs': ['ibc_153_ibc_013_insider_conviction_1512_roc_126'], 'func': ibc_178_ibc_013_insider_conviction_1512_accel_126},
    'ibc_179_ibc_019_insider_activity_accel_1_accel_378': {'inputs': ['ibc_154_ibc_019_insider_activity_accel_1_roc_378'], 'func': ibc_179_ibc_019_insider_activity_accel_1_accel_378},
    'ibc_180_ibc_025_ceo_cfo_buy_weight_756_accel_4': {'inputs': ['ibc_155_ibc_025_ceo_cfo_buy_weight_756_roc_4'], 'func': ibc_180_ibc_025_ceo_cfo_buy_weight_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ibc_replacement_d3_001(ibc_replacement_d2_001):
    feature = _clean(ibc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_001'] = {'inputs': ['ibc_replacement_d2_001'], 'func': ibc_replacement_d3_001}


def ibc_replacement_d3_002(ibc_replacement_d2_002):
    feature = _clean(ibc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_002'] = {'inputs': ['ibc_replacement_d2_002'], 'func': ibc_replacement_d3_002}


def ibc_replacement_d3_003(ibc_replacement_d2_003):
    feature = _clean(ibc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_003'] = {'inputs': ['ibc_replacement_d2_003'], 'func': ibc_replacement_d3_003}


def ibc_replacement_d3_004(ibc_replacement_d2_004):
    feature = _clean(ibc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_004'] = {'inputs': ['ibc_replacement_d2_004'], 'func': ibc_replacement_d3_004}


def ibc_replacement_d3_005(ibc_replacement_d2_005):
    feature = _clean(ibc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_005'] = {'inputs': ['ibc_replacement_d2_005'], 'func': ibc_replacement_d3_005}


def ibc_replacement_d3_006(ibc_replacement_d2_006):
    feature = _clean(ibc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_006'] = {'inputs': ['ibc_replacement_d2_006'], 'func': ibc_replacement_d3_006}


def ibc_replacement_d3_007(ibc_replacement_d2_007):
    feature = _clean(ibc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_007'] = {'inputs': ['ibc_replacement_d2_007'], 'func': ibc_replacement_d3_007}


def ibc_replacement_d3_008(ibc_replacement_d2_008):
    feature = _clean(ibc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_008'] = {'inputs': ['ibc_replacement_d2_008'], 'func': ibc_replacement_d3_008}


def ibc_replacement_d3_009(ibc_replacement_d2_009):
    feature = _clean(ibc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_009'] = {'inputs': ['ibc_replacement_d2_009'], 'func': ibc_replacement_d3_009}


def ibc_replacement_d3_010(ibc_replacement_d2_010):
    feature = _clean(ibc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_010'] = {'inputs': ['ibc_replacement_d2_010'], 'func': ibc_replacement_d3_010}


def ibc_replacement_d3_011(ibc_replacement_d2_011):
    feature = _clean(ibc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_011'] = {'inputs': ['ibc_replacement_d2_011'], 'func': ibc_replacement_d3_011}


def ibc_replacement_d3_012(ibc_replacement_d2_012):
    feature = _clean(ibc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_012'] = {'inputs': ['ibc_replacement_d2_012'], 'func': ibc_replacement_d3_012}


def ibc_replacement_d3_013(ibc_replacement_d2_013):
    feature = _clean(ibc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_013'] = {'inputs': ['ibc_replacement_d2_013'], 'func': ibc_replacement_d3_013}


def ibc_replacement_d3_014(ibc_replacement_d2_014):
    feature = _clean(ibc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_014'] = {'inputs': ['ibc_replacement_d2_014'], 'func': ibc_replacement_d3_014}


def ibc_replacement_d3_015(ibc_replacement_d2_015):
    feature = _clean(ibc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_015'] = {'inputs': ['ibc_replacement_d2_015'], 'func': ibc_replacement_d3_015}


def ibc_replacement_d3_016(ibc_replacement_d2_016):
    feature = _clean(ibc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_016'] = {'inputs': ['ibc_replacement_d2_016'], 'func': ibc_replacement_d3_016}


def ibc_replacement_d3_017(ibc_replacement_d2_017):
    feature = _clean(ibc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_017'] = {'inputs': ['ibc_replacement_d2_017'], 'func': ibc_replacement_d3_017}


def ibc_replacement_d3_018(ibc_replacement_d2_018):
    feature = _clean(ibc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_018'] = {'inputs': ['ibc_replacement_d2_018'], 'func': ibc_replacement_d3_018}


def ibc_replacement_d3_019(ibc_replacement_d2_019):
    feature = _clean(ibc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_019'] = {'inputs': ['ibc_replacement_d2_019'], 'func': ibc_replacement_d3_019}


def ibc_replacement_d3_020(ibc_replacement_d2_020):
    feature = _clean(ibc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_020'] = {'inputs': ['ibc_replacement_d2_020'], 'func': ibc_replacement_d3_020}


def ibc_replacement_d3_021(ibc_replacement_d2_021):
    feature = _clean(ibc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_021'] = {'inputs': ['ibc_replacement_d2_021'], 'func': ibc_replacement_d3_021}


def ibc_replacement_d3_022(ibc_replacement_d2_022):
    feature = _clean(ibc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_022'] = {'inputs': ['ibc_replacement_d2_022'], 'func': ibc_replacement_d3_022}


def ibc_replacement_d3_023(ibc_replacement_d2_023):
    feature = _clean(ibc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_023'] = {'inputs': ['ibc_replacement_d2_023'], 'func': ibc_replacement_d3_023}


def ibc_replacement_d3_024(ibc_replacement_d2_024):
    feature = _clean(ibc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_024'] = {'inputs': ['ibc_replacement_d2_024'], 'func': ibc_replacement_d3_024}


def ibc_replacement_d3_025(ibc_replacement_d2_025):
    feature = _clean(ibc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_025'] = {'inputs': ['ibc_replacement_d2_025'], 'func': ibc_replacement_d3_025}


def ibc_replacement_d3_026(ibc_replacement_d2_026):
    feature = _clean(ibc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_026'] = {'inputs': ['ibc_replacement_d2_026'], 'func': ibc_replacement_d3_026}


def ibc_replacement_d3_027(ibc_replacement_d2_027):
    feature = _clean(ibc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_027'] = {'inputs': ['ibc_replacement_d2_027'], 'func': ibc_replacement_d3_027}


def ibc_replacement_d3_028(ibc_replacement_d2_028):
    feature = _clean(ibc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_028'] = {'inputs': ['ibc_replacement_d2_028'], 'func': ibc_replacement_d3_028}


def ibc_replacement_d3_029(ibc_replacement_d2_029):
    feature = _clean(ibc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_029'] = {'inputs': ['ibc_replacement_d2_029'], 'func': ibc_replacement_d3_029}


def ibc_replacement_d3_030(ibc_replacement_d2_030):
    feature = _clean(ibc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_030'] = {'inputs': ['ibc_replacement_d2_030'], 'func': ibc_replacement_d3_030}


def ibc_replacement_d3_031(ibc_replacement_d2_031):
    feature = _clean(ibc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_031'] = {'inputs': ['ibc_replacement_d2_031'], 'func': ibc_replacement_d3_031}


def ibc_replacement_d3_032(ibc_replacement_d2_032):
    feature = _clean(ibc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_032'] = {'inputs': ['ibc_replacement_d2_032'], 'func': ibc_replacement_d3_032}


def ibc_replacement_d3_033(ibc_replacement_d2_033):
    feature = _clean(ibc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_033'] = {'inputs': ['ibc_replacement_d2_033'], 'func': ibc_replacement_d3_033}


def ibc_replacement_d3_034(ibc_replacement_d2_034):
    feature = _clean(ibc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_034'] = {'inputs': ['ibc_replacement_d2_034'], 'func': ibc_replacement_d3_034}


def ibc_replacement_d3_035(ibc_replacement_d2_035):
    feature = _clean(ibc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_035'] = {'inputs': ['ibc_replacement_d2_035'], 'func': ibc_replacement_d3_035}


def ibc_replacement_d3_036(ibc_replacement_d2_036):
    feature = _clean(ibc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_036'] = {'inputs': ['ibc_replacement_d2_036'], 'func': ibc_replacement_d3_036}


def ibc_replacement_d3_037(ibc_replacement_d2_037):
    feature = _clean(ibc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_037'] = {'inputs': ['ibc_replacement_d2_037'], 'func': ibc_replacement_d3_037}


def ibc_replacement_d3_038(ibc_replacement_d2_038):
    feature = _clean(ibc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_038'] = {'inputs': ['ibc_replacement_d2_038'], 'func': ibc_replacement_d3_038}


def ibc_replacement_d3_039(ibc_replacement_d2_039):
    feature = _clean(ibc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_039'] = {'inputs': ['ibc_replacement_d2_039'], 'func': ibc_replacement_d3_039}


def ibc_replacement_d3_040(ibc_replacement_d2_040):
    feature = _clean(ibc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_040'] = {'inputs': ['ibc_replacement_d2_040'], 'func': ibc_replacement_d3_040}


def ibc_replacement_d3_041(ibc_replacement_d2_041):
    feature = _clean(ibc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_041'] = {'inputs': ['ibc_replacement_d2_041'], 'func': ibc_replacement_d3_041}


def ibc_replacement_d3_042(ibc_replacement_d2_042):
    feature = _clean(ibc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_042'] = {'inputs': ['ibc_replacement_d2_042'], 'func': ibc_replacement_d3_042}


def ibc_replacement_d3_043(ibc_replacement_d2_043):
    feature = _clean(ibc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_043'] = {'inputs': ['ibc_replacement_d2_043'], 'func': ibc_replacement_d3_043}


def ibc_replacement_d3_044(ibc_replacement_d2_044):
    feature = _clean(ibc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_044'] = {'inputs': ['ibc_replacement_d2_044'], 'func': ibc_replacement_d3_044}


def ibc_replacement_d3_045(ibc_replacement_d2_045):
    feature = _clean(ibc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_045'] = {'inputs': ['ibc_replacement_d2_045'], 'func': ibc_replacement_d3_045}


def ibc_replacement_d3_046(ibc_replacement_d2_046):
    feature = _clean(ibc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_046'] = {'inputs': ['ibc_replacement_d2_046'], 'func': ibc_replacement_d3_046}


def ibc_replacement_d3_047(ibc_replacement_d2_047):
    feature = _clean(ibc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_047'] = {'inputs': ['ibc_replacement_d2_047'], 'func': ibc_replacement_d3_047}


def ibc_replacement_d3_048(ibc_replacement_d2_048):
    feature = _clean(ibc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_048'] = {'inputs': ['ibc_replacement_d2_048'], 'func': ibc_replacement_d3_048}


def ibc_replacement_d3_049(ibc_replacement_d2_049):
    feature = _clean(ibc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_049'] = {'inputs': ['ibc_replacement_d2_049'], 'func': ibc_replacement_d3_049}


def ibc_replacement_d3_050(ibc_replacement_d2_050):
    feature = _clean(ibc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_050'] = {'inputs': ['ibc_replacement_d2_050'], 'func': ibc_replacement_d3_050}


def ibc_replacement_d3_051(ibc_replacement_d2_051):
    feature = _clean(ibc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_051'] = {'inputs': ['ibc_replacement_d2_051'], 'func': ibc_replacement_d3_051}


def ibc_replacement_d3_052(ibc_replacement_d2_052):
    feature = _clean(ibc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_052'] = {'inputs': ['ibc_replacement_d2_052'], 'func': ibc_replacement_d3_052}


def ibc_replacement_d3_053(ibc_replacement_d2_053):
    feature = _clean(ibc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_053'] = {'inputs': ['ibc_replacement_d2_053'], 'func': ibc_replacement_d3_053}


def ibc_replacement_d3_054(ibc_replacement_d2_054):
    feature = _clean(ibc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_054'] = {'inputs': ['ibc_replacement_d2_054'], 'func': ibc_replacement_d3_054}


def ibc_replacement_d3_055(ibc_replacement_d2_055):
    feature = _clean(ibc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_055'] = {'inputs': ['ibc_replacement_d2_055'], 'func': ibc_replacement_d3_055}


def ibc_replacement_d3_056(ibc_replacement_d2_056):
    feature = _clean(ibc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_056'] = {'inputs': ['ibc_replacement_d2_056'], 'func': ibc_replacement_d3_056}


def ibc_replacement_d3_057(ibc_replacement_d2_057):
    feature = _clean(ibc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_057'] = {'inputs': ['ibc_replacement_d2_057'], 'func': ibc_replacement_d3_057}


def ibc_replacement_d3_058(ibc_replacement_d2_058):
    feature = _clean(ibc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_058'] = {'inputs': ['ibc_replacement_d2_058'], 'func': ibc_replacement_d3_058}


def ibc_replacement_d3_059(ibc_replacement_d2_059):
    feature = _clean(ibc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_059'] = {'inputs': ['ibc_replacement_d2_059'], 'func': ibc_replacement_d3_059}


def ibc_replacement_d3_060(ibc_replacement_d2_060):
    feature = _clean(ibc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_060'] = {'inputs': ['ibc_replacement_d2_060'], 'func': ibc_replacement_d3_060}


def ibc_replacement_d3_061(ibc_replacement_d2_061):
    feature = _clean(ibc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_061'] = {'inputs': ['ibc_replacement_d2_061'], 'func': ibc_replacement_d3_061}


def ibc_replacement_d3_062(ibc_replacement_d2_062):
    feature = _clean(ibc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_062'] = {'inputs': ['ibc_replacement_d2_062'], 'func': ibc_replacement_d3_062}


def ibc_replacement_d3_063(ibc_replacement_d2_063):
    feature = _clean(ibc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_063'] = {'inputs': ['ibc_replacement_d2_063'], 'func': ibc_replacement_d3_063}


def ibc_replacement_d3_064(ibc_replacement_d2_064):
    feature = _clean(ibc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_064'] = {'inputs': ['ibc_replacement_d2_064'], 'func': ibc_replacement_d3_064}


def ibc_replacement_d3_065(ibc_replacement_d2_065):
    feature = _clean(ibc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_065'] = {'inputs': ['ibc_replacement_d2_065'], 'func': ibc_replacement_d3_065}


def ibc_replacement_d3_066(ibc_replacement_d2_066):
    feature = _clean(ibc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_066'] = {'inputs': ['ibc_replacement_d2_066'], 'func': ibc_replacement_d3_066}


def ibc_replacement_d3_067(ibc_replacement_d2_067):
    feature = _clean(ibc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_067'] = {'inputs': ['ibc_replacement_d2_067'], 'func': ibc_replacement_d3_067}


def ibc_replacement_d3_068(ibc_replacement_d2_068):
    feature = _clean(ibc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_068'] = {'inputs': ['ibc_replacement_d2_068'], 'func': ibc_replacement_d3_068}


def ibc_replacement_d3_069(ibc_replacement_d2_069):
    feature = _clean(ibc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_069'] = {'inputs': ['ibc_replacement_d2_069'], 'func': ibc_replacement_d3_069}


def ibc_replacement_d3_070(ibc_replacement_d2_070):
    feature = _clean(ibc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_070'] = {'inputs': ['ibc_replacement_d2_070'], 'func': ibc_replacement_d3_070}


def ibc_replacement_d3_071(ibc_replacement_d2_071):
    feature = _clean(ibc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_071'] = {'inputs': ['ibc_replacement_d2_071'], 'func': ibc_replacement_d3_071}


def ibc_replacement_d3_072(ibc_replacement_d2_072):
    feature = _clean(ibc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_072'] = {'inputs': ['ibc_replacement_d2_072'], 'func': ibc_replacement_d3_072}


def ibc_replacement_d3_073(ibc_replacement_d2_073):
    feature = _clean(ibc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_073'] = {'inputs': ['ibc_replacement_d2_073'], 'func': ibc_replacement_d3_073}


def ibc_replacement_d3_074(ibc_replacement_d2_074):
    feature = _clean(ibc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_074'] = {'inputs': ['ibc_replacement_d2_074'], 'func': ibc_replacement_d3_074}


def ibc_replacement_d3_075(ibc_replacement_d2_075):
    feature = _clean(ibc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_075'] = {'inputs': ['ibc_replacement_d2_075'], 'func': ibc_replacement_d3_075}


def ibc_replacement_d3_076(ibc_replacement_d2_076):
    feature = _clean(ibc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_076'] = {'inputs': ['ibc_replacement_d2_076'], 'func': ibc_replacement_d3_076}


def ibc_replacement_d3_077(ibc_replacement_d2_077):
    feature = _clean(ibc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_077'] = {'inputs': ['ibc_replacement_d2_077'], 'func': ibc_replacement_d3_077}


def ibc_replacement_d3_078(ibc_replacement_d2_078):
    feature = _clean(ibc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_078'] = {'inputs': ['ibc_replacement_d2_078'], 'func': ibc_replacement_d3_078}


def ibc_replacement_d3_079(ibc_replacement_d2_079):
    feature = _clean(ibc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_079'] = {'inputs': ['ibc_replacement_d2_079'], 'func': ibc_replacement_d3_079}


def ibc_replacement_d3_080(ibc_replacement_d2_080):
    feature = _clean(ibc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_080'] = {'inputs': ['ibc_replacement_d2_080'], 'func': ibc_replacement_d3_080}


def ibc_replacement_d3_081(ibc_replacement_d2_081):
    feature = _clean(ibc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_081'] = {'inputs': ['ibc_replacement_d2_081'], 'func': ibc_replacement_d3_081}


def ibc_replacement_d3_082(ibc_replacement_d2_082):
    feature = _clean(ibc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_082'] = {'inputs': ['ibc_replacement_d2_082'], 'func': ibc_replacement_d3_082}


def ibc_replacement_d3_083(ibc_replacement_d2_083):
    feature = _clean(ibc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_083'] = {'inputs': ['ibc_replacement_d2_083'], 'func': ibc_replacement_d3_083}


def ibc_replacement_d3_084(ibc_replacement_d2_084):
    feature = _clean(ibc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_084'] = {'inputs': ['ibc_replacement_d2_084'], 'func': ibc_replacement_d3_084}


def ibc_replacement_d3_085(ibc_replacement_d2_085):
    feature = _clean(ibc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_085'] = {'inputs': ['ibc_replacement_d2_085'], 'func': ibc_replacement_d3_085}


def ibc_replacement_d3_086(ibc_replacement_d2_086):
    feature = _clean(ibc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_086'] = {'inputs': ['ibc_replacement_d2_086'], 'func': ibc_replacement_d3_086}


def ibc_replacement_d3_087(ibc_replacement_d2_087):
    feature = _clean(ibc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_087'] = {'inputs': ['ibc_replacement_d2_087'], 'func': ibc_replacement_d3_087}


def ibc_replacement_d3_088(ibc_replacement_d2_088):
    feature = _clean(ibc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_088'] = {'inputs': ['ibc_replacement_d2_088'], 'func': ibc_replacement_d3_088}


def ibc_replacement_d3_089(ibc_replacement_d2_089):
    feature = _clean(ibc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_089'] = {'inputs': ['ibc_replacement_d2_089'], 'func': ibc_replacement_d3_089}


def ibc_replacement_d3_090(ibc_replacement_d2_090):
    feature = _clean(ibc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_090'] = {'inputs': ['ibc_replacement_d2_090'], 'func': ibc_replacement_d3_090}


def ibc_replacement_d3_091(ibc_replacement_d2_091):
    feature = _clean(ibc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_091'] = {'inputs': ['ibc_replacement_d2_091'], 'func': ibc_replacement_d3_091}


def ibc_replacement_d3_092(ibc_replacement_d2_092):
    feature = _clean(ibc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_092'] = {'inputs': ['ibc_replacement_d2_092'], 'func': ibc_replacement_d3_092}


def ibc_replacement_d3_093(ibc_replacement_d2_093):
    feature = _clean(ibc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_093'] = {'inputs': ['ibc_replacement_d2_093'], 'func': ibc_replacement_d3_093}


def ibc_replacement_d3_094(ibc_replacement_d2_094):
    feature = _clean(ibc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_094'] = {'inputs': ['ibc_replacement_d2_094'], 'func': ibc_replacement_d3_094}


def ibc_replacement_d3_095(ibc_replacement_d2_095):
    feature = _clean(ibc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_095'] = {'inputs': ['ibc_replacement_d2_095'], 'func': ibc_replacement_d3_095}


def ibc_replacement_d3_096(ibc_replacement_d2_096):
    feature = _clean(ibc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_096'] = {'inputs': ['ibc_replacement_d2_096'], 'func': ibc_replacement_d3_096}


def ibc_replacement_d3_097(ibc_replacement_d2_097):
    feature = _clean(ibc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_097'] = {'inputs': ['ibc_replacement_d2_097'], 'func': ibc_replacement_d3_097}


def ibc_replacement_d3_098(ibc_replacement_d2_098):
    feature = _clean(ibc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_098'] = {'inputs': ['ibc_replacement_d2_098'], 'func': ibc_replacement_d3_098}


def ibc_replacement_d3_099(ibc_replacement_d2_099):
    feature = _clean(ibc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_099'] = {'inputs': ['ibc_replacement_d2_099'], 'func': ibc_replacement_d3_099}


def ibc_replacement_d3_100(ibc_replacement_d2_100):
    feature = _clean(ibc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_100'] = {'inputs': ['ibc_replacement_d2_100'], 'func': ibc_replacement_d3_100}


def ibc_replacement_d3_101(ibc_replacement_d2_101):
    feature = _clean(ibc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_101'] = {'inputs': ['ibc_replacement_d2_101'], 'func': ibc_replacement_d3_101}


def ibc_replacement_d3_102(ibc_replacement_d2_102):
    feature = _clean(ibc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_102'] = {'inputs': ['ibc_replacement_d2_102'], 'func': ibc_replacement_d3_102}


def ibc_replacement_d3_103(ibc_replacement_d2_103):
    feature = _clean(ibc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_103'] = {'inputs': ['ibc_replacement_d2_103'], 'func': ibc_replacement_d3_103}


def ibc_replacement_d3_104(ibc_replacement_d2_104):
    feature = _clean(ibc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_104'] = {'inputs': ['ibc_replacement_d2_104'], 'func': ibc_replacement_d3_104}


def ibc_replacement_d3_105(ibc_replacement_d2_105):
    feature = _clean(ibc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_105'] = {'inputs': ['ibc_replacement_d2_105'], 'func': ibc_replacement_d3_105}


def ibc_replacement_d3_106(ibc_replacement_d2_106):
    feature = _clean(ibc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_106'] = {'inputs': ['ibc_replacement_d2_106'], 'func': ibc_replacement_d3_106}


def ibc_replacement_d3_107(ibc_replacement_d2_107):
    feature = _clean(ibc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_107'] = {'inputs': ['ibc_replacement_d2_107'], 'func': ibc_replacement_d3_107}


def ibc_replacement_d3_108(ibc_replacement_d2_108):
    feature = _clean(ibc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_108'] = {'inputs': ['ibc_replacement_d2_108'], 'func': ibc_replacement_d3_108}


def ibc_replacement_d3_109(ibc_replacement_d2_109):
    feature = _clean(ibc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_109'] = {'inputs': ['ibc_replacement_d2_109'], 'func': ibc_replacement_d3_109}


def ibc_replacement_d3_110(ibc_replacement_d2_110):
    feature = _clean(ibc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_110'] = {'inputs': ['ibc_replacement_d2_110'], 'func': ibc_replacement_d3_110}


def ibc_replacement_d3_111(ibc_replacement_d2_111):
    feature = _clean(ibc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_111'] = {'inputs': ['ibc_replacement_d2_111'], 'func': ibc_replacement_d3_111}


def ibc_replacement_d3_112(ibc_replacement_d2_112):
    feature = _clean(ibc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IBC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibc_replacement_d3_112'] = {'inputs': ['ibc_replacement_d2_112'], 'func': ibc_replacement_d3_112}


# Third-derivative extensions for repaired first-base features.
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibc_base_universe_d3_001_ibc_002_insider_net_buy_ratio_42(ibc_base_universe_d2_001_ibc_002_insider_net_buy_ratio_42):
    return _base_universe_d3(ibc_base_universe_d2_001_ibc_002_insider_net_buy_ratio_42, 1)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_001_ibc_002_insider_net_buy_ratio_42'] = {'inputs': ['ibc_base_universe_d2_001_ibc_002_insider_net_buy_ratio_42'], 'func': ibc_base_universe_d3_001_ibc_002_insider_net_buy_ratio_42}


def ibc_base_universe_d3_002_ibc_003_insider_value_ratio_63(ibc_base_universe_d2_002_ibc_003_insider_value_ratio_63):
    return _base_universe_d3(ibc_base_universe_d2_002_ibc_003_insider_value_ratio_63, 2)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_002_ibc_003_insider_value_ratio_63'] = {'inputs': ['ibc_base_universe_d2_002_ibc_003_insider_value_ratio_63'], 'func': ibc_base_universe_d3_002_ibc_003_insider_value_ratio_63}


def ibc_base_universe_d3_003_ibc_004_ceo_cfo_buy_weight_84(ibc_base_universe_d2_003_ibc_004_ceo_cfo_buy_weight_84):
    return _base_universe_d3(ibc_base_universe_d2_003_ibc_004_ceo_cfo_buy_weight_84, 3)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_003_ibc_004_ceo_cfo_buy_weight_84'] = {'inputs': ['ibc_base_universe_d2_003_ibc_004_ceo_cfo_buy_weight_84'], 'func': ibc_base_universe_d3_003_ibc_004_ceo_cfo_buy_weight_84}


def ibc_base_universe_d3_004_ibc_006_insider_conviction_189(ibc_base_universe_d2_004_ibc_006_insider_conviction_189):
    return _base_universe_d3(ibc_base_universe_d2_004_ibc_006_insider_conviction_189, 4)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_004_ibc_006_insider_conviction_189'] = {'inputs': ['ibc_base_universe_d2_004_ibc_006_insider_conviction_189'], 'func': ibc_base_universe_d3_004_ibc_006_insider_conviction_189}


def ibc_base_universe_d3_005_ibc_008_insider_buy_cluster_378(ibc_base_universe_d2_005_ibc_008_insider_buy_cluster_378):
    return _base_universe_d3(ibc_base_universe_d2_005_ibc_008_insider_buy_cluster_378, 5)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_005_ibc_008_insider_buy_cluster_378'] = {'inputs': ['ibc_base_universe_d2_005_ibc_008_insider_buy_cluster_378'], 'func': ibc_base_universe_d3_005_ibc_008_insider_buy_cluster_378}


def ibc_base_universe_d3_006_ibc_009_insider_net_buy_ratio_504(ibc_base_universe_d2_006_ibc_009_insider_net_buy_ratio_504):
    return _base_universe_d3(ibc_base_universe_d2_006_ibc_009_insider_net_buy_ratio_504, 6)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_006_ibc_009_insider_net_buy_ratio_504'] = {'inputs': ['ibc_base_universe_d2_006_ibc_009_insider_net_buy_ratio_504'], 'func': ibc_base_universe_d3_006_ibc_009_insider_net_buy_ratio_504}


def ibc_base_universe_d3_007_ibc_010_insider_value_ratio_756(ibc_base_universe_d2_007_ibc_010_insider_value_ratio_756):
    return _base_universe_d3(ibc_base_universe_d2_007_ibc_010_insider_value_ratio_756, 7)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_007_ibc_010_insider_value_ratio_756'] = {'inputs': ['ibc_base_universe_d2_007_ibc_010_insider_value_ratio_756'], 'func': ibc_base_universe_d3_007_ibc_010_insider_value_ratio_756}


def ibc_base_universe_d3_008_ibc_011_ceo_cfo_buy_weight_1008(ibc_base_universe_d2_008_ibc_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d3(ibc_base_universe_d2_008_ibc_011_ceo_cfo_buy_weight_1008, 8)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_008_ibc_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['ibc_base_universe_d2_008_ibc_011_ceo_cfo_buy_weight_1008'], 'func': ibc_base_universe_d3_008_ibc_011_ceo_cfo_buy_weight_1008}


def ibc_base_universe_d3_009_ibc_014_insider_silence_63(ibc_base_universe_d2_009_ibc_014_insider_silence_63):
    return _base_universe_d3(ibc_base_universe_d2_009_ibc_014_insider_silence_63, 9)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_009_ibc_014_insider_silence_63'] = {'inputs': ['ibc_base_universe_d2_009_ibc_014_insider_silence_63'], 'func': ibc_base_universe_d3_009_ibc_014_insider_silence_63}


def ibc_base_universe_d3_010_ibc_015_insider_buy_cluster_252(ibc_base_universe_d2_010_ibc_015_insider_buy_cluster_252):
    return _base_universe_d3(ibc_base_universe_d2_010_ibc_015_insider_buy_cluster_252, 10)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_010_ibc_015_insider_buy_cluster_252'] = {'inputs': ['ibc_base_universe_d2_010_ibc_015_insider_buy_cluster_252'], 'func': ibc_base_universe_d3_010_ibc_015_insider_buy_cluster_252}


def ibc_base_universe_d3_011_ibc_016_insider_net_buy_ratio_21(ibc_base_universe_d2_011_ibc_016_insider_net_buy_ratio_21):
    return _base_universe_d3(ibc_base_universe_d2_011_ibc_016_insider_net_buy_ratio_21, 11)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_011_ibc_016_insider_net_buy_ratio_21'] = {'inputs': ['ibc_base_universe_d2_011_ibc_016_insider_net_buy_ratio_21'], 'func': ibc_base_universe_d3_011_ibc_016_insider_net_buy_ratio_21}


def ibc_base_universe_d3_012_ibc_017_insider_value_ratio_42(ibc_base_universe_d2_012_ibc_017_insider_value_ratio_42):
    return _base_universe_d3(ibc_base_universe_d2_012_ibc_017_insider_value_ratio_42, 12)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_012_ibc_017_insider_value_ratio_42'] = {'inputs': ['ibc_base_universe_d2_012_ibc_017_insider_value_ratio_42'], 'func': ibc_base_universe_d3_012_ibc_017_insider_value_ratio_42}


def ibc_base_universe_d3_013_ibc_018_ceo_cfo_buy_weight_63(ibc_base_universe_d2_013_ibc_018_ceo_cfo_buy_weight_63):
    return _base_universe_d3(ibc_base_universe_d2_013_ibc_018_ceo_cfo_buy_weight_63, 13)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_013_ibc_018_ceo_cfo_buy_weight_63'] = {'inputs': ['ibc_base_universe_d2_013_ibc_018_ceo_cfo_buy_weight_63'], 'func': ibc_base_universe_d3_013_ibc_018_ceo_cfo_buy_weight_63}


def ibc_base_universe_d3_014_ibc_020_insider_conviction_126(ibc_base_universe_d2_014_ibc_020_insider_conviction_126):
    return _base_universe_d3(ibc_base_universe_d2_014_ibc_020_insider_conviction_126, 14)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_014_ibc_020_insider_conviction_126'] = {'inputs': ['ibc_base_universe_d2_014_ibc_020_insider_conviction_126'], 'func': ibc_base_universe_d3_014_ibc_020_insider_conviction_126}


def ibc_base_universe_d3_015_ibc_021_insider_silence_189(ibc_base_universe_d2_015_ibc_021_insider_silence_189):
    return _base_universe_d3(ibc_base_universe_d2_015_ibc_021_insider_silence_189, 15)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_015_ibc_021_insider_silence_189'] = {'inputs': ['ibc_base_universe_d2_015_ibc_021_insider_silence_189'], 'func': ibc_base_universe_d3_015_ibc_021_insider_silence_189}


def ibc_base_universe_d3_016_ibc_023_insider_net_buy_ratio_378(ibc_base_universe_d2_016_ibc_023_insider_net_buy_ratio_378):
    return _base_universe_d3(ibc_base_universe_d2_016_ibc_023_insider_net_buy_ratio_378, 16)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_016_ibc_023_insider_net_buy_ratio_378'] = {'inputs': ['ibc_base_universe_d2_016_ibc_023_insider_net_buy_ratio_378'], 'func': ibc_base_universe_d3_016_ibc_023_insider_net_buy_ratio_378}


def ibc_base_universe_d3_017_ibc_024_insider_value_ratio_504(ibc_base_universe_d2_017_ibc_024_insider_value_ratio_504):
    return _base_universe_d3(ibc_base_universe_d2_017_ibc_024_insider_value_ratio_504, 17)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_017_ibc_024_insider_value_ratio_504'] = {'inputs': ['ibc_base_universe_d2_017_ibc_024_insider_value_ratio_504'], 'func': ibc_base_universe_d3_017_ibc_024_insider_value_ratio_504}


def ibc_base_universe_d3_018_ibc_027_insider_conviction_1260(ibc_base_universe_d2_018_ibc_027_insider_conviction_1260):
    return _base_universe_d3(ibc_base_universe_d2_018_ibc_027_insider_conviction_1260, 18)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_018_ibc_027_insider_conviction_1260'] = {'inputs': ['ibc_base_universe_d2_018_ibc_027_insider_conviction_1260'], 'func': ibc_base_universe_d3_018_ibc_027_insider_conviction_1260}


def ibc_base_universe_d3_019_ibc_028_insider_silence_1512(ibc_base_universe_d2_019_ibc_028_insider_silence_1512):
    return _base_universe_d3(ibc_base_universe_d2_019_ibc_028_insider_silence_1512, 19)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_019_ibc_028_insider_silence_1512'] = {'inputs': ['ibc_base_universe_d2_019_ibc_028_insider_silence_1512'], 'func': ibc_base_universe_d3_019_ibc_028_insider_silence_1512}


def ibc_base_universe_d3_020_ibc_029_insider_buy_cluster_63(ibc_base_universe_d2_020_ibc_029_insider_buy_cluster_63):
    return _base_universe_d3(ibc_base_universe_d2_020_ibc_029_insider_buy_cluster_63, 20)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_020_ibc_029_insider_buy_cluster_63'] = {'inputs': ['ibc_base_universe_d2_020_ibc_029_insider_buy_cluster_63'], 'func': ibc_base_universe_d3_020_ibc_029_insider_buy_cluster_63}


def ibc_base_universe_d3_021_ibc_030_insider_net_buy_ratio_252(ibc_base_universe_d2_021_ibc_030_insider_net_buy_ratio_252):
    return _base_universe_d3(ibc_base_universe_d2_021_ibc_030_insider_net_buy_ratio_252, 21)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_021_ibc_030_insider_net_buy_ratio_252'] = {'inputs': ['ibc_base_universe_d2_021_ibc_030_insider_net_buy_ratio_252'], 'func': ibc_base_universe_d3_021_ibc_030_insider_net_buy_ratio_252}


def ibc_base_universe_d3_022_ibc_031_insider_value_ratio_21(ibc_base_universe_d2_022_ibc_031_insider_value_ratio_21):
    return _base_universe_d3(ibc_base_universe_d2_022_ibc_031_insider_value_ratio_21, 22)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_022_ibc_031_insider_value_ratio_21'] = {'inputs': ['ibc_base_universe_d2_022_ibc_031_insider_value_ratio_21'], 'func': ibc_base_universe_d3_022_ibc_031_insider_value_ratio_21}


def ibc_base_universe_d3_023_ibc_032_ceo_cfo_buy_weight_42(ibc_base_universe_d2_023_ibc_032_ceo_cfo_buy_weight_42):
    return _base_universe_d3(ibc_base_universe_d2_023_ibc_032_ceo_cfo_buy_weight_42, 23)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_023_ibc_032_ceo_cfo_buy_weight_42'] = {'inputs': ['ibc_base_universe_d2_023_ibc_032_ceo_cfo_buy_weight_42'], 'func': ibc_base_universe_d3_023_ibc_032_ceo_cfo_buy_weight_42}


def ibc_base_universe_d3_024_ibc_034_insider_conviction_84(ibc_base_universe_d2_024_ibc_034_insider_conviction_84):
    return _base_universe_d3(ibc_base_universe_d2_024_ibc_034_insider_conviction_84, 24)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_024_ibc_034_insider_conviction_84'] = {'inputs': ['ibc_base_universe_d2_024_ibc_034_insider_conviction_84'], 'func': ibc_base_universe_d3_024_ibc_034_insider_conviction_84}


def ibc_base_universe_d3_025_ibc_035_insider_silence_126(ibc_base_universe_d2_025_ibc_035_insider_silence_126):
    return _base_universe_d3(ibc_base_universe_d2_025_ibc_035_insider_silence_126, 25)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_025_ibc_035_insider_silence_126'] = {'inputs': ['ibc_base_universe_d2_025_ibc_035_insider_silence_126'], 'func': ibc_base_universe_d3_025_ibc_035_insider_silence_126}


def ibc_base_universe_d3_026_ibc_036_insider_buy_cluster_189(ibc_base_universe_d2_026_ibc_036_insider_buy_cluster_189):
    return _base_universe_d3(ibc_base_universe_d2_026_ibc_036_insider_buy_cluster_189, 26)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_026_ibc_036_insider_buy_cluster_189'] = {'inputs': ['ibc_base_universe_d2_026_ibc_036_insider_buy_cluster_189'], 'func': ibc_base_universe_d3_026_ibc_036_insider_buy_cluster_189}


def ibc_base_universe_d3_027_ibc_038_insider_value_ratio_378(ibc_base_universe_d2_027_ibc_038_insider_value_ratio_378):
    return _base_universe_d3(ibc_base_universe_d2_027_ibc_038_insider_value_ratio_378, 27)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_027_ibc_038_insider_value_ratio_378'] = {'inputs': ['ibc_base_universe_d2_027_ibc_038_insider_value_ratio_378'], 'func': ibc_base_universe_d3_027_ibc_038_insider_value_ratio_378}


def ibc_base_universe_d3_028_ibc_039_ceo_cfo_buy_weight_504(ibc_base_universe_d2_028_ibc_039_ceo_cfo_buy_weight_504):
    return _base_universe_d3(ibc_base_universe_d2_028_ibc_039_ceo_cfo_buy_weight_504, 28)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_028_ibc_039_ceo_cfo_buy_weight_504'] = {'inputs': ['ibc_base_universe_d2_028_ibc_039_ceo_cfo_buy_weight_504'], 'func': ibc_base_universe_d3_028_ibc_039_ceo_cfo_buy_weight_504}


def ibc_base_universe_d3_029_ibc_041_insider_conviction_1008(ibc_base_universe_d2_029_ibc_041_insider_conviction_1008):
    return _base_universe_d3(ibc_base_universe_d2_029_ibc_041_insider_conviction_1008, 29)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_029_ibc_041_insider_conviction_1008'] = {'inputs': ['ibc_base_universe_d2_029_ibc_041_insider_conviction_1008'], 'func': ibc_base_universe_d3_029_ibc_041_insider_conviction_1008}


def ibc_base_universe_d3_030_ibc_042_insider_silence_1260(ibc_base_universe_d2_030_ibc_042_insider_silence_1260):
    return _base_universe_d3(ibc_base_universe_d2_030_ibc_042_insider_silence_1260, 30)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_030_ibc_042_insider_silence_1260'] = {'inputs': ['ibc_base_universe_d2_030_ibc_042_insider_silence_1260'], 'func': ibc_base_universe_d3_030_ibc_042_insider_silence_1260}


def ibc_base_universe_d3_031_ibc_043_insider_buy_cluster_1512(ibc_base_universe_d2_031_ibc_043_insider_buy_cluster_1512):
    return _base_universe_d3(ibc_base_universe_d2_031_ibc_043_insider_buy_cluster_1512, 31)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_031_ibc_043_insider_buy_cluster_1512'] = {'inputs': ['ibc_base_universe_d2_031_ibc_043_insider_buy_cluster_1512'], 'func': ibc_base_universe_d3_031_ibc_043_insider_buy_cluster_1512}


def ibc_base_universe_d3_032_ibc_044_insider_net_buy_ratio_63(ibc_base_universe_d2_032_ibc_044_insider_net_buy_ratio_63):
    return _base_universe_d3(ibc_base_universe_d2_032_ibc_044_insider_net_buy_ratio_63, 32)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_032_ibc_044_insider_net_buy_ratio_63'] = {'inputs': ['ibc_base_universe_d2_032_ibc_044_insider_net_buy_ratio_63'], 'func': ibc_base_universe_d3_032_ibc_044_insider_net_buy_ratio_63}


def ibc_base_universe_d3_033_ibc_045_insider_value_ratio_252(ibc_base_universe_d2_033_ibc_045_insider_value_ratio_252):
    return _base_universe_d3(ibc_base_universe_d2_033_ibc_045_insider_value_ratio_252, 33)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_033_ibc_045_insider_value_ratio_252'] = {'inputs': ['ibc_base_universe_d2_033_ibc_045_insider_value_ratio_252'], 'func': ibc_base_universe_d3_033_ibc_045_insider_value_ratio_252}


def ibc_base_universe_d3_034_ibc_046_ceo_cfo_buy_weight_21(ibc_base_universe_d2_034_ibc_046_ceo_cfo_buy_weight_21):
    return _base_universe_d3(ibc_base_universe_d2_034_ibc_046_ceo_cfo_buy_weight_21, 34)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_034_ibc_046_ceo_cfo_buy_weight_21'] = {'inputs': ['ibc_base_universe_d2_034_ibc_046_ceo_cfo_buy_weight_21'], 'func': ibc_base_universe_d3_034_ibc_046_ceo_cfo_buy_weight_21}


def ibc_base_universe_d3_035_ibc_048_insider_conviction_63(ibc_base_universe_d2_035_ibc_048_insider_conviction_63):
    return _base_universe_d3(ibc_base_universe_d2_035_ibc_048_insider_conviction_63, 35)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_035_ibc_048_insider_conviction_63'] = {'inputs': ['ibc_base_universe_d2_035_ibc_048_insider_conviction_63'], 'func': ibc_base_universe_d3_035_ibc_048_insider_conviction_63}


def ibc_base_universe_d3_036_ibc_049_insider_silence_84(ibc_base_universe_d2_036_ibc_049_insider_silence_84):
    return _base_universe_d3(ibc_base_universe_d2_036_ibc_049_insider_silence_84, 36)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_036_ibc_049_insider_silence_84'] = {'inputs': ['ibc_base_universe_d2_036_ibc_049_insider_silence_84'], 'func': ibc_base_universe_d3_036_ibc_049_insider_silence_84}


def ibc_base_universe_d3_037_ibc_050_insider_buy_cluster_126(ibc_base_universe_d2_037_ibc_050_insider_buy_cluster_126):
    return _base_universe_d3(ibc_base_universe_d2_037_ibc_050_insider_buy_cluster_126, 37)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_037_ibc_050_insider_buy_cluster_126'] = {'inputs': ['ibc_base_universe_d2_037_ibc_050_insider_buy_cluster_126'], 'func': ibc_base_universe_d3_037_ibc_050_insider_buy_cluster_126}


def ibc_base_universe_d3_038_ibc_051_insider_net_buy_ratio_189(ibc_base_universe_d2_038_ibc_051_insider_net_buy_ratio_189):
    return _base_universe_d3(ibc_base_universe_d2_038_ibc_051_insider_net_buy_ratio_189, 38)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_038_ibc_051_insider_net_buy_ratio_189'] = {'inputs': ['ibc_base_universe_d2_038_ibc_051_insider_net_buy_ratio_189'], 'func': ibc_base_universe_d3_038_ibc_051_insider_net_buy_ratio_189}


def ibc_base_universe_d3_039_ibc_053_ceo_cfo_buy_weight_378(ibc_base_universe_d2_039_ibc_053_ceo_cfo_buy_weight_378):
    return _base_universe_d3(ibc_base_universe_d2_039_ibc_053_ceo_cfo_buy_weight_378, 39)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_039_ibc_053_ceo_cfo_buy_weight_378'] = {'inputs': ['ibc_base_universe_d2_039_ibc_053_ceo_cfo_buy_weight_378'], 'func': ibc_base_universe_d3_039_ibc_053_ceo_cfo_buy_weight_378}


def ibc_base_universe_d3_040_ibc_055_insider_conviction_756(ibc_base_universe_d2_040_ibc_055_insider_conviction_756):
    return _base_universe_d3(ibc_base_universe_d2_040_ibc_055_insider_conviction_756, 40)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_040_ibc_055_insider_conviction_756'] = {'inputs': ['ibc_base_universe_d2_040_ibc_055_insider_conviction_756'], 'func': ibc_base_universe_d3_040_ibc_055_insider_conviction_756}


def ibc_base_universe_d3_041_ibc_056_insider_silence_1008(ibc_base_universe_d2_041_ibc_056_insider_silence_1008):
    return _base_universe_d3(ibc_base_universe_d2_041_ibc_056_insider_silence_1008, 41)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_041_ibc_056_insider_silence_1008'] = {'inputs': ['ibc_base_universe_d2_041_ibc_056_insider_silence_1008'], 'func': ibc_base_universe_d3_041_ibc_056_insider_silence_1008}


def ibc_base_universe_d3_042_ibc_057_insider_buy_cluster_1260(ibc_base_universe_d2_042_ibc_057_insider_buy_cluster_1260):
    return _base_universe_d3(ibc_base_universe_d2_042_ibc_057_insider_buy_cluster_1260, 42)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_042_ibc_057_insider_buy_cluster_1260'] = {'inputs': ['ibc_base_universe_d2_042_ibc_057_insider_buy_cluster_1260'], 'func': ibc_base_universe_d3_042_ibc_057_insider_buy_cluster_1260}


def ibc_base_universe_d3_043_ibc_058_insider_net_buy_ratio_1512(ibc_base_universe_d2_043_ibc_058_insider_net_buy_ratio_1512):
    return _base_universe_d3(ibc_base_universe_d2_043_ibc_058_insider_net_buy_ratio_1512, 43)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_043_ibc_058_insider_net_buy_ratio_1512'] = {'inputs': ['ibc_base_universe_d2_043_ibc_058_insider_net_buy_ratio_1512'], 'func': ibc_base_universe_d3_043_ibc_058_insider_net_buy_ratio_1512}


def ibc_base_universe_d3_044_ibc_060_ceo_cfo_buy_weight_252(ibc_base_universe_d2_044_ibc_060_ceo_cfo_buy_weight_252):
    return _base_universe_d3(ibc_base_universe_d2_044_ibc_060_ceo_cfo_buy_weight_252, 44)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_044_ibc_060_ceo_cfo_buy_weight_252'] = {'inputs': ['ibc_base_universe_d2_044_ibc_060_ceo_cfo_buy_weight_252'], 'func': ibc_base_universe_d3_044_ibc_060_ceo_cfo_buy_weight_252}


def ibc_base_universe_d3_045_ibc_062_insider_conviction_42(ibc_base_universe_d2_045_ibc_062_insider_conviction_42):
    return _base_universe_d3(ibc_base_universe_d2_045_ibc_062_insider_conviction_42, 45)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_045_ibc_062_insider_conviction_42'] = {'inputs': ['ibc_base_universe_d2_045_ibc_062_insider_conviction_42'], 'func': ibc_base_universe_d3_045_ibc_062_insider_conviction_42}


def ibc_base_universe_d3_046_ibc_064_insider_buy_cluster_84(ibc_base_universe_d2_046_ibc_064_insider_buy_cluster_84):
    return _base_universe_d3(ibc_base_universe_d2_046_ibc_064_insider_buy_cluster_84, 46)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_046_ibc_064_insider_buy_cluster_84'] = {'inputs': ['ibc_base_universe_d2_046_ibc_064_insider_buy_cluster_84'], 'func': ibc_base_universe_d3_046_ibc_064_insider_buy_cluster_84}


def ibc_base_universe_d3_047_ibc_065_insider_net_buy_ratio_126(ibc_base_universe_d2_047_ibc_065_insider_net_buy_ratio_126):
    return _base_universe_d3(ibc_base_universe_d2_047_ibc_065_insider_net_buy_ratio_126, 47)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_047_ibc_065_insider_net_buy_ratio_126'] = {'inputs': ['ibc_base_universe_d2_047_ibc_065_insider_net_buy_ratio_126'], 'func': ibc_base_universe_d3_047_ibc_065_insider_net_buy_ratio_126}


def ibc_base_universe_d3_048_ibc_066_insider_value_ratio_189(ibc_base_universe_d2_048_ibc_066_insider_value_ratio_189):
    return _base_universe_d3(ibc_base_universe_d2_048_ibc_066_insider_value_ratio_189, 48)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_048_ibc_066_insider_value_ratio_189'] = {'inputs': ['ibc_base_universe_d2_048_ibc_066_insider_value_ratio_189'], 'func': ibc_base_universe_d3_048_ibc_066_insider_value_ratio_189}


def ibc_base_universe_d3_049_ibc_069_insider_conviction_504(ibc_base_universe_d2_049_ibc_069_insider_conviction_504):
    return _base_universe_d3(ibc_base_universe_d2_049_ibc_069_insider_conviction_504, 49)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_049_ibc_069_insider_conviction_504'] = {'inputs': ['ibc_base_universe_d2_049_ibc_069_insider_conviction_504'], 'func': ibc_base_universe_d3_049_ibc_069_insider_conviction_504}


def ibc_base_universe_d3_050_ibc_070_insider_silence_756(ibc_base_universe_d2_050_ibc_070_insider_silence_756):
    return _base_universe_d3(ibc_base_universe_d2_050_ibc_070_insider_silence_756, 50)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_050_ibc_070_insider_silence_756'] = {'inputs': ['ibc_base_universe_d2_050_ibc_070_insider_silence_756'], 'func': ibc_base_universe_d3_050_ibc_070_insider_silence_756}


def ibc_base_universe_d3_051_ibc_071_insider_buy_cluster_1008(ibc_base_universe_d2_051_ibc_071_insider_buy_cluster_1008):
    return _base_universe_d3(ibc_base_universe_d2_051_ibc_071_insider_buy_cluster_1008, 51)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_051_ibc_071_insider_buy_cluster_1008'] = {'inputs': ['ibc_base_universe_d2_051_ibc_071_insider_buy_cluster_1008'], 'func': ibc_base_universe_d3_051_ibc_071_insider_buy_cluster_1008}


def ibc_base_universe_d3_052_ibc_072_insider_net_buy_ratio_1260(ibc_base_universe_d2_052_ibc_072_insider_net_buy_ratio_1260):
    return _base_universe_d3(ibc_base_universe_d2_052_ibc_072_insider_net_buy_ratio_1260, 52)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_052_ibc_072_insider_net_buy_ratio_1260'] = {'inputs': ['ibc_base_universe_d2_052_ibc_072_insider_net_buy_ratio_1260'], 'func': ibc_base_universe_d3_052_ibc_072_insider_net_buy_ratio_1260}


def ibc_base_universe_d3_053_ibc_073_insider_value_ratio_1512(ibc_base_universe_d2_053_ibc_073_insider_value_ratio_1512):
    return _base_universe_d3(ibc_base_universe_d2_053_ibc_073_insider_value_ratio_1512, 53)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_053_ibc_073_insider_value_ratio_1512'] = {'inputs': ['ibc_base_universe_d2_053_ibc_073_insider_value_ratio_1512'], 'func': ibc_base_universe_d3_053_ibc_073_insider_value_ratio_1512}


def ibc_base_universe_d3_054_ibc_basefill_005(ibc_base_universe_d2_054_ibc_basefill_005):
    return _base_universe_d3(ibc_base_universe_d2_054_ibc_basefill_005, 54)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_054_ibc_basefill_005'] = {'inputs': ['ibc_base_universe_d2_054_ibc_basefill_005'], 'func': ibc_base_universe_d3_054_ibc_basefill_005}


def ibc_base_universe_d3_055_ibc_basefill_012(ibc_base_universe_d2_055_ibc_basefill_012):
    return _base_universe_d3(ibc_base_universe_d2_055_ibc_basefill_012, 55)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_055_ibc_basefill_012'] = {'inputs': ['ibc_base_universe_d2_055_ibc_basefill_012'], 'func': ibc_base_universe_d3_055_ibc_basefill_012}


def ibc_base_universe_d3_056_ibc_basefill_019(ibc_base_universe_d2_056_ibc_basefill_019):
    return _base_universe_d3(ibc_base_universe_d2_056_ibc_basefill_019, 56)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_056_ibc_basefill_019'] = {'inputs': ['ibc_base_universe_d2_056_ibc_basefill_019'], 'func': ibc_base_universe_d3_056_ibc_basefill_019}


def ibc_base_universe_d3_057_ibc_basefill_022(ibc_base_universe_d2_057_ibc_basefill_022):
    return _base_universe_d3(ibc_base_universe_d2_057_ibc_basefill_022, 57)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_057_ibc_basefill_022'] = {'inputs': ['ibc_base_universe_d2_057_ibc_basefill_022'], 'func': ibc_base_universe_d3_057_ibc_basefill_022}


def ibc_base_universe_d3_058_ibc_basefill_026(ibc_base_universe_d2_058_ibc_basefill_026):
    return _base_universe_d3(ibc_base_universe_d2_058_ibc_basefill_026, 58)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_058_ibc_basefill_026'] = {'inputs': ['ibc_base_universe_d2_058_ibc_basefill_026'], 'func': ibc_base_universe_d3_058_ibc_basefill_026}


def ibc_base_universe_d3_059_ibc_basefill_033(ibc_base_universe_d2_059_ibc_basefill_033):
    return _base_universe_d3(ibc_base_universe_d2_059_ibc_basefill_033, 59)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_059_ibc_basefill_033'] = {'inputs': ['ibc_base_universe_d2_059_ibc_basefill_033'], 'func': ibc_base_universe_d3_059_ibc_basefill_033}


def ibc_base_universe_d3_060_ibc_basefill_037(ibc_base_universe_d2_060_ibc_basefill_037):
    return _base_universe_d3(ibc_base_universe_d2_060_ibc_basefill_037, 60)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_060_ibc_basefill_037'] = {'inputs': ['ibc_base_universe_d2_060_ibc_basefill_037'], 'func': ibc_base_universe_d3_060_ibc_basefill_037}


def ibc_base_universe_d3_061_ibc_basefill_040(ibc_base_universe_d2_061_ibc_basefill_040):
    return _base_universe_d3(ibc_base_universe_d2_061_ibc_basefill_040, 61)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_061_ibc_basefill_040'] = {'inputs': ['ibc_base_universe_d2_061_ibc_basefill_040'], 'func': ibc_base_universe_d3_061_ibc_basefill_040}


def ibc_base_universe_d3_062_ibc_basefill_047(ibc_base_universe_d2_062_ibc_basefill_047):
    return _base_universe_d3(ibc_base_universe_d2_062_ibc_basefill_047, 62)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_062_ibc_basefill_047'] = {'inputs': ['ibc_base_universe_d2_062_ibc_basefill_047'], 'func': ibc_base_universe_d3_062_ibc_basefill_047}


def ibc_base_universe_d3_063_ibc_basefill_052(ibc_base_universe_d2_063_ibc_basefill_052):
    return _base_universe_d3(ibc_base_universe_d2_063_ibc_basefill_052, 63)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_063_ibc_basefill_052'] = {'inputs': ['ibc_base_universe_d2_063_ibc_basefill_052'], 'func': ibc_base_universe_d3_063_ibc_basefill_052}


def ibc_base_universe_d3_064_ibc_basefill_054(ibc_base_universe_d2_064_ibc_basefill_054):
    return _base_universe_d3(ibc_base_universe_d2_064_ibc_basefill_054, 64)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_064_ibc_basefill_054'] = {'inputs': ['ibc_base_universe_d2_064_ibc_basefill_054'], 'func': ibc_base_universe_d3_064_ibc_basefill_054}


def ibc_base_universe_d3_065_ibc_basefill_059(ibc_base_universe_d2_065_ibc_basefill_059):
    return _base_universe_d3(ibc_base_universe_d2_065_ibc_basefill_059, 65)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_065_ibc_basefill_059'] = {'inputs': ['ibc_base_universe_d2_065_ibc_basefill_059'], 'func': ibc_base_universe_d3_065_ibc_basefill_059}


def ibc_base_universe_d3_066_ibc_basefill_061(ibc_base_universe_d2_066_ibc_basefill_061):
    return _base_universe_d3(ibc_base_universe_d2_066_ibc_basefill_061, 66)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_066_ibc_basefill_061'] = {'inputs': ['ibc_base_universe_d2_066_ibc_basefill_061'], 'func': ibc_base_universe_d3_066_ibc_basefill_061}


def ibc_base_universe_d3_067_ibc_basefill_063(ibc_base_universe_d2_067_ibc_basefill_063):
    return _base_universe_d3(ibc_base_universe_d2_067_ibc_basefill_063, 67)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_067_ibc_basefill_063'] = {'inputs': ['ibc_base_universe_d2_067_ibc_basefill_063'], 'func': ibc_base_universe_d3_067_ibc_basefill_063}


def ibc_base_universe_d3_068_ibc_basefill_067(ibc_base_universe_d2_068_ibc_basefill_067):
    return _base_universe_d3(ibc_base_universe_d2_068_ibc_basefill_067, 68)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_068_ibc_basefill_067'] = {'inputs': ['ibc_base_universe_d2_068_ibc_basefill_067'], 'func': ibc_base_universe_d3_068_ibc_basefill_067}


def ibc_base_universe_d3_069_ibc_basefill_068(ibc_base_universe_d2_069_ibc_basefill_068):
    return _base_universe_d3(ibc_base_universe_d2_069_ibc_basefill_068, 69)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_069_ibc_basefill_068'] = {'inputs': ['ibc_base_universe_d2_069_ibc_basefill_068'], 'func': ibc_base_universe_d3_069_ibc_basefill_068}


def ibc_base_universe_d3_070_ibc_basefill_074(ibc_base_universe_d2_070_ibc_basefill_074):
    return _base_universe_d3(ibc_base_universe_d2_070_ibc_basefill_074, 70)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_070_ibc_basefill_074'] = {'inputs': ['ibc_base_universe_d2_070_ibc_basefill_074'], 'func': ibc_base_universe_d3_070_ibc_basefill_074}


def ibc_base_universe_d3_071_ibc_basefill_075(ibc_base_universe_d2_071_ibc_basefill_075):
    return _base_universe_d3(ibc_base_universe_d2_071_ibc_basefill_075, 71)
IBC_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibc_base_universe_d3_071_ibc_basefill_075'] = {'inputs': ['ibc_base_universe_d2_071_ibc_basefill_075'], 'func': ibc_base_universe_d3_071_ibc_basefill_075}

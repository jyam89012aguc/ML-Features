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



def icn_176_icn_001_insider_buy_cluster_21_accel_1(icn_151_icn_001_insider_buy_cluster_21_roc_1):
    feature = _s(icn_151_icn_001_insider_buy_cluster_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def icn_177_icn_007_insider_silence_252_accel_42(icn_152_icn_007_insider_silence_252_roc_42):
    feature = _s(icn_152_icn_007_insider_silence_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def icn_178_icn_013_insider_conviction_1512_accel_126(icn_153_icn_013_insider_conviction_1512_roc_126):
    feature = _s(icn_153_icn_013_insider_conviction_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def icn_179_icn_019_insider_activity_accel_1_accel_378(icn_154_icn_019_insider_activity_accel_1_roc_378):
    feature = _s(icn_154_icn_019_insider_activity_accel_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def icn_180_icn_025_ceo_cfo_buy_weight_756_accel_4(icn_155_icn_025_ceo_cfo_buy_weight_756_roc_4):
    feature = _s(icn_155_icn_025_ceo_cfo_buy_weight_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSIDER_CONVICTION_REGISTRY_3RD_DERIVATIVES = {
    'icn_176_icn_001_insider_buy_cluster_21_accel_1': {'inputs': ['icn_151_icn_001_insider_buy_cluster_21_roc_1'], 'func': icn_176_icn_001_insider_buy_cluster_21_accel_1},
    'icn_177_icn_007_insider_silence_252_accel_42': {'inputs': ['icn_152_icn_007_insider_silence_252_roc_42'], 'func': icn_177_icn_007_insider_silence_252_accel_42},
    'icn_178_icn_013_insider_conviction_1512_accel_126': {'inputs': ['icn_153_icn_013_insider_conviction_1512_roc_126'], 'func': icn_178_icn_013_insider_conviction_1512_accel_126},
    'icn_179_icn_019_insider_activity_accel_1_accel_378': {'inputs': ['icn_154_icn_019_insider_activity_accel_1_roc_378'], 'func': icn_179_icn_019_insider_activity_accel_1_accel_378},
    'icn_180_icn_025_ceo_cfo_buy_weight_756_accel_4': {'inputs': ['icn_155_icn_025_ceo_cfo_buy_weight_756_roc_4'], 'func': icn_180_icn_025_ceo_cfo_buy_weight_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ic_replacement_d3_001(ic_replacement_d2_001):
    feature = _clean(ic_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_001'] = {'inputs': ['ic_replacement_d2_001'], 'func': ic_replacement_d3_001}


def ic_replacement_d3_002(ic_replacement_d2_002):
    feature = _clean(ic_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_002'] = {'inputs': ['ic_replacement_d2_002'], 'func': ic_replacement_d3_002}


def ic_replacement_d3_003(ic_replacement_d2_003):
    feature = _clean(ic_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_003'] = {'inputs': ['ic_replacement_d2_003'], 'func': ic_replacement_d3_003}


def ic_replacement_d3_004(ic_replacement_d2_004):
    feature = _clean(ic_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_004'] = {'inputs': ['ic_replacement_d2_004'], 'func': ic_replacement_d3_004}


def ic_replacement_d3_005(ic_replacement_d2_005):
    feature = _clean(ic_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_005'] = {'inputs': ['ic_replacement_d2_005'], 'func': ic_replacement_d3_005}


def ic_replacement_d3_006(ic_replacement_d2_006):
    feature = _clean(ic_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_006'] = {'inputs': ['ic_replacement_d2_006'], 'func': ic_replacement_d3_006}


def ic_replacement_d3_007(ic_replacement_d2_007):
    feature = _clean(ic_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_007'] = {'inputs': ['ic_replacement_d2_007'], 'func': ic_replacement_d3_007}


def ic_replacement_d3_008(ic_replacement_d2_008):
    feature = _clean(ic_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_008'] = {'inputs': ['ic_replacement_d2_008'], 'func': ic_replacement_d3_008}


def ic_replacement_d3_009(ic_replacement_d2_009):
    feature = _clean(ic_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_009'] = {'inputs': ['ic_replacement_d2_009'], 'func': ic_replacement_d3_009}


def ic_replacement_d3_010(ic_replacement_d2_010):
    feature = _clean(ic_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_010'] = {'inputs': ['ic_replacement_d2_010'], 'func': ic_replacement_d3_010}


def ic_replacement_d3_011(ic_replacement_d2_011):
    feature = _clean(ic_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_011'] = {'inputs': ['ic_replacement_d2_011'], 'func': ic_replacement_d3_011}


def ic_replacement_d3_012(ic_replacement_d2_012):
    feature = _clean(ic_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_012'] = {'inputs': ['ic_replacement_d2_012'], 'func': ic_replacement_d3_012}


def ic_replacement_d3_013(ic_replacement_d2_013):
    feature = _clean(ic_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_013'] = {'inputs': ['ic_replacement_d2_013'], 'func': ic_replacement_d3_013}


def ic_replacement_d3_014(ic_replacement_d2_014):
    feature = _clean(ic_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_014'] = {'inputs': ['ic_replacement_d2_014'], 'func': ic_replacement_d3_014}


def ic_replacement_d3_015(ic_replacement_d2_015):
    feature = _clean(ic_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_015'] = {'inputs': ['ic_replacement_d2_015'], 'func': ic_replacement_d3_015}


def ic_replacement_d3_016(ic_replacement_d2_016):
    feature = _clean(ic_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_016'] = {'inputs': ['ic_replacement_d2_016'], 'func': ic_replacement_d3_016}


def ic_replacement_d3_017(ic_replacement_d2_017):
    feature = _clean(ic_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_017'] = {'inputs': ['ic_replacement_d2_017'], 'func': ic_replacement_d3_017}


def ic_replacement_d3_018(ic_replacement_d2_018):
    feature = _clean(ic_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_018'] = {'inputs': ['ic_replacement_d2_018'], 'func': ic_replacement_d3_018}


def ic_replacement_d3_019(ic_replacement_d2_019):
    feature = _clean(ic_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_019'] = {'inputs': ['ic_replacement_d2_019'], 'func': ic_replacement_d3_019}


def ic_replacement_d3_020(ic_replacement_d2_020):
    feature = _clean(ic_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_020'] = {'inputs': ['ic_replacement_d2_020'], 'func': ic_replacement_d3_020}


def ic_replacement_d3_021(ic_replacement_d2_021):
    feature = _clean(ic_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_021'] = {'inputs': ['ic_replacement_d2_021'], 'func': ic_replacement_d3_021}


def ic_replacement_d3_022(ic_replacement_d2_022):
    feature = _clean(ic_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_022'] = {'inputs': ['ic_replacement_d2_022'], 'func': ic_replacement_d3_022}


def ic_replacement_d3_023(ic_replacement_d2_023):
    feature = _clean(ic_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_023'] = {'inputs': ['ic_replacement_d2_023'], 'func': ic_replacement_d3_023}


def ic_replacement_d3_024(ic_replacement_d2_024):
    feature = _clean(ic_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_024'] = {'inputs': ['ic_replacement_d2_024'], 'func': ic_replacement_d3_024}


def ic_replacement_d3_025(ic_replacement_d2_025):
    feature = _clean(ic_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_025'] = {'inputs': ['ic_replacement_d2_025'], 'func': ic_replacement_d3_025}


def ic_replacement_d3_026(ic_replacement_d2_026):
    feature = _clean(ic_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_026'] = {'inputs': ['ic_replacement_d2_026'], 'func': ic_replacement_d3_026}


def ic_replacement_d3_027(ic_replacement_d2_027):
    feature = _clean(ic_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_027'] = {'inputs': ['ic_replacement_d2_027'], 'func': ic_replacement_d3_027}


def ic_replacement_d3_028(ic_replacement_d2_028):
    feature = _clean(ic_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_028'] = {'inputs': ['ic_replacement_d2_028'], 'func': ic_replacement_d3_028}


def ic_replacement_d3_029(ic_replacement_d2_029):
    feature = _clean(ic_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_029'] = {'inputs': ['ic_replacement_d2_029'], 'func': ic_replacement_d3_029}


def ic_replacement_d3_030(ic_replacement_d2_030):
    feature = _clean(ic_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_030'] = {'inputs': ['ic_replacement_d2_030'], 'func': ic_replacement_d3_030}


def ic_replacement_d3_031(ic_replacement_d2_031):
    feature = _clean(ic_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_031'] = {'inputs': ['ic_replacement_d2_031'], 'func': ic_replacement_d3_031}


def ic_replacement_d3_032(ic_replacement_d2_032):
    feature = _clean(ic_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_032'] = {'inputs': ['ic_replacement_d2_032'], 'func': ic_replacement_d3_032}


def ic_replacement_d3_033(ic_replacement_d2_033):
    feature = _clean(ic_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_033'] = {'inputs': ['ic_replacement_d2_033'], 'func': ic_replacement_d3_033}


def ic_replacement_d3_034(ic_replacement_d2_034):
    feature = _clean(ic_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_034'] = {'inputs': ['ic_replacement_d2_034'], 'func': ic_replacement_d3_034}


def ic_replacement_d3_035(ic_replacement_d2_035):
    feature = _clean(ic_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_035'] = {'inputs': ['ic_replacement_d2_035'], 'func': ic_replacement_d3_035}


def ic_replacement_d3_036(ic_replacement_d2_036):
    feature = _clean(ic_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_036'] = {'inputs': ['ic_replacement_d2_036'], 'func': ic_replacement_d3_036}


def ic_replacement_d3_037(ic_replacement_d2_037):
    feature = _clean(ic_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_037'] = {'inputs': ['ic_replacement_d2_037'], 'func': ic_replacement_d3_037}


def ic_replacement_d3_038(ic_replacement_d2_038):
    feature = _clean(ic_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_038'] = {'inputs': ['ic_replacement_d2_038'], 'func': ic_replacement_d3_038}


def ic_replacement_d3_039(ic_replacement_d2_039):
    feature = _clean(ic_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_039'] = {'inputs': ['ic_replacement_d2_039'], 'func': ic_replacement_d3_039}


def ic_replacement_d3_040(ic_replacement_d2_040):
    feature = _clean(ic_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_040'] = {'inputs': ['ic_replacement_d2_040'], 'func': ic_replacement_d3_040}


def ic_replacement_d3_041(ic_replacement_d2_041):
    feature = _clean(ic_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_041'] = {'inputs': ['ic_replacement_d2_041'], 'func': ic_replacement_d3_041}


def ic_replacement_d3_042(ic_replacement_d2_042):
    feature = _clean(ic_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_042'] = {'inputs': ['ic_replacement_d2_042'], 'func': ic_replacement_d3_042}


def ic_replacement_d3_043(ic_replacement_d2_043):
    feature = _clean(ic_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_043'] = {'inputs': ['ic_replacement_d2_043'], 'func': ic_replacement_d3_043}


def ic_replacement_d3_044(ic_replacement_d2_044):
    feature = _clean(ic_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_044'] = {'inputs': ['ic_replacement_d2_044'], 'func': ic_replacement_d3_044}


def ic_replacement_d3_045(ic_replacement_d2_045):
    feature = _clean(ic_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_045'] = {'inputs': ['ic_replacement_d2_045'], 'func': ic_replacement_d3_045}


def ic_replacement_d3_046(ic_replacement_d2_046):
    feature = _clean(ic_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_046'] = {'inputs': ['ic_replacement_d2_046'], 'func': ic_replacement_d3_046}


def ic_replacement_d3_047(ic_replacement_d2_047):
    feature = _clean(ic_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_047'] = {'inputs': ['ic_replacement_d2_047'], 'func': ic_replacement_d3_047}


def ic_replacement_d3_048(ic_replacement_d2_048):
    feature = _clean(ic_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_048'] = {'inputs': ['ic_replacement_d2_048'], 'func': ic_replacement_d3_048}


def ic_replacement_d3_049(ic_replacement_d2_049):
    feature = _clean(ic_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_049'] = {'inputs': ['ic_replacement_d2_049'], 'func': ic_replacement_d3_049}


def ic_replacement_d3_050(ic_replacement_d2_050):
    feature = _clean(ic_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_050'] = {'inputs': ['ic_replacement_d2_050'], 'func': ic_replacement_d3_050}


def ic_replacement_d3_051(ic_replacement_d2_051):
    feature = _clean(ic_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_051'] = {'inputs': ['ic_replacement_d2_051'], 'func': ic_replacement_d3_051}


def ic_replacement_d3_052(ic_replacement_d2_052):
    feature = _clean(ic_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_052'] = {'inputs': ['ic_replacement_d2_052'], 'func': ic_replacement_d3_052}


def ic_replacement_d3_053(ic_replacement_d2_053):
    feature = _clean(ic_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_053'] = {'inputs': ['ic_replacement_d2_053'], 'func': ic_replacement_d3_053}


def ic_replacement_d3_054(ic_replacement_d2_054):
    feature = _clean(ic_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_054'] = {'inputs': ['ic_replacement_d2_054'], 'func': ic_replacement_d3_054}


def ic_replacement_d3_055(ic_replacement_d2_055):
    feature = _clean(ic_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_055'] = {'inputs': ['ic_replacement_d2_055'], 'func': ic_replacement_d3_055}


def ic_replacement_d3_056(ic_replacement_d2_056):
    feature = _clean(ic_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_056'] = {'inputs': ['ic_replacement_d2_056'], 'func': ic_replacement_d3_056}


def ic_replacement_d3_057(ic_replacement_d2_057):
    feature = _clean(ic_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_057'] = {'inputs': ['ic_replacement_d2_057'], 'func': ic_replacement_d3_057}


def ic_replacement_d3_058(ic_replacement_d2_058):
    feature = _clean(ic_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_058'] = {'inputs': ['ic_replacement_d2_058'], 'func': ic_replacement_d3_058}


def ic_replacement_d3_059(ic_replacement_d2_059):
    feature = _clean(ic_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_059'] = {'inputs': ['ic_replacement_d2_059'], 'func': ic_replacement_d3_059}


def ic_replacement_d3_060(ic_replacement_d2_060):
    feature = _clean(ic_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_060'] = {'inputs': ['ic_replacement_d2_060'], 'func': ic_replacement_d3_060}


def ic_replacement_d3_061(ic_replacement_d2_061):
    feature = _clean(ic_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_061'] = {'inputs': ['ic_replacement_d2_061'], 'func': ic_replacement_d3_061}


def ic_replacement_d3_062(ic_replacement_d2_062):
    feature = _clean(ic_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_062'] = {'inputs': ['ic_replacement_d2_062'], 'func': ic_replacement_d3_062}


def ic_replacement_d3_063(ic_replacement_d2_063):
    feature = _clean(ic_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_063'] = {'inputs': ['ic_replacement_d2_063'], 'func': ic_replacement_d3_063}


def ic_replacement_d3_064(ic_replacement_d2_064):
    feature = _clean(ic_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_064'] = {'inputs': ['ic_replacement_d2_064'], 'func': ic_replacement_d3_064}


def ic_replacement_d3_065(ic_replacement_d2_065):
    feature = _clean(ic_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_065'] = {'inputs': ['ic_replacement_d2_065'], 'func': ic_replacement_d3_065}


def ic_replacement_d3_066(ic_replacement_d2_066):
    feature = _clean(ic_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_066'] = {'inputs': ['ic_replacement_d2_066'], 'func': ic_replacement_d3_066}


def ic_replacement_d3_067(ic_replacement_d2_067):
    feature = _clean(ic_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_067'] = {'inputs': ['ic_replacement_d2_067'], 'func': ic_replacement_d3_067}


def ic_replacement_d3_068(ic_replacement_d2_068):
    feature = _clean(ic_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_068'] = {'inputs': ['ic_replacement_d2_068'], 'func': ic_replacement_d3_068}


def ic_replacement_d3_069(ic_replacement_d2_069):
    feature = _clean(ic_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_069'] = {'inputs': ['ic_replacement_d2_069'], 'func': ic_replacement_d3_069}


def ic_replacement_d3_070(ic_replacement_d2_070):
    feature = _clean(ic_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_070'] = {'inputs': ['ic_replacement_d2_070'], 'func': ic_replacement_d3_070}


def ic_replacement_d3_071(ic_replacement_d2_071):
    feature = _clean(ic_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_071'] = {'inputs': ['ic_replacement_d2_071'], 'func': ic_replacement_d3_071}


def ic_replacement_d3_072(ic_replacement_d2_072):
    feature = _clean(ic_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_072'] = {'inputs': ['ic_replacement_d2_072'], 'func': ic_replacement_d3_072}


def ic_replacement_d3_073(ic_replacement_d2_073):
    feature = _clean(ic_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_073'] = {'inputs': ['ic_replacement_d2_073'], 'func': ic_replacement_d3_073}


def ic_replacement_d3_074(ic_replacement_d2_074):
    feature = _clean(ic_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_074'] = {'inputs': ['ic_replacement_d2_074'], 'func': ic_replacement_d3_074}


def ic_replacement_d3_075(ic_replacement_d2_075):
    feature = _clean(ic_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_075'] = {'inputs': ['ic_replacement_d2_075'], 'func': ic_replacement_d3_075}


def ic_replacement_d3_076(ic_replacement_d2_076):
    feature = _clean(ic_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_076'] = {'inputs': ['ic_replacement_d2_076'], 'func': ic_replacement_d3_076}


def ic_replacement_d3_077(ic_replacement_d2_077):
    feature = _clean(ic_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_077'] = {'inputs': ['ic_replacement_d2_077'], 'func': ic_replacement_d3_077}


def ic_replacement_d3_078(ic_replacement_d2_078):
    feature = _clean(ic_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_078'] = {'inputs': ['ic_replacement_d2_078'], 'func': ic_replacement_d3_078}


def ic_replacement_d3_079(ic_replacement_d2_079):
    feature = _clean(ic_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_079'] = {'inputs': ['ic_replacement_d2_079'], 'func': ic_replacement_d3_079}


def ic_replacement_d3_080(ic_replacement_d2_080):
    feature = _clean(ic_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_080'] = {'inputs': ['ic_replacement_d2_080'], 'func': ic_replacement_d3_080}


def ic_replacement_d3_081(ic_replacement_d2_081):
    feature = _clean(ic_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_081'] = {'inputs': ['ic_replacement_d2_081'], 'func': ic_replacement_d3_081}


def ic_replacement_d3_082(ic_replacement_d2_082):
    feature = _clean(ic_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_082'] = {'inputs': ['ic_replacement_d2_082'], 'func': ic_replacement_d3_082}


def ic_replacement_d3_083(ic_replacement_d2_083):
    feature = _clean(ic_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_083'] = {'inputs': ['ic_replacement_d2_083'], 'func': ic_replacement_d3_083}


def ic_replacement_d3_084(ic_replacement_d2_084):
    feature = _clean(ic_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_084'] = {'inputs': ['ic_replacement_d2_084'], 'func': ic_replacement_d3_084}


def ic_replacement_d3_085(ic_replacement_d2_085):
    feature = _clean(ic_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_085'] = {'inputs': ['ic_replacement_d2_085'], 'func': ic_replacement_d3_085}


def ic_replacement_d3_086(ic_replacement_d2_086):
    feature = _clean(ic_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_086'] = {'inputs': ['ic_replacement_d2_086'], 'func': ic_replacement_d3_086}


def ic_replacement_d3_087(ic_replacement_d2_087):
    feature = _clean(ic_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_087'] = {'inputs': ['ic_replacement_d2_087'], 'func': ic_replacement_d3_087}


def ic_replacement_d3_088(ic_replacement_d2_088):
    feature = _clean(ic_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_088'] = {'inputs': ['ic_replacement_d2_088'], 'func': ic_replacement_d3_088}


def ic_replacement_d3_089(ic_replacement_d2_089):
    feature = _clean(ic_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_089'] = {'inputs': ['ic_replacement_d2_089'], 'func': ic_replacement_d3_089}


def ic_replacement_d3_090(ic_replacement_d2_090):
    feature = _clean(ic_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_090'] = {'inputs': ['ic_replacement_d2_090'], 'func': ic_replacement_d3_090}


def ic_replacement_d3_091(ic_replacement_d2_091):
    feature = _clean(ic_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_091'] = {'inputs': ['ic_replacement_d2_091'], 'func': ic_replacement_d3_091}


def ic_replacement_d3_092(ic_replacement_d2_092):
    feature = _clean(ic_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_092'] = {'inputs': ['ic_replacement_d2_092'], 'func': ic_replacement_d3_092}


def ic_replacement_d3_093(ic_replacement_d2_093):
    feature = _clean(ic_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_093'] = {'inputs': ['ic_replacement_d2_093'], 'func': ic_replacement_d3_093}


def ic_replacement_d3_094(ic_replacement_d2_094):
    feature = _clean(ic_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_094'] = {'inputs': ['ic_replacement_d2_094'], 'func': ic_replacement_d3_094}


def ic_replacement_d3_095(ic_replacement_d2_095):
    feature = _clean(ic_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_095'] = {'inputs': ['ic_replacement_d2_095'], 'func': ic_replacement_d3_095}


def ic_replacement_d3_096(ic_replacement_d2_096):
    feature = _clean(ic_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_096'] = {'inputs': ['ic_replacement_d2_096'], 'func': ic_replacement_d3_096}


def ic_replacement_d3_097(ic_replacement_d2_097):
    feature = _clean(ic_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_097'] = {'inputs': ['ic_replacement_d2_097'], 'func': ic_replacement_d3_097}


def ic_replacement_d3_098(ic_replacement_d2_098):
    feature = _clean(ic_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_098'] = {'inputs': ['ic_replacement_d2_098'], 'func': ic_replacement_d3_098}


def ic_replacement_d3_099(ic_replacement_d2_099):
    feature = _clean(ic_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_099'] = {'inputs': ['ic_replacement_d2_099'], 'func': ic_replacement_d3_099}


def ic_replacement_d3_100(ic_replacement_d2_100):
    feature = _clean(ic_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_100'] = {'inputs': ['ic_replacement_d2_100'], 'func': ic_replacement_d3_100}


def ic_replacement_d3_101(ic_replacement_d2_101):
    feature = _clean(ic_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_101'] = {'inputs': ['ic_replacement_d2_101'], 'func': ic_replacement_d3_101}


def ic_replacement_d3_102(ic_replacement_d2_102):
    feature = _clean(ic_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_102'] = {'inputs': ['ic_replacement_d2_102'], 'func': ic_replacement_d3_102}


def ic_replacement_d3_103(ic_replacement_d2_103):
    feature = _clean(ic_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_103'] = {'inputs': ['ic_replacement_d2_103'], 'func': ic_replacement_d3_103}


def ic_replacement_d3_104(ic_replacement_d2_104):
    feature = _clean(ic_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_104'] = {'inputs': ['ic_replacement_d2_104'], 'func': ic_replacement_d3_104}


def ic_replacement_d3_105(ic_replacement_d2_105):
    feature = _clean(ic_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_105'] = {'inputs': ['ic_replacement_d2_105'], 'func': ic_replacement_d3_105}


def ic_replacement_d3_106(ic_replacement_d2_106):
    feature = _clean(ic_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_106'] = {'inputs': ['ic_replacement_d2_106'], 'func': ic_replacement_d3_106}


def ic_replacement_d3_107(ic_replacement_d2_107):
    feature = _clean(ic_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_107'] = {'inputs': ['ic_replacement_d2_107'], 'func': ic_replacement_d3_107}


def ic_replacement_d3_108(ic_replacement_d2_108):
    feature = _clean(ic_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_108'] = {'inputs': ['ic_replacement_d2_108'], 'func': ic_replacement_d3_108}


def ic_replacement_d3_109(ic_replacement_d2_109):
    feature = _clean(ic_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_109'] = {'inputs': ['ic_replacement_d2_109'], 'func': ic_replacement_d3_109}


def ic_replacement_d3_110(ic_replacement_d2_110):
    feature = _clean(ic_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_110'] = {'inputs': ['ic_replacement_d2_110'], 'func': ic_replacement_d3_110}


def ic_replacement_d3_111(ic_replacement_d2_111):
    feature = _clean(ic_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_111'] = {'inputs': ['ic_replacement_d2_111'], 'func': ic_replacement_d3_111}


def ic_replacement_d3_112(ic_replacement_d2_112):
    feature = _clean(ic_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ic_replacement_d3_112'] = {'inputs': ['ic_replacement_d2_112'], 'func': ic_replacement_d3_112}


# Third-derivative extensions for repaired first-base features.
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def icn_base_universe_d3_001_icn_002_insider_net_buy_ratio_42(icn_base_universe_d2_001_icn_002_insider_net_buy_ratio_42):
    return _base_universe_d3(icn_base_universe_d2_001_icn_002_insider_net_buy_ratio_42, 1)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_001_icn_002_insider_net_buy_ratio_42'] = {'inputs': ['icn_base_universe_d2_001_icn_002_insider_net_buy_ratio_42'], 'func': icn_base_universe_d3_001_icn_002_insider_net_buy_ratio_42}


def icn_base_universe_d3_002_icn_003_insider_value_ratio_63(icn_base_universe_d2_002_icn_003_insider_value_ratio_63):
    return _base_universe_d3(icn_base_universe_d2_002_icn_003_insider_value_ratio_63, 2)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_002_icn_003_insider_value_ratio_63'] = {'inputs': ['icn_base_universe_d2_002_icn_003_insider_value_ratio_63'], 'func': icn_base_universe_d3_002_icn_003_insider_value_ratio_63}


def icn_base_universe_d3_003_icn_004_ceo_cfo_buy_weight_84(icn_base_universe_d2_003_icn_004_ceo_cfo_buy_weight_84):
    return _base_universe_d3(icn_base_universe_d2_003_icn_004_ceo_cfo_buy_weight_84, 3)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_003_icn_004_ceo_cfo_buy_weight_84'] = {'inputs': ['icn_base_universe_d2_003_icn_004_ceo_cfo_buy_weight_84'], 'func': icn_base_universe_d3_003_icn_004_ceo_cfo_buy_weight_84}


def icn_base_universe_d3_004_icn_006_insider_conviction_189(icn_base_universe_d2_004_icn_006_insider_conviction_189):
    return _base_universe_d3(icn_base_universe_d2_004_icn_006_insider_conviction_189, 4)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_004_icn_006_insider_conviction_189'] = {'inputs': ['icn_base_universe_d2_004_icn_006_insider_conviction_189'], 'func': icn_base_universe_d3_004_icn_006_insider_conviction_189}


def icn_base_universe_d3_005_icn_008_insider_buy_cluster_378(icn_base_universe_d2_005_icn_008_insider_buy_cluster_378):
    return _base_universe_d3(icn_base_universe_d2_005_icn_008_insider_buy_cluster_378, 5)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_005_icn_008_insider_buy_cluster_378'] = {'inputs': ['icn_base_universe_d2_005_icn_008_insider_buy_cluster_378'], 'func': icn_base_universe_d3_005_icn_008_insider_buy_cluster_378}


def icn_base_universe_d3_006_icn_009_insider_net_buy_ratio_504(icn_base_universe_d2_006_icn_009_insider_net_buy_ratio_504):
    return _base_universe_d3(icn_base_universe_d2_006_icn_009_insider_net_buy_ratio_504, 6)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_006_icn_009_insider_net_buy_ratio_504'] = {'inputs': ['icn_base_universe_d2_006_icn_009_insider_net_buy_ratio_504'], 'func': icn_base_universe_d3_006_icn_009_insider_net_buy_ratio_504}


def icn_base_universe_d3_007_icn_010_insider_value_ratio_756(icn_base_universe_d2_007_icn_010_insider_value_ratio_756):
    return _base_universe_d3(icn_base_universe_d2_007_icn_010_insider_value_ratio_756, 7)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_007_icn_010_insider_value_ratio_756'] = {'inputs': ['icn_base_universe_d2_007_icn_010_insider_value_ratio_756'], 'func': icn_base_universe_d3_007_icn_010_insider_value_ratio_756}


def icn_base_universe_d3_008_icn_011_ceo_cfo_buy_weight_1008(icn_base_universe_d2_008_icn_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d3(icn_base_universe_d2_008_icn_011_ceo_cfo_buy_weight_1008, 8)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_008_icn_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['icn_base_universe_d2_008_icn_011_ceo_cfo_buy_weight_1008'], 'func': icn_base_universe_d3_008_icn_011_ceo_cfo_buy_weight_1008}


def icn_base_universe_d3_009_icn_014_insider_silence_63(icn_base_universe_d2_009_icn_014_insider_silence_63):
    return _base_universe_d3(icn_base_universe_d2_009_icn_014_insider_silence_63, 9)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_009_icn_014_insider_silence_63'] = {'inputs': ['icn_base_universe_d2_009_icn_014_insider_silence_63'], 'func': icn_base_universe_d3_009_icn_014_insider_silence_63}


def icn_base_universe_d3_010_icn_015_insider_buy_cluster_252(icn_base_universe_d2_010_icn_015_insider_buy_cluster_252):
    return _base_universe_d3(icn_base_universe_d2_010_icn_015_insider_buy_cluster_252, 10)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_010_icn_015_insider_buy_cluster_252'] = {'inputs': ['icn_base_universe_d2_010_icn_015_insider_buy_cluster_252'], 'func': icn_base_universe_d3_010_icn_015_insider_buy_cluster_252}


def icn_base_universe_d3_011_icn_016_insider_net_buy_ratio_21(icn_base_universe_d2_011_icn_016_insider_net_buy_ratio_21):
    return _base_universe_d3(icn_base_universe_d2_011_icn_016_insider_net_buy_ratio_21, 11)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_011_icn_016_insider_net_buy_ratio_21'] = {'inputs': ['icn_base_universe_d2_011_icn_016_insider_net_buy_ratio_21'], 'func': icn_base_universe_d3_011_icn_016_insider_net_buy_ratio_21}


def icn_base_universe_d3_012_icn_017_insider_value_ratio_42(icn_base_universe_d2_012_icn_017_insider_value_ratio_42):
    return _base_universe_d3(icn_base_universe_d2_012_icn_017_insider_value_ratio_42, 12)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_012_icn_017_insider_value_ratio_42'] = {'inputs': ['icn_base_universe_d2_012_icn_017_insider_value_ratio_42'], 'func': icn_base_universe_d3_012_icn_017_insider_value_ratio_42}


def icn_base_universe_d3_013_icn_018_ceo_cfo_buy_weight_63(icn_base_universe_d2_013_icn_018_ceo_cfo_buy_weight_63):
    return _base_universe_d3(icn_base_universe_d2_013_icn_018_ceo_cfo_buy_weight_63, 13)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_013_icn_018_ceo_cfo_buy_weight_63'] = {'inputs': ['icn_base_universe_d2_013_icn_018_ceo_cfo_buy_weight_63'], 'func': icn_base_universe_d3_013_icn_018_ceo_cfo_buy_weight_63}


def icn_base_universe_d3_014_icn_020_insider_conviction_126(icn_base_universe_d2_014_icn_020_insider_conviction_126):
    return _base_universe_d3(icn_base_universe_d2_014_icn_020_insider_conviction_126, 14)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_014_icn_020_insider_conviction_126'] = {'inputs': ['icn_base_universe_d2_014_icn_020_insider_conviction_126'], 'func': icn_base_universe_d3_014_icn_020_insider_conviction_126}


def icn_base_universe_d3_015_icn_021_insider_silence_189(icn_base_universe_d2_015_icn_021_insider_silence_189):
    return _base_universe_d3(icn_base_universe_d2_015_icn_021_insider_silence_189, 15)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_015_icn_021_insider_silence_189'] = {'inputs': ['icn_base_universe_d2_015_icn_021_insider_silence_189'], 'func': icn_base_universe_d3_015_icn_021_insider_silence_189}


def icn_base_universe_d3_016_icn_023_insider_net_buy_ratio_378(icn_base_universe_d2_016_icn_023_insider_net_buy_ratio_378):
    return _base_universe_d3(icn_base_universe_d2_016_icn_023_insider_net_buy_ratio_378, 16)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_016_icn_023_insider_net_buy_ratio_378'] = {'inputs': ['icn_base_universe_d2_016_icn_023_insider_net_buy_ratio_378'], 'func': icn_base_universe_d3_016_icn_023_insider_net_buy_ratio_378}


def icn_base_universe_d3_017_icn_024_insider_value_ratio_504(icn_base_universe_d2_017_icn_024_insider_value_ratio_504):
    return _base_universe_d3(icn_base_universe_d2_017_icn_024_insider_value_ratio_504, 17)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_017_icn_024_insider_value_ratio_504'] = {'inputs': ['icn_base_universe_d2_017_icn_024_insider_value_ratio_504'], 'func': icn_base_universe_d3_017_icn_024_insider_value_ratio_504}


def icn_base_universe_d3_018_icn_027_insider_conviction_1260(icn_base_universe_d2_018_icn_027_insider_conviction_1260):
    return _base_universe_d3(icn_base_universe_d2_018_icn_027_insider_conviction_1260, 18)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_018_icn_027_insider_conviction_1260'] = {'inputs': ['icn_base_universe_d2_018_icn_027_insider_conviction_1260'], 'func': icn_base_universe_d3_018_icn_027_insider_conviction_1260}


def icn_base_universe_d3_019_icn_028_insider_silence_1512(icn_base_universe_d2_019_icn_028_insider_silence_1512):
    return _base_universe_d3(icn_base_universe_d2_019_icn_028_insider_silence_1512, 19)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_019_icn_028_insider_silence_1512'] = {'inputs': ['icn_base_universe_d2_019_icn_028_insider_silence_1512'], 'func': icn_base_universe_d3_019_icn_028_insider_silence_1512}


def icn_base_universe_d3_020_icn_029_insider_buy_cluster_63(icn_base_universe_d2_020_icn_029_insider_buy_cluster_63):
    return _base_universe_d3(icn_base_universe_d2_020_icn_029_insider_buy_cluster_63, 20)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_020_icn_029_insider_buy_cluster_63'] = {'inputs': ['icn_base_universe_d2_020_icn_029_insider_buy_cluster_63'], 'func': icn_base_universe_d3_020_icn_029_insider_buy_cluster_63}


def icn_base_universe_d3_021_icn_030_insider_net_buy_ratio_252(icn_base_universe_d2_021_icn_030_insider_net_buy_ratio_252):
    return _base_universe_d3(icn_base_universe_d2_021_icn_030_insider_net_buy_ratio_252, 21)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_021_icn_030_insider_net_buy_ratio_252'] = {'inputs': ['icn_base_universe_d2_021_icn_030_insider_net_buy_ratio_252'], 'func': icn_base_universe_d3_021_icn_030_insider_net_buy_ratio_252}


def icn_base_universe_d3_022_icn_031_insider_value_ratio_21(icn_base_universe_d2_022_icn_031_insider_value_ratio_21):
    return _base_universe_d3(icn_base_universe_d2_022_icn_031_insider_value_ratio_21, 22)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_022_icn_031_insider_value_ratio_21'] = {'inputs': ['icn_base_universe_d2_022_icn_031_insider_value_ratio_21'], 'func': icn_base_universe_d3_022_icn_031_insider_value_ratio_21}


def icn_base_universe_d3_023_icn_032_ceo_cfo_buy_weight_42(icn_base_universe_d2_023_icn_032_ceo_cfo_buy_weight_42):
    return _base_universe_d3(icn_base_universe_d2_023_icn_032_ceo_cfo_buy_weight_42, 23)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_023_icn_032_ceo_cfo_buy_weight_42'] = {'inputs': ['icn_base_universe_d2_023_icn_032_ceo_cfo_buy_weight_42'], 'func': icn_base_universe_d3_023_icn_032_ceo_cfo_buy_weight_42}


def icn_base_universe_d3_024_icn_034_insider_conviction_84(icn_base_universe_d2_024_icn_034_insider_conviction_84):
    return _base_universe_d3(icn_base_universe_d2_024_icn_034_insider_conviction_84, 24)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_024_icn_034_insider_conviction_84'] = {'inputs': ['icn_base_universe_d2_024_icn_034_insider_conviction_84'], 'func': icn_base_universe_d3_024_icn_034_insider_conviction_84}


def icn_base_universe_d3_025_icn_035_insider_silence_126(icn_base_universe_d2_025_icn_035_insider_silence_126):
    return _base_universe_d3(icn_base_universe_d2_025_icn_035_insider_silence_126, 25)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_025_icn_035_insider_silence_126'] = {'inputs': ['icn_base_universe_d2_025_icn_035_insider_silence_126'], 'func': icn_base_universe_d3_025_icn_035_insider_silence_126}


def icn_base_universe_d3_026_icn_036_insider_buy_cluster_189(icn_base_universe_d2_026_icn_036_insider_buy_cluster_189):
    return _base_universe_d3(icn_base_universe_d2_026_icn_036_insider_buy_cluster_189, 26)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_026_icn_036_insider_buy_cluster_189'] = {'inputs': ['icn_base_universe_d2_026_icn_036_insider_buy_cluster_189'], 'func': icn_base_universe_d3_026_icn_036_insider_buy_cluster_189}


def icn_base_universe_d3_027_icn_038_insider_value_ratio_378(icn_base_universe_d2_027_icn_038_insider_value_ratio_378):
    return _base_universe_d3(icn_base_universe_d2_027_icn_038_insider_value_ratio_378, 27)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_027_icn_038_insider_value_ratio_378'] = {'inputs': ['icn_base_universe_d2_027_icn_038_insider_value_ratio_378'], 'func': icn_base_universe_d3_027_icn_038_insider_value_ratio_378}


def icn_base_universe_d3_028_icn_039_ceo_cfo_buy_weight_504(icn_base_universe_d2_028_icn_039_ceo_cfo_buy_weight_504):
    return _base_universe_d3(icn_base_universe_d2_028_icn_039_ceo_cfo_buy_weight_504, 28)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_028_icn_039_ceo_cfo_buy_weight_504'] = {'inputs': ['icn_base_universe_d2_028_icn_039_ceo_cfo_buy_weight_504'], 'func': icn_base_universe_d3_028_icn_039_ceo_cfo_buy_weight_504}


def icn_base_universe_d3_029_icn_041_insider_conviction_1008(icn_base_universe_d2_029_icn_041_insider_conviction_1008):
    return _base_universe_d3(icn_base_universe_d2_029_icn_041_insider_conviction_1008, 29)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_029_icn_041_insider_conviction_1008'] = {'inputs': ['icn_base_universe_d2_029_icn_041_insider_conviction_1008'], 'func': icn_base_universe_d3_029_icn_041_insider_conviction_1008}


def icn_base_universe_d3_030_icn_042_insider_silence_1260(icn_base_universe_d2_030_icn_042_insider_silence_1260):
    return _base_universe_d3(icn_base_universe_d2_030_icn_042_insider_silence_1260, 30)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_030_icn_042_insider_silence_1260'] = {'inputs': ['icn_base_universe_d2_030_icn_042_insider_silence_1260'], 'func': icn_base_universe_d3_030_icn_042_insider_silence_1260}


def icn_base_universe_d3_031_icn_043_insider_buy_cluster_1512(icn_base_universe_d2_031_icn_043_insider_buy_cluster_1512):
    return _base_universe_d3(icn_base_universe_d2_031_icn_043_insider_buy_cluster_1512, 31)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_031_icn_043_insider_buy_cluster_1512'] = {'inputs': ['icn_base_universe_d2_031_icn_043_insider_buy_cluster_1512'], 'func': icn_base_universe_d3_031_icn_043_insider_buy_cluster_1512}


def icn_base_universe_d3_032_icn_044_insider_net_buy_ratio_63(icn_base_universe_d2_032_icn_044_insider_net_buy_ratio_63):
    return _base_universe_d3(icn_base_universe_d2_032_icn_044_insider_net_buy_ratio_63, 32)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_032_icn_044_insider_net_buy_ratio_63'] = {'inputs': ['icn_base_universe_d2_032_icn_044_insider_net_buy_ratio_63'], 'func': icn_base_universe_d3_032_icn_044_insider_net_buy_ratio_63}


def icn_base_universe_d3_033_icn_045_insider_value_ratio_252(icn_base_universe_d2_033_icn_045_insider_value_ratio_252):
    return _base_universe_d3(icn_base_universe_d2_033_icn_045_insider_value_ratio_252, 33)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_033_icn_045_insider_value_ratio_252'] = {'inputs': ['icn_base_universe_d2_033_icn_045_insider_value_ratio_252'], 'func': icn_base_universe_d3_033_icn_045_insider_value_ratio_252}


def icn_base_universe_d3_034_icn_046_ceo_cfo_buy_weight_21(icn_base_universe_d2_034_icn_046_ceo_cfo_buy_weight_21):
    return _base_universe_d3(icn_base_universe_d2_034_icn_046_ceo_cfo_buy_weight_21, 34)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_034_icn_046_ceo_cfo_buy_weight_21'] = {'inputs': ['icn_base_universe_d2_034_icn_046_ceo_cfo_buy_weight_21'], 'func': icn_base_universe_d3_034_icn_046_ceo_cfo_buy_weight_21}


def icn_base_universe_d3_035_icn_048_insider_conviction_63(icn_base_universe_d2_035_icn_048_insider_conviction_63):
    return _base_universe_d3(icn_base_universe_d2_035_icn_048_insider_conviction_63, 35)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_035_icn_048_insider_conviction_63'] = {'inputs': ['icn_base_universe_d2_035_icn_048_insider_conviction_63'], 'func': icn_base_universe_d3_035_icn_048_insider_conviction_63}


def icn_base_universe_d3_036_icn_049_insider_silence_84(icn_base_universe_d2_036_icn_049_insider_silence_84):
    return _base_universe_d3(icn_base_universe_d2_036_icn_049_insider_silence_84, 36)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_036_icn_049_insider_silence_84'] = {'inputs': ['icn_base_universe_d2_036_icn_049_insider_silence_84'], 'func': icn_base_universe_d3_036_icn_049_insider_silence_84}


def icn_base_universe_d3_037_icn_050_insider_buy_cluster_126(icn_base_universe_d2_037_icn_050_insider_buy_cluster_126):
    return _base_universe_d3(icn_base_universe_d2_037_icn_050_insider_buy_cluster_126, 37)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_037_icn_050_insider_buy_cluster_126'] = {'inputs': ['icn_base_universe_d2_037_icn_050_insider_buy_cluster_126'], 'func': icn_base_universe_d3_037_icn_050_insider_buy_cluster_126}


def icn_base_universe_d3_038_icn_051_insider_net_buy_ratio_189(icn_base_universe_d2_038_icn_051_insider_net_buy_ratio_189):
    return _base_universe_d3(icn_base_universe_d2_038_icn_051_insider_net_buy_ratio_189, 38)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_038_icn_051_insider_net_buy_ratio_189'] = {'inputs': ['icn_base_universe_d2_038_icn_051_insider_net_buy_ratio_189'], 'func': icn_base_universe_d3_038_icn_051_insider_net_buy_ratio_189}


def icn_base_universe_d3_039_icn_053_ceo_cfo_buy_weight_378(icn_base_universe_d2_039_icn_053_ceo_cfo_buy_weight_378):
    return _base_universe_d3(icn_base_universe_d2_039_icn_053_ceo_cfo_buy_weight_378, 39)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_039_icn_053_ceo_cfo_buy_weight_378'] = {'inputs': ['icn_base_universe_d2_039_icn_053_ceo_cfo_buy_weight_378'], 'func': icn_base_universe_d3_039_icn_053_ceo_cfo_buy_weight_378}


def icn_base_universe_d3_040_icn_055_insider_conviction_756(icn_base_universe_d2_040_icn_055_insider_conviction_756):
    return _base_universe_d3(icn_base_universe_d2_040_icn_055_insider_conviction_756, 40)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_040_icn_055_insider_conviction_756'] = {'inputs': ['icn_base_universe_d2_040_icn_055_insider_conviction_756'], 'func': icn_base_universe_d3_040_icn_055_insider_conviction_756}


def icn_base_universe_d3_041_icn_056_insider_silence_1008(icn_base_universe_d2_041_icn_056_insider_silence_1008):
    return _base_universe_d3(icn_base_universe_d2_041_icn_056_insider_silence_1008, 41)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_041_icn_056_insider_silence_1008'] = {'inputs': ['icn_base_universe_d2_041_icn_056_insider_silence_1008'], 'func': icn_base_universe_d3_041_icn_056_insider_silence_1008}


def icn_base_universe_d3_042_icn_057_insider_buy_cluster_1260(icn_base_universe_d2_042_icn_057_insider_buy_cluster_1260):
    return _base_universe_d3(icn_base_universe_d2_042_icn_057_insider_buy_cluster_1260, 42)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_042_icn_057_insider_buy_cluster_1260'] = {'inputs': ['icn_base_universe_d2_042_icn_057_insider_buy_cluster_1260'], 'func': icn_base_universe_d3_042_icn_057_insider_buy_cluster_1260}


def icn_base_universe_d3_043_icn_058_insider_net_buy_ratio_1512(icn_base_universe_d2_043_icn_058_insider_net_buy_ratio_1512):
    return _base_universe_d3(icn_base_universe_d2_043_icn_058_insider_net_buy_ratio_1512, 43)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_043_icn_058_insider_net_buy_ratio_1512'] = {'inputs': ['icn_base_universe_d2_043_icn_058_insider_net_buy_ratio_1512'], 'func': icn_base_universe_d3_043_icn_058_insider_net_buy_ratio_1512}


def icn_base_universe_d3_044_icn_060_ceo_cfo_buy_weight_252(icn_base_universe_d2_044_icn_060_ceo_cfo_buy_weight_252):
    return _base_universe_d3(icn_base_universe_d2_044_icn_060_ceo_cfo_buy_weight_252, 44)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_044_icn_060_ceo_cfo_buy_weight_252'] = {'inputs': ['icn_base_universe_d2_044_icn_060_ceo_cfo_buy_weight_252'], 'func': icn_base_universe_d3_044_icn_060_ceo_cfo_buy_weight_252}


def icn_base_universe_d3_045_icn_062_insider_conviction_42(icn_base_universe_d2_045_icn_062_insider_conviction_42):
    return _base_universe_d3(icn_base_universe_d2_045_icn_062_insider_conviction_42, 45)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_045_icn_062_insider_conviction_42'] = {'inputs': ['icn_base_universe_d2_045_icn_062_insider_conviction_42'], 'func': icn_base_universe_d3_045_icn_062_insider_conviction_42}


def icn_base_universe_d3_046_icn_064_insider_buy_cluster_84(icn_base_universe_d2_046_icn_064_insider_buy_cluster_84):
    return _base_universe_d3(icn_base_universe_d2_046_icn_064_insider_buy_cluster_84, 46)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_046_icn_064_insider_buy_cluster_84'] = {'inputs': ['icn_base_universe_d2_046_icn_064_insider_buy_cluster_84'], 'func': icn_base_universe_d3_046_icn_064_insider_buy_cluster_84}


def icn_base_universe_d3_047_icn_065_insider_net_buy_ratio_126(icn_base_universe_d2_047_icn_065_insider_net_buy_ratio_126):
    return _base_universe_d3(icn_base_universe_d2_047_icn_065_insider_net_buy_ratio_126, 47)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_047_icn_065_insider_net_buy_ratio_126'] = {'inputs': ['icn_base_universe_d2_047_icn_065_insider_net_buy_ratio_126'], 'func': icn_base_universe_d3_047_icn_065_insider_net_buy_ratio_126}


def icn_base_universe_d3_048_icn_066_insider_value_ratio_189(icn_base_universe_d2_048_icn_066_insider_value_ratio_189):
    return _base_universe_d3(icn_base_universe_d2_048_icn_066_insider_value_ratio_189, 48)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_048_icn_066_insider_value_ratio_189'] = {'inputs': ['icn_base_universe_d2_048_icn_066_insider_value_ratio_189'], 'func': icn_base_universe_d3_048_icn_066_insider_value_ratio_189}


def icn_base_universe_d3_049_icn_069_insider_conviction_504(icn_base_universe_d2_049_icn_069_insider_conviction_504):
    return _base_universe_d3(icn_base_universe_d2_049_icn_069_insider_conviction_504, 49)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_049_icn_069_insider_conviction_504'] = {'inputs': ['icn_base_universe_d2_049_icn_069_insider_conviction_504'], 'func': icn_base_universe_d3_049_icn_069_insider_conviction_504}


def icn_base_universe_d3_050_icn_070_insider_silence_756(icn_base_universe_d2_050_icn_070_insider_silence_756):
    return _base_universe_d3(icn_base_universe_d2_050_icn_070_insider_silence_756, 50)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_050_icn_070_insider_silence_756'] = {'inputs': ['icn_base_universe_d2_050_icn_070_insider_silence_756'], 'func': icn_base_universe_d3_050_icn_070_insider_silence_756}


def icn_base_universe_d3_051_icn_071_insider_buy_cluster_1008(icn_base_universe_d2_051_icn_071_insider_buy_cluster_1008):
    return _base_universe_d3(icn_base_universe_d2_051_icn_071_insider_buy_cluster_1008, 51)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_051_icn_071_insider_buy_cluster_1008'] = {'inputs': ['icn_base_universe_d2_051_icn_071_insider_buy_cluster_1008'], 'func': icn_base_universe_d3_051_icn_071_insider_buy_cluster_1008}


def icn_base_universe_d3_052_icn_072_insider_net_buy_ratio_1260(icn_base_universe_d2_052_icn_072_insider_net_buy_ratio_1260):
    return _base_universe_d3(icn_base_universe_d2_052_icn_072_insider_net_buy_ratio_1260, 52)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_052_icn_072_insider_net_buy_ratio_1260'] = {'inputs': ['icn_base_universe_d2_052_icn_072_insider_net_buy_ratio_1260'], 'func': icn_base_universe_d3_052_icn_072_insider_net_buy_ratio_1260}


def icn_base_universe_d3_053_icn_073_insider_value_ratio_1512(icn_base_universe_d2_053_icn_073_insider_value_ratio_1512):
    return _base_universe_d3(icn_base_universe_d2_053_icn_073_insider_value_ratio_1512, 53)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_053_icn_073_insider_value_ratio_1512'] = {'inputs': ['icn_base_universe_d2_053_icn_073_insider_value_ratio_1512'], 'func': icn_base_universe_d3_053_icn_073_insider_value_ratio_1512}


def icn_base_universe_d3_054_icn_basefill_005(icn_base_universe_d2_054_icn_basefill_005):
    return _base_universe_d3(icn_base_universe_d2_054_icn_basefill_005, 54)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_054_icn_basefill_005'] = {'inputs': ['icn_base_universe_d2_054_icn_basefill_005'], 'func': icn_base_universe_d3_054_icn_basefill_005}


def icn_base_universe_d3_055_icn_basefill_012(icn_base_universe_d2_055_icn_basefill_012):
    return _base_universe_d3(icn_base_universe_d2_055_icn_basefill_012, 55)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_055_icn_basefill_012'] = {'inputs': ['icn_base_universe_d2_055_icn_basefill_012'], 'func': icn_base_universe_d3_055_icn_basefill_012}


def icn_base_universe_d3_056_icn_basefill_019(icn_base_universe_d2_056_icn_basefill_019):
    return _base_universe_d3(icn_base_universe_d2_056_icn_basefill_019, 56)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_056_icn_basefill_019'] = {'inputs': ['icn_base_universe_d2_056_icn_basefill_019'], 'func': icn_base_universe_d3_056_icn_basefill_019}


def icn_base_universe_d3_057_icn_basefill_022(icn_base_universe_d2_057_icn_basefill_022):
    return _base_universe_d3(icn_base_universe_d2_057_icn_basefill_022, 57)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_057_icn_basefill_022'] = {'inputs': ['icn_base_universe_d2_057_icn_basefill_022'], 'func': icn_base_universe_d3_057_icn_basefill_022}


def icn_base_universe_d3_058_icn_basefill_026(icn_base_universe_d2_058_icn_basefill_026):
    return _base_universe_d3(icn_base_universe_d2_058_icn_basefill_026, 58)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_058_icn_basefill_026'] = {'inputs': ['icn_base_universe_d2_058_icn_basefill_026'], 'func': icn_base_universe_d3_058_icn_basefill_026}


def icn_base_universe_d3_059_icn_basefill_033(icn_base_universe_d2_059_icn_basefill_033):
    return _base_universe_d3(icn_base_universe_d2_059_icn_basefill_033, 59)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_059_icn_basefill_033'] = {'inputs': ['icn_base_universe_d2_059_icn_basefill_033'], 'func': icn_base_universe_d3_059_icn_basefill_033}


def icn_base_universe_d3_060_icn_basefill_037(icn_base_universe_d2_060_icn_basefill_037):
    return _base_universe_d3(icn_base_universe_d2_060_icn_basefill_037, 60)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_060_icn_basefill_037'] = {'inputs': ['icn_base_universe_d2_060_icn_basefill_037'], 'func': icn_base_universe_d3_060_icn_basefill_037}


def icn_base_universe_d3_061_icn_basefill_040(icn_base_universe_d2_061_icn_basefill_040):
    return _base_universe_d3(icn_base_universe_d2_061_icn_basefill_040, 61)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_061_icn_basefill_040'] = {'inputs': ['icn_base_universe_d2_061_icn_basefill_040'], 'func': icn_base_universe_d3_061_icn_basefill_040}


def icn_base_universe_d3_062_icn_basefill_047(icn_base_universe_d2_062_icn_basefill_047):
    return _base_universe_d3(icn_base_universe_d2_062_icn_basefill_047, 62)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_062_icn_basefill_047'] = {'inputs': ['icn_base_universe_d2_062_icn_basefill_047'], 'func': icn_base_universe_d3_062_icn_basefill_047}


def icn_base_universe_d3_063_icn_basefill_052(icn_base_universe_d2_063_icn_basefill_052):
    return _base_universe_d3(icn_base_universe_d2_063_icn_basefill_052, 63)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_063_icn_basefill_052'] = {'inputs': ['icn_base_universe_d2_063_icn_basefill_052'], 'func': icn_base_universe_d3_063_icn_basefill_052}


def icn_base_universe_d3_064_icn_basefill_054(icn_base_universe_d2_064_icn_basefill_054):
    return _base_universe_d3(icn_base_universe_d2_064_icn_basefill_054, 64)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_064_icn_basefill_054'] = {'inputs': ['icn_base_universe_d2_064_icn_basefill_054'], 'func': icn_base_universe_d3_064_icn_basefill_054}


def icn_base_universe_d3_065_icn_basefill_059(icn_base_universe_d2_065_icn_basefill_059):
    return _base_universe_d3(icn_base_universe_d2_065_icn_basefill_059, 65)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_065_icn_basefill_059'] = {'inputs': ['icn_base_universe_d2_065_icn_basefill_059'], 'func': icn_base_universe_d3_065_icn_basefill_059}


def icn_base_universe_d3_066_icn_basefill_061(icn_base_universe_d2_066_icn_basefill_061):
    return _base_universe_d3(icn_base_universe_d2_066_icn_basefill_061, 66)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_066_icn_basefill_061'] = {'inputs': ['icn_base_universe_d2_066_icn_basefill_061'], 'func': icn_base_universe_d3_066_icn_basefill_061}


def icn_base_universe_d3_067_icn_basefill_063(icn_base_universe_d2_067_icn_basefill_063):
    return _base_universe_d3(icn_base_universe_d2_067_icn_basefill_063, 67)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_067_icn_basefill_063'] = {'inputs': ['icn_base_universe_d2_067_icn_basefill_063'], 'func': icn_base_universe_d3_067_icn_basefill_063}


def icn_base_universe_d3_068_icn_basefill_067(icn_base_universe_d2_068_icn_basefill_067):
    return _base_universe_d3(icn_base_universe_d2_068_icn_basefill_067, 68)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_068_icn_basefill_067'] = {'inputs': ['icn_base_universe_d2_068_icn_basefill_067'], 'func': icn_base_universe_d3_068_icn_basefill_067}


def icn_base_universe_d3_069_icn_basefill_068(icn_base_universe_d2_069_icn_basefill_068):
    return _base_universe_d3(icn_base_universe_d2_069_icn_basefill_068, 69)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_069_icn_basefill_068'] = {'inputs': ['icn_base_universe_d2_069_icn_basefill_068'], 'func': icn_base_universe_d3_069_icn_basefill_068}


def icn_base_universe_d3_070_icn_basefill_074(icn_base_universe_d2_070_icn_basefill_074):
    return _base_universe_d3(icn_base_universe_d2_070_icn_basefill_074, 70)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_070_icn_basefill_074'] = {'inputs': ['icn_base_universe_d2_070_icn_basefill_074'], 'func': icn_base_universe_d3_070_icn_basefill_074}


def icn_base_universe_d3_071_icn_basefill_075(icn_base_universe_d2_071_icn_basefill_075):
    return _base_universe_d3(icn_base_universe_d2_071_icn_basefill_075, 71)
ICN_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['icn_base_universe_d3_071_icn_basefill_075'] = {'inputs': ['icn_base_universe_d2_071_icn_basefill_075'], 'func': icn_base_universe_d3_071_icn_basefill_075}

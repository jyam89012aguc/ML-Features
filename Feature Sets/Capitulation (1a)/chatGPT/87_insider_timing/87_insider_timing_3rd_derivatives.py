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



def itm_176_itm_001_insider_buy_cluster_21_accel_1(itm_151_itm_001_insider_buy_cluster_21_roc_1):
    feature = _s(itm_151_itm_001_insider_buy_cluster_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def itm_177_itm_007_insider_silence_252_accel_42(itm_152_itm_007_insider_silence_252_roc_42):
    feature = _s(itm_152_itm_007_insider_silence_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def itm_178_itm_013_insider_conviction_1512_accel_126(itm_153_itm_013_insider_conviction_1512_roc_126):
    feature = _s(itm_153_itm_013_insider_conviction_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def itm_179_itm_019_insider_activity_accel_1_accel_378(itm_154_itm_019_insider_activity_accel_1_roc_378):
    feature = _s(itm_154_itm_019_insider_activity_accel_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def itm_180_itm_025_ceo_cfo_buy_weight_756_accel_4(itm_155_itm_025_ceo_cfo_buy_weight_756_roc_4):
    feature = _s(itm_155_itm_025_ceo_cfo_buy_weight_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSIDER_TIMING_REGISTRY_3RD_DERIVATIVES = {
    'itm_176_itm_001_insider_buy_cluster_21_accel_1': {'inputs': ['itm_151_itm_001_insider_buy_cluster_21_roc_1'], 'func': itm_176_itm_001_insider_buy_cluster_21_accel_1},
    'itm_177_itm_007_insider_silence_252_accel_42': {'inputs': ['itm_152_itm_007_insider_silence_252_roc_42'], 'func': itm_177_itm_007_insider_silence_252_accel_42},
    'itm_178_itm_013_insider_conviction_1512_accel_126': {'inputs': ['itm_153_itm_013_insider_conviction_1512_roc_126'], 'func': itm_178_itm_013_insider_conviction_1512_accel_126},
    'itm_179_itm_019_insider_activity_accel_1_accel_378': {'inputs': ['itm_154_itm_019_insider_activity_accel_1_roc_378'], 'func': itm_179_itm_019_insider_activity_accel_1_accel_378},
    'itm_180_itm_025_ceo_cfo_buy_weight_756_accel_4': {'inputs': ['itm_155_itm_025_ceo_cfo_buy_weight_756_roc_4'], 'func': itm_180_itm_025_ceo_cfo_buy_weight_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def it_replacement_d3_001(it_replacement_d2_001):
    feature = _clean(it_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_001'] = {'inputs': ['it_replacement_d2_001'], 'func': it_replacement_d3_001}


def it_replacement_d3_002(it_replacement_d2_002):
    feature = _clean(it_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_002'] = {'inputs': ['it_replacement_d2_002'], 'func': it_replacement_d3_002}


def it_replacement_d3_003(it_replacement_d2_003):
    feature = _clean(it_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_003'] = {'inputs': ['it_replacement_d2_003'], 'func': it_replacement_d3_003}


def it_replacement_d3_004(it_replacement_d2_004):
    feature = _clean(it_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_004'] = {'inputs': ['it_replacement_d2_004'], 'func': it_replacement_d3_004}


def it_replacement_d3_005(it_replacement_d2_005):
    feature = _clean(it_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_005'] = {'inputs': ['it_replacement_d2_005'], 'func': it_replacement_d3_005}


def it_replacement_d3_006(it_replacement_d2_006):
    feature = _clean(it_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_006'] = {'inputs': ['it_replacement_d2_006'], 'func': it_replacement_d3_006}


def it_replacement_d3_007(it_replacement_d2_007):
    feature = _clean(it_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_007'] = {'inputs': ['it_replacement_d2_007'], 'func': it_replacement_d3_007}


def it_replacement_d3_008(it_replacement_d2_008):
    feature = _clean(it_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_008'] = {'inputs': ['it_replacement_d2_008'], 'func': it_replacement_d3_008}


def it_replacement_d3_009(it_replacement_d2_009):
    feature = _clean(it_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_009'] = {'inputs': ['it_replacement_d2_009'], 'func': it_replacement_d3_009}


def it_replacement_d3_010(it_replacement_d2_010):
    feature = _clean(it_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_010'] = {'inputs': ['it_replacement_d2_010'], 'func': it_replacement_d3_010}


def it_replacement_d3_011(it_replacement_d2_011):
    feature = _clean(it_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_011'] = {'inputs': ['it_replacement_d2_011'], 'func': it_replacement_d3_011}


def it_replacement_d3_012(it_replacement_d2_012):
    feature = _clean(it_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_012'] = {'inputs': ['it_replacement_d2_012'], 'func': it_replacement_d3_012}


def it_replacement_d3_013(it_replacement_d2_013):
    feature = _clean(it_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_013'] = {'inputs': ['it_replacement_d2_013'], 'func': it_replacement_d3_013}


def it_replacement_d3_014(it_replacement_d2_014):
    feature = _clean(it_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_014'] = {'inputs': ['it_replacement_d2_014'], 'func': it_replacement_d3_014}


def it_replacement_d3_015(it_replacement_d2_015):
    feature = _clean(it_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_015'] = {'inputs': ['it_replacement_d2_015'], 'func': it_replacement_d3_015}


def it_replacement_d3_016(it_replacement_d2_016):
    feature = _clean(it_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_016'] = {'inputs': ['it_replacement_d2_016'], 'func': it_replacement_d3_016}


def it_replacement_d3_017(it_replacement_d2_017):
    feature = _clean(it_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_017'] = {'inputs': ['it_replacement_d2_017'], 'func': it_replacement_d3_017}


def it_replacement_d3_018(it_replacement_d2_018):
    feature = _clean(it_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_018'] = {'inputs': ['it_replacement_d2_018'], 'func': it_replacement_d3_018}


def it_replacement_d3_019(it_replacement_d2_019):
    feature = _clean(it_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_019'] = {'inputs': ['it_replacement_d2_019'], 'func': it_replacement_d3_019}


def it_replacement_d3_020(it_replacement_d2_020):
    feature = _clean(it_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_020'] = {'inputs': ['it_replacement_d2_020'], 'func': it_replacement_d3_020}


def it_replacement_d3_021(it_replacement_d2_021):
    feature = _clean(it_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_021'] = {'inputs': ['it_replacement_d2_021'], 'func': it_replacement_d3_021}


def it_replacement_d3_022(it_replacement_d2_022):
    feature = _clean(it_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_022'] = {'inputs': ['it_replacement_d2_022'], 'func': it_replacement_d3_022}


def it_replacement_d3_023(it_replacement_d2_023):
    feature = _clean(it_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_023'] = {'inputs': ['it_replacement_d2_023'], 'func': it_replacement_d3_023}


def it_replacement_d3_024(it_replacement_d2_024):
    feature = _clean(it_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_024'] = {'inputs': ['it_replacement_d2_024'], 'func': it_replacement_d3_024}


def it_replacement_d3_025(it_replacement_d2_025):
    feature = _clean(it_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_025'] = {'inputs': ['it_replacement_d2_025'], 'func': it_replacement_d3_025}


def it_replacement_d3_026(it_replacement_d2_026):
    feature = _clean(it_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_026'] = {'inputs': ['it_replacement_d2_026'], 'func': it_replacement_d3_026}


def it_replacement_d3_027(it_replacement_d2_027):
    feature = _clean(it_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_027'] = {'inputs': ['it_replacement_d2_027'], 'func': it_replacement_d3_027}


def it_replacement_d3_028(it_replacement_d2_028):
    feature = _clean(it_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_028'] = {'inputs': ['it_replacement_d2_028'], 'func': it_replacement_d3_028}


def it_replacement_d3_029(it_replacement_d2_029):
    feature = _clean(it_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_029'] = {'inputs': ['it_replacement_d2_029'], 'func': it_replacement_d3_029}


def it_replacement_d3_030(it_replacement_d2_030):
    feature = _clean(it_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_030'] = {'inputs': ['it_replacement_d2_030'], 'func': it_replacement_d3_030}


def it_replacement_d3_031(it_replacement_d2_031):
    feature = _clean(it_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_031'] = {'inputs': ['it_replacement_d2_031'], 'func': it_replacement_d3_031}


def it_replacement_d3_032(it_replacement_d2_032):
    feature = _clean(it_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_032'] = {'inputs': ['it_replacement_d2_032'], 'func': it_replacement_d3_032}


def it_replacement_d3_033(it_replacement_d2_033):
    feature = _clean(it_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_033'] = {'inputs': ['it_replacement_d2_033'], 'func': it_replacement_d3_033}


def it_replacement_d3_034(it_replacement_d2_034):
    feature = _clean(it_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_034'] = {'inputs': ['it_replacement_d2_034'], 'func': it_replacement_d3_034}


def it_replacement_d3_035(it_replacement_d2_035):
    feature = _clean(it_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_035'] = {'inputs': ['it_replacement_d2_035'], 'func': it_replacement_d3_035}


def it_replacement_d3_036(it_replacement_d2_036):
    feature = _clean(it_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_036'] = {'inputs': ['it_replacement_d2_036'], 'func': it_replacement_d3_036}


def it_replacement_d3_037(it_replacement_d2_037):
    feature = _clean(it_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_037'] = {'inputs': ['it_replacement_d2_037'], 'func': it_replacement_d3_037}


def it_replacement_d3_038(it_replacement_d2_038):
    feature = _clean(it_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_038'] = {'inputs': ['it_replacement_d2_038'], 'func': it_replacement_d3_038}


def it_replacement_d3_039(it_replacement_d2_039):
    feature = _clean(it_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_039'] = {'inputs': ['it_replacement_d2_039'], 'func': it_replacement_d3_039}


def it_replacement_d3_040(it_replacement_d2_040):
    feature = _clean(it_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_040'] = {'inputs': ['it_replacement_d2_040'], 'func': it_replacement_d3_040}


def it_replacement_d3_041(it_replacement_d2_041):
    feature = _clean(it_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_041'] = {'inputs': ['it_replacement_d2_041'], 'func': it_replacement_d3_041}


def it_replacement_d3_042(it_replacement_d2_042):
    feature = _clean(it_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_042'] = {'inputs': ['it_replacement_d2_042'], 'func': it_replacement_d3_042}


def it_replacement_d3_043(it_replacement_d2_043):
    feature = _clean(it_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_043'] = {'inputs': ['it_replacement_d2_043'], 'func': it_replacement_d3_043}


def it_replacement_d3_044(it_replacement_d2_044):
    feature = _clean(it_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_044'] = {'inputs': ['it_replacement_d2_044'], 'func': it_replacement_d3_044}


def it_replacement_d3_045(it_replacement_d2_045):
    feature = _clean(it_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_045'] = {'inputs': ['it_replacement_d2_045'], 'func': it_replacement_d3_045}


def it_replacement_d3_046(it_replacement_d2_046):
    feature = _clean(it_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_046'] = {'inputs': ['it_replacement_d2_046'], 'func': it_replacement_d3_046}


def it_replacement_d3_047(it_replacement_d2_047):
    feature = _clean(it_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_047'] = {'inputs': ['it_replacement_d2_047'], 'func': it_replacement_d3_047}


def it_replacement_d3_048(it_replacement_d2_048):
    feature = _clean(it_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_048'] = {'inputs': ['it_replacement_d2_048'], 'func': it_replacement_d3_048}


def it_replacement_d3_049(it_replacement_d2_049):
    feature = _clean(it_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_049'] = {'inputs': ['it_replacement_d2_049'], 'func': it_replacement_d3_049}


def it_replacement_d3_050(it_replacement_d2_050):
    feature = _clean(it_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_050'] = {'inputs': ['it_replacement_d2_050'], 'func': it_replacement_d3_050}


def it_replacement_d3_051(it_replacement_d2_051):
    feature = _clean(it_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_051'] = {'inputs': ['it_replacement_d2_051'], 'func': it_replacement_d3_051}


def it_replacement_d3_052(it_replacement_d2_052):
    feature = _clean(it_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_052'] = {'inputs': ['it_replacement_d2_052'], 'func': it_replacement_d3_052}


def it_replacement_d3_053(it_replacement_d2_053):
    feature = _clean(it_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_053'] = {'inputs': ['it_replacement_d2_053'], 'func': it_replacement_d3_053}


def it_replacement_d3_054(it_replacement_d2_054):
    feature = _clean(it_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_054'] = {'inputs': ['it_replacement_d2_054'], 'func': it_replacement_d3_054}


def it_replacement_d3_055(it_replacement_d2_055):
    feature = _clean(it_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_055'] = {'inputs': ['it_replacement_d2_055'], 'func': it_replacement_d3_055}


def it_replacement_d3_056(it_replacement_d2_056):
    feature = _clean(it_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_056'] = {'inputs': ['it_replacement_d2_056'], 'func': it_replacement_d3_056}


def it_replacement_d3_057(it_replacement_d2_057):
    feature = _clean(it_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_057'] = {'inputs': ['it_replacement_d2_057'], 'func': it_replacement_d3_057}


def it_replacement_d3_058(it_replacement_d2_058):
    feature = _clean(it_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_058'] = {'inputs': ['it_replacement_d2_058'], 'func': it_replacement_d3_058}


def it_replacement_d3_059(it_replacement_d2_059):
    feature = _clean(it_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_059'] = {'inputs': ['it_replacement_d2_059'], 'func': it_replacement_d3_059}


def it_replacement_d3_060(it_replacement_d2_060):
    feature = _clean(it_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_060'] = {'inputs': ['it_replacement_d2_060'], 'func': it_replacement_d3_060}


def it_replacement_d3_061(it_replacement_d2_061):
    feature = _clean(it_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_061'] = {'inputs': ['it_replacement_d2_061'], 'func': it_replacement_d3_061}


def it_replacement_d3_062(it_replacement_d2_062):
    feature = _clean(it_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_062'] = {'inputs': ['it_replacement_d2_062'], 'func': it_replacement_d3_062}


def it_replacement_d3_063(it_replacement_d2_063):
    feature = _clean(it_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_063'] = {'inputs': ['it_replacement_d2_063'], 'func': it_replacement_d3_063}


def it_replacement_d3_064(it_replacement_d2_064):
    feature = _clean(it_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_064'] = {'inputs': ['it_replacement_d2_064'], 'func': it_replacement_d3_064}


def it_replacement_d3_065(it_replacement_d2_065):
    feature = _clean(it_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_065'] = {'inputs': ['it_replacement_d2_065'], 'func': it_replacement_d3_065}


def it_replacement_d3_066(it_replacement_d2_066):
    feature = _clean(it_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_066'] = {'inputs': ['it_replacement_d2_066'], 'func': it_replacement_d3_066}


def it_replacement_d3_067(it_replacement_d2_067):
    feature = _clean(it_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_067'] = {'inputs': ['it_replacement_d2_067'], 'func': it_replacement_d3_067}


def it_replacement_d3_068(it_replacement_d2_068):
    feature = _clean(it_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_068'] = {'inputs': ['it_replacement_d2_068'], 'func': it_replacement_d3_068}


def it_replacement_d3_069(it_replacement_d2_069):
    feature = _clean(it_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_069'] = {'inputs': ['it_replacement_d2_069'], 'func': it_replacement_d3_069}


def it_replacement_d3_070(it_replacement_d2_070):
    feature = _clean(it_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_070'] = {'inputs': ['it_replacement_d2_070'], 'func': it_replacement_d3_070}


def it_replacement_d3_071(it_replacement_d2_071):
    feature = _clean(it_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_071'] = {'inputs': ['it_replacement_d2_071'], 'func': it_replacement_d3_071}


def it_replacement_d3_072(it_replacement_d2_072):
    feature = _clean(it_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_072'] = {'inputs': ['it_replacement_d2_072'], 'func': it_replacement_d3_072}


def it_replacement_d3_073(it_replacement_d2_073):
    feature = _clean(it_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_073'] = {'inputs': ['it_replacement_d2_073'], 'func': it_replacement_d3_073}


def it_replacement_d3_074(it_replacement_d2_074):
    feature = _clean(it_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_074'] = {'inputs': ['it_replacement_d2_074'], 'func': it_replacement_d3_074}


def it_replacement_d3_075(it_replacement_d2_075):
    feature = _clean(it_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_075'] = {'inputs': ['it_replacement_d2_075'], 'func': it_replacement_d3_075}


def it_replacement_d3_076(it_replacement_d2_076):
    feature = _clean(it_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_076'] = {'inputs': ['it_replacement_d2_076'], 'func': it_replacement_d3_076}


def it_replacement_d3_077(it_replacement_d2_077):
    feature = _clean(it_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_077'] = {'inputs': ['it_replacement_d2_077'], 'func': it_replacement_d3_077}


def it_replacement_d3_078(it_replacement_d2_078):
    feature = _clean(it_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_078'] = {'inputs': ['it_replacement_d2_078'], 'func': it_replacement_d3_078}


def it_replacement_d3_079(it_replacement_d2_079):
    feature = _clean(it_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_079'] = {'inputs': ['it_replacement_d2_079'], 'func': it_replacement_d3_079}


def it_replacement_d3_080(it_replacement_d2_080):
    feature = _clean(it_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_080'] = {'inputs': ['it_replacement_d2_080'], 'func': it_replacement_d3_080}


def it_replacement_d3_081(it_replacement_d2_081):
    feature = _clean(it_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_081'] = {'inputs': ['it_replacement_d2_081'], 'func': it_replacement_d3_081}


def it_replacement_d3_082(it_replacement_d2_082):
    feature = _clean(it_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_082'] = {'inputs': ['it_replacement_d2_082'], 'func': it_replacement_d3_082}


def it_replacement_d3_083(it_replacement_d2_083):
    feature = _clean(it_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_083'] = {'inputs': ['it_replacement_d2_083'], 'func': it_replacement_d3_083}


def it_replacement_d3_084(it_replacement_d2_084):
    feature = _clean(it_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_084'] = {'inputs': ['it_replacement_d2_084'], 'func': it_replacement_d3_084}


def it_replacement_d3_085(it_replacement_d2_085):
    feature = _clean(it_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_085'] = {'inputs': ['it_replacement_d2_085'], 'func': it_replacement_d3_085}


def it_replacement_d3_086(it_replacement_d2_086):
    feature = _clean(it_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_086'] = {'inputs': ['it_replacement_d2_086'], 'func': it_replacement_d3_086}


def it_replacement_d3_087(it_replacement_d2_087):
    feature = _clean(it_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_087'] = {'inputs': ['it_replacement_d2_087'], 'func': it_replacement_d3_087}


def it_replacement_d3_088(it_replacement_d2_088):
    feature = _clean(it_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_088'] = {'inputs': ['it_replacement_d2_088'], 'func': it_replacement_d3_088}


def it_replacement_d3_089(it_replacement_d2_089):
    feature = _clean(it_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_089'] = {'inputs': ['it_replacement_d2_089'], 'func': it_replacement_d3_089}


def it_replacement_d3_090(it_replacement_d2_090):
    feature = _clean(it_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_090'] = {'inputs': ['it_replacement_d2_090'], 'func': it_replacement_d3_090}


def it_replacement_d3_091(it_replacement_d2_091):
    feature = _clean(it_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_091'] = {'inputs': ['it_replacement_d2_091'], 'func': it_replacement_d3_091}


def it_replacement_d3_092(it_replacement_d2_092):
    feature = _clean(it_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_092'] = {'inputs': ['it_replacement_d2_092'], 'func': it_replacement_d3_092}


def it_replacement_d3_093(it_replacement_d2_093):
    feature = _clean(it_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_093'] = {'inputs': ['it_replacement_d2_093'], 'func': it_replacement_d3_093}


def it_replacement_d3_094(it_replacement_d2_094):
    feature = _clean(it_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_094'] = {'inputs': ['it_replacement_d2_094'], 'func': it_replacement_d3_094}


def it_replacement_d3_095(it_replacement_d2_095):
    feature = _clean(it_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_095'] = {'inputs': ['it_replacement_d2_095'], 'func': it_replacement_d3_095}


def it_replacement_d3_096(it_replacement_d2_096):
    feature = _clean(it_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_096'] = {'inputs': ['it_replacement_d2_096'], 'func': it_replacement_d3_096}


def it_replacement_d3_097(it_replacement_d2_097):
    feature = _clean(it_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_097'] = {'inputs': ['it_replacement_d2_097'], 'func': it_replacement_d3_097}


def it_replacement_d3_098(it_replacement_d2_098):
    feature = _clean(it_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_098'] = {'inputs': ['it_replacement_d2_098'], 'func': it_replacement_d3_098}


def it_replacement_d3_099(it_replacement_d2_099):
    feature = _clean(it_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_099'] = {'inputs': ['it_replacement_d2_099'], 'func': it_replacement_d3_099}


def it_replacement_d3_100(it_replacement_d2_100):
    feature = _clean(it_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_100'] = {'inputs': ['it_replacement_d2_100'], 'func': it_replacement_d3_100}


def it_replacement_d3_101(it_replacement_d2_101):
    feature = _clean(it_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_101'] = {'inputs': ['it_replacement_d2_101'], 'func': it_replacement_d3_101}


def it_replacement_d3_102(it_replacement_d2_102):
    feature = _clean(it_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_102'] = {'inputs': ['it_replacement_d2_102'], 'func': it_replacement_d3_102}


def it_replacement_d3_103(it_replacement_d2_103):
    feature = _clean(it_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_103'] = {'inputs': ['it_replacement_d2_103'], 'func': it_replacement_d3_103}


def it_replacement_d3_104(it_replacement_d2_104):
    feature = _clean(it_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_104'] = {'inputs': ['it_replacement_d2_104'], 'func': it_replacement_d3_104}


def it_replacement_d3_105(it_replacement_d2_105):
    feature = _clean(it_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_105'] = {'inputs': ['it_replacement_d2_105'], 'func': it_replacement_d3_105}


def it_replacement_d3_106(it_replacement_d2_106):
    feature = _clean(it_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_106'] = {'inputs': ['it_replacement_d2_106'], 'func': it_replacement_d3_106}


def it_replacement_d3_107(it_replacement_d2_107):
    feature = _clean(it_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_107'] = {'inputs': ['it_replacement_d2_107'], 'func': it_replacement_d3_107}


def it_replacement_d3_108(it_replacement_d2_108):
    feature = _clean(it_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_108'] = {'inputs': ['it_replacement_d2_108'], 'func': it_replacement_d3_108}


def it_replacement_d3_109(it_replacement_d2_109):
    feature = _clean(it_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_109'] = {'inputs': ['it_replacement_d2_109'], 'func': it_replacement_d3_109}


def it_replacement_d3_110(it_replacement_d2_110):
    feature = _clean(it_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_110'] = {'inputs': ['it_replacement_d2_110'], 'func': it_replacement_d3_110}


def it_replacement_d3_111(it_replacement_d2_111):
    feature = _clean(it_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_111'] = {'inputs': ['it_replacement_d2_111'], 'func': it_replacement_d3_111}


def it_replacement_d3_112(it_replacement_d2_112):
    feature = _clean(it_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['it_replacement_d3_112'] = {'inputs': ['it_replacement_d2_112'], 'func': it_replacement_d3_112}


# Third-derivative extensions for repaired first-base features.
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def itm_base_universe_d3_001_itm_002_insider_net_buy_ratio_42(itm_base_universe_d2_001_itm_002_insider_net_buy_ratio_42):
    return _base_universe_d3(itm_base_universe_d2_001_itm_002_insider_net_buy_ratio_42, 1)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_001_itm_002_insider_net_buy_ratio_42'] = {'inputs': ['itm_base_universe_d2_001_itm_002_insider_net_buy_ratio_42'], 'func': itm_base_universe_d3_001_itm_002_insider_net_buy_ratio_42}


def itm_base_universe_d3_002_itm_003_insider_value_ratio_63(itm_base_universe_d2_002_itm_003_insider_value_ratio_63):
    return _base_universe_d3(itm_base_universe_d2_002_itm_003_insider_value_ratio_63, 2)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_002_itm_003_insider_value_ratio_63'] = {'inputs': ['itm_base_universe_d2_002_itm_003_insider_value_ratio_63'], 'func': itm_base_universe_d3_002_itm_003_insider_value_ratio_63}


def itm_base_universe_d3_003_itm_004_ceo_cfo_buy_weight_84(itm_base_universe_d2_003_itm_004_ceo_cfo_buy_weight_84):
    return _base_universe_d3(itm_base_universe_d2_003_itm_004_ceo_cfo_buy_weight_84, 3)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_003_itm_004_ceo_cfo_buy_weight_84'] = {'inputs': ['itm_base_universe_d2_003_itm_004_ceo_cfo_buy_weight_84'], 'func': itm_base_universe_d3_003_itm_004_ceo_cfo_buy_weight_84}


def itm_base_universe_d3_004_itm_006_insider_conviction_189(itm_base_universe_d2_004_itm_006_insider_conviction_189):
    return _base_universe_d3(itm_base_universe_d2_004_itm_006_insider_conviction_189, 4)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_004_itm_006_insider_conviction_189'] = {'inputs': ['itm_base_universe_d2_004_itm_006_insider_conviction_189'], 'func': itm_base_universe_d3_004_itm_006_insider_conviction_189}


def itm_base_universe_d3_005_itm_008_insider_buy_cluster_378(itm_base_universe_d2_005_itm_008_insider_buy_cluster_378):
    return _base_universe_d3(itm_base_universe_d2_005_itm_008_insider_buy_cluster_378, 5)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_005_itm_008_insider_buy_cluster_378'] = {'inputs': ['itm_base_universe_d2_005_itm_008_insider_buy_cluster_378'], 'func': itm_base_universe_d3_005_itm_008_insider_buy_cluster_378}


def itm_base_universe_d3_006_itm_009_insider_net_buy_ratio_504(itm_base_universe_d2_006_itm_009_insider_net_buy_ratio_504):
    return _base_universe_d3(itm_base_universe_d2_006_itm_009_insider_net_buy_ratio_504, 6)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_006_itm_009_insider_net_buy_ratio_504'] = {'inputs': ['itm_base_universe_d2_006_itm_009_insider_net_buy_ratio_504'], 'func': itm_base_universe_d3_006_itm_009_insider_net_buy_ratio_504}


def itm_base_universe_d3_007_itm_010_insider_value_ratio_756(itm_base_universe_d2_007_itm_010_insider_value_ratio_756):
    return _base_universe_d3(itm_base_universe_d2_007_itm_010_insider_value_ratio_756, 7)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_007_itm_010_insider_value_ratio_756'] = {'inputs': ['itm_base_universe_d2_007_itm_010_insider_value_ratio_756'], 'func': itm_base_universe_d3_007_itm_010_insider_value_ratio_756}


def itm_base_universe_d3_008_itm_011_ceo_cfo_buy_weight_1008(itm_base_universe_d2_008_itm_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d3(itm_base_universe_d2_008_itm_011_ceo_cfo_buy_weight_1008, 8)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_008_itm_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['itm_base_universe_d2_008_itm_011_ceo_cfo_buy_weight_1008'], 'func': itm_base_universe_d3_008_itm_011_ceo_cfo_buy_weight_1008}


def itm_base_universe_d3_009_itm_014_insider_silence_63(itm_base_universe_d2_009_itm_014_insider_silence_63):
    return _base_universe_d3(itm_base_universe_d2_009_itm_014_insider_silence_63, 9)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_009_itm_014_insider_silence_63'] = {'inputs': ['itm_base_universe_d2_009_itm_014_insider_silence_63'], 'func': itm_base_universe_d3_009_itm_014_insider_silence_63}


def itm_base_universe_d3_010_itm_015_insider_buy_cluster_252(itm_base_universe_d2_010_itm_015_insider_buy_cluster_252):
    return _base_universe_d3(itm_base_universe_d2_010_itm_015_insider_buy_cluster_252, 10)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_010_itm_015_insider_buy_cluster_252'] = {'inputs': ['itm_base_universe_d2_010_itm_015_insider_buy_cluster_252'], 'func': itm_base_universe_d3_010_itm_015_insider_buy_cluster_252}


def itm_base_universe_d3_011_itm_016_insider_net_buy_ratio_21(itm_base_universe_d2_011_itm_016_insider_net_buy_ratio_21):
    return _base_universe_d3(itm_base_universe_d2_011_itm_016_insider_net_buy_ratio_21, 11)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_011_itm_016_insider_net_buy_ratio_21'] = {'inputs': ['itm_base_universe_d2_011_itm_016_insider_net_buy_ratio_21'], 'func': itm_base_universe_d3_011_itm_016_insider_net_buy_ratio_21}


def itm_base_universe_d3_012_itm_017_insider_value_ratio_42(itm_base_universe_d2_012_itm_017_insider_value_ratio_42):
    return _base_universe_d3(itm_base_universe_d2_012_itm_017_insider_value_ratio_42, 12)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_012_itm_017_insider_value_ratio_42'] = {'inputs': ['itm_base_universe_d2_012_itm_017_insider_value_ratio_42'], 'func': itm_base_universe_d3_012_itm_017_insider_value_ratio_42}


def itm_base_universe_d3_013_itm_018_ceo_cfo_buy_weight_63(itm_base_universe_d2_013_itm_018_ceo_cfo_buy_weight_63):
    return _base_universe_d3(itm_base_universe_d2_013_itm_018_ceo_cfo_buy_weight_63, 13)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_013_itm_018_ceo_cfo_buy_weight_63'] = {'inputs': ['itm_base_universe_d2_013_itm_018_ceo_cfo_buy_weight_63'], 'func': itm_base_universe_d3_013_itm_018_ceo_cfo_buy_weight_63}


def itm_base_universe_d3_014_itm_020_insider_conviction_126(itm_base_universe_d2_014_itm_020_insider_conviction_126):
    return _base_universe_d3(itm_base_universe_d2_014_itm_020_insider_conviction_126, 14)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_014_itm_020_insider_conviction_126'] = {'inputs': ['itm_base_universe_d2_014_itm_020_insider_conviction_126'], 'func': itm_base_universe_d3_014_itm_020_insider_conviction_126}


def itm_base_universe_d3_015_itm_021_insider_silence_189(itm_base_universe_d2_015_itm_021_insider_silence_189):
    return _base_universe_d3(itm_base_universe_d2_015_itm_021_insider_silence_189, 15)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_015_itm_021_insider_silence_189'] = {'inputs': ['itm_base_universe_d2_015_itm_021_insider_silence_189'], 'func': itm_base_universe_d3_015_itm_021_insider_silence_189}


def itm_base_universe_d3_016_itm_023_insider_net_buy_ratio_378(itm_base_universe_d2_016_itm_023_insider_net_buy_ratio_378):
    return _base_universe_d3(itm_base_universe_d2_016_itm_023_insider_net_buy_ratio_378, 16)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_016_itm_023_insider_net_buy_ratio_378'] = {'inputs': ['itm_base_universe_d2_016_itm_023_insider_net_buy_ratio_378'], 'func': itm_base_universe_d3_016_itm_023_insider_net_buy_ratio_378}


def itm_base_universe_d3_017_itm_024_insider_value_ratio_504(itm_base_universe_d2_017_itm_024_insider_value_ratio_504):
    return _base_universe_d3(itm_base_universe_d2_017_itm_024_insider_value_ratio_504, 17)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_017_itm_024_insider_value_ratio_504'] = {'inputs': ['itm_base_universe_d2_017_itm_024_insider_value_ratio_504'], 'func': itm_base_universe_d3_017_itm_024_insider_value_ratio_504}


def itm_base_universe_d3_018_itm_027_insider_conviction_1260(itm_base_universe_d2_018_itm_027_insider_conviction_1260):
    return _base_universe_d3(itm_base_universe_d2_018_itm_027_insider_conviction_1260, 18)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_018_itm_027_insider_conviction_1260'] = {'inputs': ['itm_base_universe_d2_018_itm_027_insider_conviction_1260'], 'func': itm_base_universe_d3_018_itm_027_insider_conviction_1260}


def itm_base_universe_d3_019_itm_028_insider_silence_1512(itm_base_universe_d2_019_itm_028_insider_silence_1512):
    return _base_universe_d3(itm_base_universe_d2_019_itm_028_insider_silence_1512, 19)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_019_itm_028_insider_silence_1512'] = {'inputs': ['itm_base_universe_d2_019_itm_028_insider_silence_1512'], 'func': itm_base_universe_d3_019_itm_028_insider_silence_1512}


def itm_base_universe_d3_020_itm_029_insider_buy_cluster_63(itm_base_universe_d2_020_itm_029_insider_buy_cluster_63):
    return _base_universe_d3(itm_base_universe_d2_020_itm_029_insider_buy_cluster_63, 20)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_020_itm_029_insider_buy_cluster_63'] = {'inputs': ['itm_base_universe_d2_020_itm_029_insider_buy_cluster_63'], 'func': itm_base_universe_d3_020_itm_029_insider_buy_cluster_63}


def itm_base_universe_d3_021_itm_030_insider_net_buy_ratio_252(itm_base_universe_d2_021_itm_030_insider_net_buy_ratio_252):
    return _base_universe_d3(itm_base_universe_d2_021_itm_030_insider_net_buy_ratio_252, 21)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_021_itm_030_insider_net_buy_ratio_252'] = {'inputs': ['itm_base_universe_d2_021_itm_030_insider_net_buy_ratio_252'], 'func': itm_base_universe_d3_021_itm_030_insider_net_buy_ratio_252}


def itm_base_universe_d3_022_itm_031_insider_value_ratio_21(itm_base_universe_d2_022_itm_031_insider_value_ratio_21):
    return _base_universe_d3(itm_base_universe_d2_022_itm_031_insider_value_ratio_21, 22)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_022_itm_031_insider_value_ratio_21'] = {'inputs': ['itm_base_universe_d2_022_itm_031_insider_value_ratio_21'], 'func': itm_base_universe_d3_022_itm_031_insider_value_ratio_21}


def itm_base_universe_d3_023_itm_032_ceo_cfo_buy_weight_42(itm_base_universe_d2_023_itm_032_ceo_cfo_buy_weight_42):
    return _base_universe_d3(itm_base_universe_d2_023_itm_032_ceo_cfo_buy_weight_42, 23)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_023_itm_032_ceo_cfo_buy_weight_42'] = {'inputs': ['itm_base_universe_d2_023_itm_032_ceo_cfo_buy_weight_42'], 'func': itm_base_universe_d3_023_itm_032_ceo_cfo_buy_weight_42}


def itm_base_universe_d3_024_itm_034_insider_conviction_84(itm_base_universe_d2_024_itm_034_insider_conviction_84):
    return _base_universe_d3(itm_base_universe_d2_024_itm_034_insider_conviction_84, 24)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_024_itm_034_insider_conviction_84'] = {'inputs': ['itm_base_universe_d2_024_itm_034_insider_conviction_84'], 'func': itm_base_universe_d3_024_itm_034_insider_conviction_84}


def itm_base_universe_d3_025_itm_035_insider_silence_126(itm_base_universe_d2_025_itm_035_insider_silence_126):
    return _base_universe_d3(itm_base_universe_d2_025_itm_035_insider_silence_126, 25)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_025_itm_035_insider_silence_126'] = {'inputs': ['itm_base_universe_d2_025_itm_035_insider_silence_126'], 'func': itm_base_universe_d3_025_itm_035_insider_silence_126}


def itm_base_universe_d3_026_itm_036_insider_buy_cluster_189(itm_base_universe_d2_026_itm_036_insider_buy_cluster_189):
    return _base_universe_d3(itm_base_universe_d2_026_itm_036_insider_buy_cluster_189, 26)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_026_itm_036_insider_buy_cluster_189'] = {'inputs': ['itm_base_universe_d2_026_itm_036_insider_buy_cluster_189'], 'func': itm_base_universe_d3_026_itm_036_insider_buy_cluster_189}


def itm_base_universe_d3_027_itm_038_insider_value_ratio_378(itm_base_universe_d2_027_itm_038_insider_value_ratio_378):
    return _base_universe_d3(itm_base_universe_d2_027_itm_038_insider_value_ratio_378, 27)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_027_itm_038_insider_value_ratio_378'] = {'inputs': ['itm_base_universe_d2_027_itm_038_insider_value_ratio_378'], 'func': itm_base_universe_d3_027_itm_038_insider_value_ratio_378}


def itm_base_universe_d3_028_itm_039_ceo_cfo_buy_weight_504(itm_base_universe_d2_028_itm_039_ceo_cfo_buy_weight_504):
    return _base_universe_d3(itm_base_universe_d2_028_itm_039_ceo_cfo_buy_weight_504, 28)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_028_itm_039_ceo_cfo_buy_weight_504'] = {'inputs': ['itm_base_universe_d2_028_itm_039_ceo_cfo_buy_weight_504'], 'func': itm_base_universe_d3_028_itm_039_ceo_cfo_buy_weight_504}


def itm_base_universe_d3_029_itm_041_insider_conviction_1008(itm_base_universe_d2_029_itm_041_insider_conviction_1008):
    return _base_universe_d3(itm_base_universe_d2_029_itm_041_insider_conviction_1008, 29)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_029_itm_041_insider_conviction_1008'] = {'inputs': ['itm_base_universe_d2_029_itm_041_insider_conviction_1008'], 'func': itm_base_universe_d3_029_itm_041_insider_conviction_1008}


def itm_base_universe_d3_030_itm_042_insider_silence_1260(itm_base_universe_d2_030_itm_042_insider_silence_1260):
    return _base_universe_d3(itm_base_universe_d2_030_itm_042_insider_silence_1260, 30)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_030_itm_042_insider_silence_1260'] = {'inputs': ['itm_base_universe_d2_030_itm_042_insider_silence_1260'], 'func': itm_base_universe_d3_030_itm_042_insider_silence_1260}


def itm_base_universe_d3_031_itm_043_insider_buy_cluster_1512(itm_base_universe_d2_031_itm_043_insider_buy_cluster_1512):
    return _base_universe_d3(itm_base_universe_d2_031_itm_043_insider_buy_cluster_1512, 31)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_031_itm_043_insider_buy_cluster_1512'] = {'inputs': ['itm_base_universe_d2_031_itm_043_insider_buy_cluster_1512'], 'func': itm_base_universe_d3_031_itm_043_insider_buy_cluster_1512}


def itm_base_universe_d3_032_itm_044_insider_net_buy_ratio_63(itm_base_universe_d2_032_itm_044_insider_net_buy_ratio_63):
    return _base_universe_d3(itm_base_universe_d2_032_itm_044_insider_net_buy_ratio_63, 32)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_032_itm_044_insider_net_buy_ratio_63'] = {'inputs': ['itm_base_universe_d2_032_itm_044_insider_net_buy_ratio_63'], 'func': itm_base_universe_d3_032_itm_044_insider_net_buy_ratio_63}


def itm_base_universe_d3_033_itm_045_insider_value_ratio_252(itm_base_universe_d2_033_itm_045_insider_value_ratio_252):
    return _base_universe_d3(itm_base_universe_d2_033_itm_045_insider_value_ratio_252, 33)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_033_itm_045_insider_value_ratio_252'] = {'inputs': ['itm_base_universe_d2_033_itm_045_insider_value_ratio_252'], 'func': itm_base_universe_d3_033_itm_045_insider_value_ratio_252}


def itm_base_universe_d3_034_itm_046_ceo_cfo_buy_weight_21(itm_base_universe_d2_034_itm_046_ceo_cfo_buy_weight_21):
    return _base_universe_d3(itm_base_universe_d2_034_itm_046_ceo_cfo_buy_weight_21, 34)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_034_itm_046_ceo_cfo_buy_weight_21'] = {'inputs': ['itm_base_universe_d2_034_itm_046_ceo_cfo_buy_weight_21'], 'func': itm_base_universe_d3_034_itm_046_ceo_cfo_buy_weight_21}


def itm_base_universe_d3_035_itm_048_insider_conviction_63(itm_base_universe_d2_035_itm_048_insider_conviction_63):
    return _base_universe_d3(itm_base_universe_d2_035_itm_048_insider_conviction_63, 35)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_035_itm_048_insider_conviction_63'] = {'inputs': ['itm_base_universe_d2_035_itm_048_insider_conviction_63'], 'func': itm_base_universe_d3_035_itm_048_insider_conviction_63}


def itm_base_universe_d3_036_itm_049_insider_silence_84(itm_base_universe_d2_036_itm_049_insider_silence_84):
    return _base_universe_d3(itm_base_universe_d2_036_itm_049_insider_silence_84, 36)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_036_itm_049_insider_silence_84'] = {'inputs': ['itm_base_universe_d2_036_itm_049_insider_silence_84'], 'func': itm_base_universe_d3_036_itm_049_insider_silence_84}


def itm_base_universe_d3_037_itm_050_insider_buy_cluster_126(itm_base_universe_d2_037_itm_050_insider_buy_cluster_126):
    return _base_universe_d3(itm_base_universe_d2_037_itm_050_insider_buy_cluster_126, 37)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_037_itm_050_insider_buy_cluster_126'] = {'inputs': ['itm_base_universe_d2_037_itm_050_insider_buy_cluster_126'], 'func': itm_base_universe_d3_037_itm_050_insider_buy_cluster_126}


def itm_base_universe_d3_038_itm_051_insider_net_buy_ratio_189(itm_base_universe_d2_038_itm_051_insider_net_buy_ratio_189):
    return _base_universe_d3(itm_base_universe_d2_038_itm_051_insider_net_buy_ratio_189, 38)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_038_itm_051_insider_net_buy_ratio_189'] = {'inputs': ['itm_base_universe_d2_038_itm_051_insider_net_buy_ratio_189'], 'func': itm_base_universe_d3_038_itm_051_insider_net_buy_ratio_189}


def itm_base_universe_d3_039_itm_053_ceo_cfo_buy_weight_378(itm_base_universe_d2_039_itm_053_ceo_cfo_buy_weight_378):
    return _base_universe_d3(itm_base_universe_d2_039_itm_053_ceo_cfo_buy_weight_378, 39)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_039_itm_053_ceo_cfo_buy_weight_378'] = {'inputs': ['itm_base_universe_d2_039_itm_053_ceo_cfo_buy_weight_378'], 'func': itm_base_universe_d3_039_itm_053_ceo_cfo_buy_weight_378}


def itm_base_universe_d3_040_itm_055_insider_conviction_756(itm_base_universe_d2_040_itm_055_insider_conviction_756):
    return _base_universe_d3(itm_base_universe_d2_040_itm_055_insider_conviction_756, 40)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_040_itm_055_insider_conviction_756'] = {'inputs': ['itm_base_universe_d2_040_itm_055_insider_conviction_756'], 'func': itm_base_universe_d3_040_itm_055_insider_conviction_756}


def itm_base_universe_d3_041_itm_056_insider_silence_1008(itm_base_universe_d2_041_itm_056_insider_silence_1008):
    return _base_universe_d3(itm_base_universe_d2_041_itm_056_insider_silence_1008, 41)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_041_itm_056_insider_silence_1008'] = {'inputs': ['itm_base_universe_d2_041_itm_056_insider_silence_1008'], 'func': itm_base_universe_d3_041_itm_056_insider_silence_1008}


def itm_base_universe_d3_042_itm_057_insider_buy_cluster_1260(itm_base_universe_d2_042_itm_057_insider_buy_cluster_1260):
    return _base_universe_d3(itm_base_universe_d2_042_itm_057_insider_buy_cluster_1260, 42)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_042_itm_057_insider_buy_cluster_1260'] = {'inputs': ['itm_base_universe_d2_042_itm_057_insider_buy_cluster_1260'], 'func': itm_base_universe_d3_042_itm_057_insider_buy_cluster_1260}


def itm_base_universe_d3_043_itm_058_insider_net_buy_ratio_1512(itm_base_universe_d2_043_itm_058_insider_net_buy_ratio_1512):
    return _base_universe_d3(itm_base_universe_d2_043_itm_058_insider_net_buy_ratio_1512, 43)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_043_itm_058_insider_net_buy_ratio_1512'] = {'inputs': ['itm_base_universe_d2_043_itm_058_insider_net_buy_ratio_1512'], 'func': itm_base_universe_d3_043_itm_058_insider_net_buy_ratio_1512}


def itm_base_universe_d3_044_itm_060_ceo_cfo_buy_weight_252(itm_base_universe_d2_044_itm_060_ceo_cfo_buy_weight_252):
    return _base_universe_d3(itm_base_universe_d2_044_itm_060_ceo_cfo_buy_weight_252, 44)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_044_itm_060_ceo_cfo_buy_weight_252'] = {'inputs': ['itm_base_universe_d2_044_itm_060_ceo_cfo_buy_weight_252'], 'func': itm_base_universe_d3_044_itm_060_ceo_cfo_buy_weight_252}


def itm_base_universe_d3_045_itm_062_insider_conviction_42(itm_base_universe_d2_045_itm_062_insider_conviction_42):
    return _base_universe_d3(itm_base_universe_d2_045_itm_062_insider_conviction_42, 45)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_045_itm_062_insider_conviction_42'] = {'inputs': ['itm_base_universe_d2_045_itm_062_insider_conviction_42'], 'func': itm_base_universe_d3_045_itm_062_insider_conviction_42}


def itm_base_universe_d3_046_itm_064_insider_buy_cluster_84(itm_base_universe_d2_046_itm_064_insider_buy_cluster_84):
    return _base_universe_d3(itm_base_universe_d2_046_itm_064_insider_buy_cluster_84, 46)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_046_itm_064_insider_buy_cluster_84'] = {'inputs': ['itm_base_universe_d2_046_itm_064_insider_buy_cluster_84'], 'func': itm_base_universe_d3_046_itm_064_insider_buy_cluster_84}


def itm_base_universe_d3_047_itm_065_insider_net_buy_ratio_126(itm_base_universe_d2_047_itm_065_insider_net_buy_ratio_126):
    return _base_universe_d3(itm_base_universe_d2_047_itm_065_insider_net_buy_ratio_126, 47)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_047_itm_065_insider_net_buy_ratio_126'] = {'inputs': ['itm_base_universe_d2_047_itm_065_insider_net_buy_ratio_126'], 'func': itm_base_universe_d3_047_itm_065_insider_net_buy_ratio_126}


def itm_base_universe_d3_048_itm_066_insider_value_ratio_189(itm_base_universe_d2_048_itm_066_insider_value_ratio_189):
    return _base_universe_d3(itm_base_universe_d2_048_itm_066_insider_value_ratio_189, 48)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_048_itm_066_insider_value_ratio_189'] = {'inputs': ['itm_base_universe_d2_048_itm_066_insider_value_ratio_189'], 'func': itm_base_universe_d3_048_itm_066_insider_value_ratio_189}


def itm_base_universe_d3_049_itm_069_insider_conviction_504(itm_base_universe_d2_049_itm_069_insider_conviction_504):
    return _base_universe_d3(itm_base_universe_d2_049_itm_069_insider_conviction_504, 49)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_049_itm_069_insider_conviction_504'] = {'inputs': ['itm_base_universe_d2_049_itm_069_insider_conviction_504'], 'func': itm_base_universe_d3_049_itm_069_insider_conviction_504}


def itm_base_universe_d3_050_itm_070_insider_silence_756(itm_base_universe_d2_050_itm_070_insider_silence_756):
    return _base_universe_d3(itm_base_universe_d2_050_itm_070_insider_silence_756, 50)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_050_itm_070_insider_silence_756'] = {'inputs': ['itm_base_universe_d2_050_itm_070_insider_silence_756'], 'func': itm_base_universe_d3_050_itm_070_insider_silence_756}


def itm_base_universe_d3_051_itm_071_insider_buy_cluster_1008(itm_base_universe_d2_051_itm_071_insider_buy_cluster_1008):
    return _base_universe_d3(itm_base_universe_d2_051_itm_071_insider_buy_cluster_1008, 51)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_051_itm_071_insider_buy_cluster_1008'] = {'inputs': ['itm_base_universe_d2_051_itm_071_insider_buy_cluster_1008'], 'func': itm_base_universe_d3_051_itm_071_insider_buy_cluster_1008}


def itm_base_universe_d3_052_itm_072_insider_net_buy_ratio_1260(itm_base_universe_d2_052_itm_072_insider_net_buy_ratio_1260):
    return _base_universe_d3(itm_base_universe_d2_052_itm_072_insider_net_buy_ratio_1260, 52)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_052_itm_072_insider_net_buy_ratio_1260'] = {'inputs': ['itm_base_universe_d2_052_itm_072_insider_net_buy_ratio_1260'], 'func': itm_base_universe_d3_052_itm_072_insider_net_buy_ratio_1260}


def itm_base_universe_d3_053_itm_073_insider_value_ratio_1512(itm_base_universe_d2_053_itm_073_insider_value_ratio_1512):
    return _base_universe_d3(itm_base_universe_d2_053_itm_073_insider_value_ratio_1512, 53)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_053_itm_073_insider_value_ratio_1512'] = {'inputs': ['itm_base_universe_d2_053_itm_073_insider_value_ratio_1512'], 'func': itm_base_universe_d3_053_itm_073_insider_value_ratio_1512}


def itm_base_universe_d3_054_itm_basefill_005(itm_base_universe_d2_054_itm_basefill_005):
    return _base_universe_d3(itm_base_universe_d2_054_itm_basefill_005, 54)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_054_itm_basefill_005'] = {'inputs': ['itm_base_universe_d2_054_itm_basefill_005'], 'func': itm_base_universe_d3_054_itm_basefill_005}


def itm_base_universe_d3_055_itm_basefill_012(itm_base_universe_d2_055_itm_basefill_012):
    return _base_universe_d3(itm_base_universe_d2_055_itm_basefill_012, 55)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_055_itm_basefill_012'] = {'inputs': ['itm_base_universe_d2_055_itm_basefill_012'], 'func': itm_base_universe_d3_055_itm_basefill_012}


def itm_base_universe_d3_056_itm_basefill_019(itm_base_universe_d2_056_itm_basefill_019):
    return _base_universe_d3(itm_base_universe_d2_056_itm_basefill_019, 56)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_056_itm_basefill_019'] = {'inputs': ['itm_base_universe_d2_056_itm_basefill_019'], 'func': itm_base_universe_d3_056_itm_basefill_019}


def itm_base_universe_d3_057_itm_basefill_022(itm_base_universe_d2_057_itm_basefill_022):
    return _base_universe_d3(itm_base_universe_d2_057_itm_basefill_022, 57)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_057_itm_basefill_022'] = {'inputs': ['itm_base_universe_d2_057_itm_basefill_022'], 'func': itm_base_universe_d3_057_itm_basefill_022}


def itm_base_universe_d3_058_itm_basefill_026(itm_base_universe_d2_058_itm_basefill_026):
    return _base_universe_d3(itm_base_universe_d2_058_itm_basefill_026, 58)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_058_itm_basefill_026'] = {'inputs': ['itm_base_universe_d2_058_itm_basefill_026'], 'func': itm_base_universe_d3_058_itm_basefill_026}


def itm_base_universe_d3_059_itm_basefill_033(itm_base_universe_d2_059_itm_basefill_033):
    return _base_universe_d3(itm_base_universe_d2_059_itm_basefill_033, 59)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_059_itm_basefill_033'] = {'inputs': ['itm_base_universe_d2_059_itm_basefill_033'], 'func': itm_base_universe_d3_059_itm_basefill_033}


def itm_base_universe_d3_060_itm_basefill_037(itm_base_universe_d2_060_itm_basefill_037):
    return _base_universe_d3(itm_base_universe_d2_060_itm_basefill_037, 60)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_060_itm_basefill_037'] = {'inputs': ['itm_base_universe_d2_060_itm_basefill_037'], 'func': itm_base_universe_d3_060_itm_basefill_037}


def itm_base_universe_d3_061_itm_basefill_040(itm_base_universe_d2_061_itm_basefill_040):
    return _base_universe_d3(itm_base_universe_d2_061_itm_basefill_040, 61)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_061_itm_basefill_040'] = {'inputs': ['itm_base_universe_d2_061_itm_basefill_040'], 'func': itm_base_universe_d3_061_itm_basefill_040}


def itm_base_universe_d3_062_itm_basefill_047(itm_base_universe_d2_062_itm_basefill_047):
    return _base_universe_d3(itm_base_universe_d2_062_itm_basefill_047, 62)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_062_itm_basefill_047'] = {'inputs': ['itm_base_universe_d2_062_itm_basefill_047'], 'func': itm_base_universe_d3_062_itm_basefill_047}


def itm_base_universe_d3_063_itm_basefill_052(itm_base_universe_d2_063_itm_basefill_052):
    return _base_universe_d3(itm_base_universe_d2_063_itm_basefill_052, 63)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_063_itm_basefill_052'] = {'inputs': ['itm_base_universe_d2_063_itm_basefill_052'], 'func': itm_base_universe_d3_063_itm_basefill_052}


def itm_base_universe_d3_064_itm_basefill_054(itm_base_universe_d2_064_itm_basefill_054):
    return _base_universe_d3(itm_base_universe_d2_064_itm_basefill_054, 64)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_064_itm_basefill_054'] = {'inputs': ['itm_base_universe_d2_064_itm_basefill_054'], 'func': itm_base_universe_d3_064_itm_basefill_054}


def itm_base_universe_d3_065_itm_basefill_059(itm_base_universe_d2_065_itm_basefill_059):
    return _base_universe_d3(itm_base_universe_d2_065_itm_basefill_059, 65)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_065_itm_basefill_059'] = {'inputs': ['itm_base_universe_d2_065_itm_basefill_059'], 'func': itm_base_universe_d3_065_itm_basefill_059}


def itm_base_universe_d3_066_itm_basefill_061(itm_base_universe_d2_066_itm_basefill_061):
    return _base_universe_d3(itm_base_universe_d2_066_itm_basefill_061, 66)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_066_itm_basefill_061'] = {'inputs': ['itm_base_universe_d2_066_itm_basefill_061'], 'func': itm_base_universe_d3_066_itm_basefill_061}


def itm_base_universe_d3_067_itm_basefill_063(itm_base_universe_d2_067_itm_basefill_063):
    return _base_universe_d3(itm_base_universe_d2_067_itm_basefill_063, 67)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_067_itm_basefill_063'] = {'inputs': ['itm_base_universe_d2_067_itm_basefill_063'], 'func': itm_base_universe_d3_067_itm_basefill_063}


def itm_base_universe_d3_068_itm_basefill_067(itm_base_universe_d2_068_itm_basefill_067):
    return _base_universe_d3(itm_base_universe_d2_068_itm_basefill_067, 68)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_068_itm_basefill_067'] = {'inputs': ['itm_base_universe_d2_068_itm_basefill_067'], 'func': itm_base_universe_d3_068_itm_basefill_067}


def itm_base_universe_d3_069_itm_basefill_068(itm_base_universe_d2_069_itm_basefill_068):
    return _base_universe_d3(itm_base_universe_d2_069_itm_basefill_068, 69)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_069_itm_basefill_068'] = {'inputs': ['itm_base_universe_d2_069_itm_basefill_068'], 'func': itm_base_universe_d3_069_itm_basefill_068}


def itm_base_universe_d3_070_itm_basefill_074(itm_base_universe_d2_070_itm_basefill_074):
    return _base_universe_d3(itm_base_universe_d2_070_itm_basefill_074, 70)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_070_itm_basefill_074'] = {'inputs': ['itm_base_universe_d2_070_itm_basefill_074'], 'func': itm_base_universe_d3_070_itm_basefill_074}


def itm_base_universe_d3_071_itm_basefill_075(itm_base_universe_d2_071_itm_basefill_075):
    return _base_universe_d3(itm_base_universe_d2_071_itm_basefill_075, 71)
ITM_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['itm_base_universe_d3_071_itm_basefill_075'] = {'inputs': ['itm_base_universe_d2_071_itm_basefill_075'], 'func': itm_base_universe_d3_071_itm_basefill_075}

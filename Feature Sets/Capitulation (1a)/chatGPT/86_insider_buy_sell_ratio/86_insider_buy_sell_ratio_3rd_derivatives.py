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



def ibr_176_ibr_001_insider_buy_cluster_21_accel_1(ibr_151_ibr_001_insider_buy_cluster_21_roc_1):
    feature = _s(ibr_151_ibr_001_insider_buy_cluster_21_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ibr_177_ibr_007_insider_silence_252_accel_42(ibr_152_ibr_007_insider_silence_252_roc_42):
    feature = _s(ibr_152_ibr_007_insider_silence_252_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ibr_178_ibr_013_insider_conviction_1512_accel_126(ibr_153_ibr_013_insider_conviction_1512_roc_126):
    feature = _s(ibr_153_ibr_013_insider_conviction_1512_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ibr_179_ibr_019_insider_activity_accel_1_accel_378(ibr_154_ibr_019_insider_activity_accel_1_roc_378):
    feature = _s(ibr_154_ibr_019_insider_activity_accel_1_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)

def ibr_180_ibr_025_ceo_cfo_buy_weight_756_accel_4(ibr_155_ibr_025_ceo_cfo_buy_weight_756_roc_4):
    feature = _s(ibr_155_ibr_025_ceo_cfo_buy_weight_756_roc_4)
    return (_roc(feature, 4).diff(1)).reindex(feature.index)






















INSIDER_BUY_SELL_RATIO_REGISTRY_3RD_DERIVATIVES = {
    'ibr_176_ibr_001_insider_buy_cluster_21_accel_1': {'inputs': ['ibr_151_ibr_001_insider_buy_cluster_21_roc_1'], 'func': ibr_176_ibr_001_insider_buy_cluster_21_accel_1},
    'ibr_177_ibr_007_insider_silence_252_accel_42': {'inputs': ['ibr_152_ibr_007_insider_silence_252_roc_42'], 'func': ibr_177_ibr_007_insider_silence_252_accel_42},
    'ibr_178_ibr_013_insider_conviction_1512_accel_126': {'inputs': ['ibr_153_ibr_013_insider_conviction_1512_roc_126'], 'func': ibr_178_ibr_013_insider_conviction_1512_accel_126},
    'ibr_179_ibr_019_insider_activity_accel_1_accel_378': {'inputs': ['ibr_154_ibr_019_insider_activity_accel_1_roc_378'], 'func': ibr_179_ibr_019_insider_activity_accel_1_accel_378},
    'ibr_180_ibr_025_ceo_cfo_buy_weight_756_accel_4': {'inputs': ['ibr_155_ibr_025_ceo_cfo_buy_weight_756_roc_4'], 'func': ibr_180_ibr_025_ceo_cfo_buy_weight_756_accel_4},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ibsr_replacement_d3_001(ibsr_replacement_d2_001):
    feature = _clean(ibsr_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_001'] = {'inputs': ['ibsr_replacement_d2_001'], 'func': ibsr_replacement_d3_001}


def ibsr_replacement_d3_002(ibsr_replacement_d2_002):
    feature = _clean(ibsr_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_002'] = {'inputs': ['ibsr_replacement_d2_002'], 'func': ibsr_replacement_d3_002}


def ibsr_replacement_d3_003(ibsr_replacement_d2_003):
    feature = _clean(ibsr_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_003'] = {'inputs': ['ibsr_replacement_d2_003'], 'func': ibsr_replacement_d3_003}


def ibsr_replacement_d3_004(ibsr_replacement_d2_004):
    feature = _clean(ibsr_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_004'] = {'inputs': ['ibsr_replacement_d2_004'], 'func': ibsr_replacement_d3_004}


def ibsr_replacement_d3_005(ibsr_replacement_d2_005):
    feature = _clean(ibsr_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_005'] = {'inputs': ['ibsr_replacement_d2_005'], 'func': ibsr_replacement_d3_005}


def ibsr_replacement_d3_006(ibsr_replacement_d2_006):
    feature = _clean(ibsr_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_006'] = {'inputs': ['ibsr_replacement_d2_006'], 'func': ibsr_replacement_d3_006}


def ibsr_replacement_d3_007(ibsr_replacement_d2_007):
    feature = _clean(ibsr_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_007'] = {'inputs': ['ibsr_replacement_d2_007'], 'func': ibsr_replacement_d3_007}


def ibsr_replacement_d3_008(ibsr_replacement_d2_008):
    feature = _clean(ibsr_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_008'] = {'inputs': ['ibsr_replacement_d2_008'], 'func': ibsr_replacement_d3_008}


def ibsr_replacement_d3_009(ibsr_replacement_d2_009):
    feature = _clean(ibsr_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_009'] = {'inputs': ['ibsr_replacement_d2_009'], 'func': ibsr_replacement_d3_009}


def ibsr_replacement_d3_010(ibsr_replacement_d2_010):
    feature = _clean(ibsr_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_010'] = {'inputs': ['ibsr_replacement_d2_010'], 'func': ibsr_replacement_d3_010}


def ibsr_replacement_d3_011(ibsr_replacement_d2_011):
    feature = _clean(ibsr_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_011'] = {'inputs': ['ibsr_replacement_d2_011'], 'func': ibsr_replacement_d3_011}


def ibsr_replacement_d3_012(ibsr_replacement_d2_012):
    feature = _clean(ibsr_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_012'] = {'inputs': ['ibsr_replacement_d2_012'], 'func': ibsr_replacement_d3_012}


def ibsr_replacement_d3_013(ibsr_replacement_d2_013):
    feature = _clean(ibsr_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_013'] = {'inputs': ['ibsr_replacement_d2_013'], 'func': ibsr_replacement_d3_013}


def ibsr_replacement_d3_014(ibsr_replacement_d2_014):
    feature = _clean(ibsr_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_014'] = {'inputs': ['ibsr_replacement_d2_014'], 'func': ibsr_replacement_d3_014}


def ibsr_replacement_d3_015(ibsr_replacement_d2_015):
    feature = _clean(ibsr_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_015'] = {'inputs': ['ibsr_replacement_d2_015'], 'func': ibsr_replacement_d3_015}


def ibsr_replacement_d3_016(ibsr_replacement_d2_016):
    feature = _clean(ibsr_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_016'] = {'inputs': ['ibsr_replacement_d2_016'], 'func': ibsr_replacement_d3_016}


def ibsr_replacement_d3_017(ibsr_replacement_d2_017):
    feature = _clean(ibsr_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_017'] = {'inputs': ['ibsr_replacement_d2_017'], 'func': ibsr_replacement_d3_017}


def ibsr_replacement_d3_018(ibsr_replacement_d2_018):
    feature = _clean(ibsr_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_018'] = {'inputs': ['ibsr_replacement_d2_018'], 'func': ibsr_replacement_d3_018}


def ibsr_replacement_d3_019(ibsr_replacement_d2_019):
    feature = _clean(ibsr_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_019'] = {'inputs': ['ibsr_replacement_d2_019'], 'func': ibsr_replacement_d3_019}


def ibsr_replacement_d3_020(ibsr_replacement_d2_020):
    feature = _clean(ibsr_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_020'] = {'inputs': ['ibsr_replacement_d2_020'], 'func': ibsr_replacement_d3_020}


def ibsr_replacement_d3_021(ibsr_replacement_d2_021):
    feature = _clean(ibsr_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_021'] = {'inputs': ['ibsr_replacement_d2_021'], 'func': ibsr_replacement_d3_021}


def ibsr_replacement_d3_022(ibsr_replacement_d2_022):
    feature = _clean(ibsr_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_022'] = {'inputs': ['ibsr_replacement_d2_022'], 'func': ibsr_replacement_d3_022}


def ibsr_replacement_d3_023(ibsr_replacement_d2_023):
    feature = _clean(ibsr_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_023'] = {'inputs': ['ibsr_replacement_d2_023'], 'func': ibsr_replacement_d3_023}


def ibsr_replacement_d3_024(ibsr_replacement_d2_024):
    feature = _clean(ibsr_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_024'] = {'inputs': ['ibsr_replacement_d2_024'], 'func': ibsr_replacement_d3_024}


def ibsr_replacement_d3_025(ibsr_replacement_d2_025):
    feature = _clean(ibsr_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_025'] = {'inputs': ['ibsr_replacement_d2_025'], 'func': ibsr_replacement_d3_025}


def ibsr_replacement_d3_026(ibsr_replacement_d2_026):
    feature = _clean(ibsr_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_026'] = {'inputs': ['ibsr_replacement_d2_026'], 'func': ibsr_replacement_d3_026}


def ibsr_replacement_d3_027(ibsr_replacement_d2_027):
    feature = _clean(ibsr_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_027'] = {'inputs': ['ibsr_replacement_d2_027'], 'func': ibsr_replacement_d3_027}


def ibsr_replacement_d3_028(ibsr_replacement_d2_028):
    feature = _clean(ibsr_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_028'] = {'inputs': ['ibsr_replacement_d2_028'], 'func': ibsr_replacement_d3_028}


def ibsr_replacement_d3_029(ibsr_replacement_d2_029):
    feature = _clean(ibsr_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_029'] = {'inputs': ['ibsr_replacement_d2_029'], 'func': ibsr_replacement_d3_029}


def ibsr_replacement_d3_030(ibsr_replacement_d2_030):
    feature = _clean(ibsr_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_030'] = {'inputs': ['ibsr_replacement_d2_030'], 'func': ibsr_replacement_d3_030}


def ibsr_replacement_d3_031(ibsr_replacement_d2_031):
    feature = _clean(ibsr_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_031'] = {'inputs': ['ibsr_replacement_d2_031'], 'func': ibsr_replacement_d3_031}


def ibsr_replacement_d3_032(ibsr_replacement_d2_032):
    feature = _clean(ibsr_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_032'] = {'inputs': ['ibsr_replacement_d2_032'], 'func': ibsr_replacement_d3_032}


def ibsr_replacement_d3_033(ibsr_replacement_d2_033):
    feature = _clean(ibsr_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_033'] = {'inputs': ['ibsr_replacement_d2_033'], 'func': ibsr_replacement_d3_033}


def ibsr_replacement_d3_034(ibsr_replacement_d2_034):
    feature = _clean(ibsr_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_034'] = {'inputs': ['ibsr_replacement_d2_034'], 'func': ibsr_replacement_d3_034}


def ibsr_replacement_d3_035(ibsr_replacement_d2_035):
    feature = _clean(ibsr_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_035'] = {'inputs': ['ibsr_replacement_d2_035'], 'func': ibsr_replacement_d3_035}


def ibsr_replacement_d3_036(ibsr_replacement_d2_036):
    feature = _clean(ibsr_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_036'] = {'inputs': ['ibsr_replacement_d2_036'], 'func': ibsr_replacement_d3_036}


def ibsr_replacement_d3_037(ibsr_replacement_d2_037):
    feature = _clean(ibsr_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_037'] = {'inputs': ['ibsr_replacement_d2_037'], 'func': ibsr_replacement_d3_037}


def ibsr_replacement_d3_038(ibsr_replacement_d2_038):
    feature = _clean(ibsr_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_038'] = {'inputs': ['ibsr_replacement_d2_038'], 'func': ibsr_replacement_d3_038}


def ibsr_replacement_d3_039(ibsr_replacement_d2_039):
    feature = _clean(ibsr_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_039'] = {'inputs': ['ibsr_replacement_d2_039'], 'func': ibsr_replacement_d3_039}


def ibsr_replacement_d3_040(ibsr_replacement_d2_040):
    feature = _clean(ibsr_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_040'] = {'inputs': ['ibsr_replacement_d2_040'], 'func': ibsr_replacement_d3_040}


def ibsr_replacement_d3_041(ibsr_replacement_d2_041):
    feature = _clean(ibsr_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_041'] = {'inputs': ['ibsr_replacement_d2_041'], 'func': ibsr_replacement_d3_041}


def ibsr_replacement_d3_042(ibsr_replacement_d2_042):
    feature = _clean(ibsr_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_042'] = {'inputs': ['ibsr_replacement_d2_042'], 'func': ibsr_replacement_d3_042}


def ibsr_replacement_d3_043(ibsr_replacement_d2_043):
    feature = _clean(ibsr_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_043'] = {'inputs': ['ibsr_replacement_d2_043'], 'func': ibsr_replacement_d3_043}


def ibsr_replacement_d3_044(ibsr_replacement_d2_044):
    feature = _clean(ibsr_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_044'] = {'inputs': ['ibsr_replacement_d2_044'], 'func': ibsr_replacement_d3_044}


def ibsr_replacement_d3_045(ibsr_replacement_d2_045):
    feature = _clean(ibsr_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_045'] = {'inputs': ['ibsr_replacement_d2_045'], 'func': ibsr_replacement_d3_045}


def ibsr_replacement_d3_046(ibsr_replacement_d2_046):
    feature = _clean(ibsr_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_046'] = {'inputs': ['ibsr_replacement_d2_046'], 'func': ibsr_replacement_d3_046}


def ibsr_replacement_d3_047(ibsr_replacement_d2_047):
    feature = _clean(ibsr_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_047'] = {'inputs': ['ibsr_replacement_d2_047'], 'func': ibsr_replacement_d3_047}


def ibsr_replacement_d3_048(ibsr_replacement_d2_048):
    feature = _clean(ibsr_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_048'] = {'inputs': ['ibsr_replacement_d2_048'], 'func': ibsr_replacement_d3_048}


def ibsr_replacement_d3_049(ibsr_replacement_d2_049):
    feature = _clean(ibsr_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_049'] = {'inputs': ['ibsr_replacement_d2_049'], 'func': ibsr_replacement_d3_049}


def ibsr_replacement_d3_050(ibsr_replacement_d2_050):
    feature = _clean(ibsr_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_050'] = {'inputs': ['ibsr_replacement_d2_050'], 'func': ibsr_replacement_d3_050}


def ibsr_replacement_d3_051(ibsr_replacement_d2_051):
    feature = _clean(ibsr_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_051'] = {'inputs': ['ibsr_replacement_d2_051'], 'func': ibsr_replacement_d3_051}


def ibsr_replacement_d3_052(ibsr_replacement_d2_052):
    feature = _clean(ibsr_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_052'] = {'inputs': ['ibsr_replacement_d2_052'], 'func': ibsr_replacement_d3_052}


def ibsr_replacement_d3_053(ibsr_replacement_d2_053):
    feature = _clean(ibsr_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_053'] = {'inputs': ['ibsr_replacement_d2_053'], 'func': ibsr_replacement_d3_053}


def ibsr_replacement_d3_054(ibsr_replacement_d2_054):
    feature = _clean(ibsr_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_054'] = {'inputs': ['ibsr_replacement_d2_054'], 'func': ibsr_replacement_d3_054}


def ibsr_replacement_d3_055(ibsr_replacement_d2_055):
    feature = _clean(ibsr_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_055'] = {'inputs': ['ibsr_replacement_d2_055'], 'func': ibsr_replacement_d3_055}


def ibsr_replacement_d3_056(ibsr_replacement_d2_056):
    feature = _clean(ibsr_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_056'] = {'inputs': ['ibsr_replacement_d2_056'], 'func': ibsr_replacement_d3_056}


def ibsr_replacement_d3_057(ibsr_replacement_d2_057):
    feature = _clean(ibsr_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_057'] = {'inputs': ['ibsr_replacement_d2_057'], 'func': ibsr_replacement_d3_057}


def ibsr_replacement_d3_058(ibsr_replacement_d2_058):
    feature = _clean(ibsr_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_058'] = {'inputs': ['ibsr_replacement_d2_058'], 'func': ibsr_replacement_d3_058}


def ibsr_replacement_d3_059(ibsr_replacement_d2_059):
    feature = _clean(ibsr_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_059'] = {'inputs': ['ibsr_replacement_d2_059'], 'func': ibsr_replacement_d3_059}


def ibsr_replacement_d3_060(ibsr_replacement_d2_060):
    feature = _clean(ibsr_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_060'] = {'inputs': ['ibsr_replacement_d2_060'], 'func': ibsr_replacement_d3_060}


def ibsr_replacement_d3_061(ibsr_replacement_d2_061):
    feature = _clean(ibsr_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_061'] = {'inputs': ['ibsr_replacement_d2_061'], 'func': ibsr_replacement_d3_061}


def ibsr_replacement_d3_062(ibsr_replacement_d2_062):
    feature = _clean(ibsr_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_062'] = {'inputs': ['ibsr_replacement_d2_062'], 'func': ibsr_replacement_d3_062}


def ibsr_replacement_d3_063(ibsr_replacement_d2_063):
    feature = _clean(ibsr_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_063'] = {'inputs': ['ibsr_replacement_d2_063'], 'func': ibsr_replacement_d3_063}


def ibsr_replacement_d3_064(ibsr_replacement_d2_064):
    feature = _clean(ibsr_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_064'] = {'inputs': ['ibsr_replacement_d2_064'], 'func': ibsr_replacement_d3_064}


def ibsr_replacement_d3_065(ibsr_replacement_d2_065):
    feature = _clean(ibsr_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_065'] = {'inputs': ['ibsr_replacement_d2_065'], 'func': ibsr_replacement_d3_065}


def ibsr_replacement_d3_066(ibsr_replacement_d2_066):
    feature = _clean(ibsr_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_066'] = {'inputs': ['ibsr_replacement_d2_066'], 'func': ibsr_replacement_d3_066}


def ibsr_replacement_d3_067(ibsr_replacement_d2_067):
    feature = _clean(ibsr_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_067'] = {'inputs': ['ibsr_replacement_d2_067'], 'func': ibsr_replacement_d3_067}


def ibsr_replacement_d3_068(ibsr_replacement_d2_068):
    feature = _clean(ibsr_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_068'] = {'inputs': ['ibsr_replacement_d2_068'], 'func': ibsr_replacement_d3_068}


def ibsr_replacement_d3_069(ibsr_replacement_d2_069):
    feature = _clean(ibsr_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_069'] = {'inputs': ['ibsr_replacement_d2_069'], 'func': ibsr_replacement_d3_069}


def ibsr_replacement_d3_070(ibsr_replacement_d2_070):
    feature = _clean(ibsr_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_070'] = {'inputs': ['ibsr_replacement_d2_070'], 'func': ibsr_replacement_d3_070}


def ibsr_replacement_d3_071(ibsr_replacement_d2_071):
    feature = _clean(ibsr_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_071'] = {'inputs': ['ibsr_replacement_d2_071'], 'func': ibsr_replacement_d3_071}


def ibsr_replacement_d3_072(ibsr_replacement_d2_072):
    feature = _clean(ibsr_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_072'] = {'inputs': ['ibsr_replacement_d2_072'], 'func': ibsr_replacement_d3_072}


def ibsr_replacement_d3_073(ibsr_replacement_d2_073):
    feature = _clean(ibsr_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_073'] = {'inputs': ['ibsr_replacement_d2_073'], 'func': ibsr_replacement_d3_073}


def ibsr_replacement_d3_074(ibsr_replacement_d2_074):
    feature = _clean(ibsr_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_074'] = {'inputs': ['ibsr_replacement_d2_074'], 'func': ibsr_replacement_d3_074}


def ibsr_replacement_d3_075(ibsr_replacement_d2_075):
    feature = _clean(ibsr_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_075'] = {'inputs': ['ibsr_replacement_d2_075'], 'func': ibsr_replacement_d3_075}


def ibsr_replacement_d3_076(ibsr_replacement_d2_076):
    feature = _clean(ibsr_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_076'] = {'inputs': ['ibsr_replacement_d2_076'], 'func': ibsr_replacement_d3_076}


def ibsr_replacement_d3_077(ibsr_replacement_d2_077):
    feature = _clean(ibsr_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_077'] = {'inputs': ['ibsr_replacement_d2_077'], 'func': ibsr_replacement_d3_077}


def ibsr_replacement_d3_078(ibsr_replacement_d2_078):
    feature = _clean(ibsr_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_078'] = {'inputs': ['ibsr_replacement_d2_078'], 'func': ibsr_replacement_d3_078}


def ibsr_replacement_d3_079(ibsr_replacement_d2_079):
    feature = _clean(ibsr_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_079'] = {'inputs': ['ibsr_replacement_d2_079'], 'func': ibsr_replacement_d3_079}


def ibsr_replacement_d3_080(ibsr_replacement_d2_080):
    feature = _clean(ibsr_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_080'] = {'inputs': ['ibsr_replacement_d2_080'], 'func': ibsr_replacement_d3_080}


def ibsr_replacement_d3_081(ibsr_replacement_d2_081):
    feature = _clean(ibsr_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_081'] = {'inputs': ['ibsr_replacement_d2_081'], 'func': ibsr_replacement_d3_081}


def ibsr_replacement_d3_082(ibsr_replacement_d2_082):
    feature = _clean(ibsr_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_082'] = {'inputs': ['ibsr_replacement_d2_082'], 'func': ibsr_replacement_d3_082}


def ibsr_replacement_d3_083(ibsr_replacement_d2_083):
    feature = _clean(ibsr_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_083'] = {'inputs': ['ibsr_replacement_d2_083'], 'func': ibsr_replacement_d3_083}


def ibsr_replacement_d3_084(ibsr_replacement_d2_084):
    feature = _clean(ibsr_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_084'] = {'inputs': ['ibsr_replacement_d2_084'], 'func': ibsr_replacement_d3_084}


def ibsr_replacement_d3_085(ibsr_replacement_d2_085):
    feature = _clean(ibsr_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_085'] = {'inputs': ['ibsr_replacement_d2_085'], 'func': ibsr_replacement_d3_085}


def ibsr_replacement_d3_086(ibsr_replacement_d2_086):
    feature = _clean(ibsr_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_086'] = {'inputs': ['ibsr_replacement_d2_086'], 'func': ibsr_replacement_d3_086}


def ibsr_replacement_d3_087(ibsr_replacement_d2_087):
    feature = _clean(ibsr_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_087'] = {'inputs': ['ibsr_replacement_d2_087'], 'func': ibsr_replacement_d3_087}


def ibsr_replacement_d3_088(ibsr_replacement_d2_088):
    feature = _clean(ibsr_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_088'] = {'inputs': ['ibsr_replacement_d2_088'], 'func': ibsr_replacement_d3_088}


def ibsr_replacement_d3_089(ibsr_replacement_d2_089):
    feature = _clean(ibsr_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_089'] = {'inputs': ['ibsr_replacement_d2_089'], 'func': ibsr_replacement_d3_089}


def ibsr_replacement_d3_090(ibsr_replacement_d2_090):
    feature = _clean(ibsr_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_090'] = {'inputs': ['ibsr_replacement_d2_090'], 'func': ibsr_replacement_d3_090}


def ibsr_replacement_d3_091(ibsr_replacement_d2_091):
    feature = _clean(ibsr_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_091'] = {'inputs': ['ibsr_replacement_d2_091'], 'func': ibsr_replacement_d3_091}


def ibsr_replacement_d3_092(ibsr_replacement_d2_092):
    feature = _clean(ibsr_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_092'] = {'inputs': ['ibsr_replacement_d2_092'], 'func': ibsr_replacement_d3_092}


def ibsr_replacement_d3_093(ibsr_replacement_d2_093):
    feature = _clean(ibsr_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_093'] = {'inputs': ['ibsr_replacement_d2_093'], 'func': ibsr_replacement_d3_093}


def ibsr_replacement_d3_094(ibsr_replacement_d2_094):
    feature = _clean(ibsr_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_094'] = {'inputs': ['ibsr_replacement_d2_094'], 'func': ibsr_replacement_d3_094}


def ibsr_replacement_d3_095(ibsr_replacement_d2_095):
    feature = _clean(ibsr_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_095'] = {'inputs': ['ibsr_replacement_d2_095'], 'func': ibsr_replacement_d3_095}


def ibsr_replacement_d3_096(ibsr_replacement_d2_096):
    feature = _clean(ibsr_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_096'] = {'inputs': ['ibsr_replacement_d2_096'], 'func': ibsr_replacement_d3_096}


def ibsr_replacement_d3_097(ibsr_replacement_d2_097):
    feature = _clean(ibsr_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_097'] = {'inputs': ['ibsr_replacement_d2_097'], 'func': ibsr_replacement_d3_097}


def ibsr_replacement_d3_098(ibsr_replacement_d2_098):
    feature = _clean(ibsr_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_098'] = {'inputs': ['ibsr_replacement_d2_098'], 'func': ibsr_replacement_d3_098}


def ibsr_replacement_d3_099(ibsr_replacement_d2_099):
    feature = _clean(ibsr_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_099'] = {'inputs': ['ibsr_replacement_d2_099'], 'func': ibsr_replacement_d3_099}


def ibsr_replacement_d3_100(ibsr_replacement_d2_100):
    feature = _clean(ibsr_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_100'] = {'inputs': ['ibsr_replacement_d2_100'], 'func': ibsr_replacement_d3_100}


def ibsr_replacement_d3_101(ibsr_replacement_d2_101):
    feature = _clean(ibsr_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_101'] = {'inputs': ['ibsr_replacement_d2_101'], 'func': ibsr_replacement_d3_101}


def ibsr_replacement_d3_102(ibsr_replacement_d2_102):
    feature = _clean(ibsr_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_102'] = {'inputs': ['ibsr_replacement_d2_102'], 'func': ibsr_replacement_d3_102}


def ibsr_replacement_d3_103(ibsr_replacement_d2_103):
    feature = _clean(ibsr_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_103'] = {'inputs': ['ibsr_replacement_d2_103'], 'func': ibsr_replacement_d3_103}


def ibsr_replacement_d3_104(ibsr_replacement_d2_104):
    feature = _clean(ibsr_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_104'] = {'inputs': ['ibsr_replacement_d2_104'], 'func': ibsr_replacement_d3_104}


def ibsr_replacement_d3_105(ibsr_replacement_d2_105):
    feature = _clean(ibsr_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_105'] = {'inputs': ['ibsr_replacement_d2_105'], 'func': ibsr_replacement_d3_105}


def ibsr_replacement_d3_106(ibsr_replacement_d2_106):
    feature = _clean(ibsr_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_106'] = {'inputs': ['ibsr_replacement_d2_106'], 'func': ibsr_replacement_d3_106}


def ibsr_replacement_d3_107(ibsr_replacement_d2_107):
    feature = _clean(ibsr_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_107'] = {'inputs': ['ibsr_replacement_d2_107'], 'func': ibsr_replacement_d3_107}


def ibsr_replacement_d3_108(ibsr_replacement_d2_108):
    feature = _clean(ibsr_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_108'] = {'inputs': ['ibsr_replacement_d2_108'], 'func': ibsr_replacement_d3_108}


def ibsr_replacement_d3_109(ibsr_replacement_d2_109):
    feature = _clean(ibsr_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_109'] = {'inputs': ['ibsr_replacement_d2_109'], 'func': ibsr_replacement_d3_109}


def ibsr_replacement_d3_110(ibsr_replacement_d2_110):
    feature = _clean(ibsr_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_110'] = {'inputs': ['ibsr_replacement_d2_110'], 'func': ibsr_replacement_d3_110}


def ibsr_replacement_d3_111(ibsr_replacement_d2_111):
    feature = _clean(ibsr_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_111'] = {'inputs': ['ibsr_replacement_d2_111'], 'func': ibsr_replacement_d3_111}


def ibsr_replacement_d3_112(ibsr_replacement_d2_112):
    feature = _clean(ibsr_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
IBSR_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ibsr_replacement_d3_112'] = {'inputs': ['ibsr_replacement_d2_112'], 'func': ibsr_replacement_d3_112}


# Third-derivative extensions for repaired first-base features.
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ibr_base_universe_d3_001_ibr_002_insider_net_buy_ratio_42(ibr_base_universe_d2_001_ibr_002_insider_net_buy_ratio_42):
    return _base_universe_d3(ibr_base_universe_d2_001_ibr_002_insider_net_buy_ratio_42, 1)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_001_ibr_002_insider_net_buy_ratio_42'] = {'inputs': ['ibr_base_universe_d2_001_ibr_002_insider_net_buy_ratio_42'], 'func': ibr_base_universe_d3_001_ibr_002_insider_net_buy_ratio_42}


def ibr_base_universe_d3_002_ibr_003_insider_value_ratio_63(ibr_base_universe_d2_002_ibr_003_insider_value_ratio_63):
    return _base_universe_d3(ibr_base_universe_d2_002_ibr_003_insider_value_ratio_63, 2)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_002_ibr_003_insider_value_ratio_63'] = {'inputs': ['ibr_base_universe_d2_002_ibr_003_insider_value_ratio_63'], 'func': ibr_base_universe_d3_002_ibr_003_insider_value_ratio_63}


def ibr_base_universe_d3_003_ibr_004_ceo_cfo_buy_weight_84(ibr_base_universe_d2_003_ibr_004_ceo_cfo_buy_weight_84):
    return _base_universe_d3(ibr_base_universe_d2_003_ibr_004_ceo_cfo_buy_weight_84, 3)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_003_ibr_004_ceo_cfo_buy_weight_84'] = {'inputs': ['ibr_base_universe_d2_003_ibr_004_ceo_cfo_buy_weight_84'], 'func': ibr_base_universe_d3_003_ibr_004_ceo_cfo_buy_weight_84}


def ibr_base_universe_d3_004_ibr_006_insider_conviction_189(ibr_base_universe_d2_004_ibr_006_insider_conviction_189):
    return _base_universe_d3(ibr_base_universe_d2_004_ibr_006_insider_conviction_189, 4)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_004_ibr_006_insider_conviction_189'] = {'inputs': ['ibr_base_universe_d2_004_ibr_006_insider_conviction_189'], 'func': ibr_base_universe_d3_004_ibr_006_insider_conviction_189}


def ibr_base_universe_d3_005_ibr_008_insider_buy_cluster_378(ibr_base_universe_d2_005_ibr_008_insider_buy_cluster_378):
    return _base_universe_d3(ibr_base_universe_d2_005_ibr_008_insider_buy_cluster_378, 5)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_005_ibr_008_insider_buy_cluster_378'] = {'inputs': ['ibr_base_universe_d2_005_ibr_008_insider_buy_cluster_378'], 'func': ibr_base_universe_d3_005_ibr_008_insider_buy_cluster_378}


def ibr_base_universe_d3_006_ibr_009_insider_net_buy_ratio_504(ibr_base_universe_d2_006_ibr_009_insider_net_buy_ratio_504):
    return _base_universe_d3(ibr_base_universe_d2_006_ibr_009_insider_net_buy_ratio_504, 6)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_006_ibr_009_insider_net_buy_ratio_504'] = {'inputs': ['ibr_base_universe_d2_006_ibr_009_insider_net_buy_ratio_504'], 'func': ibr_base_universe_d3_006_ibr_009_insider_net_buy_ratio_504}


def ibr_base_universe_d3_007_ibr_010_insider_value_ratio_756(ibr_base_universe_d2_007_ibr_010_insider_value_ratio_756):
    return _base_universe_d3(ibr_base_universe_d2_007_ibr_010_insider_value_ratio_756, 7)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_007_ibr_010_insider_value_ratio_756'] = {'inputs': ['ibr_base_universe_d2_007_ibr_010_insider_value_ratio_756'], 'func': ibr_base_universe_d3_007_ibr_010_insider_value_ratio_756}


def ibr_base_universe_d3_008_ibr_011_ceo_cfo_buy_weight_1008(ibr_base_universe_d2_008_ibr_011_ceo_cfo_buy_weight_1008):
    return _base_universe_d3(ibr_base_universe_d2_008_ibr_011_ceo_cfo_buy_weight_1008, 8)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_008_ibr_011_ceo_cfo_buy_weight_1008'] = {'inputs': ['ibr_base_universe_d2_008_ibr_011_ceo_cfo_buy_weight_1008'], 'func': ibr_base_universe_d3_008_ibr_011_ceo_cfo_buy_weight_1008}


def ibr_base_universe_d3_009_ibr_014_insider_silence_63(ibr_base_universe_d2_009_ibr_014_insider_silence_63):
    return _base_universe_d3(ibr_base_universe_d2_009_ibr_014_insider_silence_63, 9)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_009_ibr_014_insider_silence_63'] = {'inputs': ['ibr_base_universe_d2_009_ibr_014_insider_silence_63'], 'func': ibr_base_universe_d3_009_ibr_014_insider_silence_63}


def ibr_base_universe_d3_010_ibr_015_insider_buy_cluster_252(ibr_base_universe_d2_010_ibr_015_insider_buy_cluster_252):
    return _base_universe_d3(ibr_base_universe_d2_010_ibr_015_insider_buy_cluster_252, 10)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_010_ibr_015_insider_buy_cluster_252'] = {'inputs': ['ibr_base_universe_d2_010_ibr_015_insider_buy_cluster_252'], 'func': ibr_base_universe_d3_010_ibr_015_insider_buy_cluster_252}


def ibr_base_universe_d3_011_ibr_016_insider_net_buy_ratio_21(ibr_base_universe_d2_011_ibr_016_insider_net_buy_ratio_21):
    return _base_universe_d3(ibr_base_universe_d2_011_ibr_016_insider_net_buy_ratio_21, 11)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_011_ibr_016_insider_net_buy_ratio_21'] = {'inputs': ['ibr_base_universe_d2_011_ibr_016_insider_net_buy_ratio_21'], 'func': ibr_base_universe_d3_011_ibr_016_insider_net_buy_ratio_21}


def ibr_base_universe_d3_012_ibr_017_insider_value_ratio_42(ibr_base_universe_d2_012_ibr_017_insider_value_ratio_42):
    return _base_universe_d3(ibr_base_universe_d2_012_ibr_017_insider_value_ratio_42, 12)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_012_ibr_017_insider_value_ratio_42'] = {'inputs': ['ibr_base_universe_d2_012_ibr_017_insider_value_ratio_42'], 'func': ibr_base_universe_d3_012_ibr_017_insider_value_ratio_42}


def ibr_base_universe_d3_013_ibr_018_ceo_cfo_buy_weight_63(ibr_base_universe_d2_013_ibr_018_ceo_cfo_buy_weight_63):
    return _base_universe_d3(ibr_base_universe_d2_013_ibr_018_ceo_cfo_buy_weight_63, 13)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_013_ibr_018_ceo_cfo_buy_weight_63'] = {'inputs': ['ibr_base_universe_d2_013_ibr_018_ceo_cfo_buy_weight_63'], 'func': ibr_base_universe_d3_013_ibr_018_ceo_cfo_buy_weight_63}


def ibr_base_universe_d3_014_ibr_020_insider_conviction_126(ibr_base_universe_d2_014_ibr_020_insider_conviction_126):
    return _base_universe_d3(ibr_base_universe_d2_014_ibr_020_insider_conviction_126, 14)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_014_ibr_020_insider_conviction_126'] = {'inputs': ['ibr_base_universe_d2_014_ibr_020_insider_conviction_126'], 'func': ibr_base_universe_d3_014_ibr_020_insider_conviction_126}


def ibr_base_universe_d3_015_ibr_021_insider_silence_189(ibr_base_universe_d2_015_ibr_021_insider_silence_189):
    return _base_universe_d3(ibr_base_universe_d2_015_ibr_021_insider_silence_189, 15)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_015_ibr_021_insider_silence_189'] = {'inputs': ['ibr_base_universe_d2_015_ibr_021_insider_silence_189'], 'func': ibr_base_universe_d3_015_ibr_021_insider_silence_189}


def ibr_base_universe_d3_016_ibr_023_insider_net_buy_ratio_378(ibr_base_universe_d2_016_ibr_023_insider_net_buy_ratio_378):
    return _base_universe_d3(ibr_base_universe_d2_016_ibr_023_insider_net_buy_ratio_378, 16)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_016_ibr_023_insider_net_buy_ratio_378'] = {'inputs': ['ibr_base_universe_d2_016_ibr_023_insider_net_buy_ratio_378'], 'func': ibr_base_universe_d3_016_ibr_023_insider_net_buy_ratio_378}


def ibr_base_universe_d3_017_ibr_024_insider_value_ratio_504(ibr_base_universe_d2_017_ibr_024_insider_value_ratio_504):
    return _base_universe_d3(ibr_base_universe_d2_017_ibr_024_insider_value_ratio_504, 17)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_017_ibr_024_insider_value_ratio_504'] = {'inputs': ['ibr_base_universe_d2_017_ibr_024_insider_value_ratio_504'], 'func': ibr_base_universe_d3_017_ibr_024_insider_value_ratio_504}


def ibr_base_universe_d3_018_ibr_027_insider_conviction_1260(ibr_base_universe_d2_018_ibr_027_insider_conviction_1260):
    return _base_universe_d3(ibr_base_universe_d2_018_ibr_027_insider_conviction_1260, 18)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_018_ibr_027_insider_conviction_1260'] = {'inputs': ['ibr_base_universe_d2_018_ibr_027_insider_conviction_1260'], 'func': ibr_base_universe_d3_018_ibr_027_insider_conviction_1260}


def ibr_base_universe_d3_019_ibr_028_insider_silence_1512(ibr_base_universe_d2_019_ibr_028_insider_silence_1512):
    return _base_universe_d3(ibr_base_universe_d2_019_ibr_028_insider_silence_1512, 19)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_019_ibr_028_insider_silence_1512'] = {'inputs': ['ibr_base_universe_d2_019_ibr_028_insider_silence_1512'], 'func': ibr_base_universe_d3_019_ibr_028_insider_silence_1512}


def ibr_base_universe_d3_020_ibr_029_insider_buy_cluster_63(ibr_base_universe_d2_020_ibr_029_insider_buy_cluster_63):
    return _base_universe_d3(ibr_base_universe_d2_020_ibr_029_insider_buy_cluster_63, 20)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_020_ibr_029_insider_buy_cluster_63'] = {'inputs': ['ibr_base_universe_d2_020_ibr_029_insider_buy_cluster_63'], 'func': ibr_base_universe_d3_020_ibr_029_insider_buy_cluster_63}


def ibr_base_universe_d3_021_ibr_030_insider_net_buy_ratio_252(ibr_base_universe_d2_021_ibr_030_insider_net_buy_ratio_252):
    return _base_universe_d3(ibr_base_universe_d2_021_ibr_030_insider_net_buy_ratio_252, 21)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_021_ibr_030_insider_net_buy_ratio_252'] = {'inputs': ['ibr_base_universe_d2_021_ibr_030_insider_net_buy_ratio_252'], 'func': ibr_base_universe_d3_021_ibr_030_insider_net_buy_ratio_252}


def ibr_base_universe_d3_022_ibr_031_insider_value_ratio_21(ibr_base_universe_d2_022_ibr_031_insider_value_ratio_21):
    return _base_universe_d3(ibr_base_universe_d2_022_ibr_031_insider_value_ratio_21, 22)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_022_ibr_031_insider_value_ratio_21'] = {'inputs': ['ibr_base_universe_d2_022_ibr_031_insider_value_ratio_21'], 'func': ibr_base_universe_d3_022_ibr_031_insider_value_ratio_21}


def ibr_base_universe_d3_023_ibr_032_ceo_cfo_buy_weight_42(ibr_base_universe_d2_023_ibr_032_ceo_cfo_buy_weight_42):
    return _base_universe_d3(ibr_base_universe_d2_023_ibr_032_ceo_cfo_buy_weight_42, 23)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_023_ibr_032_ceo_cfo_buy_weight_42'] = {'inputs': ['ibr_base_universe_d2_023_ibr_032_ceo_cfo_buy_weight_42'], 'func': ibr_base_universe_d3_023_ibr_032_ceo_cfo_buy_weight_42}


def ibr_base_universe_d3_024_ibr_034_insider_conviction_84(ibr_base_universe_d2_024_ibr_034_insider_conviction_84):
    return _base_universe_d3(ibr_base_universe_d2_024_ibr_034_insider_conviction_84, 24)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_024_ibr_034_insider_conviction_84'] = {'inputs': ['ibr_base_universe_d2_024_ibr_034_insider_conviction_84'], 'func': ibr_base_universe_d3_024_ibr_034_insider_conviction_84}


def ibr_base_universe_d3_025_ibr_035_insider_silence_126(ibr_base_universe_d2_025_ibr_035_insider_silence_126):
    return _base_universe_d3(ibr_base_universe_d2_025_ibr_035_insider_silence_126, 25)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_025_ibr_035_insider_silence_126'] = {'inputs': ['ibr_base_universe_d2_025_ibr_035_insider_silence_126'], 'func': ibr_base_universe_d3_025_ibr_035_insider_silence_126}


def ibr_base_universe_d3_026_ibr_036_insider_buy_cluster_189(ibr_base_universe_d2_026_ibr_036_insider_buy_cluster_189):
    return _base_universe_d3(ibr_base_universe_d2_026_ibr_036_insider_buy_cluster_189, 26)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_026_ibr_036_insider_buy_cluster_189'] = {'inputs': ['ibr_base_universe_d2_026_ibr_036_insider_buy_cluster_189'], 'func': ibr_base_universe_d3_026_ibr_036_insider_buy_cluster_189}


def ibr_base_universe_d3_027_ibr_038_insider_value_ratio_378(ibr_base_universe_d2_027_ibr_038_insider_value_ratio_378):
    return _base_universe_d3(ibr_base_universe_d2_027_ibr_038_insider_value_ratio_378, 27)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_027_ibr_038_insider_value_ratio_378'] = {'inputs': ['ibr_base_universe_d2_027_ibr_038_insider_value_ratio_378'], 'func': ibr_base_universe_d3_027_ibr_038_insider_value_ratio_378}


def ibr_base_universe_d3_028_ibr_039_ceo_cfo_buy_weight_504(ibr_base_universe_d2_028_ibr_039_ceo_cfo_buy_weight_504):
    return _base_universe_d3(ibr_base_universe_d2_028_ibr_039_ceo_cfo_buy_weight_504, 28)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_028_ibr_039_ceo_cfo_buy_weight_504'] = {'inputs': ['ibr_base_universe_d2_028_ibr_039_ceo_cfo_buy_weight_504'], 'func': ibr_base_universe_d3_028_ibr_039_ceo_cfo_buy_weight_504}


def ibr_base_universe_d3_029_ibr_041_insider_conviction_1008(ibr_base_universe_d2_029_ibr_041_insider_conviction_1008):
    return _base_universe_d3(ibr_base_universe_d2_029_ibr_041_insider_conviction_1008, 29)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_029_ibr_041_insider_conviction_1008'] = {'inputs': ['ibr_base_universe_d2_029_ibr_041_insider_conviction_1008'], 'func': ibr_base_universe_d3_029_ibr_041_insider_conviction_1008}


def ibr_base_universe_d3_030_ibr_042_insider_silence_1260(ibr_base_universe_d2_030_ibr_042_insider_silence_1260):
    return _base_universe_d3(ibr_base_universe_d2_030_ibr_042_insider_silence_1260, 30)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_030_ibr_042_insider_silence_1260'] = {'inputs': ['ibr_base_universe_d2_030_ibr_042_insider_silence_1260'], 'func': ibr_base_universe_d3_030_ibr_042_insider_silence_1260}


def ibr_base_universe_d3_031_ibr_043_insider_buy_cluster_1512(ibr_base_universe_d2_031_ibr_043_insider_buy_cluster_1512):
    return _base_universe_d3(ibr_base_universe_d2_031_ibr_043_insider_buy_cluster_1512, 31)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_031_ibr_043_insider_buy_cluster_1512'] = {'inputs': ['ibr_base_universe_d2_031_ibr_043_insider_buy_cluster_1512'], 'func': ibr_base_universe_d3_031_ibr_043_insider_buy_cluster_1512}


def ibr_base_universe_d3_032_ibr_044_insider_net_buy_ratio_63(ibr_base_universe_d2_032_ibr_044_insider_net_buy_ratio_63):
    return _base_universe_d3(ibr_base_universe_d2_032_ibr_044_insider_net_buy_ratio_63, 32)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_032_ibr_044_insider_net_buy_ratio_63'] = {'inputs': ['ibr_base_universe_d2_032_ibr_044_insider_net_buy_ratio_63'], 'func': ibr_base_universe_d3_032_ibr_044_insider_net_buy_ratio_63}


def ibr_base_universe_d3_033_ibr_045_insider_value_ratio_252(ibr_base_universe_d2_033_ibr_045_insider_value_ratio_252):
    return _base_universe_d3(ibr_base_universe_d2_033_ibr_045_insider_value_ratio_252, 33)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_033_ibr_045_insider_value_ratio_252'] = {'inputs': ['ibr_base_universe_d2_033_ibr_045_insider_value_ratio_252'], 'func': ibr_base_universe_d3_033_ibr_045_insider_value_ratio_252}


def ibr_base_universe_d3_034_ibr_046_ceo_cfo_buy_weight_21(ibr_base_universe_d2_034_ibr_046_ceo_cfo_buy_weight_21):
    return _base_universe_d3(ibr_base_universe_d2_034_ibr_046_ceo_cfo_buy_weight_21, 34)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_034_ibr_046_ceo_cfo_buy_weight_21'] = {'inputs': ['ibr_base_universe_d2_034_ibr_046_ceo_cfo_buy_weight_21'], 'func': ibr_base_universe_d3_034_ibr_046_ceo_cfo_buy_weight_21}


def ibr_base_universe_d3_035_ibr_048_insider_conviction_63(ibr_base_universe_d2_035_ibr_048_insider_conviction_63):
    return _base_universe_d3(ibr_base_universe_d2_035_ibr_048_insider_conviction_63, 35)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_035_ibr_048_insider_conviction_63'] = {'inputs': ['ibr_base_universe_d2_035_ibr_048_insider_conviction_63'], 'func': ibr_base_universe_d3_035_ibr_048_insider_conviction_63}


def ibr_base_universe_d3_036_ibr_049_insider_silence_84(ibr_base_universe_d2_036_ibr_049_insider_silence_84):
    return _base_universe_d3(ibr_base_universe_d2_036_ibr_049_insider_silence_84, 36)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_036_ibr_049_insider_silence_84'] = {'inputs': ['ibr_base_universe_d2_036_ibr_049_insider_silence_84'], 'func': ibr_base_universe_d3_036_ibr_049_insider_silence_84}


def ibr_base_universe_d3_037_ibr_050_insider_buy_cluster_126(ibr_base_universe_d2_037_ibr_050_insider_buy_cluster_126):
    return _base_universe_d3(ibr_base_universe_d2_037_ibr_050_insider_buy_cluster_126, 37)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_037_ibr_050_insider_buy_cluster_126'] = {'inputs': ['ibr_base_universe_d2_037_ibr_050_insider_buy_cluster_126'], 'func': ibr_base_universe_d3_037_ibr_050_insider_buy_cluster_126}


def ibr_base_universe_d3_038_ibr_051_insider_net_buy_ratio_189(ibr_base_universe_d2_038_ibr_051_insider_net_buy_ratio_189):
    return _base_universe_d3(ibr_base_universe_d2_038_ibr_051_insider_net_buy_ratio_189, 38)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_038_ibr_051_insider_net_buy_ratio_189'] = {'inputs': ['ibr_base_universe_d2_038_ibr_051_insider_net_buy_ratio_189'], 'func': ibr_base_universe_d3_038_ibr_051_insider_net_buy_ratio_189}


def ibr_base_universe_d3_039_ibr_053_ceo_cfo_buy_weight_378(ibr_base_universe_d2_039_ibr_053_ceo_cfo_buy_weight_378):
    return _base_universe_d3(ibr_base_universe_d2_039_ibr_053_ceo_cfo_buy_weight_378, 39)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_039_ibr_053_ceo_cfo_buy_weight_378'] = {'inputs': ['ibr_base_universe_d2_039_ibr_053_ceo_cfo_buy_weight_378'], 'func': ibr_base_universe_d3_039_ibr_053_ceo_cfo_buy_weight_378}


def ibr_base_universe_d3_040_ibr_055_insider_conviction_756(ibr_base_universe_d2_040_ibr_055_insider_conviction_756):
    return _base_universe_d3(ibr_base_universe_d2_040_ibr_055_insider_conviction_756, 40)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_040_ibr_055_insider_conviction_756'] = {'inputs': ['ibr_base_universe_d2_040_ibr_055_insider_conviction_756'], 'func': ibr_base_universe_d3_040_ibr_055_insider_conviction_756}


def ibr_base_universe_d3_041_ibr_056_insider_silence_1008(ibr_base_universe_d2_041_ibr_056_insider_silence_1008):
    return _base_universe_d3(ibr_base_universe_d2_041_ibr_056_insider_silence_1008, 41)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_041_ibr_056_insider_silence_1008'] = {'inputs': ['ibr_base_universe_d2_041_ibr_056_insider_silence_1008'], 'func': ibr_base_universe_d3_041_ibr_056_insider_silence_1008}


def ibr_base_universe_d3_042_ibr_057_insider_buy_cluster_1260(ibr_base_universe_d2_042_ibr_057_insider_buy_cluster_1260):
    return _base_universe_d3(ibr_base_universe_d2_042_ibr_057_insider_buy_cluster_1260, 42)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_042_ibr_057_insider_buy_cluster_1260'] = {'inputs': ['ibr_base_universe_d2_042_ibr_057_insider_buy_cluster_1260'], 'func': ibr_base_universe_d3_042_ibr_057_insider_buy_cluster_1260}


def ibr_base_universe_d3_043_ibr_058_insider_net_buy_ratio_1512(ibr_base_universe_d2_043_ibr_058_insider_net_buy_ratio_1512):
    return _base_universe_d3(ibr_base_universe_d2_043_ibr_058_insider_net_buy_ratio_1512, 43)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_043_ibr_058_insider_net_buy_ratio_1512'] = {'inputs': ['ibr_base_universe_d2_043_ibr_058_insider_net_buy_ratio_1512'], 'func': ibr_base_universe_d3_043_ibr_058_insider_net_buy_ratio_1512}


def ibr_base_universe_d3_044_ibr_060_ceo_cfo_buy_weight_252(ibr_base_universe_d2_044_ibr_060_ceo_cfo_buy_weight_252):
    return _base_universe_d3(ibr_base_universe_d2_044_ibr_060_ceo_cfo_buy_weight_252, 44)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_044_ibr_060_ceo_cfo_buy_weight_252'] = {'inputs': ['ibr_base_universe_d2_044_ibr_060_ceo_cfo_buy_weight_252'], 'func': ibr_base_universe_d3_044_ibr_060_ceo_cfo_buy_weight_252}


def ibr_base_universe_d3_045_ibr_062_insider_conviction_42(ibr_base_universe_d2_045_ibr_062_insider_conviction_42):
    return _base_universe_d3(ibr_base_universe_d2_045_ibr_062_insider_conviction_42, 45)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_045_ibr_062_insider_conviction_42'] = {'inputs': ['ibr_base_universe_d2_045_ibr_062_insider_conviction_42'], 'func': ibr_base_universe_d3_045_ibr_062_insider_conviction_42}


def ibr_base_universe_d3_046_ibr_064_insider_buy_cluster_84(ibr_base_universe_d2_046_ibr_064_insider_buy_cluster_84):
    return _base_universe_d3(ibr_base_universe_d2_046_ibr_064_insider_buy_cluster_84, 46)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_046_ibr_064_insider_buy_cluster_84'] = {'inputs': ['ibr_base_universe_d2_046_ibr_064_insider_buy_cluster_84'], 'func': ibr_base_universe_d3_046_ibr_064_insider_buy_cluster_84}


def ibr_base_universe_d3_047_ibr_065_insider_net_buy_ratio_126(ibr_base_universe_d2_047_ibr_065_insider_net_buy_ratio_126):
    return _base_universe_d3(ibr_base_universe_d2_047_ibr_065_insider_net_buy_ratio_126, 47)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_047_ibr_065_insider_net_buy_ratio_126'] = {'inputs': ['ibr_base_universe_d2_047_ibr_065_insider_net_buy_ratio_126'], 'func': ibr_base_universe_d3_047_ibr_065_insider_net_buy_ratio_126}


def ibr_base_universe_d3_048_ibr_066_insider_value_ratio_189(ibr_base_universe_d2_048_ibr_066_insider_value_ratio_189):
    return _base_universe_d3(ibr_base_universe_d2_048_ibr_066_insider_value_ratio_189, 48)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_048_ibr_066_insider_value_ratio_189'] = {'inputs': ['ibr_base_universe_d2_048_ibr_066_insider_value_ratio_189'], 'func': ibr_base_universe_d3_048_ibr_066_insider_value_ratio_189}


def ibr_base_universe_d3_049_ibr_069_insider_conviction_504(ibr_base_universe_d2_049_ibr_069_insider_conviction_504):
    return _base_universe_d3(ibr_base_universe_d2_049_ibr_069_insider_conviction_504, 49)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_049_ibr_069_insider_conviction_504'] = {'inputs': ['ibr_base_universe_d2_049_ibr_069_insider_conviction_504'], 'func': ibr_base_universe_d3_049_ibr_069_insider_conviction_504}


def ibr_base_universe_d3_050_ibr_070_insider_silence_756(ibr_base_universe_d2_050_ibr_070_insider_silence_756):
    return _base_universe_d3(ibr_base_universe_d2_050_ibr_070_insider_silence_756, 50)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_050_ibr_070_insider_silence_756'] = {'inputs': ['ibr_base_universe_d2_050_ibr_070_insider_silence_756'], 'func': ibr_base_universe_d3_050_ibr_070_insider_silence_756}


def ibr_base_universe_d3_051_ibr_071_insider_buy_cluster_1008(ibr_base_universe_d2_051_ibr_071_insider_buy_cluster_1008):
    return _base_universe_d3(ibr_base_universe_d2_051_ibr_071_insider_buy_cluster_1008, 51)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_051_ibr_071_insider_buy_cluster_1008'] = {'inputs': ['ibr_base_universe_d2_051_ibr_071_insider_buy_cluster_1008'], 'func': ibr_base_universe_d3_051_ibr_071_insider_buy_cluster_1008}


def ibr_base_universe_d3_052_ibr_072_insider_net_buy_ratio_1260(ibr_base_universe_d2_052_ibr_072_insider_net_buy_ratio_1260):
    return _base_universe_d3(ibr_base_universe_d2_052_ibr_072_insider_net_buy_ratio_1260, 52)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_052_ibr_072_insider_net_buy_ratio_1260'] = {'inputs': ['ibr_base_universe_d2_052_ibr_072_insider_net_buy_ratio_1260'], 'func': ibr_base_universe_d3_052_ibr_072_insider_net_buy_ratio_1260}


def ibr_base_universe_d3_053_ibr_073_insider_value_ratio_1512(ibr_base_universe_d2_053_ibr_073_insider_value_ratio_1512):
    return _base_universe_d3(ibr_base_universe_d2_053_ibr_073_insider_value_ratio_1512, 53)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_053_ibr_073_insider_value_ratio_1512'] = {'inputs': ['ibr_base_universe_d2_053_ibr_073_insider_value_ratio_1512'], 'func': ibr_base_universe_d3_053_ibr_073_insider_value_ratio_1512}


def ibr_base_universe_d3_054_ibr_basefill_005(ibr_base_universe_d2_054_ibr_basefill_005):
    return _base_universe_d3(ibr_base_universe_d2_054_ibr_basefill_005, 54)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_054_ibr_basefill_005'] = {'inputs': ['ibr_base_universe_d2_054_ibr_basefill_005'], 'func': ibr_base_universe_d3_054_ibr_basefill_005}


def ibr_base_universe_d3_055_ibr_basefill_012(ibr_base_universe_d2_055_ibr_basefill_012):
    return _base_universe_d3(ibr_base_universe_d2_055_ibr_basefill_012, 55)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_055_ibr_basefill_012'] = {'inputs': ['ibr_base_universe_d2_055_ibr_basefill_012'], 'func': ibr_base_universe_d3_055_ibr_basefill_012}


def ibr_base_universe_d3_056_ibr_basefill_019(ibr_base_universe_d2_056_ibr_basefill_019):
    return _base_universe_d3(ibr_base_universe_d2_056_ibr_basefill_019, 56)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_056_ibr_basefill_019'] = {'inputs': ['ibr_base_universe_d2_056_ibr_basefill_019'], 'func': ibr_base_universe_d3_056_ibr_basefill_019}


def ibr_base_universe_d3_057_ibr_basefill_022(ibr_base_universe_d2_057_ibr_basefill_022):
    return _base_universe_d3(ibr_base_universe_d2_057_ibr_basefill_022, 57)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_057_ibr_basefill_022'] = {'inputs': ['ibr_base_universe_d2_057_ibr_basefill_022'], 'func': ibr_base_universe_d3_057_ibr_basefill_022}


def ibr_base_universe_d3_058_ibr_basefill_026(ibr_base_universe_d2_058_ibr_basefill_026):
    return _base_universe_d3(ibr_base_universe_d2_058_ibr_basefill_026, 58)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_058_ibr_basefill_026'] = {'inputs': ['ibr_base_universe_d2_058_ibr_basefill_026'], 'func': ibr_base_universe_d3_058_ibr_basefill_026}


def ibr_base_universe_d3_059_ibr_basefill_033(ibr_base_universe_d2_059_ibr_basefill_033):
    return _base_universe_d3(ibr_base_universe_d2_059_ibr_basefill_033, 59)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_059_ibr_basefill_033'] = {'inputs': ['ibr_base_universe_d2_059_ibr_basefill_033'], 'func': ibr_base_universe_d3_059_ibr_basefill_033}


def ibr_base_universe_d3_060_ibr_basefill_037(ibr_base_universe_d2_060_ibr_basefill_037):
    return _base_universe_d3(ibr_base_universe_d2_060_ibr_basefill_037, 60)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_060_ibr_basefill_037'] = {'inputs': ['ibr_base_universe_d2_060_ibr_basefill_037'], 'func': ibr_base_universe_d3_060_ibr_basefill_037}


def ibr_base_universe_d3_061_ibr_basefill_040(ibr_base_universe_d2_061_ibr_basefill_040):
    return _base_universe_d3(ibr_base_universe_d2_061_ibr_basefill_040, 61)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_061_ibr_basefill_040'] = {'inputs': ['ibr_base_universe_d2_061_ibr_basefill_040'], 'func': ibr_base_universe_d3_061_ibr_basefill_040}


def ibr_base_universe_d3_062_ibr_basefill_047(ibr_base_universe_d2_062_ibr_basefill_047):
    return _base_universe_d3(ibr_base_universe_d2_062_ibr_basefill_047, 62)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_062_ibr_basefill_047'] = {'inputs': ['ibr_base_universe_d2_062_ibr_basefill_047'], 'func': ibr_base_universe_d3_062_ibr_basefill_047}


def ibr_base_universe_d3_063_ibr_basefill_052(ibr_base_universe_d2_063_ibr_basefill_052):
    return _base_universe_d3(ibr_base_universe_d2_063_ibr_basefill_052, 63)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_063_ibr_basefill_052'] = {'inputs': ['ibr_base_universe_d2_063_ibr_basefill_052'], 'func': ibr_base_universe_d3_063_ibr_basefill_052}


def ibr_base_universe_d3_064_ibr_basefill_054(ibr_base_universe_d2_064_ibr_basefill_054):
    return _base_universe_d3(ibr_base_universe_d2_064_ibr_basefill_054, 64)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_064_ibr_basefill_054'] = {'inputs': ['ibr_base_universe_d2_064_ibr_basefill_054'], 'func': ibr_base_universe_d3_064_ibr_basefill_054}


def ibr_base_universe_d3_065_ibr_basefill_059(ibr_base_universe_d2_065_ibr_basefill_059):
    return _base_universe_d3(ibr_base_universe_d2_065_ibr_basefill_059, 65)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_065_ibr_basefill_059'] = {'inputs': ['ibr_base_universe_d2_065_ibr_basefill_059'], 'func': ibr_base_universe_d3_065_ibr_basefill_059}


def ibr_base_universe_d3_066_ibr_basefill_061(ibr_base_universe_d2_066_ibr_basefill_061):
    return _base_universe_d3(ibr_base_universe_d2_066_ibr_basefill_061, 66)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_066_ibr_basefill_061'] = {'inputs': ['ibr_base_universe_d2_066_ibr_basefill_061'], 'func': ibr_base_universe_d3_066_ibr_basefill_061}


def ibr_base_universe_d3_067_ibr_basefill_063(ibr_base_universe_d2_067_ibr_basefill_063):
    return _base_universe_d3(ibr_base_universe_d2_067_ibr_basefill_063, 67)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_067_ibr_basefill_063'] = {'inputs': ['ibr_base_universe_d2_067_ibr_basefill_063'], 'func': ibr_base_universe_d3_067_ibr_basefill_063}


def ibr_base_universe_d3_068_ibr_basefill_067(ibr_base_universe_d2_068_ibr_basefill_067):
    return _base_universe_d3(ibr_base_universe_d2_068_ibr_basefill_067, 68)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_068_ibr_basefill_067'] = {'inputs': ['ibr_base_universe_d2_068_ibr_basefill_067'], 'func': ibr_base_universe_d3_068_ibr_basefill_067}


def ibr_base_universe_d3_069_ibr_basefill_068(ibr_base_universe_d2_069_ibr_basefill_068):
    return _base_universe_d3(ibr_base_universe_d2_069_ibr_basefill_068, 69)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_069_ibr_basefill_068'] = {'inputs': ['ibr_base_universe_d2_069_ibr_basefill_068'], 'func': ibr_base_universe_d3_069_ibr_basefill_068}


def ibr_base_universe_d3_070_ibr_basefill_074(ibr_base_universe_d2_070_ibr_basefill_074):
    return _base_universe_d3(ibr_base_universe_d2_070_ibr_basefill_074, 70)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_070_ibr_basefill_074'] = {'inputs': ['ibr_base_universe_d2_070_ibr_basefill_074'], 'func': ibr_base_universe_d3_070_ibr_basefill_074}


def ibr_base_universe_d3_071_ibr_basefill_075(ibr_base_universe_d2_071_ibr_basefill_075):
    return _base_universe_d3(ibr_base_universe_d2_071_ibr_basefill_075, 71)
IBR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ibr_base_universe_d3_071_ibr_basefill_075'] = {'inputs': ['ibr_base_universe_d2_071_ibr_basefill_075'], 'func': ibr_base_universe_d3_071_ibr_basefill_075}

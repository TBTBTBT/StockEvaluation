from enum import Enum
#陽線か陰線か
class CandleDirectionType(Enum):
    NONE = 99
    STAY = 0
    POSITIVE = 1
    NEGATIVE = 2

#種類
class CandleFluctuationType(Enum):
    NONE = 99
    BIG = 0 #
    STRAIGHT = 1 # 坊主
    HUMMER = 2 # トンカチ

#ローソクの種類
class CandleState:
    def __init__(self,direction,fluctuation):
        self.direction = direction
        self.fluctuation = fluctuation
    def __repr__(self):
        return "[ candle direction '%s' : fluctuation '%s' ]" % (self.direction, self.fluctuation)
    
#------------------------------------------------
#分析
class CandleAnalyzer:
    def __init__(self):
        pass
        #ローソク足分析
    def analyze_candle(self,data):
        direction   = self.analyze_candle_direction(data)
        fluctuation = self.analyze_candle_fluctuation(data)
        state       = CandleState(direction,fluctuation)
        return state
        # 陰陽判定
    def analyze_candle_direction(self,data):
        ret = CandleDirectionType.NONE
        return ret
        # 種類分析
    def analyze_candle_fluctuation(self,data):
        ret = CandleFluctuationType.NONE
        return ret


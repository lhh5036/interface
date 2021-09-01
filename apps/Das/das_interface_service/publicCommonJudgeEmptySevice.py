'''
@File: publicCommonJudgeEmptySevice.py
@time:2021/9/1
@Author:quanliu
@Desc:数据分析接口参数判空方法
'''

class PublicCommonJudgeEmptySevice():
    # 判断哪个页面的数据需要对入参进行判空
    def needJudgeEmpty(self, platform, searchType):
        if platform == "Amazon":
            return amazonNeedJudgeEmpty(searchType)
        elif platform == "Smt":
            return smtNeedJudgeEmpty(searchType)
        elif platform == "Ali":
            return aliNeedJudgeEmpty(searchType)
        elif platform == "Ebay":
            return ebayNeedJudgeEmpty(searchType)
        elif platform == "Shopee":
            return shopeeNeedJudgeEmpty(searchType)
        else:
            return ""

# 判断Amazon平台哪些页面需要对入参判空
def amazonNeedJudgeEmpty(searchType):
    if searchType == "bestsellerMark_query":
        return True
    elif searchType == "newReleasesMark_query":
        return True
    elif searchType == "moverShakerMark_query":
        return True
    elif searchType == "mostWishMark_query":
        return True
    elif searchType == "giftIdeasMark_query":
        return True
    else:
        return False

# 判断SMT平台哪些页面需要对入参判空
def smtNeedJudgeEmpty(searchType):
    pass

# 判断1688平台哪些页面需要对入参判空
def aliNeedJudgeEmpty(searchType):
    pass

# 判断ebay平台哪些页面需要对入参判空
def ebayNeedJudgeEmpty(searchType):
    pass

# 判断shopee平台哪些页面需要对入参判空
def shopeeNeedJudgeEmpty(searchType):
    pass
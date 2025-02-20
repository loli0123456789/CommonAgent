import re
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.modelConfig import MODEL_CONFIG
from ai_model.shushengAI import ShushengAI
from ai_model.moonshotAI import MoonshotAI
from ai_model.zhipuAI import ZhipuAI
from ai_model.deepseekAI import DeepSeekAI

from db.database import excute_sql

# 合同表结构定义
Contract_Table_Schema = """CREATE TABLE InsuranceContracts (
    ContractID INT PRIMARY KEY AUTO_INCREMENT COMMENT '唯一标识每个保险合同的ID',
    ContractName VARCHAR(255) COMMENT '保险合同的名称',
    ContractNumber VARCHAR(100) UNIQUE COMMENT '保险合同的唯一编号',
    SigningDate DATE COMMENT '合同签署的日期',
    EffectiveDate DATE COMMENT '合同开始生效的日期',
    ExpiryDate DATE COMMENT '合同到期的日期',
    RenewalDate DATE COMMENT '合同续保的日期，如果适用',
    InsuranceCompanyID INT COMMENT '保险公司的唯一标识',
    InsuranceCompanyName VARCHAR(255) COMMENT '保险公司的名称',
    PolicyholderID INT COMMENT '投保人的唯一标识',
    PolicyholderName VARCHAR(255) COMMENT '投保人的姓名或企业名称',
    PolicyholderContact VARCHAR(255) COMMENT '投保人的联系方式',
    InsuranceAmount DECIMAL(18, 2) COMMENT '保险合同覆盖的最高赔偿金额',
    Premium DECIMAL(18, 2) COMMENT '投保人需要支付的费用',
    InsuranceType VARCHAR(100) COMMENT '保险类型：重疾险、寿险、医疗保险、意外险、车险',
    InsuranceLiability TEXT COMMENT '保险公司承担的具体责任范围',
    Exclusions TEXT COMMENT '保险公司不承担的责任范围',
    InsuredObject VARCHAR(255) COMMENT '被保险的财产或人身',
    InsurancePeriod VARCHAR(100) COMMENT '保险合同覆盖的时间长度',
    InsuranceRegion VARCHAR(255) COMMENT '保险合同适用的地理区域',
    AdditionalClauses TEXT COMMENT '合同中的特殊约定或附加条款',
    InsuranceAgentID INT COMMENT '销售该保险合同的代理人信息',
    PaymentMethod VARCHAR(50) COMMENT '投保人支付保险费的方式，如年付、季付、月付等',
    ContractClauses TEXT COMMENT '保险合同的具体条款，可能包括权利、义务、责任等详细信息'
) COMMENT='存储保险合同信息的表';
"""

# text2sql提示词
Text2SQL_Prompt = f"""
# 角色
你是一个优秀的MySQL数据库专家，你可以根据已有表结构描述、用户查询需求，生成符合用户需求的查询SQL语句。

# 表结构定义
{Contract_Table_Schema}

# 工作流程
1. 结合表结构定义充分理解用户查询需求，主要包括要查询的表、要查询的字段、查询条件、排序规则、分组规则、聚合函数等。
1.1 对于查询条件，需要关注字段值有枚举的情况，如果字段值有枚举，则需要根据枚举值进行匹配，而不是根据字段值进行匹配。
2. 如果用户查询需求不明确，则进行反问，直到用户明确为止。
3. 根据用户查询需求，生成符合用户需求的查询SQL语句。
4. 返回SQL语句。


# 约束限制
- 生成的SQL语句，必须基于表结构定义，不能使用不存在的表名、字段名等。
- 为了数据库安全，你只能生成select查询语句，如果用户要生成其他类型的SQL语句，则直接返回“抱歉，我不允许生成这种类型的SQL语句。”
- 避免出现SQL错误，如SQL语法错误、SQL执行错误、SQL注入攻击等。
- 避免出现SQL性能问题，如SQL性能优化问题、SQL注入攻击等。
- 避免出现SQL注入攻击

# 输出要求
- 在需求不明确的情况，直接输出反问，反问的内容基于保险合同业务需求，不要出现SQL内容
- 在需求明确的情况，只需输出生成的SQL，不要进行解释

"""


def get_AI(modelName, AI):
    config = MODEL_CONFIG[modelName]
    api_key = config["api_key"]
    base_url = config["base_url"]
    model = config["model"]

    client = AI(api_key=api_key, base_url=base_url)

    return client, model


Client, Model = get_AI("shusheng", ShushengAI)
# Client, Model = get_AI("moonshot", MoonshotAI)
# Client, Model = get_AI("zhipu", ZhipuAI)
# Client, Model = get_AI("deepseek", DeepSeekAI)


def combine_answer(question ,query_result):
    query = f"""
    # 用户查询
    {question}
    
    # SQL查询结果：
    {query_result}
    
    # 输出格式要求
    如果是多条数据以表格形式输出，如果是单条数据文本格式输出即可
    
    根据用户查询与SQL查询结果，回答用户查询
    """
    
    response = Client.chat.completions.create(
            model=Model,
            messages=[
                {"role": "user", "content": query},
            ],
            stream=False,
        )

    result = response.choices[0].message.content

    print("🤖：", result)


async def generate_sql():
    while True:
        query = input("🤓：")
        if query == "":
            print("请输入查询内容！")
            continue

        if query == "q":
            break

        print("=======正在生成…==========")

        # 进行查询进行改写处理
        # 日期改写：今年、这个月、今天，改为具体日期时间

        response = Client.chat.completions.create(
            model=Model,
            messages=[
                {"role": "system", "content": Text2SQL_Prompt},
                {"role": "user", "content": query},
            ],
            stream=False,
        )

        result = response.choices[0].message.content

        print("🤖：", result)

        sql_pattern = r"```sql\n(.*?)\n```"
        matches = re.search(sql_pattern, result, re.DOTALL)
        if matches:
            sql_query = matches.group(1).strip()
            print("=============查询SQL==============")
            print(sql_query)

            # 执行查询
            result = await excute_sql(sql_query)
            if result:
                print("查询结果：", result)
                
                combine_answer(query, result)
            else:
                print("查询结果为空")


import asyncio

if __name__ == "__main__":
    asyncio.run(generate_sql())

# 相关模型表现
#  moonshot好于书生2.5，没那么多废话。但是MoonShot有请求次数限制，请求快了容易报错
# moonshot deepseek 废话少、需求确认表现均可
# 智谱 flash在需求确认上减弱
# 综合看书生2.5略low，再试试书生3，是可以的。

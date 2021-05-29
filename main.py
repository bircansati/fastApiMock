from fastapi import FastAPI

app = FastAPI()


@app.get("/CompanySelfRiskCount/GetInfo")
async def request_811s1():
    return {
        "Result": {
            "VerifyResult": 1,
            "Data": {
                "Id": "XXXXXX",
                "SXCount": "30",
                "ZXCount": "50",
                "JUDCount": "999",
                "JSCount": "3",
                "EXCount": "0",
                "CSACount": "619",
                "TICount": "0",
                "PLECount": "8",
                "MLECount": "0",
                "ASCount": "95",
                "CTACount": "41",
                "LMCount": "0",
                "EPCount": "0",
                "SVCount": "0",
                "LACount": "8",
                "DLNCount": "0",
                "TOCount": "0",
                "PNCount": "0",
                "SCCount": "0",
                "DWCount": "0",
                "WGCount": "0",
                "STPCount": "6",
                "STCount": "78",
                "ENCCount": "82",
                "BRYCount": "0",
                "INECount": "4",
                "ELQCount": "0",
                "APCount": "2"
            }
        },
        "Status": "200",
        "Message": "查询成功",
        "OrderNumber": "COMPANYSELFRISKCOUNT2020090310253837407464"
    }

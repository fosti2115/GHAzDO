import requests

base_url = "https://your-jfrog-instance.jfrog.io"
api_key = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIyMDI0LTExLTI3VDA5LTI2LTM2LTMzMi1iYXRva2VuLW55bW9qb2FxIiwiaXNzIjoic3RvcmUiLCJzdWIiOiJNeUpGcm9nL2thcm9sbm93YWsxQG9nYXJuaWouc2UiLCJhdWQiOiJqZmJvQCoiLCJzY3AiOiJzdWJzY3JpcHRpb246NjAzNDk4ODgzOmFwaSIsImlhdCI6MTczMjY5OTU5NiwiZXhwIjoxNzY0MjM1NTk2LCJleHQiOiJ7XCJyZWZyZXNoYWJsZVwiOnRydWUsXCJyZXZvY2FibGVcIjp0cnVlfSJ9.Yi9NsDAXgL6nUTbusas7-YZdUE4wYcWC5_WZaD0CSjy7g0g2C2jJzuUv36Oox1BhDwopxRrjOiATfrnVE7r6XivHrOxIGGaKgIxdmD4iwwvMYr17tvkIDb-p5aGhVENdW4yrjWWQ3RqvSIv-t-RBIWuHtgjCMRq5-BZb0LwAIwsGBfS0DCHrKEXe22NbBHGzvUqzNTKCXYvg7CEXKLYLq4ryR2PEsaMTIPicJzz-6pOzC4xqj_hcbjDaLoopVwTyNOk1fxZeOCmZRdCjlZ6iFqNJe4OX1xHAsy4TleUaSmhILnHB9fQbRRZ5G5SU_-C36s1Y-V1geWve-jVDY0vZ3A"

headers = {
    "X-JFrog-Art-Api": api_key,
}

# Pobranie listy repozytoriów
response = requests.get(f"{base_url}/artifactory/api/repositories", headers=headers)
print(response.json())

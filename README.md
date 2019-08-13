# callsecapi

routes | methods | params
-|-|-|
/test/ | `[GET, POST]` | `[]`
/call/ | `[POST]` | `[method, url, data]`

params | exemple | optionnal
-|-|-|
url | `"https://google.com"` | required
method | `"get"` | required `["put", "delete", "patch", "post", "head", "options", "get"]`
data | {"mykey" : "value"} | optionnal

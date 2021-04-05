// 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
// 네이버 검색 Open API 예제 - 블로그 검색
var express = require("express");
var app = express();
const cors = require("cors");
var client_id = "O3n4bv3AoWJA9rRFGChc";
var client_secret = "Zu6k9klC5C";
app.use(cors());
app.get("/search", function(req, res) {
  var api_url =
    "https://openapi.naver.com/v1/search/blog?query=" +
    encodeURI('"' + req.query.query + '"'); // json 결과
  //   var api_url = 'https://openapi.naver.com/v1/search/blog.xml?query=' + encodeURI(req.query.query); // xml 결과
  var request = require("request");
  var options = {
    url: api_url,
    headers: {
      "X-Naver-Client-Id": client_id,
      "X-Naver-Client-Secret": client_secret
    }
  };
  request.get(options, function(error, response, body) {
    if (!error && response.statusCode == 200) {
      res.writeHead(200, { "Content-Type": "text/json;charset=utf-8" });
      res.end(body);
    } else {
      res.status(response.statusCode).end();
      console.log("error = " + response.statusCode);
    }
  });
});
app.listen(2000, function() {
  console.log(
    "https://j4a304.p.ssafy.io/search/search/blog?query=검색어 app listening on port 3000!"
  );
});
